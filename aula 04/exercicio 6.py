num = float(input('Insira o número: '))
res = 0
soma = 0
while soma < num:
    res += 1
    soma = soma + res
if soma == num:
    print('Numero triangular')
else:
    print('Não triangular')
