#1. Criando um Registro de Hóspedes
# Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

# Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
# De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
# O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:

qtd_hospedes = int(input('Informe a quantidade de hospedes: '))

nomes = []
cpf = []

for i in range(qtd_hospedes):
    nome_hospede = input('Informe o nome do {}º hospede: '.format(i+1))
    nomes.append(nome_hospede)
    cpf_hospede = input('Informe o CPF do {}º hospede: '.format(i+1))
    cpf.append(cpf_hospede)

for nome in nomes:
    print('Nome: {} CPF: {}'.format(nomes[i], cpf[i]))

#2. Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for item in vendas:
    if item[1] >= meta:
        print('O vendedor {} bateu a meta vendendo R$ {:.2f}.'.format(item[0], item[1]))

#3.  Comparação com Ano Anterior. Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        percentual = vendas2020[i] / vendas2019[i] - 1
        print('O produto {} R$ {:.2f} em 2019 e R$ {:.2f} e teve um aumento de {:.1%} nas vendas.'.format(produto.upper(), vendas2019[i], vendas2020[i], percentual))


#4. Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a metae informe quem foi o vendedor que mais vendeu

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
bateram_meta = 0
qtd_vendedores = len(vendas)
melhor_venda = 0
nome_melhor =''

for venda in vendas:
    if venda[1] >= meta:   
        bateram_meta += 1  
        if venda[1] > melhor_venda:
            melhor_venda = venda[1]
            nome_melhor = venda[0]
        

percentual =  bateram_meta / qtd_vendedores
print('{:.0%} dos vendedores bateram a meta!'.format(percentual))
print('O melhor vendedor foi o {} com R$ {:.2f} vendas.'.format(nome_melhor, melhor_venda))
