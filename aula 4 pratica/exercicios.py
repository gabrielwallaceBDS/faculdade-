#realize a sequencia de print com for e while:
# A) inteiros de 3 até 12, com 12 incluso
# B) inteiros de 0 até 9, esxcluindo 9, com passo de 2

#A)
x = 3 
while (x < 13):
    print(x)
    x += 1

for x in range (3,13):
    print(x)

# B)
for i in range(0,9,2):
    print(i)

x = 0
while(x < 9):
    print(x)
    x += 2