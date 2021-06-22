#um aluno, para passar de ano, precisa ser aprovado em todas as materias que esta cursando
#assuma que a media para aprovacao éa partir de 7, e que o aluno cursa 3 materias, somente. escreva um algoritimo que leia a nota final do aluno em cada materia e informe na tela se ele passou de ano ou nao 

m1 = float(input('nota final materia 1: '))
m2 = float(input('nota final materia 2: '))
m3 = float(input('nota final materia 3: '))

if (m1 >= 7.0 and m2 >= 7.0 and m3 >= 7.0):
    print('aprovado')
else:print('reprovado')

#and = se as tres for true = true
#or = e uma for true = true