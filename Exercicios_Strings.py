# 1. Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input.Caso o usuário digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente"

cpf = input('Informe o CPF: ')

cpf_tratado = cpf.strip().replace('.', '').replace('-', '')

if len(cpf_tratado) == 11 and cpf_tratado.isnumeric():
    print('Cadastro efetuado. O CPF {} foi cadastrado com sucesso!'.format(cpf_tratado))
else:
    print('Digite seu CPF corretamente!')

#2. Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente e se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido
nome = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')

if nome and email:
    if '@' in email and '.' in email[email.find('@'):]:
        print('Cadastro efetuado com sucesso!')
    else:
        print('Digite o e-mail corretamente')
else:
    print('Preencha todos os dados corretamente!')

#3.Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

txt_1 = input('Digite o primeiro texto: ')
txt_2 = input('Digite o segundo texto: ')

print('A primeira String é "{}" e possui {} caracteres.'.format(txt_1, len(txt_1)))
print('A segunda String é "{}" e possui {} caracteres.'.format(txt_2, len(txt_2)))

if len(txt_1) == len(txt_2):
    print('As duas Strings possui o mesmo tamanho!')
else:
    print('As duas Strings possuem tamanhos diferentes!')
    
if txt_1 == txt_2:
    print('As duas Strings são iguais!')
else:
    print('As duas Strings são diferentes!')

#4. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

telefone = input('Digite o número de telefone: ')

telefone = telefone.strip().replace('-', '')

if len(telefone) == 7:
    telefone = '3' + telefone
    print('Telefone sem a formatação: {}'.format(telefone))
    print('Telefone com a formatação: {}{}{}'.format(telefone[:4], '-' , telefone[4:]))
else: 
    print('O telefone não possui 7 digitos.')
