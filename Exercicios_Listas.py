#Dado as seguintes listas, respodnda: Qual foi o valor de vendas do melhor mês do Ano? E valor do pior mês do ano?Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.Crie uma lista com o top 3 valores de vendas do ano.

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)

melhor_mes = max(vendas_1sem)
pior_mes = min(vendas_1sem)

print('O valor do melhor mês do ano foi R$ {:.2f}.'.format(melhor_mes))
print('O valor do pior mês do ano foi R$ {:.2f}.'.format(pior_mes))

i_melhor_mes = vendas_1sem.index(melhor_mes)
i_pior_mes = vendas_1sem.index(pior_mes)

print('O melhor mês do ano foi {} com R$ {:.2f}.'.format(meses[i_melhor_mes], melhor_mes))
print('O pior mês do ano foi {} com R$ {:.2f}.'.format(meses[i_pior_mes], pior_mes))

faturamento_total = sum(vendas_1sem)

print('O faturamento total do ano foi de R$ {:.2f}.'.format(faturamento_total))

percentual = melhor_mes / faturamento_total

print('O melhor mês representou {:.1%} das vendas.'.format(percentual))

top3 = []

for i in range(3):
    melhor_mes = max(vendas_1sem)
    top3.append(melhor_mes)
    vendas_1sem.remove(melhor_mes)

print('A primeira melhor venda do ano foi R$ {:.2f}, a segunda foi R$ {:.2f} e a terceira foi R$ {:.2f}.'.format(top3[0], top3[1], top3[2]))
