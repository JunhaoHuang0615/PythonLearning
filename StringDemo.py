str1 = "www.ljecy.com"
print(str1[:7])

#把字符串的开头改为大写
str2 = str1.capitalize()
print(str2)
print(str1) #不是在源字符串上做改动

#把字符串弄成小写
str3 = "IUYIYTGFGSAS"
str2 = str3.casefold()
print(str2)
print(str3)

#把字符串居中
str2 = str3.center(40) #这样左边和右边都会有40个空格

#检查某个字符串是否以某一个字符结束
print(str1.endswith(".com"))

#查找某一个子字符串是否存在于字符串中，返回下标值,没有则返回-1
print(str1.find(".com"))

#判断一个字符串是否只含有字母或者数字
str1 = "www.ljecy.com"
str2 = "sadasdsafdsgter"
str3 = "sdasd12343hdjsahdfasd"
str4 = "1232412341234231"
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())
print(str4.isalnum())

#判断一个字符串是否全都是字母
print("-----------")
print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())

str5 = "32.1"
print("----------decimal")
#一个字符串是否只包含十进制数字
print(str1.isdecimal())
print(str2.isdecimal())
print(str3.isdecimal())
print(str4.isdecimal())
print(str5.isdecimal())

print("-------------digit")
#一个字符串是否只包含数字
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
print(str4.isdigit())
print(str5.isdigit())

print("lower or upper")
#一个字符串中至少包含一个小写字母,且不可以有大写
str1 = "asdgsadUYIYUBG4325"
str2 = "IUGHGH5653212"
str3 = "hjsakdsadggsgdas"
str4 = "sgdasdhgjsdaas6767323"
print(str1.islower())
print(str2.islower())
print(str3.islower())
print(str4.islower())

#一个字符串中是否包含大写字母，且不可以有小写
print(str1.isupper())
print(str2.isupper())

#一个字符串是否只有空格
str1 = "         ";
str2 = "     23     "
print(str1.isspace())
print(str2.isspace())

#以当前字符串作为分割符，把传递的字符串隔开
str1 = " "
str2 = str1.join("iloveyou")
print(str2)

#去掉字符串左边空格
str1 = "  dsahdsa dsahdsa dsa   "
print(str1.lstrip()) # it is l but not i

#去掉末尾的空格 
print(str1.rstrip())

#前面后面都要删则用 strip(),但如果给了一个参数，则会把字符串前后的这个字符都去掉
str8 = "sssssgdhsdsssssss"
print(str8.strip("s"))
str9 = "sasasasauierewrewrvgfsahufdsfsasasasasa"
print(str9.strip("sa"))

#根据某一个字符串把它分成3个元祖
str2= "wo ai ni ni ai wo ma"
print(str2.partition("ai"))

#将字符串的某个子串给替换掉
print(str2.replace("ai","hen")) #注意是所有的,且不影响原来的字符串
print(str2)

#把某个字符串按照某一个字符进行切分,返回一个列表
print(str2.split()) #不带参数则是按照空格进行切分
str3 = "3213&dasdsad&dsadsa&fghsdgf*()"
print(str3.split("&"))

#大小写反转  swapcase()
#把字符串中的某个部分按照规则转换
str7 = "sssssssaaaaaaasssssss"
print(str7.translate(str.maketrans('s','b')))
#规则可以使用正则表达式
