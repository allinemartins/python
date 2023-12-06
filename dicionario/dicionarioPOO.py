"""
Crie uma funcao que receba os valores do nome, idade e e-mail de uma pessoa e 
guarde-os em um dicionario com as chaves nome, idade e email, respectivamente. 
Sua funcao deve retornar esse dicionario.
"""

dicionario = []

class Dicionario:
  def __init__(self, nome, idade, email) :
    self.nome = nome
    self.idade = idade
    self.email = email
    
  def to_armazena(self):
      objeto = {'Nome: ': self.nome, 'Idade: ': self.idade, 'Email: ': self.email}
      dicionario.append(objeto)
        
for i in range(3):
    nome  = input('Informe o nome \n')
    idade = input('Informe a idade \n')
    email  = input('Informe o email \n')

    Dicionario(nome, idade, email).to_armazena()

print(dicionario)