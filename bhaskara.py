# Calculadora da fórmula de Bhaskara
# Dia 18/05/2021

print('##########################################')
print('#### Calculadora Fórmula de Bhaskara ####')
print('##########################################')

#formuula de baskara = (-b + ou - raiz(b² - 4ac) / 2a

import math

a = float(input('Digite o valor de A:  '))
b = float(input('Digite o valor de B:  '))
c = float(input('Digite o valor de C:  '))

delta = (b * b) - 4 * a * c

if delta < 0:
    
        print('Não tem solução')
        print('Tente outros valores')
elif delta == 0:
    fb = - b / (2 * a)
    print('O Resultado de x é' ,round(fb,1))
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print('O valor de X1 é',round(x1,2))
    print('O valor de X2 é',round(x2,2))


print('############################################')
print('#### Obrigado por usar nossa aplicação! ####')
print('############################################')  