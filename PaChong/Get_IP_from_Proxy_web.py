import requests
import re
import time 
# url = 'https://www.kuaidaili.com/proxylist/1'
# headers = {
#         "User-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
#     }

# res = requests.get(url,headers=headers)
# if res.status_code ==200:
#     print('请求成功')
#     #获取数据
#     resData = res.content.decode('utf-8')
#     #<td data-title="IP">114.239.199.233</td>
#     reg1 = '<td data-title="IP">(.*?)</td>' #获取ip
#     reg2 = '<td data-title="PORT">(.*?)</td>' #获取端口

#     ip_list = re.findall(reg1,resData)
#     post_list = re.findall(reg2,resData)
#     ip_post = list(zip(ip_list,post_list))
#     ip_post_list = []
#     for i in range(len(ip_post)):
#         conbine = ip_post[i][0] + ':' + ip_post[i][1]
#         ip_post_list.append(conbine)
#     print(ip_post_list)

#如果是分页，则要先分析每一个页数的url
def getpage(url):
    headers = {
        "User-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    if res.status_code ==200:
        print('请求成功')
        #获取数据
        resData = res.content.decode('utf-8')
        return resData

#抓取当前页的ip和port
def getInfo(resData):
    reg1 = '<td data-title="IP">(.*?)</td>' #获取ip
    reg2 = '<td data-title="PORT">(.*?)</td>' #获取端口
    ip_list = re.findall(reg1,resData)
    post_list = re.findall(reg2,resData)
    ip_post = list(zip(ip_list,post_list))
    ip_post_list = []
    for i in range(len(ip_post)):
        conbine = ip_post[i][0] + ':' + ip_post[i][1]
        ip_post_list.append(conbine)
    # print(ip_post_list)
    return ip_post_list

#测试在当前页中抓取的ip，返回可用的ip列表
def testIp(ip_list):
    print(ip_list)
    url = 'http://httpbin.org/get'
    headers = {
        "User-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    aviliableIP = []
    for i in range(0,len(ip_list)):
        print('testing:',ip_list[i])
        try:
            proxies = {
                'http':ip_list[i],
                'https':ip_list[i]
            }
            res = requests.get(url,headers,proxies = proxies,timeout = 5) #timeout参数是如果代理地址无法响应，5秒后就结束了
            if res.status_code == 200:
                aviliableIP.append(ip_list[i])
        except:
            continue
    return aviliableIP

def main(num):
    #拼接url
    url = 'https://www.kuaidaili.com/proxylist/'+str(num)
    #调用页面请求的程序
    resData = getpage(url)
    temp_list = getInfo(resData)
    total_list = []
    aviliableIP = testIp(temp_list)
    print(aviliableIP)
    total_list.append(aviliableIP)
    print(total_list)
            

if __name__ == '__main__':
    for i in range(1,3):
        print(f'now is on the page {i}')
        main(i)
        time.sleep(2)

    

        





