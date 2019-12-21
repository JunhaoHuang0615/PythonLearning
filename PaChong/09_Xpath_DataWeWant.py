#XML文档中查找信息的语言，同样适用于html语言
#常用规则：
# 如果直接下标签名，那么就直接去搜索标签
# / 从当前子节点直接选取子节点
# // 从当前子节点选取子孙节点
# . 选取当前节点
# ..选取父级节点
# @ 选取属性
# 
# 例子： title[@lang = 'eng'] 查找title标签下的属性lang的值为eng的节点
# 
# 安装： xcode-select --install
#       接下来要安装Homebrew: ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
#      now we can use brew install command to install pakage, e.g:
            #brew install wget    #这个可以更新Homebrew
            #brew install libxml2 libxslt
#       pip3.8 install lxml     
#方法二： 从网站上面下载
#     pypi.org
from lxml import etree
text = '''
<!DOCTYPE html>
<html class="fp-enabled" style="overflow: hidden; height: 100%;"><head>
<meta charset="UTF-8">
<title>welcome to ljecy</title>

<link rel="stylesheet" type="text/css" href="css/jquery.fullPage.css">
	<link rel="stylesheet" type="text/css" href="css/examples.css">
<style>
img{display: block}
body{margin:0}
ul{list-style: none;margin:0;padding: 0;}
a{text-decoration: none;}
input{border:none;outline:none;margin:0;padding:0;}
.clearfix{clear:both;}

.logo{float:left; width:10%;margin: 10px 10px;transform: rotate(0deg);transition: 0.6s;}
li:hover .logo{transform:rotate(30deg);}
#section0 img,
#section1 img{
	margin: 0 0 0 0;
}
#section2 img{
	margin: 20px 0 0 52px;
}
#section3 img{
	bottom: 0px;
	position: absolute;
	margin-left: -420px;
}

'''
# #使用etree来解析html字符串
# html = etree.HTML(text)

# #提取数据
# r = html.xpath('html/body/ul/li/a/text()')
# print(r)

# r = html.xpath('html/body/ul/li[1]/a/text()') #XML中的下标从1开始

#第二种使用方式，读取并解析
html = etree.parse('./test.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))
r = html.xpath('//li/a/text()') #页面中所有的li
print(r)

r = html.xpath('//div[@class="teacher"]//li/a/text()')
h = html.xpath('//div[@class="teacher"]//li/a/@href')
print(*zip(r,h)) #放在元祖中
print(list(zip(r,h)))

