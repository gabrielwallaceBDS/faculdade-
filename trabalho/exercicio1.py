
while True: 
    nome = input('nome do aluno: ')#nome do aluno 
    notaFinal = float(input('nota final: '))# numero flutuante nota final 
    if(notaFinal <= 2.9):# se a notaFinal for menor que 2.9 retornar print se enquadra no conceito E
     print('O aluno {} tirou a nota {} e se enquadra no conceito E'.format(nome, notaFinal))
    elif(notaFinal >= 3.0 and notaFinal <= 4.9 ):# se a notaFinal for maior do que 3.0 e menor que 4.9 retornar print se enquadra no conceito D
     print('O aluno {} tirou a nota {} e se enquadra no conceito D'.format(nome, notaFinal))
    elif(notaFinal >= 5.0 and notaFinal <= 6.9 ):# se a notaFinal for maior do que 5.0 e menor que 6.9 retornar print se enquadra no conceito C
     print('O aluno {} tirou a nota {} e se enquadra no conceito C'.format(nome, notaFinal))
    elif(notaFinal >= 7.0 and notaFinal <= 8.9 ):# se a notaFinal for maior do que 7.0 e menor que 8.9 retornar print se enquadra no conceito B
     print('O aluno {} tirou a nota {} e se enquadra no conceito B'.format(nome, notaFinal))
    elif(notaFinal >= 9.0 and notaFinal <= 10.0 ):# se a notaFinal for maior do que 9.0 e menor que 10.0 retornar print se enquadra no conceito A
     print('O aluno {} tirou a nota {} e se enquadra no conceito A'.format(nome, notaFinal))
    dados = input('deseja fazer outra operacao? \n1 - SIM \n2 - NAO\n:')# imprimir texto deseja fazer outra opercacao 1 para SIM E 2 para NAO
    if(dados == '1'):# se dados digitado for igual a 1 voltar ao inicio(reiniciar o programa)
        continue
    elif(dados == '2'):# se dados digitado for igual a 2 parar o programa 
        break

