#创建一个迭代器
str1 = 'ennotsubasa'
it = iter(str1) #it就是包含了这个str1的迭代器

print(next(it))
print(next(it))
print(next(it))
print(next(it))
#到后面无东西后，就报错了

#迭代器的魔法方法
class Fibs:
    def __init__(self, n =20):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a = self.b
        self.b = self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a