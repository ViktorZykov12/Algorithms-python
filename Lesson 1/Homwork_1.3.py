print('Введите координаты двух точек: ')
x1 = float(input('x1='))
y1 = float(input('y1='))
x2 = float(input('x2='))
y2 = float(input('y2='))

print('Уравнение прямой, проходящей через эти точки:')
k = round((y1 - y2) / (x1 - x2), 3)
b = round(y2 - k * x2, 3)

print(f'y = {k}*x + {b}')
