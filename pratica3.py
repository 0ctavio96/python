class Animal:
    def __init__(self, nome):
        self._nome = nome

    def emitir_som(self):
        print("O animal emite um som.")


class Gato(Animal):
    def Miar(self):
        print(f"O {self._nome} está miando")
        
class Cão(Animal):
    def Latir(self):
        print(f"O {self._nome} está latindo")

def main():        
    print("Qual o nome do seu animal")
    nome = str(input("nome = "))
    Animal(nome)
    
    print("Qual é seu animal, GATO ou CÃO ?")
    g_or_c = str(input("?"))
    g_or_c = g_or_c.lower()

    if g_or_c == "gato":
       gato = Gato(nome)
       gato.Miar()
       gato.emitir_som()
    elif g_or_c == "cão" or "cao":
      cao = Cão(nome)
      cao.Latir()
      cao.emitir_som()
    else:
      print("nenhum animal.")

main()
   
