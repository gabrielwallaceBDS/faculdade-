# erros de sintaxe 
# ocorre quando o programador comete algum erro de digitacao, ou esquece de alguma palavra-chave, ou caractere, ou mesmo erra na indentacao do codigo 
# ERRO EXCECAO
# NESTE TIPO DE ERRO A SINTAXE ESTA CORRETA, POREM UM ERRO DURANTE A EXECUCAO DO PROGRAMA OCORRE, NORMALMENTE DEVIDO A UM DADO DIGITADO DE MANEIRA INVALIDA E NAO TRATADO DURANTE O PROGRAMA

# ZeroDivisionError - erro de divisao por zero
# ValueError - erro de um dado nao esperadosendo digitado
# IndexError - erro de indice inexistente sendo acessado
# lista completa https://docs.python.org/pt-br/3/library/exceptions.html#bltin-exceptions

x = int(input('por favor digite um numero: '))

#//////////////////////////////////////////////////////////////////////////////////////////////
"""
while True:
    try:
    x = int(input('por favor digite um numero: '))
    break
except ValueError:
    print('Oops! Numero invalido. tente novamente...')
    
"""


#//////////////////////////////////////////////////////////////////////////////////////////////
def div():
  try:
      num1 = int(input('digite um numero'))
      num1 = int(input('digite um numero'))
      res = num1 / num2
  except ZeroDivisionError:
      print("Oops! erro de divisao por zero...")
  else:
      return res
  finally:
      print('executara sempre')

    # programa principal
print(div())
#//////////////////////////////////////////////////////////////////////////////////////////////

#funcao como parametro de funcao

def imprime_com_condicao(num, fcond):
  if fcond(num):
      print(num)

def par(x):
  return x % 2 == 0
def impar(x):
  return not par(x)

#programa principal
imprime_com_condicao(5, par)

#//////////////////////////////////////////////////////////////////////////////////////////////

# funcao lambda
#funcoes mais simples, sem nome, chamadas de funcao lambda
#elas podem ser escritas em uma só linha de codigo e dentro do programa principal

res = lambda x : x * x
print(res(3))

soma = lambda x, y: x + y
print(soma(3,5))