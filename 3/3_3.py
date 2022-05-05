a = [1,2,3,4,5,6]
for i in range(len(a)):
    b = a[i]
    a[i] = a[len(a)-1]
    a[len(a) - 1] = b
    break


print(a)


