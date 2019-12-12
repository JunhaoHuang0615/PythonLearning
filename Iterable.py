# iterable: keep repeating a process in order to approach or meet a goal
# When repeating once time, we can call it is once time iterable  
# like for loop
# iterable object such as String, List, tuple


# turn a String or tuple into List
b = "it is my great honor to know you"
b = list(b)
print(b)

c = (1,1,2,3,5,8,13,21,34)
c =list(c)

#turn list, String into tuple
b= [1,2,3,4]
b=tuple(b)
print(b)

# 得到序列的长度， 序列即list,string,tuple
print(len(b))

# 返回序列内的最大值
print(max(b))
b = [432,3,5345,-100,-1000]
print(max(b))
c="1234567890"
print(max(c))

# 最小值
print(min(b))

#sum 则为总和
print(sum(b))

#排序 
print(sorted(b)) #如果b是一个列表，则与list.sort()方法相同

#反转，但这个会反转成一个对象，通常搭配对应的类型使用
print(reversed(b)) 
print(list(reversed(b))) #即把这个对象转换成列表，注意，也可以转换成其他的，比如元祖

#生成枚举类型
b =[20,30,40,50,60]
print(enumerate(b))
print(list(enumerate(b))) #[(0, 20), (1, 30), (2, 40), (3, 50), (4, 60)] 就告诉我们，0代表20，1代表30，2代表40

#打包 zip， 把两个迭代对象合并
a=[12,5345,324,"sdad",32,88,12.4]
b=("wqd",1,4,32.1,5)
print(zip(a,b))
print(list(zip(a,b)))