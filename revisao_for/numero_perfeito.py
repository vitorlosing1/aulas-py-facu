s= 0
n = int(input('Digite um número: '))

for cont in range(1, n):
    if n % cont == 0:
        s = s + cont

if s == n:
    print('Número perfeito')
    
else:
    print('Número não é perfeito')