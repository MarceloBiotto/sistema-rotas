print('Programa de app de logistica feito por Adão Biotto')

def dimensoesObjeto():       #função para calcular as dimensões do objeto
    try:
        altura = float(input("Digite a altura do objeto (em cm): "))
        comprimento = float(input("Digite o comprimento do objeto (em cm): "))
        largura = float(input("Digite a largura do objeto (em cm): "))

        volume = altura * comprimento * largura    #fazemos a conta para pegar o volume
        print("As dimensões para o objeto são de", volume, "cm³")

        return volume

    except ValueError:   #erro para caso usuario digite um valor não válido
        print("Erro: Você digitou um valor não numérico.")

volume = dimensoesObjeto() #salvamos dentro da variavel volume

valorDimensoes = 0

if volume < 1000:    # a partir daqui fazemos as verificações de em qual enquadramento o volume se enquadra
    valorDimensoes = 10.00
    print("Valor cobrado R$10.00")
elif 1000 <= volume < 10000:
    valorDimensoes = 20.00
    print("Valor cobrado R$20.00")
elif 10000 <= volume < 30000:
    valorDimensoes = 30.00
    print("Valor cobrado R$30.00")
elif 30000 <= volume < 100000:
    valorDimensoes = 50.00
    print("Valor cobrado R$50.00")
else:
    print("Volume além do permitido...")

def pesoObjeto():    #iniciamos o peso do objeto
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if peso <= 0.1:
                return 1
            elif peso < 1:
                return 1.5   # a baixo de cada faixa de peso botamos também o multiplicador correspodente
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
            else:
                print("Peso não aceito. O peso máximo permitido é 30 kg.")
        except ValueError:
            print("Valor inválido. Por favor, digite um valor numérico.")

multiplicaPeso = pesoObjeto()
print("O multiplicador é:", multiplicaPeso)

def rotaObjeto():   # aqui pegamos as rotas possiveis em nosso transporte
    rotas = {
        "RS": 1,
        "SR": 1,
        "BS": 1.2,
        "SB": 1.2,
        "BR": 1.5,
        "RB": 1.5
    }
    print("Rotas possíveis:")
    print("**RS** Do Rio de Janeiro até São Paulo")
    print("**SR** De São Paulo até Rio de Janeiro")
    print("**BS** De Brasília até São Paulo")
    print("**SB** De São Paulo até Brasília")
    print("**BR** De Brasília até Rio de Janeiro")
    print("**RB** De Rio de Janeiro até Brasília")

    rota = input("Digite a rota desejada: ")

    if rota in rotas:
        multiplicaRota = rotas[rota]
        print(f"O multiplicador para a rota {rota} é {multiplicaRota}.")
        return multiplicaRota
    else:
        print("Rota inválida. Por favor, tente novamente.")

valorRota = rotaObjeto()
valorTotal = float(valorDimensoes * multiplicaPeso * valorRota)   #juntamos tudo em uma conta final para passar o total ao usuario

print("Valor total:", valorTotal)