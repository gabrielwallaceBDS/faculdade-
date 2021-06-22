#ESCREVA UM ALGORITIMO QUE LEIA DOIS VALORES NUMERICOS E QUE PERGUNTE AO USUARIO QUAL OPERACAO ELE DESEJAREALIZAR: ADICAO (+), SUBTRACAO (-), MULTIPLICACAO (*) OU DIVISAO(/). EXIBA NA TELA O RESULTADO DA OPERACAO DESEJADA #

print('qual operacao deseja fazer?')
print('1 - adicao\n2 - subtracao\n3 - multiplicacao\n4 - divisao\n :')
opcao = input('digite a opcao desejada: ')
if(opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4'):
    val1 = int(input('digite o primeiro valor: '))
    val2 = int(input('digite o segundo valor: '))
    adicao = (val1 + val2)
    subtracao = (val1 - val2)
    multiplicacao = (val1 * val2)
    divisao = (val1 / val2)



if(opcao == '1'):
    print('a adicao de {} + {} = {}'.format(val1, val2, adicao))
elif(opcao == '2'):
    print('a subtracao de {} - {} = {}'.format(val1, val2, subtracao))
elif(opcao == '3'):
    print('a multiplicacao de {} x {} = {}'.format(val1, val2,multiplicacao))
elif(opcao == '4'):
    print('a divisao de {} / {} = {}'.format(val1, val2,divisao))
else:
    print('opercacao invalida ')

print('encerrando o programa')
 
