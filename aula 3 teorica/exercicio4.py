# escreva um algoritimo em python em que o ususario escolhe se quer comprar macas, laranjas ou bananas. devera ser apresentado na tela um menu com as opcoes: 1 para maca, 2 para laranja e 3 para banana apos escolhida a fruta deve se digitar quantas unidades se quer comprar. o algoritimo deve calcular o preco total a pagar do produto escolhido e mostra-lo na tela considere que uma maca custa r$2,30, uma laranja r$ 3,60 e uma banana r$ 1,85
fruta = int(input('escolha a fruta que deseja comprar:\ndigite 1 para maca\ndigite 2 para laranja\ndigite 3 para banana\n:'))

unid = int(input('quantas unidades voce deseja comprar: '))
 
maca = unid * 2.30
laranja = unid * 3.60
banana = unid * 1.85


if (fruta == 1):
    print('o preco total ficou {}'.format(maca))
if (fruta == 2):
    print('o preco total ficou {}'.format(laranja))
if (fruta == 3):
    print('o preco total ficou {}'.format(banana))