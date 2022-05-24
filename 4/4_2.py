import cProfile
def func():
    a = 199999
    x = True
    for i in range(2,a - 1):
        if a % i == 0:
            x = False
            break

    if x:
        print("Easy")
    else:
        print("Not easy")
        return
#print(input(func(199999)))
cProfile.run("func()")
#print(input(func(199999)))





