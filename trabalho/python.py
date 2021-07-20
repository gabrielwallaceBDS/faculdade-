i = 0
j = -9
k = 7

for cont in range(4, 11, 1):
    i = cont + 5
    while k > 0:
        k = k - 1
        j = k + j/2

print("i: %i j: %i k: %i" % (i, j, k))