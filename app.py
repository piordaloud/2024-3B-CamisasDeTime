import os

camisas = [
    {'nome': 'Neymar', 'categoria': 'Tailandesa', 'ativo': True},
    {'nome': 'L. MESSI', 'categoria': 'Tailandesa', 'ativo': True},
    {'nome': 'C. RONALDO', 'categoria': 'Tailandesa', 'ativo': True},
    {'nome': 'PIRLO', 'categoria': 'Tailandesa', 'ativo': True}
]

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\nPressione uma tecla para voltar ao menu principal...')
    main()

def mostra_titulo():
    print('''

    Camisas de time

    ''')

def mostra_escolhas():
    print('1. Cadastro de camisas')
    print('2. Listar camisas')
    print('3. Ativar/desativar camisas')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_camisas()
        elif opcao_escolhida == 2:
            mostrar_camisas()
        elif opcao_escolhida == 3:
            ativar_desativar_camisas()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def cadastrar_camisas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Cadastrando Camisa...')
    nome_camisa = input('Digite o nome da camisa: ')
    categoria_camisa = input('Digite a categoria da camisa: ')
    
    nova_camisa = {'nome': nome_camisa, 'categoria': categoria_camisa, 'ativo': True}
    camisas.append(nova_camisa)
    
    print(f'A camisa {nome_camisa} foi adicionada às camisas de time.')
    input('Pressione qualquer tecla para voltar...')
    main()

def mostrar_camisas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Lista de camisas:')
    for camisa in camisas:
        status = 'Ativa' if camisa['ativo'] else 'Inativa'
        print(f"{camisa['nome']} - Categoria: {camisa['categoria']} - Status: {status}")
    input('Pressione qualquer tecla para voltar...')
    main()

def ativar_desativar_camisas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Ativar/Desativar Camisas:')
    for i, camisa in enumerate(camisas):
        status = 'Ativa' if camisa['ativo'] else 'Inativa'
        print(f"{i + 1}. {camisa['nome']} - Status: {status}")
    
    try:
        opcao = int(input('Escolha o número da camisa para ativar/desativar: '))
        if 1 <= opcao <= len(camisas):
            camisas[opcao - 1]['ativo'] = not camisas[opcao - 1]['ativo']
            print(f"A camisa {camisas[opcao - 1]['nome']} foi {'desativada' if not camisas[opcao - 1]['ativo'] else 'ativada'}.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
    
    input('Pressione qualquer tecla para voltar...')
    main()

def finalizar_programa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando o programa...')
    exit()

def opcao_invalida():
    print('Essa opção não é válida.')
    input('Pressione qualquer tecla para tentar novamente...')
    main()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()
