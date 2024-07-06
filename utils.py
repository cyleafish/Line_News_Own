import requests
import logging
import google.generativeai as genai

def fetch_news_data(query, api_key):
    #Fetch news data from News API.
    
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()


def generate_gmini_story(prompt, api_key):

    #Generate story using Google Gemini API.

    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    response = model.generate_content(promot)
    return response.text




"""        
def generate_gmini_story(prompt, api_key):
    
    #Generate story using Google Gemini API.
    
    #url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}

    # 创建一个会话对象并配置重试策略
    session = requests.Session()
    retry = Retry(
        total=5,  # 最大重试次数
        backoff_factor=1,  # 重试之间的等待时间
        status_forcelist=[429, 500, 502, 503, 504]  # 重试的 HTTP 状态码列表
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    try:
        response = session.post(url, json=payload, headers=headers)
        response.raise_for_status()  # 如果响应状态码不是 200，则引发 HTTPError
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to generate story: {e}")
        return {"error": "無法生成故事。"}
"""
# 配置重试策略所需的导入
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
