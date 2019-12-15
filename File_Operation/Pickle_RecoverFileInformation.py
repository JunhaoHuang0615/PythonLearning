#Pickle是读取文件中的信息，并恢复成元祖，list，字典等的模块
#一般一些用于代码运行的数据，我们要打包成pkl（或者自己命名的其他扩展名）文件
#这样简化了代码
import pickle
#写用一个变量存储要存储的数据
my_file = ["this is my file",2 ,4 ,6,[32,56,3],(24,67,3),{2:"23",3:"45"}]
#保存成文件写入到磁盘
save_file = open('File_Operation/pickleFile.ljecy','wb') #这一步就将文件创建出来啦
#接下来把my_file写入文件中
pickle.dump(my_file,save_file)
#写完后把文件关闭
save_file.close()
# 由于dump相当于二进制写入的，打开后一定是乱码

# 接下来我们要通过代码将my_file还原
#首先打开文件
recover_file = open('File_Operation/pickleFile.ljecy','rb')
my_recover_list = pickle.load(recover_file)
print(my_recover_list)



