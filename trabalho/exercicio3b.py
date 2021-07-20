import random # importar a biblioteca random 
print('digite 1 para Adicionar nomes ou 2 para terminar o programa.')# imprimir texto 
print('selecione uma opcao ')# imprimir texto
opcao = int(input('1 ou 2: ')) # digitar alguma das opcoes
nomes = []
while opcao == 1 : # enquanto a opcao digitada for igual a 1 executar o laco abaixo
    nome = str(input('digite o nome: ')) # nome tipo string que sera digitado 
    doacao = float(input('digite o valor doado: '))# valor doado do tipo flutuante 
    nomes.extend( ((nome + ' ') * int(doacao//10)).split() ) # adicionar a nomes o nome digitado mais o espaco quantas vezes a doacao for dividida por 10 em 10 
    opcao = int(input('selecione uma opcao 1 ou 2: ')) # final do laco opcao pode ser escolhida para adicionar mais nomes ou parar
if opcao == 2: # se a opcao for igual a 2 executar o codigo abaixo 
    random.shuffle(nomes) # organizar a lista de nomes que foram digitados * doacao dividido por 10 
    sorteado = random.choice(nomes) # retornar um nome aleatorio da lista nomes que sera o sorteado 
    print(sorteado)# imprimir o nome sorteado 
    print(nomes)
     

