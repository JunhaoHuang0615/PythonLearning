def fun1():
    print("fun1在被调用")
    def innerfun1():
        print("innerfun1正在被调用")
    innerfun1() #注意这个是在fun1中调用innerfun1

#外部是不可以调用内嵌函数的方法的，内嵌函数只有自己的函数体内部可以使用

#函数的闭包(closer)
def funX(x):
    def funY(y):
        return x*y #内部函数的返回值是两个参数的乘积
    return funY #外部函数返回的是这个方法，即只执行外部函数的话，那么久得到了内部函数这个方法，这个内部的方法又可以存储到一个对象中去

i = funX(30) #这个时候，i就是一个带有参数x=30的一个funY的方法
print(i) 
print(i(2)) #这时候相当于运行了内部方法 30*2
print(i(5)) #30*5
print(funX(30)(3))

# def fun3():
#     x = 5
#     def fun4():
#         x = x * x #这里好像是想用外部的x，但又给一个x赋值，那么等号右边的两个x会被认为是外部的x=5，但左边的这个x会被认为是内部自己的x，与外部的x不一样
#         return x #这里就会报错，到底应该返回哪一个x比较好？ 自己的？ 还是外部的？
#     return fun4() 

def fun3():
    x = 5
    def fun4():
        nonlocal x
        x = x * x 
        return x
    return fun4() 

print(fun3())