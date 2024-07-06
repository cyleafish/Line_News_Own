import requests
import logging
import google.generativeai as genai

def fetch_news_data(query, api_key):
    """
    Fetch news data from News API.
    """
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # 确保请求成功，否则引发异常
    return response.json()

def generate_gmini_story(prompt, api_key):
    """
    Generate story using Google Gemini API.
    """
    # 配置 Google Gemini API Key
    genai.configure(api_key=api_key)

    try:
        # 调用 Google Gemini API 生成内容
        response = genai.generate_content(prompt=prompt)
        
        # 检查响应内容并提取故事文本
        if 'contents' in response and response['contents']:
            parts = response['contents'][0].get('parts', [])
            if parts:
                return parts[0].get('text', "没有故事。")
        return "没有故事。"
    
    except Exception as e:
        logging.error(f"Failed to generate story: {e}")
        return {"error": "無法生成故事。"}
