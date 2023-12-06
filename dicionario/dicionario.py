"""
Crie uma funcao que receba os valores do nome, idade e e-mail de uma pessoa e 
guarde-os em um dicionario com as chaves nome, idade e email, respectivamente. 
Sua funcao deve retornar esse dicionario.
"""

def setDadosDicionario(nome, idade, email):
    dicionario={'Nome': nome,'Idade': idade,'Email': email}
    print(dicionario)

nome  = input('Informe o nome \n')
idade = input('Informe a idade \n')
email  = input('Informe o email \n')

setDadosDicionario(nome, idade, email)