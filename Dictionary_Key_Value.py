brand = ["tsubasa","gennmetsu",'usagi']
slogan = ['世界よ、我に従え！！','滅べ！','バカ']
print(brand[1],'のセリフは',slogan[brand.index("tsubasa")])

#这样子想反映一一对应的的关系太麻烦了，我们可以用字典的方式
dict1 = {"tsubasa":'世界よ、我に従え！！',"gennmetsu":'滅べ！','usagi':"バカ"} #注意字典不是序列类型，不可迭代,是映射类型
#   key : value
print(dict1["tsubasa"]) #[]内部放的是键值

#构造字典的方法二
mappingObj = (["tsubasa",'世界よ、我に従え！！'],["gennmetsu",'滅べ！'])
dict2 = dict(mappingObj)
print(dict2)

#构造字典的方法三
dict3 = dict(tsubasa = '世界よ、我に従え！！', gennmetsu = '滅べ！',你是谁 = '不知道' )
print(dict3)

#改变键值
dict3['tsubasa'] = '君を愛している'
print(dict3)

#重新创建字典
dict1 = {}
dict1 = dict1.fromkeys((1,2,3),'number') #不是在原字典里面添加
print(dict1)
#打印键
for eachKey in dict1.keys():
    print(eachKey)
#打印键值
for eachValue in dict1.values():
    print(eachValue)
#打印键和值
for item in dict1.items():
    print(item)

#判断某个键是否在字典中
print(1 in dict1)
print(4 in dict1)

#清空字典
dict1.clear()
#最好不要用 dict1 = {}

#字典的拷贝
a = {1 : "213", 2:'3213'}
b = a
c = a.copy()
print(id(a))
print(id(b))
print(id(c)) #地址不同

#弹出字典内的数据
print(a.popitem()) #由于字典没有顺序，是随机弹出的,弹出后则没有了
print(a)

#加入数据进字典中
print(a.setdefault("你好",'不好'))
print(a)

#用其他字典去更新
a = {1 : 'a', 2 : 'b'}
b = {1 : 'c', 3 : 'f'}
a.update(b)
print(a)