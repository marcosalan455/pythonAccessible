
while True:
    menu = ('''
    [1] = Cadastro pessoal,
    [2] - Lista de compras,
    [3] - sair do sistema
    ''')
    print(menu)
    opc = int(input("Escolha uma opção do menu: "))

    if opc == 1:
        print("Bem vindos ao sistema de cadastro de pessoas")
        for pessoas in range(1, 3):
            nome = str(input(f"Digite o nome da {pessoas}ª pessoa: "))

            while True:
                try:
                    idade = int(input("Digite a idade: "))
                except(ValueError, TypeError):
                    print("ERRO: Por favor digite um valor de idade válido.")
                    continue
                else:
                    break

            sexo = str(input("Digite o sexo [m/f]: ")).strip().upper()[0]
            while sexo not in 'MmFf':
                print("ERRO: Por favor digite um sexo válido.")
                sexo = str(input("Digite o sexo [m/f]: ")).strip().upper()[0]

            cadastro = open('cadastroPessoal.txt', 'at+', encoding='UTF-8')
            cadastro.write(f"Nome {nome} idade {idade} do sexo {sexo}\n")
            cadastro.close()

    elif opc == 2:
        print("Digite seus itens de compra")
        itens = str(input("Digite seus itens para compras: "))

        mercado = open('listaDeCompras.txt', 'at+', encoding='UTF-8')
        mercado.writelines(f"lista de compras\n{itens}")
        mercado.close()


    elif opc == 3:
        print("Obrigado por usar nosso sistema! Até logo!")
        break


    else:
        print("ERRO: Por favor escolha uma opção válida do menu.")


