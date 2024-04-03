import random


class Carro:
    vencedor = ""

    def __init__(self, nome, velocidade):
        self.nome = nome
        self.velocidade = velocidade

    def correr(self):
        tempo = random.randint(1, 10) * (10 / self.velocidade)
        return tempo


def corrida():
    carros = [
        Carro("Mc Laren", 200),
        Carro("Ferari GTR", 180),
        Carro("Mercedes AMZ", 220),
    ]
    while True:
        print("Escolha um carro:")
        for i, carros in enumerate(carros):
            print(f"{i + 1}).{carros.nome} - Velocidade: {carros.velocidade} km/h")

        escolha = input("Qual carro deseja competir: A - B - C ou 's' para sair")
        escolha = escolha.upper()
        if escolha == "S":
            break
        elif escolha in ["A", "B", "C"]:
            indice_carro = ord(escolha) - ord("A")
            carro_escolhido = carros[indice_carro]
            tempo_corrida = carro_escolhido.correr()

            print(
                f"O carro vencedor foi {carro_escolhido.nome} com o tempo de corrida de {tempo_corrida:.2f} segungos\n"
            )
        else:
            print("Escolha invalida.")

        if Carro.vencedor:
            print(f"O vencedor é {Carro.vencedor}")
        else:
            print("Nnenhuma corrida")


corrida()
