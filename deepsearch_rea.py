import re
import requests
import config
from tool import *


class ReActResearcher:
    def __init__(self, user_request):
        self.user_request = user_request
        self.context = {
            'outline': [],
            'search_history': [],
            'content': {},
            'uncertainties': []
        }

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
        return call_openai_api(messages)

    def act(self, action_plan):
        """增强版行动执行器"""
        if "搜索验证" in action_plan:
            query = re.search(r'搜索验证\[(.*?)\]', action_plan).group(1)
            results = get_bing_search_results(
                query,
                config.subscription_key,
                config.search_url
            )
            self.context['search_history'].append({
                'query': query,
                'results': results
            })
            return f"搜索完成：{query}，发现{len(results)}条结果"

        elif "内容扩展" in action_plan:
            section = re.search(r'内容扩展\[(.*?)\]', action_plan).group(1)
            # 优先使用搜索结果中的内容
            search_content = []
            for entry in self.context['search_history']:
                if section.lower() in entry['query'].lower():
                    search_content.extend(entry['results'])

            messages = [
                {"role": "system",
                 "content": f"根据以下资料扩展{section}部分，要求包含技术细节和最新案例"},
                {"role": "user",
                 "content": f"参考资料：{search_content[:3]}"}  # 取最新3条搜索结果
            ]
            expanded = call_openai_api(messages)
            self.context['content'][section] = expanded
            return f"扩展完成：{section}（{len(expanded.split())}字）"

        elif "大纲重构" in action_plan:
            new_outline = re.findall(r'大纲重构\[(.*?)\]', action_plan)[0].split('|')
            self.context['outline'] = new_outline
            return f"大纲更新：{new_outline}"

    def generate_report(self):
        """最终生成报告"""
        messages = [
            {"role": "system",
             "content": "将研究结果整理为包含摘要、章节内容、参考文献的完整报告"},
            {"role": "user",
             "content": f"研究数据：{self.context}"}
        ]
        return call_openai_api(messages)

    def research_loop(self, max_iter=5):
        """改进的主循环"""
        for i in range(max_iter):
            print(f"\n--- 第{i + 1}轮反思 ---")

            # 优先构建大纲
            if not self.context['outline']:
                action_plan = "大纲重构[研究背景|技术原理|应用场景|挑战与展望]"
                print("自动触发大纲构建")
            else:
                action_plan = self.reflect()

            print("行动计划：", action_plan)

            if "研究完成" in action_plan:
                break

            action_response = self.act(action_plan)
            print("行动结果：", action_response)

        return self.generate_report()


def react_deepsearch(user_request):
    researcher = ReActResearcher(user_request)
    report = researcher.research_loop()
    with open('react_result.md', 'w', encoding='utf-8') as f:
        f.write(report)
    return report


# 示例调用
user_request = "分析大语言模型在医疗诊断中的最新应用进展"
result = react_deepsearch(user_request)