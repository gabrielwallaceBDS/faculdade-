#DESENVOLVA UM ALGORITIMO QUE SOLICITE AO USUARIO O PRECO DE UM PRODUTO E UM PERCENTUAL DE DESCONTO A SER APLICADO A ELE.CALCULE E EXIBA O VALOR DO DESCONTO E O PRECO FINAL DO PRODUTO (EXERCICIO DA APOSTILA - AULA 2)


preco = float(input('Digite o Preco do produto: '))
desc = float(input('Digite o Desconto do produto(0-100)%: '))

desconto =  preco * (desc / 100)
final = preco - desconto

print ('O PRECO DO PRODUTO COM DESCONTO DEU {}R$! '.format(final))
