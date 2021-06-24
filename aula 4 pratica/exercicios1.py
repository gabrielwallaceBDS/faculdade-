#escreva um algoritimo que leia dois valores numericos e que pergunte ao usuario qual operecao ele deseja realizar adicao (+), subtracao (-), multiplicacao (*), divisao (/) e sair.and
# exiba na tela o resultado da opercacao desejada
# repita até que a opcao saida seja escolhida 
"""print('digite dois valores inteiros')
val1 = int(input('digite o primeiro valor: '))  
val2 = int(input('digite o segundo valor: '))   
print('selecione a operacao que deseja fazer ()')
oper = input('+ - adicao\n- - subtracao\n* - multiplicacao\n- - divisao\nsair - exit\n digite: ')
while True:
    if(oper != ):
        oper = input('digite uma opereracao')
        continue
    if(oper == '+' or '-' or '/' or '*' or 'sair'):
        break
"""
"""print('CALCULADORA')
print('+ adicao')
print('- subtracao')
print('* multiplicacao')
print('/ divisao')
print('pressione outra tecla para sair')

op = input('Qual operacao deeja fazer?')
if (op == '+' or op == '-' or op == '/' or op == '*'):
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

while (op != 's'):
    if (op == '+'):
        res = x + y
        print('resultado: {} + {} = {}'.format(x, y, res))
    elif (op == '-'):
        res = x - y
        print('resultado: {} - {} = {}'.format(x, y, res))
    elif (op == '*'):
        res = x * y
        print('resultado: {} * {} = {}'.format(x, y, res))
    elif (op == '/'):
        res = x / y
        print('resultado: {} / {} = {}'.format(x, y, res))
    else: 
        print('Operacao invalida')

    op = input('Qual operacao deeja fazer?')
    if (op == '+' or op == '-' or op == '/' or op == '*'):
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

print('encerando o programa')"""


print('CALCULADORA')
print('+ adicao')
print('- subtracao')
print('* multiplicacao')
print('/ divisao')
print('pressione outra tecla para sair')

while True:
    op = input('Qual operacao deeja fazer?')
    if (op == '+' or op == '-' or op == '/' or op == '*'):
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))
    if (op == '+'):
        res = x + y
        print('resultado: {} + {} = {}'.format(x, y, res))
        continue
    elif (op == '-'):
        res = x - y
        print('resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('resultado: {} / {} = {}'.format(x, y, res))  
        continue 
    elif(op == 's'):
        break
    else: 
        print('Operacao invalida')
 
        

print('encerando o programa')