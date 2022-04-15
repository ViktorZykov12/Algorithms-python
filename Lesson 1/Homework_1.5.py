print('Введите две буквы')
char1 = ord(input('Первая буква: '))
char2 = ord(input('Вторая буква: '))

pos1 = char1 - ord('a') + 1
print(f'Позиция первой буквы {pos1}')

pos2 = char2 - ord('a') + 1
print(f'Позиция первой буквы {pos2}')

dist = pos2 - pos1 - 1
print(f'Между ними {dist} букв ')