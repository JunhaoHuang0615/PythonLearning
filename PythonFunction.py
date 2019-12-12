def myfirstFunction():
    print("this is my first function")

myfirstFunction()

name = "Ken"
def sayHello(name):
    print(name + " こんにちは")

sayHello(name)

def addFunction(num1,num2):
    return num1 + num2

print(addFunction(1,2))

def function1(name):
    'this function is just a test'  #这个是函数的介绍
    print("you - "+name+"- are my king")

print(function1.__doc__) #打印函数的说明文
# help(function1) #访问函数的说明文

#关键字参数使得在赋值的时候可以不遵循顺序
def notOrder(name, words):
    print(name + " " + words)

notOrder(words="my", name = "you")

#默认参数
def defaultMethod(name = 'default', age = "1"):
    print(name + " is " +age +" years old")

defaultMethod() #有了默认参数，则不给参数也不会报错了
defaultMethod('Ken', "1000")

#不确定的参数个数
def infinitePar(*params):
    print(params)                 #this is a tuple
    print(params[0]+params[1])

infinitePar(2,3,4,5,6)
#如果即想有收集参数，又想有确定的参数
def mixMethod(*params, name):
    print(name + " wants to know"+str(params))

mixMethod(123,456,785,name = "Ken")

#函数的返回值
def function2():
    return [1,2,"123"] #这样是返回一个列表

def function3():
    return 3213,6,"shsad"  #这是返回一个元祖