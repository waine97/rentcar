import os

carros = [('Chevrolet Tracker', 120),
          ('Chevrolet Onix', 90),
          ('Chevrolet Spin', 150),
          ('Hyundai HB20', 85),
          ('Hyundai Tucson', 120),
          ('Fiat Uno', 60),
          ('Fiat Mobi', 70),
          ('Fiat Pulse', 130)]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia".format(i, car[0], car[1]))

mostrar_lista_de_carros(carros)

while True:
    os.system("cls")
    print("======")
    print("Bem vindo a locadora de carro")
    print("======")
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")

    op = int(input())

    os.system("cls")

    if op == 0:
        mostrar_lista_de_carros(carros)
    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("======")
        print("Escolha o código do carro:")
        cod_car = int(input())
        print("Por quantos dias você deseja aludar este carro?")
        dias = int(input())
        os.system("cls")

        print("Você escolher {} por {} dias.".format(carros[cod_car][0], dias))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * carros[cod_car][1]))
        print("0 - Confirma| 1 - Não")
        conf = int(input())
        if conf == 0:
            os.system("cls")
            print("Parabéns você alugou o {} por {}".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))
    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros para devolver.")
        else:
            print("Segue a lista de carros alugados. Qual deseja devolver?")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o carro {}".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))

    
    print("")
    print("======")
    print("0 - Continuar| 1 - SAIR")

    if int(input()) == 1:
        break

