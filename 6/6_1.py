import sys
a = int(input("Введите число: "))
sum_a = 0
pro_a = []
while a > 0:
  sum_a += a % 10
  pro_a.append(a % 10)
  a //= 10
result = 1
for i in pro_a:
    result = result * i

print(sum_a,result)
print(pro_a)
print(sys.getsizeof(pro_a)) # 88-56-28 =4 байта,откуда они взялись?
print(sys.getsizeof(5,2)) #28 байт
print(sys.getsizeof([])) #56 байт





