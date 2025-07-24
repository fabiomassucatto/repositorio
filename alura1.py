import os
restaurantes =[ {'nome':'praça','categoria':'japonesa','ativo':False},
                 {'nome':'Pizza suprema','categoria':'pizza','ativo':True},
                 {'nome':'cantina','categoria':'italiano','ativo':False}]


def exibir_nome_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

def exibir_opcoes():
    print('1. cadastrar restaurante ')
    print('2. listar restaurante ')
    print('3. alterar estado do restaurante ')
    print('4. Sair\n ')
    
def finalizar_app():
    exibir_sub_titulos('finalizando app.')
    
def voltar_ao_menu():
    input("\ndigite uma tecla para voltar ao menu")
    main()

def opcao_invalida():    
    print("opção invalida!\n")
    voltar_ao_menu()

def exibir_sub_titulos(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


    
def cadastrar_novo_restaurante():
    exibir_sub_titulos('cadastro de novos restaurantes')
    nome_do_restaurante=input("diga o nome dos restaurantes deseja cadastrar ")
    categoria=input(f'digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante= {'nome': nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"o restaurante {nome_do_restaurante} foi cadastrado com sucesso\n")
    voltar_ao_menu()
    
def listar_restaurantes():
    exibir_sub_titulos('listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} |{' Categoria'.ljust(22)}|{' Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante ='ativado' if  restaurante['ativo'] else 'desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}")
    
    voltar_ao_menu()

def alterar_restaurante():
    exibir_sub_titulos("alterando o estado do restaurante..")
    nome_restaurante = input('digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado=False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f"o restaurante {nome_restaurante} foi ativado com sucesso" if restaurante ['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('restaurante n encontrado')
    voltar_ao_menu()

    
def escolher_opcao():
    try:    
        escolha_escolhida=int(input("escolha uma opção: "))

        if escolha_escolhida ==1:
            cadastrar_novo_restaurante()
            
            
        elif escolha_escolhida ==2:
            listar_restaurantes()
            
            
        elif escolha_escolhida ==3:
            alterar_restaurante()
            
        elif escolha_escolhida ==4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    
        
        
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__ == "__main__":
    main()