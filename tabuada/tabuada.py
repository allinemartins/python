'''Faca um programa que receba um numero e usando lacos de repeticao calcule e mostre a tabuada (Soma/Multiplicacao/Divisao) desse número.'''

def cabecalho(t):
    print('=' * 41)
    print('{:^41}'.format(t))
    print('=' * 41)

cabecalho('TABUADA')
print()

def operacoes(oper, n, min, max):        
    if oper == 'S':      
      [print(f'{x} + {n} = {x+n}') for x in range(min, max)]
    if oper == 'M':
       [print(f'{x} x {n} = {x*n}') for x in range(min, max)]
    if oper == 'D':
       [print(f'{x} / {n} = {x/n}') for x in range(min, max)]

oper = ' '
while oper not in 'SMD':    
    oper = str(input('Escolha a operacao desejada [soma = S ou multiplicacao = M ou divisao = D]: ').upper().strip()[0])
    print()
    num = int(input('Digite o numero: '))
    print()
    operacoes(oper, num, 1, 50)   
    
cabecalho('FIM')