
# declaração de variáveis

lista_cadastro_usuarios = []
lista_intermediária = []

#definição de funções

def input_string(complemento): # retorna uma string

    while True:

        string = str(input(f'\ndigite {complemento}: ')).strip()

        if string != '':
        
            break

        print('\nfrase inválida, tente novamente')

    return string

def input_classe_usuario(): # retorna um inteiro

    while True:
        
        classe_usuário = int(input('\ndigite o seu tipo de usuário\n\n[1] paciente\n[2] profissional de saúde\n\n'))

        if classe_usuário == 1 or classe_usuário == 2:
            break

        print('\nresposta inválida, tente novamente')
    
    return classe_usuário

def input_tipo_diabetes(): # retorna um inteiro

    while True: 

        tipo = int(input("\nInsira seu tipo de diabetes: \n \n[1] diabetes tipo 1\n[2] diabetes tipo 2\n[3] diabetes gestacional\n[4] pré diabetes\n\n"))

        if tipo > 0 and tipo < 6:
            break

        print('\nresposta inválida, tente novamente')

    return tipo

def verificacao_nivel_glicose(glicose):

    if glicose <= 70:{
        print("\nvocê está em estado de Hipoglicemia, procure ajuda assim que possível")
    }
    elif 70 < glicose <= 150:{
        print("\nGlicose dentro do intervalo ideal")
    }
    elif 150 < glicose <= 300:{
        print("\nGlicose acima do intervalo ideal, recomenda-se a adoção de uma medida preventiva assim que possível")
    }
    else:{
        print("\n você está em estado de Hiperglicemia, faça uso da dose adequada de insulina asim que possível")
    }
     
def calculador_quant_insulina(glicose, qtd_carbo): # retorna um valor numérico

    fator_correcao = 50
    glicemia_alvo = 100
    razao_carbo = 15

    unidades_insulina = (((glicose - glicemia_alvo) / fator_correcao) + (qtd_carbo / razao_carbo))

    return unidades_insulina

def formatacao_unidades_de_isulina(unidades_insulina): # formata o valor retornado na função anteriror

    import math

    insulina_inteiro = math.trunc(unidades_insulina)

    if (unidades_insulina - insulina_inteiro) == 0:
        insulina_print = unidades_insulina

    elif (unidades_insulina - insulina_inteiro) > 0 and (unidades_insulina - insulina_inteiro) < 0.5:
        insulina_print = math.floor(unidades_insulina)

    elif (unidades_insulina - insulina_inteiro) > 0.5:
        insulina_print = math.ceil(unidades_insulina)

    return insulina_print

def monitoramento_consulta(): # calcula o intervalo entre a última consulta e a "data atual", retornando um veedback via print

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


def menu_funcionalidades_paciente(): # retorna uma string

    while True:

        user_choise = str(input('\nselecione a funcionalidade que você deseja utilisar\n\n[1] calculadora de carboidratos\n[2] calculadora de alimentos\n[3] situação da glicemia\n[4] monitoramento consultas\n\n')).strip()

        if user_choise != '':

            break

    return user_choise

def verificacao_de_prossegimento(complemento_pergunta, complemento_negacao): # retorna uma string

    while True:

        verificacao = str(input(f'\ndeseja continuar {complemento_pergunta}?\n\n[1] sim\n[2] não, {complemento_negacao}\n\n')).strip()

        if verificacao != '':

            break

        print('\nresposta inválida, tente novamente')

    return verificacao

def match_funcionalidades(user_choise): 
    
    # faz o match de execução das funcionalidades baseado na seleção realizada na função "menu_funcionalidades_paciente"

    global lista_cadastro_usuarios

    match user_choise:

        case '1':

            glicose = float(input_string('sua glicemia'))
            qtd_carbo = float(input_string('sua quantidade de carboidratos ingeridos'))

            unidades_insulina = calculador_quant_insulina(glicose, qtd_carbo)

            insulina_print = formatacao_unidades_de_isulina(unidades_insulina)

            print(f'\nA quantidade de insulina a ser tomada é: {insulina_print}ml')

        case '3':

            glicemia = float(input_string('sua glicemia'))

            verificacao_nivel_glicose(glicemia)

        case '4':

            monitoramento_consulta()
      
def main(): # função principal de execução

    # importação de variavei de escopo global para dentro da função

    global lista_cadastro_usuarios
    global lista_intermediária

    # laço principal do programa

    while True:

        nome = input_string('seu nome')

        if nome != 'grupo6projetos1cesarschoolXD': # palavra passe para acesso ao usuários cadastrados, deve ser inserida no momento de digitar o nome

            classe_usuario = input_classe_usuario()

            if classe_usuario != 2: # se for diferente de proficional de saúde

                tipo = input_tipo_diabetes()

            # input das informações dos usuários em uma lista intermediária

            lista_intermediária.append(nome)
            lista_intermediária.append(classe_usuario)

            if classe_usuario == 2: # caso seja proficional de saúde

                lista_intermediária.append('-')

            else: # caso seja paciente

                lista_intermediária.append(tipo)

            lista_cadastro_usuarios.append(lista_intermediária[:]) # incorporação da cópia da lista intermediária à lista de usuários cadastrados

            lista_intermediária.clear() # limpeza da lista intermadiária para a execução do laço


            if classe_usuario != 2: # caso seja paciente

                while True: # laço das funcionalidades

                    user_choise = menu_funcionalidades_paciente()

                    match_funcionalidades(user_choise)

                    continuidade_funcionalidades = verificacao_de_prossegimento('usando alguma outra funcionalidade', 'sair do menu de funcionalidades')

                    if continuidade_funcionalidades == '2': # caso deseje sair do menu de funcionalidades

                        break

            else: # caso seja proficional de saúde

                print('\nainda estamos desenvolvendo as funcionalidades referentes a esta classe de usuário, atuaizações virão em breve ;)')

        else: # caso a palavra passe seja inserida

            # print da tabela de usuários

            print(f'\n\n\nnome do usuário          classe de usuário          tipo de diabetes \n')

            for c in lista_cadastro_usuarios: # laço para a impressão de cada usuário cadastrado

                print(f'{c[0]:<13}       {c[1]:>13}              ', end='')

                match c[2]: # match para cada tipo de diabetes, com detalhamento se necessário

                    case 1:

                        print(f'{c[2]:>13}')

                    case 2:

                        print(f'{c[2]:>13}')

                    case 3:

                        print(f'{c[2]:>13} (gestacional)')

                    case 4:

                        print(f'{c[2]:>13} (pré-diabetes)')

                    case '-': # caso seja proficional de saúde

                        print(f'{c[2]:>13}')

            print('\n\n') # separação da tabela do resto do fluxo principal de execução                      

        verificacao = verificacao_de_prossegimento('a cadastrar algum outro usuário', 'encerrar programa') # verificação de proceguimento, ou não, do fluxo principal do programa 

        if verificacao == '2': # caso deseje encerrar o programa

            break

    print('\nobrigado por utilisar a nossa aplicação, volte quando quiser :)\n') # mensagenzinha de encerramento

main()
