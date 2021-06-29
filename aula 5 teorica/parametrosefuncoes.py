# parametros - dados recebidos pelas funcoes 
# o ato de enviar um dado para uma funcao é chamado de paisagem de parametro
def realce(s1):
     print('|','__' * 10,'|')
     print('|','__' * 10,'|')
     print(s1)
     print('|','__' * 10,'|')
     print('|','__' * 10,'|')

# programa principal
realce('           MENU')

def sub2 (x, y):
    res = x - y
    print(res)

# programa principal
sub2(5, 7)
sub2(7, 5)
sub2(y = 7, x = 5)


# parametros opcionais
def soma3 (x, y, z):
    res = x + y + z
    print(res)

def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    print(res)

soma3(1,2,3)
soma3(1,2)# z foi omitido
soma3(1)  # y e z foram omitidos  
soma3()   # x, y e z foram omitidos
