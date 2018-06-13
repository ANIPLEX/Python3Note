import json,requests
while True:
    print(json.loads(requests.get('https://v1.hitokoto.cn/').text)['hitokoto'])