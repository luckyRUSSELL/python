a = int(input("Nunber1: "))
b = int(input("Nunber2: "))
c = int(input("Nunber3: "))
list1 = []
list2 = []
list3 = []

while a > 0:
    p = a % 10
    list1.append(p)
    a //= 10
while b > 0:
    po = b % 10
    list2.append(po)
    b //= 10
while c > 0:
    pt = c % 10
    list3.append(pt)
    c //= 10


if sum(list1) > sum(list2) and sum(list1) > sum(list3):
    print(sum(list1))
elif sum(list2) > sum(list1) and sum(list2) > sum(list3):
    print(sum(list2))
else:
    print(sum(list3))





