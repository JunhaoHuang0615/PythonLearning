class A:
    count = 0

class B(A):
    pass

# issubclass 检查是否是自身的子类
print(issubclass(B,A)) #判断B是否是A的子类
print(issubclass(A,A)) #自己也是自己的子类，第二个参数可以是一个元祖，判断前一个参数的类，是不是后面这个元祖中的某一个类的子集
#所有类都是object类的子集

#isinstance  检查一个实例对象是否属于某一个类
b1 = B()
print(isinstance(b1,A)) #子集的实例也是父级的实例

#判断一个实例是否有属性
print(hasattr(b1,"count"))
print(hasattr(b1,"cou"))

#得到一个实例的某一个属性的值
print(getattr(b1,'count'))
print(getattr(b1,'cou','你访问的属性不存在')) #第三个参数是假如访问的属性不存在该说什么

#给一个实例设计一个属性，并赋值 setattr(object,name,value)
setattr(b1,'age',5)
print(b1.age) #但是其他的实例是没有的

#删除一个对象中的某个属性
print(b1,'age') #如果本身就没有那么汇报异常

class C:
    def __init__(self,size = 10):
        self.size = size #这里的size就是实例自身的size了
    def getSize(self):
        return self.size
    def setSize(self,size):
        self.size = size
    def delSize(self):
        del self.size
    x = property(getSize,setSize,delSize) #定义了这个以后，实例的某一个属性就可以通过这个属性来调用方法了

c1 = C()
#通过x来执行getSize方法
print(c1.x)
print(c1.size)
#通过x来执行set方法
c1.x = 15
print(c1.x)
print(c1.size)
#通过x来执行delSize方法
del c1.x
# print(c1.x)
# print(c1.size) 两个都会报错

    