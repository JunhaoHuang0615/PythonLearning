import re
#正则表达式：
#re.match() 函数： 要么第一个就符合要求，要么不符合,只匹配开头
str1 = 'i love you si mi da123da 456 love'
str2 = "love "
str3 = " love"
reg = 'love'
result = re.match(reg,str1)
print(result)
result = re.match(reg,str2) 
print(result)
print(result.group()) #可以用group来获取match的返回对象
print(result.span()) #获取匹配结果的下标
result = re.match(reg,str3) 
print(result)

print('----------search----------')
#re.search() 函数： 为从头匹配到结尾，进行搜索，有就返回match对象,只返回一个
result = re.search(reg,str1)
print(result)
result = re.search(reg,str2) 
print(result)
print(result.group()) #可以用group来获取match的返回对象
print(result.span()) #获取匹配结果的下标
result = re.search(reg,str3) 
print(result)

#re.findall()
result = re.findall(reg,str1)
print(result)
result = re.findall(reg,str2)
print(result)
result = re.findall(reg,str3)
print(result)

#re.finditer() 返回一个迭代器，可以转换成list，或者tuple等

#re.sub() 搜索替换 参数： pattern:正则表达式的规则    repl:替换后的字符串    string: 被替换的原始字符 返回值：字符串

#把一个正则表达式转换成一个正则对象，然后通过正则对象去调用上面的方法
reg = re.compile('\d{3}')
str1 = 'dhsaudhsaf123ncsw3245jksndfd23ncjkds453' #注意：324也会被匹配，但是3245不会
print(reg.findall(str1))

lines = [
    '4324ffdsf4325dsad23',
    'dsahjd78323hjkhasd874bjhbxcdf8s7fdgsa643',
    '666hc6766e3bbdsy87342bjkbfsd6yf78'
    ]
print('----------------------')
for i in lines:
    res = reg.findall(i)
    print(res)

print("正在表达式，不区分大小写模式")
str2 = 'dgsTTT'
reg = "[a-z]{5,10}"
result = re.search(reg,str2)
print(result)
result = re.search(reg,str2,re.I)
print(result)