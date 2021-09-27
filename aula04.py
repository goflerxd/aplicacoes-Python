#Cálculo do IMC
print('##############################################')
print('################Cálculo do IMC################')
print('################Balança Digital##############')
print('##############################################')

nome = input("Digite seu nome:  ")
peso = float(input("Digite seu peso:  "))
altura = float(input("Digite sua altura:  "))

imc = peso / pow(altura,2) #(altura*altura)
print()
print(nome, 'o seu IMC é igual a %2.f' % imc)
print()

if imc< 18.5:
    print(nome, ', você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(nome, ', você com o peso ideal')
elif imc >= 25 and imc <40:
    print(nome, ", você está com sobrepeso")
else:
    print(nome, ", você está obeso")


print('##############################################')
print('##############################################')
print('######## Obrigado, Se Cuide! #################')
print('##############################################')
