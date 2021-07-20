lista = []# a lista de codigo, estoque e minimo

def cadproduto(cadastrodeproduto: dict):# cria um dicionario na lista para cada produto novo 
    lista.append(cadastrodeproduto)# adicionar a lista o produdo cadastrado
    return

opcao = int(input('Cadastrar um produto?: 1 - Sim   0 - Nao'))#opcao em numero inteiro 0 ou 1
while opcao == 1:# enquanto a opcao for igual a 1 criar novo dicionario 'novoproduto'
    novoProduto = {}#dicionario vazio que sera preenchido no proximos passos

    novoProduto['codigo'] = int(input('digite o codigo do produto:  '))# digita o codigo do produto 
    if novoProduto['codigo'] == 0:# se o codigo do produto digitado for igual a zero encerrar o programa
        break # e quabrar o codigo 
    novoProduto['estoque'] = int(input('digite a quantidade em estoque: '))# se o if nao for igual a zero perguntar o estoque 
    novoProduto['minimo'] = int(input('digite a quantidade minima do estoque: '))# e o minimo em estoque

    cadproduto(novoProduto)# adicionar o novo produto a lista sem tirar o anterio 
    opcao = int(input('Cadastrar produto ? 0 - Nao 1 - Sim'))# perguntar a opcao se quer cadastrar produto novo se for igual a 0 continuar o codigo para o proximo passo se nao voltar while acima e criar um novo produto para adicionar a lista sem remover o anterior

if len(lista) > 0: # se tiver item na lista retornar a lista com todos 'novoproduto' mas em ordem crescente
    print(' Codigo   ', end='') # imprimir o texto codigo na mesma linha (end='')
    print('Estoque  ', end='') # imprimir o estoque  na mesma linha do texto codigo 
    print(' minimo') # os tres prints na mesma linha no terminal

    for produto in sorted(lista, key=lambda item: item['codigo']):#Retorna o produto contendo todos os itens do iterável em ordem crescente 
        print(str(produto['codigo']).center(10), end='') #imprimir a string codigo do produto do dicionario e o center(10) é o método que irá centralizar a string em 10 espacos 
        print(str(produto['estoque']).center(10), end='') # imprimir estoque do dicionario 
        print(str(produto['minimo']).center(10))# imprime minimo do dicionario todos os 3 centralizados em 10 espacos 
print(lista)