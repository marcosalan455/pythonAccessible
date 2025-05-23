

try:
    idade = int(input("Digite sua idade: "))
except (TypeError, ValueError):
    print("ERRO: Por favor digite um número inteiro válido.\nPrograma encerrado.")
else:
    if idade < 18:
        print("menor de idade.")
    elif idade <21:
        print("Você ainda não é maior de idade ")
    elif idade < 65:
        print("Você é maior de idade.")
    elif idade < 100:
        print("Você está na melhor idade.")
    else:
        print("Erro não esperado, digite um valor entre (1 e 100)")

