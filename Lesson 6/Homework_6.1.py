from size import count_size

print('Введите координаты двух точек: ')
x1 = float(input('x1='))
y1 = float(input('y1='))
x2 = float(input('x2='))
y2 = float(input('y2='))

print('Уравнение прямой, проходящей через эти точки:')
k = round((y1 - y2) / (x1 - x2), 3)
b = round(y2 - k * x2, 3)

print(f'y = {k}*x + {b}')

sum = 0
var_lst = (x1, y1, x2, y2, k, b)
for i in var_lst:
    sum += count_size(i)
print(f'Под переменные задействованно {sum} байт памяти')

# Под переменные задействованно 144 байт памяти
# 64-разрядная операционная система
# Python 3.9.0
