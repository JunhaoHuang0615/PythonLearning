import urllib.request  #导入网络爬虫包
response = urllib.request.urlopen("https://www.bilibili.com/video/av27789609?p=54") #这个就是从服务器获取网站的过程，获得网页的源代码
html = response.read() #把这个网页的 二进制 数据都城字符串
html = html.decode('utf-8')
print(html)
