termial = float(input('Insira o número: '))
finalRange = int(termial + 1)
res = float(0)
for i in range(1, finalRange):
    res += i
print(f'Resultado: {res:.0f}')