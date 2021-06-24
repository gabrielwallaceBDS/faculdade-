#m cinema cobra precos diferentes para os ingressos de acordo coma idade de uma pessoas. se a pessoa tiver menos de 3 de idade, o ingresso sera gratuito, se tiver entre 3 e 12 anos, o ingresso custara R$15, se tiver mais de 12 anos , custara R$ 30

idade = int(input('qual sua idade? '))

if (idade < 3):
    print('o ingresso é gratuito')
elif(idade >= 3 and idade <= 12):
    print('o ingresso custa R$ 15')
if(idade > 12):
    print('o ingresso custa R$ 30')
