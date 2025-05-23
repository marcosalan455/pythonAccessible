
print('''
[1] - cadastrar pessoas.
[2] - lista de mercado.
''')

opc = int(input("Escolha uma opção: "))

if opc == 1:

    arquivo1 = open('cadastroDePessoas.txt', 'w+', encoding='UTF-8')

    print('-'*42)
    print("Bem vindo ao sistema de cadastro.".center(42))
    print('-'*42)

    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))

    arquivo1.write(f"Meu nome é {nome}\nMinha idade é {idade} anos.")
    arquivo1.close()

elif opc == 2:

    arquivo2 = open('listaMercado.txt', 'w+', encoding='UTF-8')

    print('-'*42)
    print("Lista de mercado.".center(42))
    print('-'*42)

    lista = str(input("Digite os itens que deseja comprar: "))

    arquivo2.write(f"Lista de compra\n{lista}\n")
    arquivo2.close()

else:
    print("\33[0;36;42mPor favor escolha uma opção válida.\33[m")
