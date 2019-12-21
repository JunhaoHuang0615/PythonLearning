import requests
#url = 'https://www.ljecy.com' #https就是加密的，http没有加密
url = 'http://www.sikiedu.com/my/course/46' #这是一个代理服务器的网站
#定义请求头信息，再发送请求之前！ 可以上网去查
#这个是用我们自己的方法，先去获得cookie信息，然而我们还可以让python自己去寻找
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'cookie':'PHPSESSID=22g9io2ki7hgnrumu3gg57ae5j; _ga=GA1.2.30092853.1576843256; _gid=GA1.2.1463605262.1576843256; _gat=1; Hm_lvt_7b741b98bcf0532f9add944e2593c8af=1576843256; Hm_lpvt_7b741b98bcf0532f9add944e2593c8af=1576843256; online-uuid=3C7EF561-5510-536A-CACA-3B985DC12598'
}

#发送get请求
res = requests.get(url=url,headers = headers)
#获取相应状态码
code = res.status_code
print(code)  #code为503，则表示服务器拒绝你的请求，因为对方检测到我们是python

if(code == 200):
    with open('./test.html','w') as fp:
        fp.write(res.text)