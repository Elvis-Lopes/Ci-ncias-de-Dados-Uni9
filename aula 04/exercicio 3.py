pessoas = int()
ingresso = float()
while True:
    dec = int(input('Comprar ingresso?\n1-Sim\n2-Não\n'))
    if(dec == 1):
        pessoas += 1
        idade = int(input('Insira a idade: '))
        if idade < 3:
            ingresso += 0
        elif idade >= 3 and idade < 12:
            ingresso += 3
        else:
            ingresso += 10
    else:
        break
print(f'Total R$ {ingresso:.2f}')
