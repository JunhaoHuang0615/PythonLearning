import requests
import os
def getPagesData(keyword,pageNum):
    #找到每翻动一页，变动的XHR
    params = []
    for i in range(30,30*pageNum+30,30): #根据分析百度的网页，每页30个图片， 第三个参数为步长
        params.append ({
            'tn':'resultjson_com',
            'ipn':'rj',
            'ct':'201326592',
            'is':' ',
            'fp':'result',
            'queryWord':keyword,
            'cl':'2',
            'lm':'-1',
            'ie':'utf-8',
            'oe':'utf-8',
            'adpicid':' ',
            'st':' ',
            'z':' ',
            'ic':' ',
            'hd':' ',
            'latest':' ',
            'copyright':' ',
            'word':keyword,
            's':' ',
            'se':' ',
            'tab':' ',
            'width':' ',
            'height':' ',
            'face':' ',
            'istype':' ',
            'qc':' ',
            'nc':'1',
            'fr':' ',
            'expermode':' ',
            'force':' ',
            'pn':i,
            'rn':'30',
            'gsm':' ',
        })
    url = 'http://image.baidu.com/search/acjson'
    urlData = []
    for eachdata in params:
        #向每一个页面发送请求,并获得数据
        res = requests.get(url,params = eachdata).json()['data']
        # print(res.content)
        #把获取每一个页面的数据存入序列中
        urlData.append(res)
    return urlData
# 下载得到的图片
def downloadingImg(datalist,path):
    # print(datalist)
    if os.path.exists(path) == False :
        os.mkdir(path)
    #循环下载数据
    #图片编号
    x = 0
    headers = {
        "User-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'
    }
    for eachdata in datalist:
        # print(eachdata)
        for each in eachdata:
            if each.get('thumbURL') != None:
                print(f"下载图片{each.get('thumbURL')}")
                #享图片地址发请求
                imgres = requests.get(each.get('thumbURL'),headers=headers)
                # print(imgres.content)
                print(imgres.status_code)
                with open(f'{path}/{x}.jpg','wb') as fp:
                    fp.write(imgres.content)
                x += 1


#获取用户输入的信息
keyword = input('Please enter the keyword you want to search ')
#调用函数，进行爬虫，可以指定关键字和下载页数
datalist = getPagesData(keyword,2)
#调用函数，保存数据，可以指定文件保存的路径
downloadingImg(datalist,'./baidutupian')