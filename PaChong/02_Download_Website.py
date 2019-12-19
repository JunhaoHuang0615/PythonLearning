import urllib.request  #导入网络爬虫包
response = urllib.request.urlopen("http://www.ljecy.com") #这个就是从服务器获取网站的过程，获得网页的源代码
html = response.read() #把这个网页的 二进制 数据都城字符串
#如果这个网站是一个图片或者视频，那么可以直接通过二进制，open的方法把它存储下来
# with open ("[filename].[filetype]",'wp') as f:
#   f.write(html)
html = html.decode('utf-8')
print(html)

print(response.geturl()) #得到url
#response.getcode() 这个如果是200，说明网页是可以打开的，404则为找不到
#在社差元素的时候：  Method：Get 是向服务器请求获得数据
                #          Post： 向指定拂去其提交被处理的数据
                #   NetWork：User Agent: 这个是识别是浏览器访问，还是代码访问