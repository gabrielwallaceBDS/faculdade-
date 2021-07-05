
while True: 
    nome = input('nome do aluno: ')
    notaFinal = float(input('nota final: '))
    if(notaFinal <= 2.9):
     print('O aluno {} tirou a nota {} e se enquadra no conceito E'.format(nome, notaFinal))
    elif(notaFinal >= 3.0 and notaFinal <= 4.9 ):
     print('O aluno {} tirou a nota {} e se enquadra no conceito D'.format(nome, notaFinal))
    elif(notaFinal >= 5.0 and notaFinal <= 6.9 ):
     print('O aluno {} tirou a nota {} e se enquadra no conceito C'.format(nome, notaFinal))
    elif(notaFinal >= 7.0 and notaFinal <= 8.9 ):
     print('O aluno {} tirou a nota {} e se enquadra no conceito B'.format(nome, notaFinal))
    elif(notaFinal >= 9.0 and notaFinal <= 10.0 ):
     print('O aluno {} tirou a nota {} e se enquadra no conceito A'.format(nome, notaFinal))
    cod = input('deseja fazer outra operacao? \n1 - SIM \n2 - NAO\n::')
    if(cod == '1'):
        continue
    elif(cod == '2'):
        break

