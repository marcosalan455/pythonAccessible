

arquivo = open('documento.txt', 'w+', encoding='UTF-8')


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
arquivo.write(f"Meu nome é {nome}\nminha idade é {idade} anos, você é menor de idade")


arquivo.close()