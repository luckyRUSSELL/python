x = int(input("Введите число: "))
list = []
even = []
off = []
while x > 0:
    a = x % 10
    list.append(a)
    x //= 10
for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            off.append(i)

how_even = len(even)
how_off = len(off)
print (f'Количество чётных чисел: {how_even},количество нечётных чисел: {how_off}')


