import random

my_list = [random.randint(0, 10) for a in range(10)]
print(my_list)

min_el = my_list[0]
max_el = my_list[1]
min_index = 0
max_index = 0

for i, item in enumerate(my_list):
    if item <= min_el:
        min_el = item
        min_index = i
    if item >= max_el:
        max_el = item
        max_index = i

if max_index < min_index:
    max_index, min_index = min_el, max_index

result = 0

for i in range(my_list[min_index + 1], my_list[max_index]):
    result += my_list[i]

print(result)
