
nome = str(input("Digite seu nome: "))
leia_int = "Digite sua idade: "
ok = False
idade = 0

while True:
    n = str(input(leia_int))
    if n.isnumeric():
        idade = int(n)
        ok = True
    else:
        print("ERRO: Por favor digite um número inteiro válido.")
    if ok:
        break

#print(f"Sua idade é {idade} anos.") print somente com a idade

print(f"Bem vindo {nome}\nSua idade é {idade} anos.")