import time
#==========================================================这些都不是重点，重点在下面=========================================================
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

class B:
    def __getattribute__(self, name): #当一个实例的属性被访问时调用的方法 name代表访问的是什么属性
        print('__getattribute__ is being called')
        return super().__getattribute__(name)
    
    def __getattr__(self,name): # 用户试图获取一个不存在的属性时的行为调用的方法
        print ('__getattr__ is being called')

    def __setattr__(self, name, value): # 某一个属性被设置时调用的方法
        print('__setattr__ was being called')
        return super().__setattr__(name, value)

    def __delattr__(self,name): # 当实例的某一个属性被删除时调用的方法
        print('__delattr__ is being called')
        return super().__delattr__(name)


b1 = B()
b1.x  #会先调用 __getattribute__ 如果找不到这个属性，则会去调用__getattr__
time.sleep(2)
b1.x = 5
time.sleep(2)
b1.x
time.sleep(2)
del b1.x

class Rectangle:
    def __init__(self,width = 2,height = 1):
        self.width = width
        self.height = height
    
    def __setattr__(self, name, value):
        if(name == 'square'):   #如果实例化对象想要创造属性的时候，如果创建的属性为square
            self.height = value
            self.width = value
        else:
            return super().__setattr__(name, value)
            #方法2： self.__dict__[name] = value

r1 = Rectangle()
print(r1.height , r1.width)
r1.square = 5
print(r1.height , r1.width)

print(r1.__dict__) #这是每一个实例的特殊属性，作用是使用字典的形式，打印这个实例化的所有属性的键和值

#=========================================================重点来了==========================================================

#特殊类： 即必须实现__get__ , __set__ , __delete__ 这三个方法的其中某一个，两个或三个都实现方法的类，这三个是属于描述符的方法
# __get__(self,instance,owner) 用于访问属性，返回属性的值
#__set__(self,instance,owner) 在属性分配操作中调用，不返回任何值
#__delete__(self,instance) 属性删除，不返回任何值
class MyDescriptor:
    def __get__(self,instance,owner):
        print('geting', instance , owner) #instance 就是 实例对象， owner是类本身
    def __set__(self,instance,owner):
        print( 'seting', instance , owner)
    def __delete__(self,instance):
        print('it is deleting',instance)

class Test:
    x = MyDescriptor()

test1 = Test()
test1.x #调用了__get__方法
time.sleep(2)
test1.x = 5 #调用了__set__方法
time.sleep(2)
del test1.x

class MyProperty:
    def __init__(self, fget=none , fset = none, fdel = none):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    
    def __get__(self,instance,owner):
        return self.fget(instance)
    def __set__(self,instance,value):
        self.fset(instance,value)
    def __del__(self,instance):
        self.fdel(instance)

class D:
    def __init__(self,size = 10):
        self._size = size #这里的size就是实例自身的size了
    def getSize(self):
        return self._size
    def setSize(self,size):
        self._size = _size
    def delSize(self):
        del self._size
    x = MyProperty(getSize,setSize,delSize)