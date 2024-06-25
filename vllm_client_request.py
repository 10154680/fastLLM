import json

import requests

def clear_lines():
    print('\033[2J')


history = []

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token-123",
}

# 调用api_server
response = requests.post('http://192.168.108.4:8888/v1/completions', headers=headers, json={
    "model": "/root/model/Qwen-14B-Chat-Int4",
    "prompt": "陕西省会是哪里",
    "max_tokens": 7,
    "temperature": 0
}, stream=True)

data = json.loads(response.content)
text = data["choices"][0]["text"].rstrip('\r\n')
print(text)
