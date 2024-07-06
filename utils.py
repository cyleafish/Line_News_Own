import requests
import logging
import google.generativeai as genai
import os

# Initialize Firebase (or any other database) to store conversation states
from firebase import firebase
firebase_url = os.getenv('FIREBASE_URL')
fdb = firebase.FirebaseApplication(firebase_url, None)

def fetch_news_data(query, api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to fetch news data: {response.status_code}")
        return {"status": "error", "message": "無法獲取新聞數據"}

def generate_gmini_story(prompt, api_key, user_id=None, user_choice=None):
    """
    Generate story using Google Gemini API. If user_id and user_choice are provided,
    continue the conversation based on the user's choice.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    # Fetch user conversation history from Firebase
    user_chat_path = f'/conversations/{user_id}'
    messages = fdb.get(user_chat_path, None) if user_id else None

    if messages is None:
        messages = [{'role': 'system', 'parts': [prompt]}]
    elif user_choice:
        messages.append({'role': 'user', 'parts': [user_choice]})

    try:
        response = model.generate_content(messages)
        if response and response.text:
            messages.append({'role': 'model', 'parts': [response.text]})
            # Update conversation history in Firebase
            if user_id:
                fdb.put_async(user_chat_path, None, messages)
            return response.text
        else:
            logging.error("No generations found in response.")
            return "無法生成故事。"

    except Exception as e:
        logging.error(f"Failed to generate story: {e}")
        return "無法生成故事。"
