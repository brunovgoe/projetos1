#input do nome do usuário

nome = input("Insira seu nome: ")

#verificação e validação do tipo de diabetes

while True:
    tipo = int(input(" \nInsira seu tipo de diabetes: \n \n[1]diabetes tipo 1\n[2]diabetes tipo 2\n[3]diabetes gestacional\n[4]pré diabetes\n[5]proficional de saúde\n \n"))
    if tipo > 0 and tipo < 5:
        break
    print('\nresposta inválida, tente novamente') 

#input da glicemia

glicose = float(input(" \nInsira sua glicemia: "))

#verificação do nível glicêmico

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

#calculadora de carbos

qtd_carbo = float(input("Informe a quantidade de carboidratos: "))

fator_correcao = 50
glicemia_alvo = 100
razao_carbo = 15

unidades_insulina = (((glicose - glicemia_alvo) / fator_correcao) + (qtd_carbo / razao_carbo))

#arredondamento da quantidade de insulina

import math
insulina_inteiro = math.trunc(unidades_insulina)
if (unidades_insulina - insulina_inteiro) == 0:
    insulina_print = unidades_insulina

if (unidades_insulina - insulina_inteiro) > 0 and (unidades_insulina - insulina_inteiro) < 0.5:
    insulina_print = math.floor(unidades_insulina)

if (unidades_insulina - insulina_inteiro) > 0.5:
    insulina_print = math.ceil(unidades_insulina)

#retorno unidades de insulina formatada

print(f"A quantidade de insulina a ser tomada é: {insulina_print}")

#diario

diario = str(input("escreva aqui seu acompanhamento diario: "))
print(diario)




