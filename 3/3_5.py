mas = [23,56,45,-32,-41,9,-21]
min = 0
index = 0
for idx in range(len(mas)):
        if mas[idx] < 0 and mas[idx]< min:
                min = mas[idx]
                index = idx
        else:
                continue
print(f'Максимальный отрицательный элемент: {min}',f'Позиция в массиве: {index}')
























































