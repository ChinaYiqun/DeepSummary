# Shocking! Ultra - Simplified DeepSummary, Unlock a New Way of In - Depth Information Mining with One Click! 😲
![img.png](img.png)
## I. Project Introduction
Are you still struggling with organizing and summarizing a vast amount of information? Do you long for an efficient and convenient tool that can quickly distill complex information into valuable content? Ultra - Simplified DeepSummary is the magical tool designed to solve these problems! 🚀

This project mainly consists of two core files, `tool.py` and `deepsearch_tst.py`. By integrating a variety of powerful functions, it realizes the full - process automation from the decomposition of user requests, information search, content polishing to the final report generation. Whether it's the research progress of new - energy batteries or information summarization in other fields, Ultra - Simplified DeepSummary can handle it easily, making information processing easier than ever before! 😎

## II. Highlights of Core Functions

### 1. Intelligent Task Decomposition (TaskAgent)
- Utilize the advanced OpenAI API to instantly decompose complex user requests into multiple independent sub - queries. Just like a super - intelligent assistant, it precisely grasps user needs and points the way for subsequent information searches. 🌟
- Example: Input "Research progress of new - energy batteries", and the system can quickly break it down into multiple targeted sub - questions, greatly improving the efficiency of information search.

### 2. Powerful Information Search (Bing Search)
- Deeply integrated with the Bing search engine, it can quickly and accurately obtain relevant web information. Moreover, it can conduct in - depth mining of search results and extract detailed web content to ensure the comprehensiveness and accuracy of information. 🔍
- Support customizing the number of searches, allowing you to flexibly adjust the number of search results according to actual needs to meet the requirements of different scenarios.

### 3. Professional Content Polishing (PolishAgent)
- It has a professional content - polishing function that can polish the raw content obtained from the Internet, making it more fluent, professional, and grammatically correct. Just like a senior editor, it adds luster to your content. ✨
- Combine the user's original request and sub - queries to ensure that the polished content closely revolves around the theme and is highly targeted.

### 4. Efficient Content Summarization (SummaryAgent)
- Organize and re - format all the polished content to generate a high - quality summary report. The report is not only rich in content and well - organized but also includes all reference links at the end of the text for users to further consult. 📄
- Support saving the summary report as a Markdown file and automatically optimize the titles in the file to make it more readable and professional.

## III. Code Structure Explanation

### 1. `tool.py`
- This file contains the core tool functions of the project, such as calling the OpenAI API, obtaining Bing search results, web content crawling, string cleaning, and Markdown title modification.
- Introduction to main functions:
  - `call_openai_api(messages)`: Call the OpenAI API to get the corresponding response based on the input messages.
  - `get_bing_search_results(query, subscription_key, search_url, top_n = 3)`: Obtain search results for the specified query through the Bing search engine.
  - `get_bing_search_detail_results(query, subscription_key, search_url, top_n = 3)`: Get detailed content of Bing search results, including the title, link, and specific content of the web page.
  - `WebCrawler` class: Used for asynchronous web content crawling and cleaning the content, removing Markdown links and useless information.
  - `clean_string(s)`: Remove all whitespace and escape characters from the string.
  - `modify_md_titles(file_path)`: Modify the titles in the Markdown file, add links to the titles, and improve the readability of the file.

### 2. `deepsearch_tst.py`
- This file implements the main logic of the entire information - processing process, including task decomposition, information search, content polishing, and summary report generation.
- Introduction to main functions:
  - `taskagent(user_request)`: Decompose the user request into multiple sub - queries.
  - `polishagent(content, user_request, sub_query)`: Polish the content of the search results.
  - `summaryagent(user_request, task_info, search_results_list, polished_content_list)`: Organize all the polished content to generate a summary report.
  - `deepsearch(user_request)`: The main function, call the above functions to complete the entire information - processing process, and save the final result as a Markdown file.

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

Come and experience the charm of Ultra - Simplified DeepSummary! Let information processing no longer be cumbersome and start a new chapter of efficient information mining! 🎉# Shocking! Ultra - Simplified DeepSummary, Unlock a New Way of In - Depth Information Mining with One Click! 😲

## I. Project Introduction
Are you still struggling with organizing and summarizing a vast amount of information? Do you long for an efficient and convenient tool that can quickly distill complex information into valuable content? Ultra - Simplified DeepSummary is the magical tool designed to solve these problems! 🚀

This project mainly consists of two core files, `tool.py` and `deepsearch_tst.py`. By integrating a variety of powerful functions, it realizes the full - process automation from the decomposition of user requests, information search, content polishing to the final report generation. Whether it's the research progress of new - energy batteries or information summarization in other fields, Ultra - Simplified DeepSummary can handle it easily, making information processing easier than ever before! 😎

## II. Highlights of Core Functions

### 1. Intelligent Task Decomposition (TaskAgent)
- Utilize the advanced OpenAI API to instantly decompose complex user requests into multiple independent sub - queries. Just like a super - intelligent assistant, it precisely grasps user needs and points the way for subsequent information searches. 🌟
- Example: Input "Research progress of new - energy batteries", and the system can quickly break it down into multiple targeted sub - questions, greatly improving the efficiency of information search.

### 2. Powerful Information Search (Bing Search)
- Deeply integrated with the Bing search engine, it can quickly and accurately obtain relevant web information. Moreover, it can conduct in - depth mining of search results and extract detailed web content to ensure the comprehensiveness and accuracy of information. 🔍
- Support customizing the number of searches, allowing you to flexibly adjust the number of search results according to actual needs to meet the requirements of different scenarios.

### 3. Professional Content Polishing (PolishAgent)
- It has a professional content - polishing function that can polish the raw content obtained from the Internet, making it more fluent, professional, and grammatically correct. Just like a senior editor, it adds luster to your content. ✨
- Combine the user's original request and sub - queries to ensure that the polished content closely revolves around the theme and is highly targeted.

### 4. Efficient Content Summarization (SummaryAgent)
- Organize and re - format all the polished content to generate a high - quality summary report. The report is not only rich in content and well - organized but also includes all reference links at the end of the text for users to further consult. 📄
- Support saving the summary report as a Markdown file and automatically optimize the titles in the file to make it more readable and professional.

## III. Code Structure Explanation

### 1. `tool.py`
- This file contains the core tool functions of the project, such as calling the OpenAI API, obtaining Bing search results, web content crawling, string cleaning, and Markdown title modification.
- Introduction to main functions:
  - `call_openai_api(messages)`: Call the OpenAI API to get the corresponding response based on the input messages.
  - `get_bing_search_results(query, subscription_key, search_url, top_n = 3)`: Obtain search results for the specified query through the Bing search engine.
  - `get_bing_search_detail_results(query, subscription_key, search_url, top_n = 3)`: Get detailed content of Bing search results, including the title, link, and specific content of the web page.
  - `WebCrawler` class: Used for asynchronous web content crawling and cleaning the content, removing Markdown links and useless information.
  - `clean_string(s)`: Remove all whitespace and escape characters from the string.
  - `modify_md_titles(file_path)`: Modify the titles in the Markdown file, add links to the titles, and improve the readability of the file.

### 2. `deepsearch_tst.py`
- This file implements the main logic of the entire information - processing process, including task decomposition, information search, content polishing, and summary report generation.
- Introduction to main functions:
  - `taskagent(user_request)`: Decompose the user request into multiple sub - queries.
  - `polishagent(content, user_request, sub_query)`: Polish the content of the search results.
  - `summaryagent(user_request, task_info, search_results_list, polished_content_list)`: Organize all the polished content to generate a summary report.
  - `deepsearch(user_request)`: The main function, call the above functions to complete the entire information - processing process, and save the final result as a Markdown file.

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

