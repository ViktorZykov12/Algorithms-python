num = input('Введите число: ')

ls = list(num)
ls1 = []
ls2 = []

for i in ls:
    i = int(i)
    if i % 2 == 0:
        ls1.append(i)
    else:
        ls2.append(i)

print(f'В вашем числе {len(ls1)} четных и {len(ls2)} нечетных чисел')