# -*- coding: UTF-8 -*-

print(" this is a test file");
temp = input("Could you please guess a number?") #this is something like print something before scanner
            # wants to know how to use a function in python:
                                #type: help(functionName) in the shell
guess = int(temp)
if  guess ==8:
    print("you got me!")
else:
    print("sorry, you are wrong") #Tab is so important in python! that's how seperate things
print("The game finished.....")

#Use r to avoid \
path = r"/Users/apple/Desktop/python/pythonworkspace/First_python_file.py"
path2 = "/Users/apple/Desktop/python/pythonworkspace/First_python_file.py"
print(path) 
print(path2)
print("123\n456")
print(r"123\n456")

#如果想要在 原始字符的最后添加一个\，那么必须要写2个，否则会报错
str = r'C:\Program Files\FishC\Good''\\'
print(str)

#三重引号可以直接输出多行，不需要\n
Multipleline = """
I want you
But please give me some time
i will leave you as time goes by
See you
"""
print(Multipleline)

# 先查看shell的类型： dscl . -read $HOME shell
# Python 配置环境变量的方法
# 先看看version：Python3 --version
# 把Python的路径找到  输入 which Python3
# 比如说是：/usr/local/bin/python3 或者 /Users/apple/Library/Python/3.8/bin
# 查看环境变量的值：echo $PATH
# 每一个PATH是靠分号隔开的
# vi ~/.bash_profile
# export PATH="/Users/apple/Library/Python/3.8/bin:${PATH}"
# 修改立即生效：source ~/.bash_profile

#方法2： 在VS Code 中按 F1
# 输入 Python: Select Interpreter
# 选择python的版本