# matriz 3 x 2
valor = [["d","s"],     # linha 0
         ["f","k","o"], # linha 1
         ["r","m"]      # linha 2
]

print(valor)
print()
print(valor[2][0]) # letra r

valor.append(['h','j'])
print(valor)
print()

valor.insert(0,['z','y'])
print(valor)
print()

valor[3][0] = 'a'
print(valor)
print()

valor.pop(1)
print(valor)
print()

valor.sort()
print(valor)
print()

print(len(valor))
print(valor)