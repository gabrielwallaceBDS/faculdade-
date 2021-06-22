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

if (norte and sul and leste and oeste == 0):
    print('voce escapou')