import requests
from credentials import GPT_TOKEN


def ask_chat_gpt(question):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {GPT_TOKEN}'}
    data = {'model': 'gpt-3.5-turbo','messages': [{'role': 'user', 'content': question}]}
    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    return data['choices'][0]['message']['content']
