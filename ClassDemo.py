class ClassDemo:
    #Attributes
    color = 'yellow'
    weight = 10
    height = 1.49
    shell = True
    __age = 18 # __ means private,, 但其实是伪私有，它还可以通过类去访问这个属性
    #Constructer
    def __init__(self,weight,height,color,age):
        self.weight = weight
        self.height = height
        self.color = color
        self.__age = age
    #Methods
    def eat(self): #只要是类的对象自己调用的方法，都一定要传递一个self过来，相当于this
        print("it is eating")
        self.weight+=50
    
    def displayWeight(self):
        print(self.weight)
    def dispalyProperty(self):
        print(self.color,self.__age,self.weight,self.height)

classObj = ClassDemo(100,20,"pink",20)
classObj.eat()
classObj.displayWeight()
classObj.dispalyProperty()
# print(classObj.__age)  访问不了的
print(classObj._ClassDemo__age)