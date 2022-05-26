#criando a primeira funcao que retornara objeto 
def setDadosDicionario(nome, idade, email):
    dicionario={'Nome': nome,'Idade': idade,'Email': email}
    print(dicionario)

nome  = input('Informe o nome \n')
idade = input('Informe a idade \n')
email  = input('Informe o email \n')

setDadosDicionario(nome, idade, email)