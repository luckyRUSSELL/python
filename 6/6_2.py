import sys

mas = [10,20,5,25,50]
more_min = []
min_number = 0
less_max = []
max_number = 0
#ost = []
for idx in range(len(mas)):
    if mas[idx] > min_number:
        more_min.append(mas[idx])
        min_number = mas[idx]
    else:
        min_number = mas[idx]
for index in range(len(more_min)):
    if more_min[index] > max_number:
        max_number = more_min[index]
for index_2 in range(len(more_min)):
    if max_number > more_min[index_2]:
        less_max.append(more_min[index_2])



print(sum(less_max))
print(sys.getsizeof(less_max)) # 88 байт


import sys
mas = [10,20,5,25,50]
mas.remove(max(mas))
mas.remove(min(mas))
print(mas)
mas_new = sum(mas)
print(mas_new)
print(sys.getsizeof(mas_new)) # 28 байт

# Разница в скриптах 60 байт
# Версия пайтон 3.7 64 разрядная ОС
