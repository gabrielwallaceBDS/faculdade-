# funcao x procedimento
# procedimento (procedure) - uma rotina sem retorno
# funcao - uma rotina que retorna um dado a quem a invocou


def soma3(x = 0, y = 0, z = 0):
  res = x + y + z 
  return res

#forma alternativa simplificada
print(soma3(2,2))

# programa principal
retornando1 = soma3(1,2,3)
retornando2 = soma3(1,2)
retornando3 = soma3()
print('Somatorios: {}, {} e {}.'.format(retornando1,retornando2,retornando3))