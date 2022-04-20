for i in range(32, 128):
    if i % 10 == 0:
        a = '\n'
    else:
        a = ' '
    print(f'{i}-{chr(i)}', end= a )
