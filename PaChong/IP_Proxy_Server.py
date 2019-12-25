'''
代理IP:
党同一个ip频繁请求一个网站是，对方会认为是攻击或者盗取数据，对方会禁用你的ip
因此我们可以使用代理IP
透明代理： 远程服务器是知道你使用了代理的，如一个小孩去买酱油，超市老板一定知道你不是给自己买的，对方是知道你使用的真是ip的
匿名代理： 对方不知道你的真是IP，但知道你是代理
高匿代理： 对方不知道你是代理

'''

import requests
# from fake_useragent import  UserAgent

# ua = UserAgent()

#定义代理IP
proxies = {
    'http':'47.104.67.148:3128',
    'https':'47.104.67.148:3128'
}

#获取访问ip的地址
try:
    url = 'http://httpbin.org/get'
    headers = {
        "User-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    res = requests.get(url,headers,proxies = proxies,timeout = 5) #timeout参数是如果代理地址无法响应，5秒后就结束了
    if res.status_code == 200:
        print('地址访问成功')
        resData = res.json()
        print(resData['origin'])
except:
    print("请求失败")
