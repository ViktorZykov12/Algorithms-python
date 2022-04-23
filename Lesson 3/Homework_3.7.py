import random

my_list = [random.randint(0,100) for i in range(10)]

my_list.sort()

min_first = my_list[0]
min_second = my_list[1]

print(f'Два самых минимальны значения {min_first} {min_second}')