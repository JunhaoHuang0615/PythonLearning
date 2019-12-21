import requests
#url = 'https://www.ljecy.com' #https就是加密的，http没有加密
url = 'https://www.xicidaili.com/nn' #这是一个代理服务器的网站
#定义请求头信息，再发送请求之前！ 可以上网去查
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

#发送get请求
res = requests.get(url=url,headers = headers)
#获取相应状态码
code = res.status_code
print(code)  #code为503，则表示服务器拒绝你的请求，因为对方检测到我们是python

if(code == 200):
    with open('./test.html','w') as fp:
        fp.write(res.text)
