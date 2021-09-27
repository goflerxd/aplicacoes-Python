valori = int(input('Digite o valor inicial  '))
valorf = int(input('Digite o valor final  '))

# com while
while valori <= valorf:
    print('Número',valori)
    valori = valori + 1

    print()
    #com for
    for valori in range(valorf):
     print('Número' ,valori+1)