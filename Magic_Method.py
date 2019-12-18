#魔法方法总是可以在适当的时候被调用
# __init__  这个是构造函数的方法，创建实例时会被自动调用
class Rectangle():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def getA(self):
        return self.a
    def getB(self,b):
        self.b = b
    def getPeri(self):
        return (self.a+self.b)*2
    def getArea(self):
        return self.a * self.b

r1 = Rectangle(3,4)
print(r1.getArea())

#重写 __new__ 方法, 这是一个每一次实例化对象都一定会调用的方法，相当于java里的new
#想要一个类，这个类不管什么情况下，实例化时用户传过来的字符串不管是什么最终都要把字符串转化为大写的
class CapStr(str): 
    def __new__(cls,string):
        string = string.upper() #先把这个字符串全部转换成字符串
        return str.__new__(cls,string) #再依靠字符串类 （str）的new方法来创建出这个实例化对象

a = CapStr("this is a present")
print(a) 
#由于字符串是一个不可改变的类型

class C:
    def __init__(self):
        print(" i am __init__ method")
    def __del__(self): #这个方法是没有reference指向时会被调用的方法，我们给重写了.....
        print("我是del，我被执行了，再见....")

c1 = C()

c2 = c1 
del c2 #此时不会调用__del__，因为还是有c1去指向一个内存地址
del c1 #调用了__del__

