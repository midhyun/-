from django.test import TestCase

# Create your tests here.
import json
import requests
"https://kauth.kakao.com/oauth/authorize?client_id=6fd6f93cc19bfd4fb51226ad8e0c1e82&redirect_uri=https://example.com/oauth&response_type=code"

import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '6fd6f93cc19bfd4fb51226ad8e0c1e82'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'qS1IS4ZIH6GwoQN4rR7d3H4WofRm8Aeh14xIvy1vJGoyWdPrMi9BGLn2v1ZJ5Ie6sGJcZQo9dJcAAAGEYokpkg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)

