import cProfile
n = int(input())
def func():
    k = set(range(2, n + 1))
    prosto_set = set()

    while k:
        pr = min(k)
        prosto_set.add(pr)
        k -= set(range(pr, n + 1,pr))
        #print((k))

cProfile.run("func()")
#1print(*prosto_set)



