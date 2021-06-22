#EXERCICIO 1 
# FACA UM ALGORITIMO QUE RECEBA TRES VALORES, REPRESENTANDO OS LADOS DE UM TRIANGULO FORNECIDOS PELO USUARIO. VERIFIQUE SE OS VALORES FORMAM UM TRIANGULO E CLASIFIQUE COMO 
# A)EQUILATERO (TRES LADOS IGUAIS) 
# B)ISOCELES (DOIS LADOS IGUAIS)
# C)ESCALENO (TRES LADOS DIFERENTES
lado1 = float(input('Digite o primeiro valor: '))
lado2 = float(input('Digite o segundo valor: '))
lado3 = float(input('Digite o terceiro valor: '))

if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 != lado2 and lado1 != lado3 and lado2 !=lado3:
            print('triangulo escaleno')
        else:
            if lado1 == lado2 and lado2 == lado3 and lado2 == lado3:
                print('triangulo equilatero')
            else:
                print('triangulo isoceles')
    else:
        print('ao menos um dos valores indicados nao servem para formar um triangulo')
else:
    print('ao menos um dos valores nao servem para formar um triangulo')
            