nota = 8.5
s1 ='Voce tirou %f na disciplina de Algoritimos' % nota
print(s1)

#limitando casas decimais 
nota = 8.5
s1 ='Voce tirou %.2f na disciplina de Algoritimos' % nota
print(s1)

#varias variaveis
nota = 8.5
disciplina = 'Algoritimo'
s1 = 'Voce tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)
"""
MARCADOR    TIPO
%d ou %i    numeros inteiros
%f          numeros de ponto flutuante
%s          Strings

"""

#composicao mais moderna
#antiga
'Voce tirou %d na disciplina de %s' %(nota,disciplina)

#novo
'Voce tirou {} na disciplina de {}'.format(nota,disciplina)


#FATIAMENTO
s1 = 'Logica de Programacao e Algoritimos'
print(s1[0:6])

s1 = 'Logica de Programacao e Algoritimos'
print(s1[24:34])

s1 = 'Logica de Programacao e Algoritimos'
print(s1[:6])

#TAMANHO
s1 = 'Logica de Programacao e Algoritimos'
tamanho = len(s1)
print(tamanho)