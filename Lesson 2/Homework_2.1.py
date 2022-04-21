def calculator(num1, num2, znak):
    if znak == '+':
        return num1 + num2
    elif znak == '-':
        return num1 - num2
    elif znak == '*':
        return num1 * num2
    elif znak == '/':
        return num1 / num2
    elif znak == '0':
        return 'stop'


result = 0
lst = ['0', '+', '-', '*', '/']
while result != 'stop':
    print('Введите два числа и знак, при вводе значения знака "0" программа завершается')
    num1 = int(input('num1 = '))
    while True:
        znak = input('znak = ')
        if znak in lst:
            break
        else:
            print('Введите верный знак')
    while True:
        num2 = int(input('num2 = '))
        if num2 != 0:
            break
        else:
            print('Деление на 0 невозможно!')

    result = calculator(num1, num2, znak)
    print(result)
