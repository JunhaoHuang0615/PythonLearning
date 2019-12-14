def splitFile(filepath):
    file1 = open(filepath)

    ken = []
    ennotsubasa = []
    count = 1

    for eachline in file1: #这里的eachline是str类型的
        if eachline[:6] != "======" :
            (role, line_spoken) = eachline.split(":",1) #元组内如果放的是两个变量，那么就是一个变量元组，这两个变量会跟据后面的对象进行赋值
                                                        # split内的第一个参数是根据什么来进行拆分， 第二个参数是指定最大拆分次数，1则为拆分一次， 拆分返回一个列表
            if(role == 'Ken'):
                ken.append(line_spoken)
            if(role == 'Ennotsubasa'):
                ennotsubasa.append(line_spoken)
        else:
            # filepath1 = "/Users/apple/Desktop/python/pythonworkspace/File_Operation/"+"Ken_" + str(count) + '.txt'
            # filepath2 = "/Users/apple/Desktop/python/pythonworkspace/File_Operation/"+'Ennotsubasa_' + str(count) + '.txt'

            # kenfile = open(filepath1,'w')
            # ennotsubasafile = open(filepath2,'w')

            # kenfile.writelines(ken) #不能用write，因为这里的ken是list，writelines会根据每一个元素写一行
            # ennotsubasafile.writelines(ennotsubasa)

            # kenfile.close()
            # ennotsubasafile.close()
            saveFile(ken,ennotsubasa,times=count)

            ken = []
            ennotsubasa = []
            count+=1
    saveFile(ken,ennotsubasa,times=count)


def saveFile(*content,times):
    filepath1 = '/Users/apple/Desktop/python/pythonworkspace/File_Operation/'+"file1_"+str(times)+".txt"
    filepath2 = '/Users/apple/Desktop/python/pythonworkspace/File_Operation/'+"file2_"+str(times)+".txt"

    kenfile = open(filepath1,'w')
    ennotsubasafile = open(filepath2,'w')

    #注意，下标初始是0！！！！！！！！
    kenfile.writelines(content[0]) #不能用write，因为这里的ken是list，writelines会根据每一个元素写一行
    ennotsubasafile.writelines(content[1])

    kenfile.close()
    ennotsubasafile.close()

splitFile('/Users/apple/Desktop/python/pythonworkspace/File_Operation/record')



