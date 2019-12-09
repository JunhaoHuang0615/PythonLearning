print("this is a number guess game")
count = 0
while count<3:
    temp = input("enter a number please ")
    number = int(temp)
    answer = 8
    if number < answer:
        print("your number is too small")
    else:
        if number > answer:
            print("your number is too big")
        else:
            print("you got it")
            break
    count = count+1
print("game end")
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