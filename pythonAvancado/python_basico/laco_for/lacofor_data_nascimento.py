from datetime import date

data_atual = date.today().year

total_menores = 0
total_maiores = 0

for pessoas in range(1, 5):
    data_nascimento = int(input(f"Digite a data de nascimento da {pessoas}ª pessoa: "))
    idade = data_atual - data_nascimento

    if idade <= 21:
        total_menores += 1
        print(f"No ano de {data_atual} você tem {idade} anos")
    else:
        total_maiores += 1
        print(f"No ano de {data_atual}, você tem {idade} anos")


print('-'*42)
print(f"Temos um total de {total_menores} pessoas menores de idade.")
print(f"Temos um total de {total_maiores} pessoas com maior idade.")