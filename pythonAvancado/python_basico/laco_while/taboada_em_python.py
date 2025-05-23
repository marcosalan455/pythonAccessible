
while True:
    resposta = ''
    try:
        n = int(input("Qual o número que deseja ver a taboada: "))
    except(ValueError, TypeError):
        print("ERRO: Por favor digite um número inteiro válido.")
        continue
    else:
        print('-' * 30)
        for c in range(1, 11):
            print(f"{n} x {c} = {n*c}")
        print('-' * 30)

        resposta = str(input("Quer continuar? [S/N]: "))
        if resposta == 'n':
            print("Programa encerrado.")
            break

