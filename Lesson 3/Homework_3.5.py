import random

my_list = [random.randint(-10,10) for i in range(10)]
print(my_list)

min_el = my_list[0]
min_index = 0
for i, item in enumerate(my_list):
    if item <= min_el:
        min_el = item
        min_index = i

print(f'Минимальный элемент {min_el}, индекс минимального элемента {min_index}')