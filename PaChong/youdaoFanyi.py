#先去有道的页面，获取Network下，XHR(专门处理不刷新自动发送请求的脚本)的服务器地址
#Request URL: http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
#Request Method: POST
#data:
'''
i: 123  这个就是要翻译的文案
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15771127261875
sign: 817bfed6d88c4a41e3593a2598361715
ts: 1577112726187
bv: 88e4853c728099c68c5344d28efe9e83
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME

'''
import requests
#请求的url
URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule" #这里去掉了translate_o后面的_o，避开验证，别说为啥，反正就是要去掉....否则有res.text是errorcode:50
#定义请求的数据
content = input("请输入你要翻译的内容")
data = {
    'i' : content,
    'doctype':'json'
}

res = requests.post(URL,data)
if(res.status_code == 200):
    print('request accepted')
    #如果返回类型是一个json文件，那么可以直接解析
    resData = res.json()
    if resData['errorCode'] == 0:
        print('请求成功')

# 查看请求结果
        print(resData['translateResult'][0][0]['tgt'])


