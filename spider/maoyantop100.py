import requests
from multiprocessing import pool
from requests.exceptions import RequestException
import re
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?">([0-9]{1,2}|100)</i>.*?data-src="(.*?)"'
                         +'.*?<a.*?>(.*?)</a></p>.*?star">(.*?)</p>.*?releasetime">'
                          +'(.*?)</p>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'Rank':item[0],
            'imageurl':item[1],
            'title':item[2],
            'actor':item[3],
            'time':item[4]
        }

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)

if __name__ == '__main__':
    for i in  range(10):
        main(i*10)
    # pool = Pool()
    # pool.map(main,[i*10 for i in range(10)])
