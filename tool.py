import requests
import config
import re
# API 端点
API_URL = f"{config.AZURE_OPENAI_BASE_URL}/openai/deployments/{config.AZURE_DEPLOYMENT_NAME}/chat/completions?api-version={config.AZURE_API_VERSION}"
headers = {
    "Content-Type": "application/json",
    "api-key": config.AZURE_OPENAI_API_KEY,
}


def call_openai_api(messages):
    data = {
        "messages": messages,
        "max_tokens": 16384,
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"请求失败，状态码: {response.status_code}，错误信息: {response.text}")
        return None
def get_bing_search_results(query, subscription_key, search_url, top_n=3):
    try:
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": query, "count": top_n}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json().get("webPages", {}).get("value", [])
        results = [
            {
                "url": result.get("url", ""),
                "title": result.get("name", ""),
                "content": result.get("snippet", "")
            }
            for result in search_results
        ]
        return results
    except Exception as e:
        print(f"**ERROR**: {e}")
        return []


from crawl4ai import *
import asyncio
from crawl4ai import MemoryAdaptiveDispatcher
import re


class WebCrawler():
    def __init__(self):
        pass

    def _remove_markdown_links(self, text):
        # 移除行内式链接
        pattern_inline = r'\[([^\]]+)\]\([^)]+\)'
        text = re.sub(pattern_inline, '', text)
        # 移除引用式链接定义
        pattern_reference_def = r'\[([^\]]+)\]:\s*[^\s]+'
        text = re.sub(pattern_reference_def, '', text)
        # 移除引用式链接使用
        pattern_reference_use = r'\[([^\]]+)\]\[[^\]]+\]'
        text = re.sub(pattern_reference_use, '', text)
        text = text.replace("\n", "")
        text = re.sub(r'$$.*?$$', '', text)  # 去除中括号及其内容
        text = re.sub(r'$.*?$', '', text)  # 去除小括号及其内容
        text = re.sub(r'https?://\S+', '', text)  # 去除http或https链接
        return text

    def craw(self, web_url):
        """
        Crawl the specified web URLs asynchronously and remove markdown links from the content.
        Args:
            web_url (list): A list of URLs to crawl.
        Returns:
            list: A list containing the cleaned content from each URL. If a URL cannot be crawled, None is returned in its place.
        """

        async def crawl_urls():
            # 初始化异步爬虫
            async with AsyncWebCrawler(verbose=True) as crawler:
                # 配置爬取参数
                config = CrawlerRunConfig(
                    cache_mode=None,  # 缓存模式，这里设置为None表示不使用特定缓存模式
                    # bypass_cache=True,  # 绕过缓存
                    verbose=True,  # 详细输出信息
                    stream=False,  # Default: get all results at once
                    page_timeout=12000,
                    # delay_before_return_html=3.5,
                    # max_range = 3,
                )

                # 初始化调度器
                dispatcher = MemoryAdaptiveDispatcher(
                    rate_limiter=None  # 速率限制器，这里设置为None表示不使用特定限制器
                )
                # 开始爬取多个URL
                results = await crawler.arun_many(
                    urls=web_url,
                    config=config,
                    dispatcher=dispatcher,
                )

                # 提取详细内容
                details = []
                for result in results:
                    if result.success:
                        content_detial = self._remove_markdown_links(result.markdown)
                        details.append(content_detial)
                    else:
                        details.append(None)
                return details

        return asyncio.run(crawl_urls())


def get_bing_search_detail_results(query, subscription_key, search_url, top_n=3):
    try:
        results = get_bing_search_results(query, subscription_key, search_url, top_n)
        web_crawler = WebCrawler()
        details_web_crawler = web_crawler.craw([result["url"] for result in results])

        for i in range(len(results)):
            if details_web_crawler[i] is not None:
                results[i]["content"] = details_web_crawler[i]

        return results
    except Exception as e:
        print(f"**ERROR**: {e}")
        return []

def clean_string(s):
    # 去掉所有空白字符和转义字符
    pattern = r'[\s\x00-\x1f\x7f]'
    return re.sub(pattern, '', s)

def modify_md_titles(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 正则表达式匹配 Markdown 标题
        pattern = r'(#+)\s+(.*)'

        def replace_title(match):
            heading_level = match.group(1)
            title_text = match.group(2)
            link_text = f"{title_text.replace(' ', '')}.md"
            return f"{heading_level} [{title_text}]({link_text})"

        new_content = re.sub(pattern, replace_title, content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"文件 {file_path} 已成功修改。")
    except FileNotFoundError:
        print(f"错误：未找到文件 {file_path}。")
    except Exception as e:
        print(f"发生未知错误：{e}")


# def call_openai_api(prompt):
#
#     url = "https://ai-api.betteryeah.com/v1/public_api/rest_api/3053d8368c69462aa49ce84fec487a54/execute_flow"
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Access-Key': 'YTM2MWIwYTEzOWE1NGZmNjgyYjliNmM2ZGFjMmE3NGIsMTAxOCwxNzE3Mzk0NTg4MjYy',
#         'Workspace-Id': 'a361b0a139a54ff682b9b6c6dac2a74b'
#     }
#
#     data = {
#         "inputs": {
#             "message": prompt
#         }
#     }
#
#     try:
#         response = requests.post(url, headers=headers, json=data)
#         response.raise_for_status()  # 若请求失败（状态码非 200），抛出异常
#         response_data = response.json()
#         if response_data.get('success'):
#             run_result = response_data['data']['run_result']
#             return run_result
#         else:
#             print("请求未成功，错误信息:", response_data.get('message', '未知错误'))
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP 错误发生: {http_err}")
#     except requests.exceptions.RequestException as req_err:
#         print(f"请求发生错误: {req_err}")
