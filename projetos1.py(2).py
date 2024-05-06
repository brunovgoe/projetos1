# declaração de variáveis
lista_cadastro_usuarios = []
lista_intermediária = []

# definição de funções
def input_string(complemento):  # retorna uma string
    while True:
        string = str(input(f'\ndigite {complemento}: ')).strip()
        if string != '':
            break
        print('\nfrase inválida, tente novamente')
    return string

def input_classe_usuario():  # retorna um inteiro
    while True:
        classe_usuário = int(input('\ndigite o seu tipo de usuário\n\n[1] paciente\n[2] profissional de saúde\n\n'))
        if classe_usuário == 1 or classe_usuário == 2:
            break
        print('\nresposta inválida, tente novamente')
    return classe_usuário

def input_tipo_diabetes():  # retorna um inteiro
    while True:
        tipo = int(input("\nInsira seu tipo de diabetes: \n \n[1] diabetes tipo 1\n[2] diabetes tipo 2\n[3] diabetes gestacional\n[4] pré diabetes\n\n"))
        if tipo > 0 and tipo < 6:
            break
        print('\nresposta inválida, tente novamente')
    return tipo

def verificacao_nivel_glicose(glicose):
    if glicose <= 70:
        print("\nvocê está em estado de Hipoglicemia, procure ajuda assim que possível")
    elif 70 < glicose <= 150:
        print("\nGlicose dentro do intervalo ideal")
    elif 150 < glicose <= 300:
        print("\nGlicose acima do intervalo ideal, recomenda-se a adoção de uma medida preventiva assim que possível")
    else:
        print("\n você está em estado de Hiperglicemia, faça uso da dose adequada de insulina asim que possível")

def calculador_quant_insulina(glicose, qtd_carbo):  # retorna um valor numérico
    fator_correcao = 50
    glicemia_alvo = 100
    razao_carbo = 15
    unidades_insulina = (((glicose - glicemia_alvo) / fator_correcao) + (qtd_carbo / razao_carbo))
    return unidades_insulina

def formatacao_unidades_de_isulina(unidades_insulina):  # formata o valor retornado na função anterior
    import math
    insulina_inteiro = math.trunc(unidades_insulina)
    if (unidades_insulina - insulina_inteiro) == 0:
        insulina_print = unidades_insulina
    elif (unidades_insulina - insulina_inteiro) > 0 and (unidades_insulina - insulina_inteiro) < 0.5:
        insulina_print = math.floor(unidades_insulina)
    elif (unidades_insulina - insulina_inteiro) > 0.5:
        insulina_print = math.ceil(unidades_insulina)
    return insulina_print

def monitoramento_consulta():  # calcula o intervalo entre a última consulta e a "data atual", retornando um veedback via print
    data_ultima_consulta = str(input('\ndigite a data da sua última consulta médica (ex: 01/01/2001): ')).strip()
    dia_ultima_consulta = int(data_ultima_consulta[:2])
    mes_ultima_consulta = int(data_ultima_consulta[3:5])
    ano_ultima_consulta = int(data_ultima_consulta[6:10])
    data_atual = '02/05/2024'
    dia_atual = int(data_atual[:2])
    mes_atual = int(data_atual[3:5])
    ano_atual = int(data_atual[6:10])
    if ((dia_ultima_consulta - dia_atual)**2 + ((mes_ultima_consulta - mes_atual) * 30)**2 + ((ano_ultima_consulta - ano_atual) * 365)**2) > 180 ** 2:
        print('\nparece que faz muito tempo desde a sua última consulta, vá imadiatamente consular o seu médico')
    elif ((dia_ultima_consulta - dia_atual)**2 + ((mes_ultima_consulta - mes_atual) * 30)**2 + ((ano_ultima_consulta - ano_atual) * 365)**2) > 90 ** 2:
        print('\nparece que faz um tempo desde a sua última consulta, é recomendado que você volte para uma nova conúlta com o seu médico responsável')
    else:
        print('\nparece que você ainda está dentro do prazo recomendado, continue com um bom acompanhamento')

def calculadora_alimentos():  # mostra a quatidade de carboidratos em determinados alimentos
    print("1 - Arroz\n" "2 - Macarrao\n" "3 - Feijão\n" "4 - Uva\n" "5 - Batata Inglesa\n" "6 - Tapioca\n" "7 - Cuscuz\n" "8 - Macaxeira\n" "9 - Chocolate\n" "10 - Batata Frita\n" "11 - Pão de Forma\n" "12 - Batata Doce\n" "13 - Banana\n" "14 - Maçã\n" "15 - Pão Francês")
    escolha = int(input("qual alimento você deseja? "))
    match(escolha):
        case 1:
            qtd_arroz = float(input("informe a quantidade de arroz em gramas: "))
            total_arroz = qtd_arroz * 0.28
            print("a quantidade de carboidratos é: ", total_arroz)
        case 2:
            qtd_macarrao = float(input("informe a quantidade de macarrão em gramas: "))
            total_macarrao = qtd_macarrao * 0.31
            print("a quantidade de carboidratos é: ", total_macarrao)
        case 3:
            qtd_feijao = float(input("informe a quantidade de feijão em gramas: "))
            total_feijao = qtd_feijao * 0.14
            print("a quantidade de carboidratos é :", total_feijao)
        case 4:
            qtd_uva = float(input("informe a quantidade de uva em gramas: "))
            total_uva = qtd_uva * 0.14
            print("a quantidade de carboidratos é: ", total_uva)
        case 5:
            qtd_batata_inglesa = float(input("Informe a quantidade de batata inglesa em gramas : "))
            total_batata_inglesa = qtd_batata_inglesa * 0.19
            print("a quantidade de carboidratos é: ", total_batata_inglesa)
        case 6:
            qtd_tapioca = float(input("Informe a quantidade de goma de tapioca em gramas : "))
            total_tapioca = qtd_tapioca * 0.93
            print("a quantidade de carboidratos é:", total_tapioca)
        case 7:
            qtd_cuscuz = float(input("Informe a quantidade de farinha de milho (cuscuz) em gramas : "))
            total_cuscuz = qtd_cuscuz * 0.77
            print("a quantidade de carboidratos é:", total_cuscuz)
        case 8:
            qtd_macaxeira = float(input("Informe a quantidade de macaxeira em gramas : "))
            total_macaxeira = qtd_macaxeira * 0.30
            print("a quantidade de carboidratos é:", total_macaxeira)
        case 9:
            qtd_chocolate = float(input("Informe a quantidade de chocolate ao leite em gramas : "))
            total_chocolate = qtd_chocolate * 0.56
            print("a quantidade de carboidratos é: ", total_chocolate)
        case 10:
            qtd_batata_frita = float(input("Informe a quantidade de batata frita em gramas : "))
            total_batata_frita = qtd_batata_frita * 0.35
            print("a quantidade de carboidratos é:", total_batata_frita)
        case 11:
            qtd_pao_forma = float(input("Informe a quantidade de fatias de pão de forma : "))
            total_pao_forma = qtd_pao_forma * 25
            print("a quantidade de carboidratos é: ", total_pao_forma)
        case 12:
            qtd_batata_doce = float(input("informe a quantidade de batata doce em gramas: "))
            total_batata_doce = qtd_batata_doce * 0.19
            print("a quantidade de carboidratos é: ", total_batata_doce)
        case 13:
            qtd_banana = float(input("informe a quantidade de bananas "))
            total_bananas = qtd_banana * 26
            print("a quantide de carboidratos é: ", total_bananas)
        case 14:
            qtd_maca = float(input("informe a quantidade de maçãs : "))
            total_maca = qtd_maca * 15
            print("a quantidade de carboiddratos é: ", total_maca)
        case 15:
            qtd_pao_frances = float(input("informe a qunatidade de paes franceses : "))
            total_pao_frances = qtd_pao_frances * 28
            print("a quantidade de carboidratos é: ", total_pao_frances)

def menu_funcionalidades_paciente():  # retorna uma string
    while True:
        user_choise = str(input('\nselecione a funcionalidade que você deseja utilisar\n\n[1] calculadora de carboidratos\n[2] calculadora de alimentos\n[3] situação da glicemia\n[4] monitoramento consultas\n\n')).strip()
        if user_choise != '':
            break
    return user_choise

def verificacao_de_prossegimento(complemento_pergunta, complemento_negacao):  # retorna uma string
    while True:
        verificacao = str(input(f'\ndeseja continuar {complemento_pergunta}?\n\n[1] sim\n[2] não, {complemento_negacao}\n\n')).strip()
        if verificacao != '':
            break
        print('\nresposta inválida, tente novamente')
    return verificacao

def match_funcionalidades(user_choise):
    global lista_cadastro_usuarios
    match user_choise:
        case '1':
            glicose = float(input_string('sua glicemia'))
            qtd_carbo = float(input_string('sua quantidade de carboidratos ingeridos'))
            unidades_insulina = calculador_quant_insulina(glicose, qtd_carbo)
            insulina_print = formatacao_unidades_de_isulina(unidades_insulina)
            print(f'\nA quantidade de insulina a ser tomada é: {insulina_print}ml')
        case '2':
            calculadora_alimentos()
        case '3':
            glicemia = float(input_string('sua glicemia'))
            verificacao_nivel_glicose(glicemia)
        case '4':
            monitoramento_consulta()

def main():  # função principal de execução
    global lista_cadastro_usuarios
    global lista_intermediária
    while True:
        nome = input_string('seu nome')
        if nome != 'grupo6projetos1cesarschoolXD':  # palavra passe para acesso ao usuários cadastrados, deve ser inserida no momento de digitar o nome
            classe_usuario = input_classe_usuario()
            if classe_usuario != 2:  # se for diferente de profissional de saúde
                tipo = input_tipo_diabetes()
            lista_intermediária.append(nome)
            lista_intermediária.append(classe_usuario)
            if classe_usuario == 2:  # caso seja profissional de saúde
                lista_intermediária.append('-')
            else:  # caso seja paciente
                lista_intermediária.append(tipo)
            lista_cadastro_usuarios.append(lista_intermediária[:])  # incorporação da cópia da lista intermediária à lista de usuários cadastrados
            lista_intermediária.clear()  # limpeza da lista intermediária para a execução do laço
            if classe_usuario != 2:  # caso seja paciente
                while True:  # laço das funcionalidades
                    user_choise = menu_funcionalidades_paciente()
                    match_funcionalidades(user_choise)
                    continuidade_funcionalidades = verificacao_de_prossegimento('usando alguma outra funcionalidade', 'sair do menu de funcionalidades')
                    if continuidade_funcionalidades == '2':  # caso deseje sair do menu de funcionalidades
                        break
            else:  # caso seja profissional de saúde
                print('\nainda estamos desenvolvendo as funcionalidades referentes a esta classe de usuário, atualizações virão em breve ;)')
        else:  # caso a palavra passe seja inserida
            print(f'\n\n\nnome do usuário          classe de usuário          tipo de diabetes \n')
            for c in lista_cadastro_usuarios:  # laço para a impressão de cada usuário cadastrado
                print(f'{c[0]:<13}       {c[1]:>13}              ', end='')
                match c[2]:  # match para cada tipo de diabetes, com detalhamento se necessário
                    case 1:
                        print(f'{c[2]:>13}')
                    case 2:
                        print(f'{c[2]:>13}')
                    case 3:
                        print(f'{c[2]:>13} (gestacional)')
                    case 4:
                        print(f'{c[2]:>13} (pré-diabetes)')
                    case '-':  # caso seja profissional de saúde
                        print(f'{c[2]:>13}')
            print('\n\n')  # separação da tabela do resto do fluxo principal de execução
        verificacao = verificacao_de_prossegimento('a cadastrar algum outro usuário', 'encerrar programa')  # verificação de prosseguimento, ou não, do fluxo principal do programa
        if verificacao == '2':  # caso deseje encerrar o programa
            break
    print('\nobrigado por utilizar a nossa aplicação, volte quando quiser :)\n')  # mensagenzinha de encerramento

main()
