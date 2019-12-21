#一般的翻译网站，当我们输入翻译内容的时候，翻译是自动出来的，并没有刷新，这个时候的请求方式大多都是POST请求
import requests
#定义请求的url：
url = 'https://fanyi.baidu.com/sug' #这个url主要是看网站上通过这个url返回的是一个什么东西，先过去网站上去看

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#Post发送的数据
data = {'kw':'你好'}

#发送get请求
res = requests.post(url=url,headers = headers,data = data)

code = res.status_code
if(code == 200):
    print('请求成功')
    #接收返回数据
    data = res.json()
    if(data['errno'] == 0):
        print('响应成功')
        k = data['data'][0]['k']
        v = data['data'][0]['v'].split(';')[-2]
        print(k,'===',v)
    # print(res.json())