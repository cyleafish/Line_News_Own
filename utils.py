import requests
import logging
from bs4 import BeautifulSoup

def fetch_news_data(query, api_key):
    """
    使用 News API 获取新闻数据。
    """
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    return response.json()

def fetch_udn_news():
    """
    抓取聯合新聞網的最新新聞。
    """
    url = "https://udn.com/news/index"
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找新闻条目 (需要根据实际网页的结构进行调整)
    news_section = soup.find('section', {'id': 'tab1'})  # 假设新闻在id为'tab1'的section中
    news_items = news_section.find_all('a', href=True, limit=5)  # 获取前5条新闻

    news_list = []
    for item in news_items:
        title = item.get_text(strip=True)
        link = "https://udn.com" + item['href']
        news_list.append(f"{title}\n{link}")

    return "\n\n".join(news_list)

def generate_gemini_response(prompt, api_key):
    """
    使用 Gemini API 生成响应。
    """
    url = "https://api.gmini.ai/generate"
    payload = {"prompt": prompt}
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # 如果响应状态码不是 200，则引发 HTTPError
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to generate response: {e}")
        return {"error": "無法生成響應。"}
