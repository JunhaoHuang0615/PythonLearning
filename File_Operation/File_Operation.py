# the type of opeing file
# r : only read
# w : write  覆盖已经存在的文件
# x : 新建文件，该文件不可以存在
# a : 以写入方式打开，如果文件存在并有内容，那么会在内容尾部添加新内容
# b : 以二进制模式打开
# t : 以文本模式打开
# + : 可读写模式，可添加到到其他模式中使用
# U : 通用换行符支持

file1 = open('/Users/apple/Desktop/python/pythonworkspace/File_Operation/testFile.json') #不写模式默认为r
str1 = file1.read() #不写参数为全部读取
print (str1)
str1 = file1.read() #第一次read已经将指针读取到了尾部，第二次则会读取空的字符串了
print("----------")
print(str1) 
#重新打开一次
file1 = open('/Users/apple/Desktop/python/pythonworkspace/File_Operation/testFile.json') 
str1 = file1.read(5) #只读取前五个字符
print(str1)
#使用tell方法可以开到文件指针读取到哪里了
print(file1.tell())

#重置文件指针
file1.seek(45,0) #参数： 第一个参数代表偏移多少个字节
                 #      第二个参数有三个值， 0代表从文件的起始位置向后偏移； 1代表从指针当前位置向后偏移； 2代表从文件末尾位置向后偏移
str2 = file1.readline() #这个只读一行，注意，一行里面如果有换行符是会被读到的
print('----------------------')
print(str2)

#如果想要逐行输出整个文件
print("------------213123123")
file1.seek(0,0)
for eachline in file1:
    print(eachline)

#文件的写入
file2 = open('/Users/apple/Desktop/python/pythonworkspace/File_Operation/testFile2.json','w')
jon = '''{
    "Name":"Ken",
    "Level":99,
    "Age":18,
    "SkillList": [
        {"id" : 2, "name" : "Kick","damage" :123},
        {"id" : 3, "name" : "shoot","damage" :89},
        {"id" : 4, "name" : "cut","damage" :673}
        ]
    
    }'''
file2.write(jon)
file1.close()
file2.close()