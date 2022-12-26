#1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.
print('Alo mundo!')

#2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."
numero = float(input('Informe um número: '))
print('O número informado foi {}.'.format(numero))

#3. Faça um Programa que peça dois números e imprima a soma
n1 = float(input('Informe o primeiro número: '))
n2= float(input('Informe o segundo número: '))
soma = n1 + n2
print('A soma de {} com {} é de {}.'.format(n1, n2, soma))

#4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.
n1 = float(input('Informa a 1ª nota: '))
n2 = float(input('Informa a 2ª nota: '))
n3 = float(input('Informa a 3ª nota: '))
n4 = float(input('Informa a 4ª nota: '))

media = (n1 + n2 + n3 + n4) / 4

print('A média do aluno foi de {:.2f}.'.format(media))

#5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

metro = float(input('Informe a quantidade em metros: '))

centimetros = metro * 100

print('{} metro(s) equivalem a {} cm(s).'.format(metro, centimetros))

#6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

comprimento = float(input('Informe o comprimento da sala: '))
largura = float(input('Informe a largura da sala: '))

area = comprimento * largura

print('Uma sala de {} metros de comprimento e {} metros de largura tem uma área de {} m²'.format(comprimento, largura, area))

#7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Informe quanto você ganha por hora: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhada no mês: '))

salario = valor_hora * horas_trabalhadas

print('Seu sálario mensal vai ser de R$ {}.'.format(salario))

#8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))

celsius = (fahrenheit - 32) * 1.8

print('{} °F equivalem a {} °C.'.format(fahrenheit, celsius))

#9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Informe a temperatura em Celsius: '))

fahrenheit =  1.8 * celsius + 32

print('{} °C equivalem a {} °F.'.format(celsius, fahrenheit))

#10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: P=72,7h−58

altura = float(input('Informe sua altura: '))

peso_ideal = 72.7 * altura - 58

print('O peso ideal de uma pessoa com {} metro(s) de altura é de {} kg.'.format(altura, peso_ideal))

#11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: a. Para homens:  P=72,7h−58 b. Para mulheres:  P=62,1h−44,7

altura = float(input('Informe sua altura: '))

peso_ideal_homens = 72.7 * altura - 58
peso_ideal_mulheres = 62.1 * altura - 44.7

print('O peso ideal com essa altura para homens é {:.2f} kg.'.format(peso_ideal_homens))
print('O peso ideal com essa altura para mulheres é: {:.2f} kg.'.format(peso_ideal_mulheres))

"""12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
a. Calcule o salário bruto
b. Calcule o desconto do IR (11% do salário bruto)
c. Calcule o desconto do INSS (8% do salário bruto)
d. Calcule o desconto do sindicato (5% do salário bruto)
e. Calcule o salário líquido (salário bruto - descontos)"""

valor_hora = float(input('Informe quanto você ganha por hora: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhada no mês: '))

salario_bruto = valor_hora * horas_trabalhadas
print('O seu salário bruto é de R$ {:.2f}.'.format(salario_bruto))

desconto_ir = salario_bruto * 0.11
print('Seu desconto de IR é de R$ {:.2f}.'.format(desconto_ir))

desconto_inss = salario_bruto * 0.08
print('Seu desconto de INSS é de R$ {}.'.format(desconto_inss))

desconto_sindicado = salario_bruto * 0.05
print('Seu desconto de Sindicaro é de R$ {}.'.format(desconto_sindicado))

descontos_totais = desconto_ir + desconto_inss + desconto_sindicado
salario_liquido = salario_bruto - descontos_totais
print('Seu sálario liquído é de R$ {}.'.format(salario_liquido))

#13. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 

area = float(input('Informe a quantidade de m² a serem pintadas: '))

litros_tinta = area / 3
latas = litros_tinta / 18
preco_total = latas * 80

print('É necessario {:.2f} latas de tintas para pintar {:.2f} m², ficando no valor de R$ {:.2f}'.format(latas, area, preco_total))

"""
#14. Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano. 
Obs: faça tudo usando variáveis.

Valores do último ano:

Quantidade de Vendas de Coca = 150
Quantidade de Vendas de Pepsi = 130
Preço Unitário da Coca = 1,50 
Preço Unitário da Pepsi = 1,50
Custo da Loja: 2.500,00

Qual foi o faturamento de Pepsi da Loja?
Qual foi o faturamento de Coca da Loja?
Qual foi o Lucro da loja?
Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual

"""
qtd_vendas_coca = 150
qtd_vendas_pepsi = 130
preco_coca = 1.50
preco_pepsi = 1.50
custo = 2500

#Qual foi o faturamento de Pepsi da Loja?
faturamento_pepsi = preco_pepsi * qtd_vendas_pepsi
print('O faturamento da pespi foi de R$ {:.2f}'.format(faturamento_pepsi))

#Qual foi o faturamento de Coca da Loja?
fautramento_coca = preco_coca * qtd_vendas_coca
print('O faturamento da Coca-Cola foi de R$ {:.2f}'.format(fautramento_coca))

#Qual foi o Lucro da loja?
faturamento_total = faturamento_pepsi + fautramento_coca
lucro =  faturamento_total - custo
print('O lucro da loja foi de R$ {:.2f}'.format(lucro))

#Qual foi a Margem da Loja? 
margem = lucro / faturamento_total
print('A margem de lucro foi de  {:.0%}'.format(margem))

"""
#15. Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.
Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

Coca -> Código: BEB1300543
Pepsi -> Código: BEB1300545
Vinho Primitivo Lucarelli -> Código: BAC1546001
Vodka Smirnoff -> Código: BAC17675002

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.
"""
cod_coca = 'BEB1300543'
cod_pepsi = 'BEB1300545'
cod_vinho_lucarelli = 'BAC1546001'
cod_vodka_smirnoff = 'BAC17675002'

codigo = input('Isira o código da bebida: ')
if 'BAC' in codigo:
    print('Bebida Alcoólica')
else:
    print('Bebida não Alcoólica')