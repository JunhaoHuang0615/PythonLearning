#一般情况下我们是通过浏览器去发送请求，现在我们用python来向服务器发送请求
import requests
#发起请求的URL
url = 'https://www.baidu.com' #https就是加密的，http没有加密
#发送get请求
res = requests.get(url=url)
#获取响应结果
print(res) #<Response [200]> 200的意思就是网页存在
print('--------------------------------------')
print(res.text) #跟decode那个一样
print('--------------------------------------')
print(res.content.decode('utf-8')) #二进制文本流转换成utf-8字符集
print('--------------------------------------')
print(res.headers)#响应头信息
#{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Fri, 20 Dec 2019 10:34:29 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:24:33 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
print('--------------------------------------')
print(res.status_code) #请求状态码
print('--------------------------------------')
print(res.request.headers)#请求的头信息
#{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#python-requests/2.22.0明确告诉是python程序发的请求
print('--------------------------------------')
print(res.content) #这个就是二进制的文本流