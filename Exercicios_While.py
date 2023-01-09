#1. Input até o usuário parar -Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em uma lista.O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade. Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

vendas = []

while True:
    produto = input("Informe o nome do produto: ")
    if not produto:
        break    
    quantidade = int(input("Informe a quantidade: "))
    vendas.append([produto, quantidade])

print(vendas)

#2. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

notas = []

nota = float(input("Informe uma nota entre 0 e 10: "))

while True:
    if nota <= 10:
        notas.append(nota)
        print("Nota inserida com sucesso!")
        break
    else:
        print("Valor incorreto! Só é permitido valores entre 0 a 10. Tente novamente!")
        nota = float(input("Informe uma nota entre 0 e 10: "))

#3. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

login = input("Informe o login: ")
senha = input("Informe a senha: ")

while True:
    if senha == login:
        print("Sua senha não pode ser igual ao login, tente novamente!")
        login = input("Informe o login: ")
        senha = input("Informe a senha: ")
    else:
        print("Cadastro realizado com sucesso!")
        break

#terminar
#4. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):

#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
# salario = int(input("Infome seu salario: R$ "))
# sexo = input("Informe seu sexo: ")
# estado_civil = input("Informe seu Estado Civil: ")

while True:
    nome = input("Informe seu nome: ")
    if len(nome) < 3:
        print("Nome inválido, digite novamente!")
        nome = input("Informe seu nome: ")
    if not (idade >= 0 and idade <= 150):
        print("Idade inválida, digite novamente!")
        idade = input("Informe sua idade: ")
    else:
        print("Cadastro realizado com sucesso!")
        break

#5. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

#6. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

#7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento

#8. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o faturamento total (soma) e o faturamento médio por mês (média).

#9.  Faça um programa que consiga categorizar a idade das equipes de uma empresa. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da equipe varia entre 0 e 25 (jovem) ,26 e 60 (sênior) e maior que 60 (idosa); e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada.

#10. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

#11. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

#12. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

##12. O Sr. Manoel Joaquim possui uma grande loja de artigos de R\\$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

#13. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário desse funcionário em 2003. 

#14. O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
