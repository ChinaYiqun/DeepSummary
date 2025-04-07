import requests
import config
from tool import *
import os


# 请求头

def taskagent(user_request):
    messages = [
        {"role": "system",
         "content": "根据用户的提问，重写成多个独立的子标题，可以补充用户提问生成用于生成研究报告，结果必须用||分割"},
        {"role": "user", "content": f"请将以下用户请求：{user_request}"},
    ]
    return call_openai_api(messages)


def polishagent(content, user_request, sub_query):
    messages = [
        {"role": "system",
         "content": f"你是一个专业的内容润色专家，能够将给定的内容进行润色，使其更加流畅、专业和符合语法规范。" +
                    f"用户的提问是{user_request},现在进行{sub_query}的书写， 你需要对 {sub_query}子内容的润色。直接返回润色结果即可"},
        {"role": "user", "content": f"请对以下内容进行润色：这些内容是我从互联网上查到的，如下{content}"},
    ]
    return call_openai_api(messages)


def summaryagent(user_request, task_info, search_results_list, polished_content_list):
    all_info = ""
    for i in range(len(task_info)):
        all_info += f"{polished_content_list[i]} \n\n"

    messages = [
        {"role": "system",
         "content": f"你是一个文章撰写专家，请分成{task_info}这几点，重新排版 all_info 中的内容，all_info 的内容是对是回答用户的提问的回答" +
                    f"文尾需要有包含所有参考链接{search_results_list}"},
        {"role": "user",
         "content": f"用户的提问是{user_request}，all_info 信息：：\n{all_info[:50000]}"},
    ]
    with open("tmp", 'w', encoding='utf-8') as f:
        f.write(str(messages))
    return call_openai_api(messages)


def deepsearch(user_request):
    folder_name = user_request
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 1. TaskAgent 分解用户请求，将用户请求分解成多个子查询，进入循环
    task_info = taskagent(user_request)
    task_info = task_info.split("||")
    print("INFO: 任务分解结果：", task_info)

    search_results_list = []
    polished_content_list = []

    for sub_query in task_info:
        # 2. 串行的调用 bing search 获取网页信息
        search_query = f"{sub_query} {user_request}"
        search_results = get_bing_search_detail_results(search_query, config.subscription_key, config.search_url, 3)
        search_results_list.append(search_results)

        print(f"INFO: 子查询 {sub_query} 的搜索结果：", search_results)

        # 3. 循环每个第二步得到的结果 PolishAgent 润色结果
        polished_content = polishagent(", ".join([result["content"] for result in search_results]), user_request,
                                       sub_query)
        polished_content_list.append(polished_content)
        print(f"INFO: 子查询 {sub_query} 润色后内容：", polished_content)

        # 将每个子查询润色后的内容保存为单独的文件
        file_name = os.path.join(folder_name, f"{clean_string(sub_query)}.md")
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(polished_content)
    urls = []
    for result in search_results_list:
        for object in result:
            urls.append(object["url"])
    # 4. SummaryAgent 整理所有内容
    summary = summaryagent(user_request, task_info, urls, polished_content_list)
    print("INFO: 总结报告：", summary)
    # 5. summary 将所有内容输出到 result.md 中
    result_file_path = os.path.join(folder_name, 'result.md')
    with open(result_file_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    modify_md_titles(result_file_path)
    return summary


# 示例调用
user_request = "新能源电池的研究进展"
result = deepsearch(user_request)
