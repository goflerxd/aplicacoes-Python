# Calculadora média aritmética do aluno
# Média superior a 7.0

print('Calculadora de médias do aluno')
print("Insira as notas dos bimestres conforme o inidicado")
nota1 = float(input("Nota 1º: "))

nota2 = float(input('Nota 2º: '))

nota3 = float(input('Nota 3º: '))

nota4 = float(input('Nota 4º: '))



media1 = (nota1+nota2+nota3+nota4)/4


print (media1)

if media1 >= 7:
   print("Aprovado!")


if media1 < 7:
   print("Reprovado")
