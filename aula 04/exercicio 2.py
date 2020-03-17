valor = float(input('Insira o valor do produto: '))
valorTotal = valor
while True:
    escolha = int(input('Adicionar novo produto?\n1-Sim\n2-Não '))
    if escolha == 1:
        valor = float(input('Insira o valor do produto: '))
        valorTotal = valorTotal + valor
    else:
        break
print(f'Total da compra R${valorTotal}')