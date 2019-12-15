import os
#返回当前的工作目录
print(os.getcwd())
#改变工作目录
path = '/Users/apple/Desktop/python/pythonworkspace'
os.chdir(path)
#列举指定目录中的文件名
print(os.listdir(path)) #也可以传入参数'.'表示当前目录,或者'..'表示上级目录 ,返回列表
#创建文件夹
os.mkdir('A') #在当前工作目录下创建
                #也可以创建此目录下的子文件夹
                #但如果已经有了这个文件夹，则会报错
#创建多层目录
os.makedirs('A/C/B')
os.makedirs('A/B/H')

#删除文件,注意是文件，不是文件夹
# os.remove('A/B/H/text.txt')

#删除文件夹，且必须是空的文件夹
#os.rmdir('A/B/H')
#os.removedirs('A/B/H') 递归删除目录，从子目录到父目录逐层递归删除

#模拟运行计算机的terminal
#os.system("cd .")

#当前目录 但会'.'
#os.curdir()
#上级目录  返回'..'
#os.pardir()


#os.path 对文件的操作
#想要知道某一个路径下的单独的某一个文件，即只返回文件名
os.path.basename('A/B/H/text.txt') #不管文件是否存在，这个方法只是对字符串操作
#想知道某一个路径下的文件的路径，即只返回路径
os.path.dirname('A/B/H/text.txt') #用于想要得到当前文件的目录下的其他文件
#将各个部分组合成一个路径名
print(os.path.join('c:/','A','B'))

#将文件名和路径分开  如果只写了路径，默认将最后一个部分当成文件名称分开
print(os.path.split('A/B/H/text.txt'))

#分离文件名称和扩展名名称
print(os.path.splitext('A/B/H/text.txt'))


