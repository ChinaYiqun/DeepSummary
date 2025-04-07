import requests
import config
from tool import *


def generate_outline(user_request):
    """生成初步大纲（Step 1）"""
    messages = [
        {"role": "system", "content": "根据用户需求生成一个3级大纲，要求逻辑连贯且覆盖核心问题"},
        {"role": "user", "content": f"用户需求：{user_request}"}
    ]
    return call_openai_api(messages).split("\n")


def fill_section_content(outline, user_request):
    """根据大纲填充核心内容（Step 2）"""
    filled_content = []
    for section in outline:
        messages = [
            {"role": "system", "content": f"根据用户需求和大纲项 [{section}] 生成核心内容，要求包含关键数据和案例"},
            {"role": "user", "content": f"用户需求：{user_request}\n当前大纲项：{section}"}
        ]
        content = call_openai_api(messages)
        filled_content.append((section, content))
    return filled_content


def validate_and_expand(filled_content, user_request):
    """验证内容准确性并补充数据（Step 3）"""
    validated_content = []
    for section, content in filled_content:
        # 调用搜索引擎验证关键数据
        search_query = f"{section} {user_request} 验证数据"
        search_results = get_bing_search_results(search_query, config.subscription_key, config.search_url)

        # 扩展内容
        messages = [
            {"role": "system", "content": "根据搜索结果验证并扩展内容，修正错误数据，补充最新案例"},
            {"role": "user", "content": f"原内容：{content}\n搜索结果：{search_results}"}
        ]
        expanded_content = call_openai_api(messages)
        validated_content.append((section, expanded_content))
    return validated_content


def structure_report(validated_content, user_request):
    """结构化整合报告（Step 4）"""
    messages = [
        {"role": "system", "content": "将验证后的内容整合为完整报告，要求包含：摘要、章节内容、参考文献"},
        {"role": "user", "content": f"用户需求：{user_request}\n内容片段：{validated_content}"}
    ]
    return call_openai_api(messages)


def step_by_step_deepsearch(user_request):
    # Step 1: 生成大纲
    outline = generate_outline(user_request)
    print("INFO: 生成大纲:", outline)

    # Step 2: 填充核心内容
    filled_content = fill_section_content(outline, user_request)
    print("INFO: 核心内容填充完成")

    # Step 3: 验证与扩展
    validated_content = validate_and_expand(filled_content, user_request)
    print("INFO: 内容验证与扩展完成")

    # Step 4: 整合报告
    report = structure_report(validated_content, user_request)

    # 输出到文件
    with open('result.md', 'w', encoding='utf-8') as f:
        f.write(report)
    return report


# 示例调用
user_request = "对比分析TensorFlow和PyTorch的动态计算图实现机制"
result = step_by_step_deepsearch(user_request)