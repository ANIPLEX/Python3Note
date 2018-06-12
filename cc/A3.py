#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 引用 json 库用于解析 json 对象
import json
# 使用 requests 库
import requests
print(json.loads(requests.get('https://v1.hitokoto.cn/').text)['hitokoto'])
