from multiprocessing import Process
from threading import Thread
import time,threading
import os
def work(person):
    print(f"let us call {person}, process number {os.getpid()}, thread number: {threading.current_thread()}")
    time.sleep(3)
    print(f"{person} is so stupid, process number: {os.getpid()}, thread number: {threading.current_thread()}")

userlist = ['ken','ennotsubasa','baka']

# 启动了一个单进程，这个进程是主线程
# for i in range(0,len(userlist)):
#     work(userlist[i])

#多进程，多个工厂来完成同一个任务，但每个工厂的任务都一样
# plist=[]
# for item in userlist:
#     #循环创建进程
#     p = Process(target = work,args = (item,)) ## (item,) 表示只有一个元素的元祖， args对应的是target函数的参数
#     #启动进程 #启动了但是并没有开始工作，相当于只是创建了
#     p.start() 
#     #加入到列表中
#     plist.append(p)

#阻塞 终止进程 的执行 列表里其他进程没有完成的时候，列表里的进程不会结束
# [i.join() for i in plist]

plist=[]
for item in userlist:
    #循环创建线程
    p = Thread(target = work,args = (item,)) ## (item,) 表示只有一个元素的元祖， args对应的是target函数的参数
    #启动进程 #启动了但是并没有开始工作，相当于只是创建了
    p.start() 
    #加入到列表中
    plist.append(p)

[i.join() for i in plist]