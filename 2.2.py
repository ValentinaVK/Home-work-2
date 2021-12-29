list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(list_1)
list_2 = []

for x in list_1:
    if x.isdecimal() == False :
        if x.isalnum() == True:
            list_2.append(x)
        if x.isalnum() == False:
            if len(x) < 3:
                x = str(x[0]) + "0" + str(x[1])
            list_2.append("\"")
            list_2.append(x)
            list_2.append("\"")

    if x.isdecimal() == True :
        if len(x) < 2:
            x = "0" + str(x)
        list_2.append("\"")
        list_2.append(x)
        list_2.append("\"")

print(' '.join(map(str,list_2)))

sp = ' '.join(map(str,list_2))
print(sp)
