# 黄金分割比例 0.618 
# 1 1 2 3 5 8 13 21 34 55 89 144 （后一个数等于前两个数的和)
# 相邻两个数的比值，越往后越接近0.618

def fabFinalResult(n):
    '算第n个fibonacci个数的值'
    if(n<1):
        print("输入有误")
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fabFinalResult(n-1) + fabFinalResult(n-2)

def generateFibList(n):
    fabList =[]
    for i in range(1,n+1):
        fabList.append(fabFinalResult(i))
    return fabList

print(fabFinalResult(20))    
print(generateFibList(20))

#如果我们用迭代的方法来实现,会发现迭代的方法比递归的速度快！！
def fabNumber(n):
    if(n<1):
        print("you cannot input 1 or less than 1")
    n1 = 1
    n2 = 1
    while(n>2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n-=1
    return n3

print(fabNumber(20))
