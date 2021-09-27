# Atividade de Função 
# Escreva uma função que recebe como entrada um número inteiro positivo n e retorne 
# a soma de todos os inteiros positivos menores ou iguais a n.

def somanumeros(x):
    i = 1 
    soma = 0 
    while i <= x:
        soma = soma + i
        i = i + 1 
    return soma
        
valor = int(input('Digite o valor para ser somado:  '))
print()
print('A soma é' ,somanumeros(valor))