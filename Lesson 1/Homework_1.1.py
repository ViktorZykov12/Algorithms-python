num = int(input('Введите трехзначное число: '))

a = num // 100
b = num % 100 // 10
c = num % 10

print(a + b + c)
print(a * b * c)
