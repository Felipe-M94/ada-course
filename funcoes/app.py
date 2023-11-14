# Função Inicial

def saudacao():
    print('Bem Vindo!')
    
saudacao()

# Função com Parâmetros

def saudacao(nome):
    print(f'Bem Vindo!, {nome}')
    
saudacao('Felipe')

# Função Default

def saudacao(nome='Felipe'):
    print(f'Bem Vindo!, {nome}')
    
saudacao()

# Funções Retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print(f'O resultado da soma é: {resultado}')


