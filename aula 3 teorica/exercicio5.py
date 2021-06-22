#escreva um algoritimo que le um nome e uma idade caso o nome digitado seja vinicius escreva isso na tela caso o usuario digite outro nome verfique sua idade se for menr que 18 anos informe que é de menor se for maior que 1000 anos informe que esta pessoa possivlemente nao existe 
nome = input('qual seu nome? ')
idade = int(input('qual sua idade? '))
if nome == 'Vinicius':
    print('Ola, Vinicius')
elif idade < 18:
    print('Voce nao é o Vinicius! E é menor de idade ')
elif idade > 100:
    print('Diferente de voce, o vinicius nao é imortal')

