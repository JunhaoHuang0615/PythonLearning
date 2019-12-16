class Turtle:
    number = 0
    def __init__(self,number):
        self.number = number

class Fish:
    number = 0
    def __init__(self,number):
        self.number = number

class Pool:
    def __init__(self,number_of_fish,number_of_turtle):
        #设置成员的attribute,可以通过构造函数来设置
        self.number_of_fish = Fish(number_of_fish)
        self.number_of_turtle = Turtle(number_of_turtle) # 创建对象不想java一样需要new
    def display(self):
        print(self.number_of_fish.number, self.number_of_turtle.number)

pool1 = Pool(5,4)
pool1.display()

class C:
    count = 0

a = C()
b = C()
c = C()

print(a.count,b.count,c.count)

c.count += 10

print(a.count,b.count,c.count)

C.count += 20

print(a.count,b.count,c.count)

#Class 的属性默认是static的，可以通过类和对象访问到， 但一旦通过对象去修改过，那么就会在这个对象上面新建一个对象的属性，
# 即实例化后面的属性， 那么就不会受static的制约了
# 但是没有通过对象修改过的属性，依然受类的制约

#如果属性与方法同名，则属性覆盖方法

#方法如果不传递self，那么就实例化对象就无法使用了

