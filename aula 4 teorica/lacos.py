#podemos inserir lacos dentro de outro laco
#nao existe limite para quantos lacos podemos colocar dentro de outro
#podemos misturar while e for

# escreva um algoritimos em python que calcule a tabuada de todos os numeros de 1 até 10, e, para cada numero vamos calcular a tabuada multiplicando-o pelo intervalo de 1ate 10

# 2 while
tabuada = 1 
while tabuada <= 10:
    print('TABUADA DO {}'.format(tabuada))
    i = 1
    while i <= 10:
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1
# 2 for
for tabuada in range(1,11,1):
    print('TABUADA DO {}'.format(tabuada))
    for i in range(1,11,1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
 
 #while + for 

tabuada = 1 
while tabuada <= 10:
    print('TABUADA DO {}: '.format(tabuada))
    for i in range(1,11,1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
    tabuada += 1