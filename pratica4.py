class Veiculo():
  def __init__(self, marca, ano):
      self._marca = marca
      self._ano = ano
      
  def exibir_infos(self):
      print(f"Marca: {self._marca}\n Ano:{self._ano}")


class Carro(Veiculo):
      def __init__(self, marca, ano, numero_de_portas):
          super().__init__(marca, ano)
          self._numero_de_portas = numero_de_portas 
               
      def infos_carro(self):
         super().exibir_infos()
         print(f"Numero de portas: {self._numero_de_portas}")

class Moto(Veiculo):
    def __init__(self, marca, ano, tipo_de_moto):
        super().__init__(marca, ano)
        self._tipo_de_moto = tipo_de_moto  

    def infos_moto(self):
        super().exibir_infos()
        print(f"Tipo de moto: {self._tipo_de_moto}")


def main():
    while True:
        print("Qual é seu veiculo ?\n Carro ou Moto?")
        resposta = str(input(": "))
        resposta = resposta.lower()
        if resposta != resposta:
            print("Parar programa.")
            break

        if resposta == "carro":
            marca_caro = str(input("Marca:"));
            ano_carro = int(input("Ano: "))
            num_de_portas = int(input("Numero de porta: "))
            carro = Carro(marca_caro, ano_carro, num_de_portas)
            carro.exibir_infos()
            continuar = str(input("Deseja continuar (sim/não)"))
            continuar = continuar.lower()
            if continuar == "sim":
              return main()
            else:
              print("Muito obrigado!")
              break 
        elif resposta == "moto":
            marca_moto = str(input("Marca:"))
            ano_moto = int(input("Ano: "))
            tipo_moto = str(input("Tipo de moto: "))
            moto = Moto(marca_moto, ano_moto, tipo_moto)
            moto.exibir_infos()
            continuar = str(input("Deseja continuar (sim/não)"))
            continuar = continuar.lower()
            if continuar == "sim":
              return main()
            else:
              print("Muito obrigado!")
              break 
        else:
            print("Resposta invalida.")
            return

main()