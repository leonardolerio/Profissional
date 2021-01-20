from cores import cor, limpa
from espacos import tio, tracos

def calculoImposto(taxas):
    #informações das ações
    acao = input('Digite o código da ação: ')
    valorAcao = float(input('Digite o valor da operação: '))
    tipo = input('C/V? ').upper()
    print()

    #Cálculo do imposto
    porcentagemL = taxas[0] / total
    porcentagemE = taxas[1] / total
    porcentagemC = taxas[2] / total
    porcentagemIS = taxas[3] / total
    porcentagemB = taxas[4] / total
    porcentagemIR = taxas[5] / total
    taxaL = valorAcao * porcentagemL
    taxaE = valorAcao * porcentagemE
    taxaC = valorAcao * porcentagemC
    taxaIS = valorAcao * porcentagemIS
    taxaB = valorAcao * porcentagemB
    taxaIR = valorAcao * porcentagemIR
    subTotal = taxaL + taxaE + taxaC + taxaIS + taxaB + taxaIR
    if tipo == 'C': subTotal -= taxaIR

    #Impressão dos impostos
    print(f'{cor(1)}Subtotal das taxas = {subTotal:.2f}{cor(1,37)}')
    return subTotal, acao


def recebeTaxas():
    print('-'*50)
    taxas = []
    taxas.append(float(input(f'{cor(1,37)}Taxa de liquidação: ')))
    taxas.append(float(input('Emolumentos: ')))
    taxas.append(float(input('Taxa de corretagem: ')))
    taxas.append(float(input('Taxa de ISS: ')))
    taxas.append(float(input('Taxa Bovespa: ')))
    taxas.append(float(input('Taxa de IRRF: ')))
    print('-'*50)
    return taxas

print(cor(1))
tracos('IMPOSTO DE MOVIMENTO DE RENDA VARIÁVEL', 50)
total = float(input('Digite o valor total da operação do dia: '))
taxas = recebeTaxas()

subtotais, acoes = [], []
while True:
    valorTaxa, acao = calculoImposto(taxas)
    subtotais.append(valorTaxa)
    acoes.append(acao)
    print('-'*40)
    resposta = input('Deseja calcular mais alguma ação? [S/N]: ').upper()
    if resposta == 'N':
        limpa()
        print()
        break
    if resposta not in 'SN': resposta = input('Digite uma resposta válida[S/N]: ')

print(f'{cor(1)}{"-"*15}RESULTADO{"-"*15}')
print()
print(f'Os valores dos impostos são:')

for x in range(len(subtotais)):
    print(f'{x + 1}° - {acoes[x]}: {subtotais[x]:.2f}')