import os

def mostra_título():
    print("""
        
    Camisa de time tailandesa
        
    """)

def mostra_escolhas():
    print('1. Cadastro de camisas')
    print('2. Listar camisas')
    print('3. Ativar camisas')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            print('Cadastrar camisa')
        elif opcao_escolhida == 2:
            print('Listar camisas')
        elif opcao_escolhida == 3:
            print('Ativar/desativar camisa')
        elif opcao_escolhida == 4:
            finalizar_programa
        else:
           opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_camisas():
    os.system('cls')
    print(' Cadastrando Camisa... ')
    nome_camisa = input('Digite o nome da camisa')
    camisas.append(nome_camisa)
    print(f'O {nome_camisa} foi adicionado (a) as camisas de time')
    input('Digite qualquer tecla para voltar')
    main()

def mostrar_camisas():
    os.system('cls')
    print('Lista de camisas')

    for camisa

def finalizar_programa():
    os.system('cls')
    print('finalizando programa')

def opcao_invalida():
    print('Esse caracter não é permitido')
    input('digite qualquer tecla')
    main()


def main():
    mostra_título()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()