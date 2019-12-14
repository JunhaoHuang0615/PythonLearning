#分治算法
def hanoi(n,x,y,z):
    'n is how many plates need to be moved'
    'x , y ,z  are the three tower， x的位置为起始柱子， y的位置为过渡，z的位置为结束的柱子'
    '目标： 把x的盘子移动到z上'
    if (n ==1) :
        #只有一个盘子的情况，那么就直接把这个盘子移动到z上，即递归的结束条件
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y)#首先将前面n-1个盘子全部移动到y上
        print(x,"-->",z) #将底下最后一个盘子移动到Z上
        hanoi(n-1,y,x,z) #将剩下的n-1个盘子从y移动到z上