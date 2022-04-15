year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 and year % 400:
    print('Год високосный')
else:
    print('Год не високосный')