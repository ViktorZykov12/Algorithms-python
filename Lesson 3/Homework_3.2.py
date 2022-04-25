first_lst = [8, 3, 15, 6, 4, 2]
index_lst = []

for i, item in enumerate(first_lst):
    if item % 2 == 0:
        index_lst.append(i)

print(index_lst)