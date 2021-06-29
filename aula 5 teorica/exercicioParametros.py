# escreva uma rotina que crie uma borda ao redor de uma palavra para destaca-la como sendo um titulo. A rotina deve receber como parametro a palavra a ser destacada. O tamanho da caixa de texto devera ser adaptavel de acordo com o tamanho da palavra.

#exercicio
def borda(s1):
 tam = len(s1)
# so imprime caso exista algum caractere
 if tam:
     print('+','-' * tam,'+')
     print('|',s1,'|')
     print('+','-' * tam,'+')
#programa principal
borda('ola, Mundo')
borda('logica de programacao e algoritimos')

