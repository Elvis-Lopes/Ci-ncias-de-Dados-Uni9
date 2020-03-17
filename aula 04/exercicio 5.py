n = float(input('Insira o número: '))
finalRange = int(n)
adicional = 1
res = 1
for i in range(1, finalRange):
    adicional += 2
    res += adicional
print(f'Resultado {res}')
