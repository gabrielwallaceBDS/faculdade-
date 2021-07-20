import random
opcao = int(input('1 ou 2'))
nomes = ''
while opcao == 1 :
    nome = input('digite o nome: ')
    doacao = float(input('digite o valor doado: '))
    nomes_sorteio2 = (nome + ',') * int((doacao//10)) 
    nomes = nomes + nomes_sorteio2 
    print(nomes) 
    opcao = int(input('1 ou 2'))

nomes = []
random.shuffle(nomes)
sorteado = random.choice(nomes)
print(sorteado)
    