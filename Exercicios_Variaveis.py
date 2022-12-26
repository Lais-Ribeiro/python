"""
Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano. 
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
Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.
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