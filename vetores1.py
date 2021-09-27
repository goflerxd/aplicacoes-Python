
print('Lista de 1 a 10 somente com números pares')
print("> Lista original (1, 2, 3, 4, 5, 6, 7, 8, 9,10)")

input('>>> Digite enter para iniciar a aplicação:  ')

lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] #Lista inicial/original
print(len(lista))

# Números para remover

lista.remove('1')
lista.remove('3')
lista.remove('5')
lista.remove('7')
lista.remove('9')

print(">>> Lista atualizada")
print(lista)