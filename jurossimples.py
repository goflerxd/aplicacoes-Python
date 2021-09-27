# Calculadora Juros Simples
print('##############################################')
print('######## Calculadora Juros Simples  ##########')
print('##############################################')

# Entrada de Dados
capital = float(input('Digite o valor do empréstimo em real:  '))
taxa = float(input('Digite a taxa de juros em %:   '))
mes = float(input('Digite o tempo do empréstimos em meses:  '))

#processamento


juros = capital * (taxa/100) * mes 
montate = capital + juros

print()
print('O Valor de juros a pagar é de R$ %.2f' % juros)
print("O Valor total a pagar é de R$ %.2f" % montate)
print()

print('##############################################')
print('##### Obrigado por usar nossa aplicação  #####')
print('##############################################')
