import re
import requests
import config
import logging
from tool import *

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='react_deepsearch.log',
    filemode='w'
)


class ReActResearcher:
    def __init__(self, user_request):
        self.user_request = user_request
        self.context = {
            'outline': [],
            'search_history': [],
            'content': {},
            'uncertainties': []
        }
        logging.info(f"初始化 ReActResearcher，用户需求: {user_request}")

    def reflect(self):
        """改进后的反思模块 - 强制生成可执行指令"""
        messages = [
            {"role": "system",
             "content": f"""
             你是一个研究策略专家，需要根据当前状态生成具体可执行的指令。
             必须使用以下格式之一：
             1. 搜索验证[关键词] 
             2. 内容扩展[大纲项]
             3. 大纲重构[新大纲项1|新大纲项2...]
             4. 研究完成

             当前状态：
             {self.context}
             """},
            {"role": "user",
             "content": f"用户需求：{self.user_request}"}
        ]
        logging.info(f"调用 OpenAI API 进行反思，请求消息: {messages}")
        result = call_openai_api(messages)
        logging.info(f"反思模块生成的行动计划: {result}")
        return result

    def act(self, action_plan):
        """增强版行动执行器"""
        if "搜索验证" in action_plan:
            query = re.search(r'搜索验证\[(.*?)\]', action_plan).group(1)
            logging.info(f"准备进行搜索验证，关键词: {query}")
            results = get_bing_search_detail_results(
                query,
                config.subscription_key,
                config.search_url,
                top_n= 10
            )
            logging.info(f"搜索验证完成，关键词: {query}，发现 {len(results)} 条结果")

            # 清洗内容
            cleaned_results = []
            for result in results:
                content = result['content']
                messages = [
                    {"role": "system",
                     "content": f"请根据关键词 '{query}' 清洗以下内容，去除无关信息，保留相关内容，并以 Markdown 格式返回。"},
                    {"role": "user",
                     "content": content}
                ]
                cleaned_content = call_openai_api(messages)
                cleaned_result = {
                    "url": result['url'],
                    "title": result['title'],
                    "content": cleaned_content
                }
                cleaned_results.append(cleaned_result)

            self.context['search_history'].append({
                'query': query,
                'results': cleaned_results
            })
            response = f"搜索完成：{query}，发现{len(results)}条结果"
            logging.info(response)
            return response

        elif "内容扩展" in action_plan:
            section = re.search(r'内容扩展\[(.*?)\]', action_plan).group(1)
            logging.info(f"准备进行内容扩展，大纲项: {section}")
            # 优先使用搜索结果中的内容
            search_content = []
            for entry in self.context['search_history']:
                if section.lower() in entry['query'].lower():
                    search_content.extend(entry['results'])
            logging.info(f"为内容扩展找到 {len(search_content)} 条相关搜索结果")
            messages = [
                {"role": "system",
                 "content": f"根据以下资料扩展{section}部分，要求包含技术细节和最新案例"},
                {"role": "user",
                 "content": f"参考资料：{search_content[:3]}"}  # 取最新3条搜索结果
            ]
            logging.info(f"调用 OpenAI API 进行内容扩展，请求消息: {messages}")
            expanded = call_openai_api(messages)
            self.context['content'][section] = expanded
            response = f"扩展完成：{section}（{len(expanded.split())}字）"
            logging.info(response)
            return response

        elif "大纲重构" in action_plan:
            new_outline = re.findall(r'大纲重构\[(.*?)\]', action_plan)[0].split('|')
            logging.info(f"准备进行大纲重构，新大纲: {new_outline}")
            self.context['outline'] = new_outline
            response = f"大纲更新：{new_outline}"
            logging.info(response)
            return response

    def generate_report(self):
        """最终生成报告"""
        messages = [
            {"role": "system",
             "content": "将研究结果整理为包含摘要、章节内容、参考文献的完整报告。要求不允许丢失任何信息，最终结果越长越好"},
            {"role": "user",
             "content": f"研究数据：{self.context}"}
        ]
        logging.info(f"调用 OpenAI API 生成报告，请求消息: {messages}")
        logging.info(f"研究数据: {self.context}")
        result = call_openai_api(messages)
        logging.info("报告生成完成")
        return result

    def research_loop(self, max_iter=5):
        """改进的主循环"""
        for i in range(max_iter):
            logging.info(f"\n--- 第{i + 1}轮反思 ---")
            print(f"\n--- 第{i + 1}轮反思 ---")

            # 优先构建大纲
            if not self.context['outline']:
                action_plan = "大纲重构[研究背景|技术原理|应用场景|挑战与展望]"
                logging.info("自动触发大纲构建")
                print("自动触发大纲构建")
            else:
                action_plan = self.reflect()

            logging.info(f"行动计划：{action_plan}")
            print("行动计划：", action_plan)

            if "研究完成" in action_plan:
                break

            action_response = self.act(action_plan)
            logging.info(f"行动结果：{action_response}")
            print("行动结果：", action_response)

        report = self.generate_report()
        logging.info("研究循环结束，报告已生成")
        return report


def react_deepsearch(user_request):
    researcher = ReActResearcher(user_request)
    report = researcher.research_loop()
    with open('react_result.md', 'w', encoding='utf-8') as f:
        logging.info(f"准备将报告保存到 react_result.md，报告长度: {len(report)} 字")
        f.write(report)
    logging.info("报告已保存到 react_result.md")
    return report


# 示例调用
user_request = "分析大语言模型在医疗诊断中的最新应用进展"
result = react_deepsearch(user_request)
