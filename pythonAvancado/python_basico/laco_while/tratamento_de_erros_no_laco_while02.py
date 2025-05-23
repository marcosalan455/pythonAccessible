
numero = 0
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
    except (ValueError, TypeError):
        print("ERRO: Por favor digite um número inteiro válido.")
        continue
        print(0)
    else:
        print(f"O número digitado foi  {numero}")
        break

