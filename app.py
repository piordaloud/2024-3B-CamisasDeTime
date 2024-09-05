print("""
      
Camisa de time tailandesa
      
""")

print('1. Cadastro de camisas')
print('2. Listar camisas')
print('3. Ativar camisas')
print('4. Sair da aplicação')

opcao_escolhida = int(input('Escolha uma opcao: '))
print('Você escolheu a opção: ', opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar camisa')
elif opcao_escolhida == 2:
    print('Listar camisas')
elif opcao_escolhida == 3:
    print('Ativar/desativar camisa')
else:
    print('Saindo da aplicação')