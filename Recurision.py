def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

number = int(input("please give me a int number: "))
result = factorial(number)
print("the factorial of %d is %d" %(number,result))