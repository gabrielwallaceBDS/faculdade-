#crie um variavel de string que receba uma frase qualquer. crie uma segunda variavel, agora contendo a metade da string digitada. imprima na tela somente os dois ultimos caracteres da segunda variavel do tipo string

frase = input('digite uma frase: ')
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2)

frase3 = frase[-2:]
print(frase3)