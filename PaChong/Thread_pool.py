from concurrent.futures import ThreadPoolExecutor
import os,time,threading
def work(person):
    print(f"let us call {person}, process number {os.getpid()}, thread number: {threading.current_thread()}")
    time.sleep(3)
    print(f"{person} is so stupid, process number: {os.getpid()}, thread number: {threading.current_thread()}")

userlist = ['ken','ennotsubasa','baka','aho']

#创建线程池
pool = ThreadPoolExecutor(max_workers = 2) #最大线程数 #最大线程是2个，那么当userlist多余2个时，一个线程结束了会立马开始新的任务

#循环指派任务
[pool.submit(work,user) for user in userlist]

#关闭线程
pool.shutdown()

