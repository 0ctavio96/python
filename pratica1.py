class Aluno:
  def __init__(self, nome,idade,curso,numero_matricula):
    self.nome = nome
    self.idade = idade
    self.curso = curso
    self.numero_matricula = numero_matricula
  
  def info_aluno(self):
     print(f"Nome:{self.nome}")
     print(f"Idade:{self.idade}")
     print(f"Curso:{self.curso}")
     print(f"Numero da matricula:{self.numero_matricula}")

def sistema():
  alunos = [] 

  while True:
   print ("Informe as informações do aluno.")
   nome = str(input("Nome:"))
   idade = int(input("Idade:"))
   curso = str(input("Curso:"))
   numero_matricula = str(input("Numero da matricula:"))
   print()
  
   aluno = Aluno(nome,idade,curso,numero_matricula)
   alunos.append(aluno)
   
   continuar = input("Deseja adicionar outro aluno: (sim/não)\n")
   if continuar.lower() != "sim":
      break
  
  print("Informações dos alunos registrados:\n") 
  for aluno in alunos:
    aluno.info_aluno()
    
sistema()