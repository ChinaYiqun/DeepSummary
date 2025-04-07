# Shocking! Ultra - Simplified DeepSummary, Unlock a New Way of In - Depth Information Mining with One Click! 😲
![img.png](img.png)

## I. Project Introduction
Are you still struggling with organizing and summarizing a vast amount of information? Do you long for an efficient and convenient tool that can quickly distill complex information into valuable content? Ultra - Simplified DeepSummary is the magical tool designed to solve these problems! 🚀

This project mainly consists of several core files, including `tool.py`, `deepsearch_tst.py`, `deepsearch_obo.py`, and `deepsearch_rea.py`. By integrating advanced techniques such as OpenAI API and Bing search, it can help users quickly conduct in - depth information mining and generate high - quality summary reports.

## II. Highlights of Core Functions

### 1. Intelligent Task Decomposition (TaskAgent)
- Utilize the advanced OpenAI API to instantly decompose complex user requests into multiple independent sub - queries. Just like a super - intelligent assistant, it precisely grasps user needs and points the way for subsequent information searches. 🌟
- Example: Input "Research progress of new - energy batteries", and the system can quickly break it down into multiple targeted sub - questions, greatly improving the efficiency of information search.

### 2. Content Generation and Expansion
- **Outline Generation**: Based on the user's request, generate a 3 - level logical and coherent outline that covers the core issues.
- **Content Filling**: Fill in the core content according to the outline, including key data and cases.
- **Content Validation and Expansion**: Call the search engine to verify the key data in the content, correct errors, and supplement the latest cases.

### 3. ReAct - Based Research Process
- The `ReActResearcher` class uses a reflection - action mechanism. It can generate specific executable instructions according to the current state, such as search verification, content expansion, and outline reconstruction.
- The main loop continuously reflects and takes actions until the research is completed, gradually enriching the research content.

### 4. Efficient Content Summarization (SummaryAgent)
- Organize and re - format all the polished content to generate a high - quality summary report. The report is not only rich in content and well - organized but also includes all reference links at the end of the text for users to further consult. 📄
- Support saving the summary report as a Markdown file and automatically optimize the titles in the file to make it more readable and professional.

## III. File Introduction
- **`tool.py`**: Contains some utility functions, such as calling the OpenAI API, getting Bing search results, web crawling, and cleaning strings.
- **`deepsearch_tst.py`**: Implements the overall process of information summarization, including task decomposition, web information retrieval, content polishing, and summary report generation.
- **`deepsearch_obo.py`**: Follows a step - by - step process to generate a report, including outline generation, content filling, validation, and report structuring.
- **`deepsearch_rea.py`**: Implements a research process based on the ReAct mechanism, including reflection, action, and final report generation.

## IV. Usage Example
The following is a simple usage example showing how to call the `deepsearch` function for information summarization:
```python
from deepsearch_tst import deepsearch

# User request
user_request = "Research progress of new - energy batteries"

# Call the deepsearch function to generate a summary report
result = deepsearch(user_request)
```
After running the above code, the system will automatically create a folder named after the user request and generate multiple Markdown files in this folder, including the polished content of each sub - query and the final summary report `result.md`.

## V. Precautions
- Before using this project, please ensure that you have correctly configured the `config.py` file, including relevant information about Azure OpenAI and the subscription key for Bing search. ⚠️
- Since it involves network requests and API calls, it may be affected by network conditions and API usage limits. Please ensure a stable network connection and use API resources reasonably.

Come and experience the charm of Ultra - Simplified DeepSummary! Let information processing no longer be cumbersome and start a new chapter of efficient information mining! 🎉


| File | Process Overview | Advantages | Disadvantages |
| --- | --- | --- | --- |
| `deepsearch_tst.py` | 1. Use the `taskagent` function to decompose the user's request into multiple sub - queries and enter a loop.<br>2. Sequentially call Bing search to obtain web information for each sub - query.<br>3. For each result obtained in step 2, use the `polishagent` function to polish the content.<br>4. Save the polished content of each sub - query as a separate Markdown file.<br>5. Use the `summaryagent` function to organize all the polished content, generate a summary report with reference links, and save it as `result.md`. Optimize the titles in the file. | - The process is clear, with each step having a clear division of labor, making it easy to understand and maintain.<br> - It supports saving the results of each sub - query separately, facilitating subsequent viewing and modification.<br> - The generated summary report includes reference links, which is convenient for users to further consult the information. | - Sequential calls to Bing search may lead to long search times when there are many sub - queries.<br> - Frequent calls to the OpenAI API may increase API usage costs. |
| `deepsearch_obo.py` | 1. Generate a 3 - level outline based on the user's request using the `generate_outline` function.<br>2. Fill in the core content according to the outline using the `fill_section_content` function, requiring key data and cases to be included.<br>3. Use the `validate_and_expand` function to call the search engine to verify key data, correct errors, and supplement the latest cases.<br>4. Use the `structure_report` function to integrate the verified content into a complete report containing an abstract, chapter content, and references, and save it as `result.md`. | - It adopts a step - by - step process, from outline generation to content filling, validation, and report integration. The logic is rigorous, and it can generate relatively complete and standardized reports.<br> - It validates and expands the content, improving the accuracy and timeliness of the report. | - It relies on the OpenAI API to generate outlines and content, which may be affected by the performance and output quality of the API.<br> - The entire process is relatively fixed, with poor flexibility and difficulty in making flexible adjustments according to different needs. |
| `deepsearch_rea.py` | 1. Initialize the `ReActResearcher` class, which contains research context information.<br>2. In the `research_loop` function, perform multiple reflection and action cycles:<br>    - If there is no outline, automatically trigger outline construction.<br>    - Call the `reflect` function to generate specific executable instructions based on the current state.<br>    - According to the instructions, call the `act` function to perform corresponding operations, such as search verification, content expansion, and outline reconstruction.<br>3. When the instruction is "Research completed", end the loop and call the `generate_report` function to organize the research results into a complete report and save it as `react_result.md`. | - It adopts the Reflection - Action (ReAct) mechanism, which can dynamically adjust the research strategy according to the current state, with strong flexibility and adaptability.<br> - It can continuously optimize the outline and content during the research process, improving the quality and efficiency of the research. | - The implementation logic is relatively complex, with high understanding and maintenance costs.<br> - There is a limit on the number of loops (default is 5 times), which may not be sufficient to complete complex research tasks. |