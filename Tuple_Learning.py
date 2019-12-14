#元祖和列表用法差不多，只是元祖是不可以修改内部的元素的
tuple1 = (3,6,8,3,4)
tuple2 = tuple1[1:3]
print(tuple1[1])
print(tuple2)

temp = (1)
print(type(temp))
temp2 = 2,4,6
print(type(temp2))

#创建一个空元祖
tupleEmpty = ()
#创建一个只有一个元素的元祖
tupleOne = (1,) #或者不用括号

tuple3 = 8 * (8,)
print(tuple3)

temp = (123,"123",88)
temp = temp[:1] + (67,"78")+temp[1:] #由于不能直接对元祖改动，我们只能重新赋值啦，元祖是基本类型噢
print(temp)

#元组变量,变量可以通过组的形式，对应的来赋值
(temp,temp2) = ['123',12]
print(temp)
print(temp2)
print(type((temp,temp2)))