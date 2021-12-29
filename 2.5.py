list = [45.5, 9.9, 45.4, 13.3, 14.46, 17.08, 1.43, 78.9, 65.5, 56.7, 89.12]
list_2 = []
for i in list:
    Rub = int(i // 1)
    Kop = int(((i % 1) * 100) / 1)
    if len(str(Kop)) < 2:
        Kop = "0" + str(Kop)
    print(Rub, 'руб', Kop, 'коп', end=' ')
print('\n')

list.sort()
for i in list:
    Rub = int(i // 1)
    Kop = int(((i % 1) * 100) / 1)
    print(Rub, 'руб', Kop, 'коп', end=' ')
print('\n')


list.sort(reverse = True)
for i in list:
    Rub = int(i // 1)
    Kop = int(((i % 1) * 100) / 1)
    print(Rub, 'руб', Kop, 'коп', end=' ')
print('\n')

list_2 = list.sort(reverse = True)
list_2 = list[:5]
for i in list_2:
    Rub = int(i // 1)
    Kop = int(((i % 1) * 100) / 1)
    print(Rub, 'руб', Kop, 'коп', end=' ')
