spisok = []

for i in range(2,100):
    for d in range(2,9):
        if i % d == 0:
            spisok.append(i)

new_spisok = set(spisok)
print(new_spisok)




