import random
print("this is a number guess game")
count = 0
answer = random.randint(1,10)
while count<3:
    temp = input("enter a number please ")
    number = int(temp)
    if number < answer:
        print("your number is too small")
    else:
        if number > answer:
            print("your number is too big")
        else:
            print("you got it")
            break
    count += 1
print("game end")

