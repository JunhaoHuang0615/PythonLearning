class NewInt(int):
    #这是一个继承了int类的子类，因此int的方法它也有
    def __add__(self, value):
        return int.__sub__(self,value)
        #当这个类的对象执行加法时，实际上是执行父级int类里面的减法
    def __sub__(self, value):
        return int.__add__(self,value)
    #错误示范： 会出现无限递归
    # def __add__(self, value): #这里的self相当于a，value相当于调用a+b 后面的这个b
    #     return self + value #这里相当于又执行一次a+b 又调用一次__add__这个方法

a = NewInt('123')
b = int('123')
c = NewInt('2')
d = int('2')

print(a+b)  #执行的减法 后面的那一个数字只是一个参数，对应value，这里就是看调用的是谁的方法了
print(b+a)  #加法（看哪一个类型在前面了噢）
print(a+c)  #执行的减法
print(b+d)  #正常

class MyInt(int):
    #改写反加法函数
    def __radd__(self, value):
        return int.__sub__(self , value)
    
    def __rsub__(self, value):
        return int.__sub__(value , self) #注意一下操作符的位置，由于这里的self可是代表的后面一位

x = MyInt('1')
y = MyInt('2')
print(x+y)
print(1+x) #这里就会调用反加法，因为1并不能执行__add__这个时候，系统就会去找'+'号后面一个数执行__radd__，且把1当成value参数
