import random

print('Введите диапазон для случайного целого числа:')
num1 = int(input('От: '))
num2 = int(input('До: '))
random_num = random.randint(num1, num2)
print(f'Ваше случайное число: {random_num}')

print('Введите диапазон для случайного вещественного числа:')
num3 = float(input('От: '))
num4 = float(input('До: '))
random_float = random.uniform(num3, num4)
print(f'Ваше случайное число: {random_float}')

print('Введите диапазон для случайного знака:')
char1 = input('От: ').upper()
char2 = input('До: ').upper()
random_char = chr(random.randint(ord(char1), ord(char2)))
print(f'Ваш случайный символ: {random_char}')