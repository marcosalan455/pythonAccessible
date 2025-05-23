
soma_idade = 0

idade_home_velho = 0
nome_homem_velho = ''

mulher_menor20 = 0

for pessoa in range(1, 5):
    nome = str(input(f"Digite o nome da {pessoa}ª pessoa: "))

    while True:
        try:
            idade = int(input("Digite a idade: "))
        except(ValueError, TypeError):
            print("ERRO: Por favor digite uma idade válida.")
            continue
        else:
            break

    sexo = str(input("Digite o sexo [Mf]: ")).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input("Digite o sexo [Mf]: ")).strip().upper()[0]



    soma_idade = idade

    if pessoa == 1 and sexo in 'Mm':
        idade_home_velho = idade
        nome_homem_velho = nome

    if sexo in 'Mm' and idade > idade_home_velho:
        idade_home_velho = idade
        nome_homem_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulher_menor20 += 1

media_idade = soma_idade / 4
print(f"A média de idade do grupo é {media_idade} anos.")
print(f"O nome do homem mais velho é {nome_homem_velho} e sua idade é {idade_home_velho} anos.")
print(f"Temos um total de {mulher_menor20} mulheres menores de 20 anos.")

