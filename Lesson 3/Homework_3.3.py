import random

my_list = [random.randint(0, 100) for i in range(10)]

print(my_list)
my_list.sort()
print(my_list)

min_el = my_list[0]
max_el = my_list[len(my_list) - 1]
min_index = my_list.index(min_el)
max_index = my_list.index(max_el)


my_list[min_index] = max_el
my_list[max_index] = min_el

print(my_list)