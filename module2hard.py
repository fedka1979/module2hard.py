import tablo

booc = int(input('Введите число от 3 до 20: '))
pswrd = []
for i in range(1, int(booc/2)+1):
    for j in range(1, booc):
        if booc % (i + j) == 0 and (i != j) and pswrd.__contains__([j, i]) == False:
             pswrd.append([i, j])

print('Ваш пароль: ')
for i in range(len(pswrd)):
    print(*pswrd[i], sep='',  end='')