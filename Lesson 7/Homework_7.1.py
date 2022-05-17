import random


def bubble_sort(mas):
    swapped = False
    for i in range(len(mas) - 1, 0, -1):
        for j in range(i):
            if mas[j] < mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return mas

mas = [random.randint(-100, 100) for i in range(1, 10)]
print(*mas)
print(*bubble_sort(mas))
