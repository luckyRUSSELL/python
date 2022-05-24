def bubble_sort(spisok):
    o = False
    for i in range(len(spisok) - 1, 0, -1):
        for j in range(i):
            if spisok[j] > spisok[j + 1]:
                spisok[j + 1],spisok[j] = spisok[j],spisok[j + 1]
                o = True
        if o:
            o = False
        else:
            break


    return spisok


s = [8, 90, -13, 14, -67, 2]
print(bubble_sort(s))
