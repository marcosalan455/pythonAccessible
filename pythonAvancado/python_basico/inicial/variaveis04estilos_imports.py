from time import sleep

print("-"*42)
print("\033[1;33;41mBem vindos ao sistema de cadastro.\033[m".center(55))
print("-"*42)

nome = str(input("Digite seu nome: ").upper())
idade = int(input("Digite sua idade: "))
print("-"*60)
print("Informe seu endereço conforme os campos abaixo.")
print("-"*60)
rua = str(input("Digite o nome da sua Rua: "))
numero = int(input("Digite o número: "))
complemento = str(input("COMPLEMENTO: (casa) ou (ap/número): "))

print('-'*50)
print(f"Meu nome é {nome}\nMinha idade é {idade} anos\nMeu endereço completo é {rua, numero, complemento}")
print('-'*50)

sleep(10)
