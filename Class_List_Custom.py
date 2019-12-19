class CountList:
    def __init__(self, *args):
        self.values = [ i for i in args] # 把一个数组赋值给values， 这个数组只要是args的元素就去赋值
        self.count= {}.fromkeys(range(len(self.values)),0) #为了记录某一个元素被访问了多少次，初始化这个count字典，key为列表下标，值初始化为0

    def __len__(self):
        return len(self.values)
    def __getitem__(self,key): #每当列表的元素用下标的形式被访问时调用的方法, 如c1[0]
        self.count[key] += 1 #每当这个列表的元素被访问了就把实例化中的count+1
        return self.values[key]






# #列表推导式
# x = [i for i in range(10)]

# # 对每个元素求平方
# print([i**2 for i in x])


# # 每个元素乘以 3
# print([i*3 for i in x])


# # 获取其中的偶数
# print([i for i in x if i%2==0])

c1 = CountList(1,3,5,7,9)
c2 = CountList(2,4,6,8,10)
print(c1[1])
print(c1.count)
print(c1[3])
print(c1.count)
