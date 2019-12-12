def discount(price, rate):
    final_price =  price * rate
    old_price = 88 #这里试图修改外部的同名全局变量，但是这样子是不可以滴
    print("修改后的old——price的值为" ,old_price) #这里的old_price 不会改变外面的值
    return final_price

old_price = float(input("请输入原价 "))
rate = float(input("请输入折扣率 "))
new_price = discount(old_price,rate)
print('修改之前的价格是 ',old_price)
print('折后的价格是 ',new_price)

#global 关键字！
count = 5
def changeGlobal():
    global count #使用了这个关键字，则这个count内部外部都可以访问到了
    count = 10

print (count)