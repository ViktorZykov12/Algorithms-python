import random

num = random.randint(0,101)

user_num = None
level = 0
while num != user_num and level != 10:
    user_num = int(input('Введите число от 0 до 100: '))
    if user_num == num:
        print('Вы угадали!')
    elif user_num > num:
        print('Введите число меньше!')
    elif user_num < num:
        print('Введите число больше!')

    level = level + 1


print(f'Загаданое число {num}')
