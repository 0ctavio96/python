class ContaBancaria:
    def __init__(self, num_conta, nome_titular, saldo_inicial=0.0):
        self.__num_conta = num_conta
        self.__nome_titular = nome_titular
        self.__saldo_inicial = saldo_inicial

    def levantar(self, valor):
        if 0 < valor <= self.__saldo_inicial:
            self.__saldo_inicial -= valor
            print(f"Levantamento de {valor} realizado com sucesso")
        else:
            print("Valor indisponivel.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo_inicial += valor
            print(f"Deposito no valor de {valor} feito com sucesso.")
        else:
            print("valor incorreto")

    def verificar_saldo(self):
        print(" Seu saldo é ", self.__saldo_inicial)

    def set_num_conta(self, num_conta):
        self.__num_conta = num_conta

    def set_nome_titular(self, nome_titular):
        self.__nome_titular = nome_titular

    def set_saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial


def main():

    # Nome do titular
    print("Qual é seu nome?")
    nome = str(input(" "))
    # Numero da conta
    print("Qual o numero da sua conta?")
    numero = int(input(" "))
    # Saldo
    print("Qual o valor que você tem?")
    saldo = float(input(" "))
    contabancaria = ContaBancaria(numero, nome, saldo)
    print( f"Seja bem vindo(a) {nome}, da conta {numero}, neste momento o seu saldo é de {saldo}€ \n")
    
    while True:
    
        print("Qual operacão deseja fazer:\n1)levantaento\n2)Deposito\n3)Verificar slado\n Caso queira SAIR aperte 's'")
        escolha = input(" ")
        if escolha == "1":
            print("Qual o valor do levantamento: ")
            valor = float(input(" "))
            contabancaria.levantar(valor)
        elif escolha == "2":
            print("Quantos deseja depositar:")
            valor = float(input(" "))
            contabancaria.depositar(valor)
        elif escolha == "3":
            contabancaria.verificar_saldo()
        elif escolha.lower() == "s":
            break
        else:
            print("Opção errada")
        return

main()
