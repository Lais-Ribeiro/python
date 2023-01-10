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


#4. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento#7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento
i =  1
faturamento = 0
while i <= 5:
    mensal = int(input("Infome o faturamento do {}º mês: ".format(i)))
    if mensal > faturamento:
         faturamento = mensal
    i+= 1

print("O maior faturamento foi de R$ {:.2f}.".format(faturamento))

#5. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o faturamento total (soma) e o faturamento médio por mês (média).

i =  1
faturamento = 0
while i <= 5:
    mensal = int(input("Infome o faturamento do {}º mês: ".format(i)))
    faturamento += mensal
    i+= 1

media = faturamento / 5

print("O faturamento total foi de R$ {:.2f} e o faturamento médio foi de R$ {:.2f}." .format(faturamento, media))

#6. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input("Informe o número de eleitores: "))

i = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0

while i < eleitores:
    candidato = int(input("Informe seu voto: "))
    if candidato == 1:
        candidato1 += 1
        i += 1
    elif candidato == 2:
        candidato2 += 1
        i += 1
    elif candidato == 3:
        candidato3 += 1
        i += 1
    else:
        print("Número de candidato inválido, digite novamente!")


print("O candidato 1 recebeu {} voto(s).".format(candidato1))
print("O candidato 2 recebeu {} voto(s).".format(candidato2))
print("O candidato 2 recebeu {} voto(s).".format(candidato3))

