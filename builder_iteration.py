#生成器： yield
def myGen():
    print('生成器')
    yield 1
    yield 2
# 这个还是有了yield，就说明是一个生成器的函数了
# 它的意思是第一次调用没执行一次方法体，返回yield 1， 第二次返回yield2

#使用方法
myGen1 = myGen()
print(next(myGen1))

print(next(myGen1)) # 第二次就执行 第二个 yield了

def lib():
    a= 0
    b=1
    while True:
        a , b =b , a + b
        yield a

for each in lib():
    if each > 100:
        break
    print(each)

# 字典推导式
b = {i : i % 2 == 0 for i in range(10)}
print(b)

#生成器推导式
e = (i for i in range(10))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))

#推导式作为一个参数
print(sum(i for i in range(0,100) if i%2))