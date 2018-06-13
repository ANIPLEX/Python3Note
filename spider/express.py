import json,requests
def searchExpress():
    #输入运单号码
    expressNum = input('请输入运单号码：')
    express1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + expressNum
    #用快递API接口返回Json数据存入companyName 二维数组取得comCode字段对应的快递公司
    companyName = json.loads(requests.get(express1).text)['auto'][0]['comCode']
    #在用express2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
    express2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + expressNum
    #遍历json中date字段的值
    for item in json.loads(requests.get(express2).text)['data']:
        print(item['time'],item['context'])

searchExpress()