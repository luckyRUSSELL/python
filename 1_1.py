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
