"""A***B***C
print('A' + 3 * '*' + 'B' + 3 * '*' + 'C')

valor = int(input('digite o valor a ser somado com 100: '))
print(100 + valor)"""

x = 2
y = 5 
z = 0
resultado = 0
valor = int(input('digite o valor 1 2 ou 3: '))
if (valor == 1):
    resultado = x * valor
    valor = 2

elif (valor == 2):
    resultado = y * valor 
    valor = 3

elif (valor == 3):
    resultado = z * valor
else:
    print('valor invalido')
print(resultado)



