"""
Um hospital quer fazer o diagnostico de gripe ou dengue a partir de um questionario de sintomas. 
Tendo as perguntas abaixo, faca um programa que informe o diagnostico deste hospital:

A - Sente dor no corpo?
B - Voce tem febre?
C - Você tem tosse?
D - Esta com congestao nasal?
E - Tem manchas pelo corpo?

Para o diagnostico, e utilizada o seguint:

S - Sim 
N - Nao 

A  B  C  D  E
S  S  N  N  S  = Dengue
S  S  S  S  N  = Gripe 
N  S  S  S  N  = Gripe
S  S  S  S  N  = Gripe 
S  N  N  N  N  = Sem Doencas
N  N  N  N  N  = Sem Doencas
"""

perguntas = (
    'Sente dor no corpo?', 
    'Você tem febre?', 
    'Você tem tosse?', 
    'Está com congestão nasal?', 
    'Tem manchas pelo corpo?'
)

combinacao = {
    'SSNNS': 'Dengue',
    'SSSSN': 'Gripe',
    'NSSSN': 'Gripe',
    'SNNNN': 'Sem doenças',
    'NNNNN': 'Sem doenças'
}

print('''Suas opcoes: 
    | S | Sim
    | N | Não''')

def questionar(pergunta):
    print(f'{pergunta} [S/N]:')
    resposta = input().upper()
    if resposta in ('S', 'N'):
        return resposta
    else:
        return ''


respostas = ''.join([questionar(_pergunta) for _pergunta in perguntas])
print('\nDiagnóstico:', combinacao.get(respostas) or 'Não foi possível determinar!')
