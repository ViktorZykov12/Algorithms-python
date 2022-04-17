num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))
num3 = int(input('Третье число: '))

if num1 < num2 < num3 or num3 < num2 < num1:
    result = num2
elif num2 < num1 < num3 or num3 < num1 < num2:
    result = num1
else:
    result = num3

print(f'среднее число {result}')