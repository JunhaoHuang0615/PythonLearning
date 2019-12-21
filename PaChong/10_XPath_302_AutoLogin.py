#分析
# Step1： get请求访问 login的页面， 拿到cookie和token

#step2： post请求  提交登录数据，进行登录，并且设置cookie

#step3：  get请求  去账户中心， 获取默认订单号

import requests
from lxml import etree

#使用一个类来进行获取信息
class LSiki:
    loginurl = "http://www.sikiedu.com/login"
    logSendurl = "http://www.sikiedu.com/login_check"
    targeturl = 'http://www.sikiedu.com/my/courses/learning'

    headers = {
        "User-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

    #请求对象
    req = None
    #token 口令
    token = ''
    #初始化方法
    def __init__(self):
        #请求对象的初始化
        self.req = requests.session()

        if self.getlogin():
            if self.postlogin():
                self.getInfo()
    
    # get登录页面， 获取_token
    def getlogin(self):
        self.res = self.req.get(url=self.loginurl,headers =self.headers)
        if(self.res.status_code == 200):
            print('requests accepted')
            html = etree.HTML(self.res.text)
            self.token = html.xpath('//input[@name="_csrf_token"]/@value') #input标签中包含name这个属性的标签，value这个属性的值为...
            #print(token)
            return True
        else:
            print("Error: rejected")
            return False
    
    def postlogin(self):
        usname = input('enter your username ')
        password = input('enter your password ')

        data = {
            #siki xueyuan
            '_username': usname,
            '_password': password,
            '_remember_me': 'on',
            '_target_path': 'http://www.sikiedu.com/my/courses/learning',
            '_csrf_token': self.token

        }
        # 发起post请求
        self.res = self.req.post(url = self.logSendurl, headers = self.headers , data = data)
        if self.res.status_code == 200 or self.res.status_code == 302:
            print('login successfully')
            return True

    #请求账户target
    def getInfo(self):
        self.res = self.req.get(url = self.targeturl,headers = self.headers)
        if(self.res.status_code == 200):
            print('切换页面成功,解析中')
            html = etree.HTML(self.res.text)
            r = html.xpath('//div[contains(@class, "my-course-item__title")]//a/text()')
            #如果一个属性里面包含多个值，那么可以这么写，注意 my-course-item__title 只是class的其中一个值
            x = html.xpath('//a[contains(@class,"my-course-item__link")]//img/@src') #如果一个标签有多个属性，要么用contains，要么全写上
            print (x)

#数据整理
# data = []
# for i in range(0,len(r)):
#     eachdict = {'name=':r , "img=":x}  ##有多个就在后面加
#     data.append(eachdict)


obj = LSiki()
