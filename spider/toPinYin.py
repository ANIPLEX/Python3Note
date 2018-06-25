
import json
from spider.ShowapiRequest import ShowapiRequest


class PinYin():
    def toPinYin(ww):
        r = ShowapiRequest("http://route.showapi.com/99-38", "67537", "ad4e84171bde4260996a2076adeb7d76")
        r.addBodyPara("content", ww)
        res = r.post().text
        j = json.loads(res)['showapi_res_body']['data']
        a = j.replace(' ', '')
        return a


print(PinYin.toPinYin(''))
