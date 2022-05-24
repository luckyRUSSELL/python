kol_pr = int(input("Введите количество предприятий: "))
srg = 0
dict_name_pr = {}

for i in range(kol_pr):
    name_pr = (input(str(i+1) + "предприятие: " ))
    prib_1 = int(input(str(i+1) + " предприятие(прибыль) за 1 Квартал: "))
    prib_2 = int(input(str(i + 1) + " предприятие(прибыль) за 2 Квартал: "))
    prib_3 = int(input(str(i + 1) + " предприятие(прибыль) за 3 Квартал: "))
    prib_4 = int(input(str(i + 1) + " предприятие(прибыль) за 4 Квартал: "))
    summ = float((prib_1 + prib_2 + prib_3 + prib_4) // 4)
    srg += summ
    dict_name_pr[name_pr] = summ
    srg_all = srg // kol_pr
print(f'Средняя сумма прибыли для всех предприятий: {srg_all}')
for a in dict_name_pr:
    if dict_name_pr[a] > srg_all:
        print(f'В {a} прибыль больше средней')
    else:
        print(f'В {a} прибыль меньше средней')


    #prib = int(input("Балл: "))
