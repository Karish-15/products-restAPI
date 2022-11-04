import requests

endpoint = 'http://localhost:8000/api/products/'
data = {
    "title": "GFX card",
    "price": 32
}

headers = {
    'Authorization': "Token 9ad2800da4b7c59b207e57973f16a2958b0d1f07"
}

post_resp = requests.post(endpoint, headers=headers, json=data)
print(post_resp.json())