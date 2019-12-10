# for i in range(0,9):  #想到于JAVA里面的Foreach， 后面的Range会自动生成一个数组
#     print(i)

# for each in range(3,100,10): #第三个数据为步长
#     print(each)

# for i in range(10): #没有限制开始的值，默认从0开始
#     print(i)


# Create List  注意使用[] 而不是JAVA里面构造数组的{}
member = ["Ken","Jack","Hero"]

mix = ["1",1,3,[4,6,"baka"],'a']

#get length of a list
len(mix)

#add element into list
mix.append("opo")

for i in mix:
    print(i)
print(len(mix))

#用一个列表去扩展另一个列表，传递的参数也是一个列表
mix.extend([12,4324,"mamamiya",[23,6456,"这又是一个元素"],78323])

for i in mix:
    print(i)

#插入在一个列表的某一个位置
mix.insert(0,"123213") #插入在一个第一个位置
mix.insert(3,[23213,5345]) #插入一个列表 会把这个列表当做一个元素插入进去

print("-----------------------------")
for i in mix:
    print(i)

#删除元素：
    #知道参数得我值
mix.remove("mamamiya")
    #想删除某个下标的元素,且其他元素会自动前移
del mix[1]
    #pop 由于列表其实是按照栈来存储的，先进后出原则
mix.pop() #把最后一个元素弹出去
mix.pop(2) # 弹出某个特定的元素

print("+++++++++++++++++++++++++++++++++")
for i in mix:
    print(i)
#拷贝list中的某一个部分

subList1 = mix[3:7]
subList2 = mix[:3]
subList3 = mix[5:]
copyMix = mix[:]
print(mix)
print(subList1)
print(subList2)
print(subList3)
print(copyMix)


