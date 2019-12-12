def f(x):
    return 2*x +1

lambda x:2*x +1 #这就相当于一个匿名方法，x是函数的参数，后面是return的方法体
g = lambda x:2*x+ 2 # 此时的g就相当于与一个方法了
adder = lambda x,y: x+y

print(adder(3,4))

#应用实例 
#filter([function][none],iterable)
filter(None,[1,2,5,True,213,False]) #这个方法的意义是把列表里面的false或者0值去掉
temp = list(filter(None,[1,2,5,True,213,False,0,2])) 
print(temp)
#如果前面不传none，传一个方法，则这个filter函数会将后面的可迭代的list，tuple的每一个值带入前面的方法，过滤掉false或者0的值
def odd(x):
    if x % 2 ==0:
        return False
    else:
        return True #其实可以不用true或者false，因为如果是偶数，余数则为0，那么就会被过滤掉
temp = list(filter(odd,[34,67,43,65,87,323,3,11,6]))
print(temp)
temp = list(filter(lambda x:x % 2,[11111,22222,33333,44444]))
#temp = list(filter(lambda x:x % 2 != 0,[11111,22222,33333,44444]))
print(temp)

#map()函数，map映射的意思
#map([function][none],[iterable]) 
#用意是将迭代序列中的所有元素放入方法中，返回值形成一个新的序列
temp = list(map(lambda x: x * 2 , [1,2,3,4,5,6,7,8,9,0]))
print(temp)
temp = list(map(lambda x,y: x+y,[1,2,3,4,5],[2,4,6,8,10])) #如果参数有两个，则需要两组序列
print(temp)

