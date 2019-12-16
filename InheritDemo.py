class Person(): #继承了list这个class
    #Attributes
    name = ""
    age  = 0
    subject="Undifined"
    def __init__(self,name,age,subject):
        self.name = name
        self.age = age
        self.subject = subject

class Student(Person): #用逗号隔开可以多重继承
    def __init__(self, name, age, subject):
        super().__init__(name, age, subject) #调用父类的构造函数
        self.age = 0 #这个self代表由这个子类创造的对象

        


#多态， 两个类继承了同一个类，比如一个大类是人， 然后学生类和老师类继承了人这个大类
#那么学生对象，即是人对象，又是学生对象
#OOA：面向对象分析 OOP：面向对象编程 OOD：面向对象设计