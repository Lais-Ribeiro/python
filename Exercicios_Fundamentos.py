'''1- Imposto a pagar no Lucro Presumido

- 5% sobre faturamento de ISS (mensal)
- 0,65% de PIS sobre faturamento, (mensal)
- 3% de COFINS sobre faturmaneto, (mensal)
- 4.8% de IR (trimestral)
- 10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
- CSLL: 2,88% sobre faturamento (trimestral)'''

faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

#Formatar em numero

def formata_mumero(valor):
    valor =  float(valor.replace("R$ ", "").replace(".", "").replace(",", "."))
    return valor

def calcula_imposto_mensal(valor):
    iss = valor * 0.05
    pis = valor * 0.0065
    cofins = valor * 0.03
    imposto_mensal = iss + pis + cofins
    return imposto_mensal

def calcula_imposto_trimestral(valor):
    ir = valor * 0.048
    csll = valor * 0.0288

    if valor > 20000:
        ir_adicional = (valor - 20000) * 0.1
    else:
        ir_adicional = 0
    
    imposto_trimestral = ir + csll + ir_adicional

    return imposto_trimestral

for mes in faturamento:
    valor = formata_mumero(faturamento[mes])
    imposto_mensal = calcula_imposto_mensal(valor)
    imposto_trimestral = calcula_imposto_trimestral(valor)

    faturamento[mes] = (valor, imposto_mensal, imposto_trimestral)

print(faturamento)

# você precisa inserir no sistema um dicionário no formato:

# resultado = {
#     'mes': (faturamento, imposto_mensal, imposto_trimestral),
# }

### 2 - Puxando informações de um banco de Dados
# puxando informações SQL de um banco de dados
informacoes = [(1, 'NATHANIEL FORD', 'GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY', 167411.18, 0.0, 400184.25, None, 567595.43, 567595.43, 2011, '', 'San Francisco', ''), (2, 'GARY JIMENEZ', 'CAPTAIN III (POLICE DEPARTMENT)', 155966.02, 245131.88, 137811.38, None, 538909.28, 538909.28, 2011, '', 'San Francisco', ''), (3, 'ALBERT PARDINI', 'CAPTAIN III (POLICE DEPARTMENT)', 212739.13, 106088.18, 16452.6, None, 335279.91, 335279.91, 2011, '', 'San Francisco', ''), (4, 'CHRISTOPHER CHONG', 'WIRE ROPE CABLE MAINTENANCE MECHANIC', 77916.0, 56120.71, 198306.9, None, 332343.61, 332343.61, 2011, '', 'San Francisco', ''), (5, 'PATRICK GARDNER', 'DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)', 134401.6, 9737.0, 182234.59, None, 326373.19, 326373.19, 2011, '', 'San Francisco', ''), (6, 'DAVID SULLIVAN', 'ASSISTANT DEPUTY CHIEF II', 118602.0, 8601.0, 189082.74, None, 316285.74, 316285.74, 2011, '', 'San Francisco', ''), (7, 'ALSON LEE', 'BATTALION CHIEF, (FIRE DEPARTMENT)', 92492.01, 89062.9, 134426.14, None, 315981.05, 315981.05, 2011, '', 'San Francisco', ''), (8, 'DAVID KUSHNER', 'DEPUTY DIRECTOR OF INVESTMENTS', 256576.96, 0.0, 51322.5, None, 307899.46, 307899.46, 2011, '', 'San Francisco', ''), (9, 'MICHAEL MORRIS', 'BATTALION CHIEF, (FIRE DEPARTMENT)', 176932.64, 86362.68, 40132.23, None, 303427.55, 303427.55, 2011, '', 'San Francisco', ''), (10, 'JOANNE HAYES-WHITE', 'CHIEF OF DEPARTMENT, (FIRE DEPARTMENT)', 285262.0, 0.0, 17115.73, None, 302377.73, 302377.73, 2011, '', 'San Francisco', '')]
descricao = (('Id', "<class 'int'>", None, 10, 10, 0, True), ('EmployeeName', "<class 'str'>", None, 65536, 65536, 0, True), ('JobTitle', "<class 'str'>", None, 65536, 65536, 0, True), ('BasePay', "<class 'float'>", None, 54, 54, 0, True), ('OvertimePay', "<class 'float'>", None, 54, 54, 0, True), ('OtherPay', "<class 'float'>", None, 54, 54, 0, True), ('Benefits', "<class 'float'>", None, 54, 54, 0, True), ('TotalPay', "<class 'float'>", None, 54, 54, 0, True), ('TotalPayBenefits', "<class 'float'>", None, 54, 54, 0, True), ('Year', "<class 'int'>", None, 10, 10, 0, True), ('Notes', "<class 'str'>", None, 65536, 65536, 0, True), ('Agency', "<class 'str'>", None, 65536, 65536, 0, True), ('Status', "<class 'str'>", None, 65536, 65536, 0, True))

# precisamos 1º de uma lista com o nome das colunas para poder organizar as colunas da nossa tabela:
# o nome das colunas está na variável descrição, dê uma olhada.

import pandas as pd

colunas = [tupla[0] for tupla in descricao]
tabela = pd.DataFrame.from_records(informacoes, columns=colunas) # onde colunas é uma lista com o nome das colunas
print(tabela)


# além disso, precisamos enviar por e-mail para o RH uma lista com o nome e o cargo de cada pessoa da tabela 
# então você precisa construir o texto do corpo desse email:

texto = "RH, segue a lista dos funcionários: \n"

for item in informacoes:
    nome = item[1]
    cargo = item[2]
    texto = texto + "Nome: " + nome + " Cargo: " + cargo + "\n"

print(texto)

### 3 - Extração dos links de Download de Vídeos do Vimeo

### - Precisamos pegar os links em 1080p, 720p e 540p para importar os vídeos para uma nova plataforma

# para pegar o dicionario do vimeo, use:
from dic import dicionario_vimeo

informacoes_video = dicionario_vimeo['data']

videos = []

for dicionario in informacoes_video:
    for item in dicionario:
        uri = dicionario['uri']
        nome = dicionario['name']
        duracao = dicionario['duration']
        informacoes_download = dicionario["download"]

        link540p = ''
        link720p = ''
        link1080p = ''

        for dicionario_download in informacoes_download:
            if dicionario_download["rendition"] == "720p":
                link720p = dicionario_download["link"]
            elif dicionario_download["rendition"] == "540p":
                link540p = dicionario_download["link"]
            elif dicionario_download["rendition"] == "1080p":
                link1080p = dicionario_download["link"]

        videos.append({
            "uri": uri,
            "nome": nome,
            "duracao": duracao,
            "link540p": link540p,
            "link720p": link720p,
            "link1080p": link1080p,
        })



print(videos)

# você precisa chegar em:
# videos = [
#     {'uri': video_uri, 'nome': nome_video, 'duracao': duracao, 'link540p': link540p, 'link720p': link720p, 'link1080p': link1080p},
# ]