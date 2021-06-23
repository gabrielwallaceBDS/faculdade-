#WHILE(ENQUANTO) REPETE UM BLOCO DE INSTRUCOES ENQUANTO DETERMINADA CONDICAO SE MANTIVER VERDADEIRA CASO CONTRARIO, OCORRE O DESVIO PARA A PRIMEIRA LINHA DE CODIGO APOS ESTE BLOCO DE REPETICAO while (x > y ):

x = 1 
while (x <= 5):
    print(x)
    x = x + 1

""""LOOP INFINITO DE 1

while (x <= 5):
    print(x)
# x = x + 1"""


# variavel de controle define a condicao de parada com que o laco é executado, chamamos de iterador a variavel de controle que realiza a contagem do numero de vezes que o laco esta sendo executado 

x = 0
while (x <= 99):
    print(x)
    x = x + 1

# variaveis contadoras e acumuladas CONTADORAS: acresentam valores constantes em uma variavel ACUMULADORAS: acumulam totais, como um somatorio

#exercicios 
# escreva um algoritimo que imprima na tela somente valores dentro de um intervalo especificado pelo usuario e que sejam numero pares 

inicial = int(input('escreva um valor: ')) #10

final = int(input('escreva um valor maior que o anterior: ')) #20

x = inicial

while (x <= final ):
    if(x % 2 == 0):
        print(x)
    x = x + 1

    # exercicios 
    # escreva um algoritimo que calcule a sua media de notas em determinada disciplina vamos assumir que a media final é dada pela media aritimetica de cinco notas digitadas 

    soma = 0 
    cont = 1
    while ( cont <= 5):
        x = float(input('Digite a {} nota: '.format(cont)))
        soma = soma + x 
        cont = cont + 1
    media = soma / 5
    print('media final: {}'.format(media))