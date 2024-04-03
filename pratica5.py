class FormaDePagamento():
      def processarPagamento(self):
          print("Pagamento feito!")
        
class Cartão_de_credito(FormaDePagamento):
      def processarPagamento(self):
          print("Pagamento feito com cartão de credito")
          super().processarPagamento()
          
          
class PayPal(FormaDePagamento):
      
      def processarPagamento(self):
          print("Processando pagamento com PayPal...")
          super().processarPagamento()
def main():
    cartão = Cartão_de_credito()
    paypal = PayPal()
          
    print("Para terminar sua compra selecione uma forma de pagamento.\n 1) Cartão de crédito\n 2) PayPal")
    resposta = str(input("Metodo: (1/2)\n"))

    if resposta == "1":
       forma_pagamento = cartão  
    elif resposta == "2":
         forma_pagamento = paypal
    else:
         print("Nunhum metodo selecionado.")
        
    forma_pagamento.processarPagamento() 
main()

