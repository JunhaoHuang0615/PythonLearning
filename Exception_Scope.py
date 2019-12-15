# OSError
try:  
    filePath = 'file.txt'
    fileread = open(filePath)
    print(fileread.read())
except OSError as reason:  #这个就是异常处理,后面的reason是错误原因，自动生成
    print('can\'t find the file\n',str(reason))
finally:
    fileread.close()
#输入错误Error
count = 0
while(count<3):
    try:
        num = input("请您出入一个数字")
        temp = int(num)
        if(temp == 2):
            print('您输入正确')
            break
        else:
            count+=1
            print('您输入错误，还有',3-count,'次机会')
    except (ValueError,TypeError) as reason: #同时捕捉两个异常
        print('请不要输入其他字符')
    except: #捕捉所有异常
        print('你有毒.......')

raise ZeroDivisionError('你的分母不能为0')   #无端端的跑出个异常........
