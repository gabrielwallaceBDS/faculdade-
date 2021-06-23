# estrutura de repeticao for 
# assim como o while, essa estrutura repete um bloco de instrucoes enquanto uma condicao se mantiver verdadeira no entanto, diferentemente do while o for é empregado em situacoes em que O NUMERO DE VEZES QUE O LACO IRA EXECUTAR É FINITO E BEM DEFINIDO FOR I IN RANGE (6):
#for i in range(6):
 #   print(i)

#for (para) podemos definir o valor inicial do iterador 

#for i in range (0, 6, 1)

#for i in range (1.6,1):
 #   print(i)

#for i in range (10,0,-2):
 #   print(i)

# a mesma funcao
#x = 1
#while(x<6):
 #   print(x)
  #  x = x + 1

#mais simples 

#for i in range(1,6,1):
 #   print(i)

#exercicio escreva  um algoritimo que calcule a media dos numeros pares de 1 até 100 (1 e 100 inclusos) implemente o laso usando for

soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print('a media dos pares de 1 até 100 é: {}'.format(media))
