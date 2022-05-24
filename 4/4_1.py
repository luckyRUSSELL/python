from random import randrange
import cProfile
import trace

def mass():
    a = [randrange(1,1000) for f in range(1000)]
    for i in range(len(a)):
        b = a[i]
        a[i] = a[len(a)-1]
        a[len(a) - 1] = b
        return

print(mass())
cProfile.run('mass()')
#trace.Trace(timing)


def mass2():
    a = [randrange(1,100000) for f in range(100000)]
    for i in range(len(a)):
        b = a[i]
        a[i] = a[len(a)-1]
        a[len(a) - 1] = b
        return

print(mass2())
cProfile.run('mass2()')


def mass3():
    a = [randrange(1,1000000) for f in range(1000000)]
    for i in range(len(a)):
        b = a[i]
        a[i] = a[len(a)-1]
        a[len(a) - 1] = b
        return

print(mass3())
cProfile.run('mass3()')


