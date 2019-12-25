import requests
from lxml import etree
import re
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
            html = self.res.text
            # with open('./test3.html','w') as fq:
            #     fq.write(self.res.text)
            reg = '<a class="cd-link-major".*>(.*?)</a>'
            # <div class="my-course-item__info">
            # <div class="my-course-item__title text-overflow">
            # <a class="cd-link-major" href="/course_set/58">Unity API常用方法和类详细讲解（基于Unity5.6）</a>
            # </div>
            # <div class="my-course-item__progress cd-mt24 cd-clearfix">
            # <span class="my-course-item__progress__text">学习进度</span>
            # <div class="cd-progress cd-progress-sm">
            # <div class="progress-bar">
            # <div class="progress-outer">
            # <div class="progress-inner" style="width: 85%;"></div>
            # </div>
            # </div>
            # <div class="progress-text">85%</div>
            # </div>
            # </div>
            # </div>
            title_list = re.findall(reg,html)
            print(title_list)

obj = LSiki()