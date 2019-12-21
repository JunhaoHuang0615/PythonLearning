import requests

#最终访问地址
url = 'http://www.zmz2019.com/user/user'

#登录请求的地址
urlLog = 'http://www.zmz2019.com/User/Login/ajaxLogin'

#请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

#需要爬虫主动记录cookie并且携带cookie，那么要在requ之前调用session方法
#并使用session方法发送请求
req = requests.session()

#登录的数据：
data = {
    'account':'yichuang@itxdl.cn',
    'password':'pyTHON123',
    'remember':'1',
    'url_back':'http://www.zmz2019.com/user/user'
}
#用session发送请求，得到回应
res = req.post(url = urlLog, headers = headers, data = data)

#判断状态
code = res.status_code
print(code)
if(code == 200):
    #接收数据
    res = req.get(url = url, headers = headers)
    with open('./test2.html','w') as fq:
        fq.write(res.text)