a = []
b = []

for i in range(2,100):
    if i % 2 == 0:
        a.append(i)
    elif i % 9 == 0:
        b.append(i)

print(f'Кратны двойке {len(a)} чисел')
print(f'Кратны девтке {len(b)} чисел')
        