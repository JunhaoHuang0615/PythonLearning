# coding: utf-8
#现在写一个文件，这个文件全都是方法
#Python的pacakge相当于一个文件，一个文件的名称就是命名空间
#与JAVA的区别， JAVA有自己的包，想使用某个工具类要引入它的包，使用包中的工具函数还要通过类去调用
#Python的一个文件就是命名空间，函数可以通过命名空间来调用

def c2f(cel):
    fah = cel * 1.8 +32
    return fah

def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

def test():
    print('测试',c2f(32))
    print('测试', f2c(100))

#为了避免导入这个模块的时候执行测试语句
if __name__ == "__main__":
     test()

