#expressoes booleanas
#A)O SOMATORIO DE 2 COM 2 É MENOR DO QUE 4
#B)O VALOR 7 // 3 É IGUAL A 1 + 1  
#C)A SOMA DE 3 ELEVADO AO QUADRADO COM 4 ELEVADO AO QUADRADO É IGUAL A 25
#D)A SOMA DE 2, 4 E 6 É MAIOR DO QUE 12
# A)
print(2 + 2 < 4)
# B)
print((7 // 3) == (1 + 1))
# C)
print(3**2 + 4**2 == 25)
# D)
print(2 + 4 + 6 > 12)


#ESCREVA AS SEGUINTES EXPRESSOES BOLEANAS EM LINGUAGEM PYTHON
# A) 1387 É DIVISIVEL POR 19
# B)31 É PAR
# C)O MENOR VALOR ENTRE 34, 29 E 31 É MENOR DO QUE 30
# A)
print(1387 % 19 == 0)
# B)
print(31 % 2 == 0 )
# C)
print(34 and 29 and 31 > 30) 

#condicional simples traduza as afirmacoes a seguir para condicionais em python 
# A) SE IDADE É MAIOR QUE 60 ESCREVA "VOCE TEM DIREITO AOS BENEFICIOS"
# B) SE DANO É MAIOR DO QUE 10 E ESCUDO É IGUAL A 0 ESCREVA "VOCE ESTA MORTO"
# C) SE PELO MENOS UMA DAS VARIANTES BOOLEANAS NORTE, LESTE E OESTE RESULTAREM EM TRUE,  ESCREVA "VOCE ESCAPOU"\

# A)
if (idade > 60):
 print('voce tem direito aos beneficios!!')
# B)
if (dano > 10 and escudo == 0): 
    print('voce esta morto!')
# C)

if (norte or sul or leste or oeste):
    print('voce escapou')

#TRADUZA AS AFIRMACOES A SEGUIR PARA CONDICIONAIS EM PYTHON
# A) SE ANO É DIVISIVEL POR 4, ESCREVA: 'PODE SER UM ANO BISSEXTO'. CASO CONTRARIO, ESCREVA 'DEFINITIVAMENTE NAO É UM ANO BISSEXTO'
# B) SE AMBAS AS VARIAVEIS BOOLEANAS CIMA E BAIXO FOREM True, ESCREVA: 'DECIDA-SE!', CASO CONTRARIO, ESCREVA 'VOCE ESCOLHEU UM CAMINHO!'
# A)
if (ano % 4 == 0 ):
    print('pode ser um nao bissexto')
elif():
    print('definitivamente nao é um ano bissexto')
# B)
if (cima and baixo == True):
    print('decida-se!')
elif():
    print('voce escolheu um caminho!')