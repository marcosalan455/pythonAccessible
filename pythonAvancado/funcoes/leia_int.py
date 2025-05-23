
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print("ERRO: por favor digite um número inteiro válido.")
            continue
            return 0
        else:
            return n
            break

#numero = leiaInt("Digite um número: ")
#print(f"Você digitou {numero}")

