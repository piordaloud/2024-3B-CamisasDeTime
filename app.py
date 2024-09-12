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
    opcao_escolhida = int(input('Escolha uma opcao: '))
    print('Você escolheu a opção: ', opcao_escolhida)

    def finalizar_programa():
        os.system('cls')
        print('finalizando programa')


    if opcao_escolhida == 1:
        print('Cadastrar camisa')
    elif opcao_escolhida == 2:
        print('Listar camisas')
    elif opcao_escolhida == 3:
        print('Ativar/desativar camisa')
    else:
        finalizar_programa()

def main():
    mostra_título()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()