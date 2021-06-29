#escreva uma funcao para validar uma string essa funcao recebe como parametro a string, onumero minimo e maximo de caracteres. retorne verdadeiro se o tamanho da string estiver entre os valores de minimo e maximo, e fals0o caso contrario (elaborado com base em menezesm s.d)

def valida_string(pergunta, min, max):
  s1 = input(pergunta)
  tam = len(s1)
  while ((tam < min) or (tam > max)):
      s1 = input(pergunta)
      tam = len(s1)
  return s1

  # programa principal
  x = valida_string('Digite uma string: ', 10, 30)
  print('voce digitou a string: {}. \n Dado valido. Encerrando o programa...'.format(x))

    