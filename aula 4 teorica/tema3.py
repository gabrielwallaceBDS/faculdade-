""""
operadores especiais de atribuicao
operador    exemplo     equivalente
+=             x += 1         x = x + 1
-=             x-=1           x = x - 1
*=             x *= 2         x = x * 2
/=             x/=2           x = x / 2
**/            x ** =2        x = x ** 2
//=            x // = 4       x = x // 4
"""

""""soma = 0 
cont = 1
    while ( cont <= 5):
        x = int(input('Digite a {} nota: '.format(cont)))
        soma += x #equivalente: soma = soma + x
        cont += 1 #equivalente: cont = cont + 1
    media = soma / 5
    print('media final: {}'.format(media))"""

    # validando dados de entrada 
    # crie um valor que receba um valor do tipo inteiro via teclado 
    # no entanto, o programa so deve aceitar, obrigatoriamente valores inteiros e positivos 
    # qualquer valor negativo ou igual a zero deve ser rejeitado pelo programa e um nvo valor deve ser solicitado

"""valor = int(input('digite um valor maior que zero: '))

while (valor <= 0):
    valor = int(input('digite um valor maior que zero'))
print('voce digitou {} '.format(valor))"""

#Break a intrucao break serve para encerrar um laco de repeticao previamente, independente do estado da variavel de controle do laco 

#escreva um algoritimo que fique recebendo frases ou palavras digitadas pelo usuario, encerre o algoritimo quando a palavra sair for digitada 
"""print('digite uma frase que irei repetir para voce!')
print('para encerrar escreva "sair"')

while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('encerrando o programa')"""

#o comando continue serve para retornar o laco ao inicio a qualquer momento, independentemente do estado da variavel de controle da condicional do laco

while True:
    nome = input('Qual seu nome?')
    if (nome != 'gabriel'):
        continue
    senha = input('qual sua senha? ')
    if(senha == 'gabriel08'):
        break
print('accesso concedido')

#valores truthy e falsey dados nao booleanos tambem podem ser tratados como True ou False em uma condicao, seja esta de uma estrutura condicional ou de um laco 
#FALSEY/FALSE
    #NUMERO ZERO(INT OU FLOAT) E STRING VAZIA
#TRUTHY/TRUE
    #QUALQUER OUTRO DADO