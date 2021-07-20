from operator import itemgetter
lista = []# a lista de codigo, estoque e minimo

def cadproduto(cadastrodeproduto: dict):
    lista.append(cadastrodeproduto)# adicionar a lista o 
    return

opcao = int(input('Cadastrar produto: 0 - Nao   1 - Sim'))
while opcao == 1:
    produto_novo = {}

    produto_novo['codigo'] = int(input('digite o codigo do produto:  '))

    if produto_novo['codigo'] == 0:
        print('codigo 0, encerrando o cadastro do produto')
        break
    produto_novo['estoque'] = int(input('digite a quantidade em estoque: '))
    produto_novo['minimo'] = int(input('digite a quantidade minima do estoque: '))

    cadproduto(produto_novo)
    opcao = int(input('Cadastrar produto ? 0 - Nao 1 - Sim'))

if len(lista) > 0:
    print('Lista de produtos por codigo em ordem crescente: ')
    print('Codigo'.center(10), end='')
    print('Estoque'.center(10), end='')
    print('minimo'.center(10))

    for produto in sorted(lista, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))
else:
    print('lista vazia.')