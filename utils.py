import requests
import logging
import google.generativeai as genai
import os

def fetch_news_data(query, api_key):
    """
    Fetch news data from News API with a focus on Traditional Chinese (Taiwan) content.
    """
    # 指定语言为繁体中文（zh），国家为台湾（tw）
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to fetch news data: {response.status_code}")
        return {"status": "error", "message": "無法獲取新聞數據"}

def generate_gmini_story(prompt, api_key):
    """
    Generate story using Google Gemini API.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = "使用繁體中文回答\n" + prompt
    try:
       
        response = model.generate_content(prompt)
        # 提取生成的内容
        if response and response.text:
            return response.text
        else:
            logging.error("No generations found in response.")
            return "無法生成故事。"

    except Exception as e:
        logging.error(f"Failed to generate story: {e}")
        return "無法生成故事。"
choose = "請輸入選擇編號。如【A1.a】"
def story_A(message):
    start = ("歡迎來到超級英雄訓練營！在這裡，我們不分男女，每個人都有機會成為超級英雄！今天，我們要學習如何辨別和挑戰不公平的性別刻板印象。準備好了嗎？\n\n"+
            "訓練營的第一堂課是角色扮演。老師宣布：「今天我們要扮演拯救世界的超級英雄！男生扮演勇敢強壯的超人，女生扮演溫柔善良的護士！」\n"+
            "你聽到老師的話，心裡覺得怪怪的。這時，你有三個選擇：\n\n"+
            "A1.a：舉手跟老師說：「老師，為什麼男生一定要當超人，女生一定要當護士？我覺得女生也可以很勇敢，男生也可以很溫柔啊！」\n"+
            "A1.b：跟旁邊的同學小聲說：「你不覺得老師這樣說怪怪的嗎？為什麼女生不能當超人？」 \n"+
            "A1.c：什麼都不說，乖乖聽老師的話。"
            )
    A1a = ("太棒了！你勇敢地表達了自己的想法，也讓老師和其他同學意識到性別刻板印象的問題。\n"+
           "老師聽完你的話後，思考了一下，笑著說：「你說得對！我們不應該被傳統觀念限制，每個人都可以成為自己想成為的樣子！這樣吧，我們讓大家自由選擇角色，好不好？」"
          )
    A1b = ("你向身邊的同學表達了你的想法，很棒！你們可以一起思考，試著找機會跟老師或其他同學討論這個問題。")
    A1c = ("你選擇了沉默，但心裡可能還是有些不舒服。沒關係，意識到問題的存在就是一個好的開始。\n"+
           "下次遇到類似的情況，試著勇敢一點，表達你的想法吧！")
    
    if "A開始體驗劇本：超級英雄訓練營！" == message:
        return start
        
    elif "A1.a" == message:
        return A1a

    elif "A1.b" == message:
        return A1b
        
    elif "A1.c" == message:
        return A1c

    else:
        return choose
        
    
