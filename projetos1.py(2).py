#input do nome do usuário

nome = input("Insira seu nome: ")

#verificação classe de usuário

while True:
    classe_usuário = int(input('\ndigite o seu tipo de usuário\n\n[1]paciente\n[2]profissional de saúde\n\n'))
    if classe_usuário == 1 or classe_usuário == 2:
        break
    print('resposta inválida, tente novamente')

#verificação e validação do tipo de diabetes (usuário) formatar posteriormente em funções

while True:
    tipo = int(input("\nInsira seu tipo de diabetes: \n \n[1]diabetes tipo 1\n[2]diabetes tipo 2\n[3]diabetes gestacional\n[4]pré diabetes\n[5]proficional de saúde\n \n"))
    if tipo > 0 and tipo < 6:
        break
    print('\nresposta inválida, tente novamente') 

#input da glicemia (usuário) formatar posteriormente em funções

glicose = float(input(" \nInsira sua glicemia: "))

#verificação do nível glicêmico (usuário) formatar posteriormente em funções

if glicose <= 70:{
    print("Hipoglicemia")
}
elif 70 < glicose <= 150:{
    print("Glicose dentro do intervalo")
}
elif 150 < glicose <= 300:{
    print("Glicose acima do intervalo")
}
else:{
    print("Hiperglicemia")
}

#input quantidade decarbos (usuário) formatar posteriormente em funções

qtd_carbo = float(input("Informe a quantidade de carboidratos em gramas: "))

#calculadora quantidade de insulina (usuário) formatar posteriormente em funções

fator_correcao = 50
glicemia_alvo = 100
razao_carbo = 15

unidades_insulina = (((glicose - glicemia_alvo) / fator_correcao) + (qtd_carbo / razao_carbo))

#arredondamento da quantidade de insulina (usuário) formatar posteriormente em funções

import math

insulina_inteiro = math.trunc(unidades_insulina)

if (unidades_insulina - insulina_inteiro) == 0:
    insulina_print = unidades_insulina

if (unidades_insulina - insulina_inteiro) > 0 and (unidades_insulina - insulina_inteiro) < 0.5:
    insulina_print = math.floor(unidades_insulina)

if (unidades_insulina - insulina_inteiro) > 0.5:
    insulina_print = math.ceil(unidades_insulina)

#retorno unidades de insulina formatada (usuário) formatar posteriormente em funções

print(f"A quantidade de insulina a ser tomada é: {insulina_print}")

#diario (usuário) formatar posteriormente em funções

diario = str(input("escreva aqui seu acompanhamento diario: "))
print(diario)

#monitoramento consulta médica (usuário e medico) formatar posteriormente bibliotecas e funções

data_ultima_consulta = str(input('digite a data da sua última consulta médica (ex: 01/01/2001): '))

dia_ultima_consulta = int(data_ultima_consulta[:2])
mes_ultima_consulta = int(data_ultima_consulta[3:5])
ano_ultima_consulta = int(data_ultima_consulta[6:10])

data_atual = '20/03/2024'

dia_atual = int(data_atual[:2])
mes_atual = int(data_atual[3:5])
ano_atual = int(data_atual[6:10])

if ((dia_ultima_consulta - dia_atual) + ((mes_ultima_consulta - mes_atual) * 30) + ((ano_ultima_consulta - ano_atual) * 365)) * 2 > 180 * 2:
    
    print('parece que faz muito tempo desde a sua última consulta, vá imadiatamente consular o seu mádico')

if ((dia_ultima_consulta - dia_atual) + ((mes_ultima_consulta - mes_atual) * 30) + ((ano_ultima_consulta - ano_atual) * 365)) * 2 > 90 * 2:

    print('parece que faz um tempo desde a sua última consulta, é recomendado que você volte para uma nova conúlta com o seu médico responsável')

if ((dia_ultima_consulta - dia_atual) + ((mes_ultima_consulta - mes_atual) * 30) + ((ano_ultima_consulta - ano_atual) * 365)) * 2 < 90 * 2:

    print('parece que você ainda está dentro do prazo recomendado, continue com um bom acompanhamento')
