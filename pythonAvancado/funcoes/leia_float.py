

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(TypeError, ValueError):
            print("ERRO: por favor digite um número válido.")
            continue
            return 0
        else:
            return n


#num = leiaFloat("Digite um valor: ")
#print(f"você digitou {num}")

