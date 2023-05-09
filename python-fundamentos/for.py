s = 0
for c in range(0,51):
    if c%2!=0:
        if c%3==0:
            print(c)
            s += c
print('A soma dos números impares que são multiplos de 3 é {}'.format(s))