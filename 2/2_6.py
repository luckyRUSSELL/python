import random
x = random.randint(0,100)
n = 10
while n > 0:
    a = int(input("Введите число:" ))
    if a == x:
        print("You win")
        break
    elif a > x:
        print("Ваше число больше.")
    else:
        print("Ваше число меньше")
    n -= 1
if n == 0:
    print("You lose")




