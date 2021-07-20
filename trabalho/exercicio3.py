import random


nome = input('digite o nome: ')
doacao = float(input('digite o valor doado: '))

nomes_sorteio = ['']

nomes_sorteio1 = (nome + ',') * int((doacao//10))
print(nomes_sorteio)
opcao = input('Deseja adicionar outro nome?\n\ndigite 1 para SIM e 2 para NAO: ')

while opcao == '1' :
    nome = input('digite o nome: ')
    doacao = float(input('digite o valor doado: '))
    nomes_sorteio = (nome + ',') * int((doacao//10))
    opcao = input('Deseja adicionar outro nome?\n\ndigite 1 para SIM e 2 para NAO: ')
while opcao == '1':
    nomes_sorteio = [nomes_sorteio]
    lista = nomes_sorteio1 + nomes_sorteio
    print(lista)







