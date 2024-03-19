#taxas

nome = input("Insira seu nome: ")
tipo = int(input("Insira seu tipo de diabetes: "))
glicose = float(input("Insira sua glicemia: "))

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

print(f"A quantidade de insulina a ser tomada é: {unidades_insulina:.2f}")

#diario

diario = str(input("escreva aqui seu acompanhamento diario: "))
print(diario)


