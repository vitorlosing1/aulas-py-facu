s= 0

for cont in range(1, 101):
    if cont % 2 == 0:
        print(f'{cont}', end = ', ')
        s = s + cont

print(f'Soma dos pares: {s}')