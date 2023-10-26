# Qual o problema de fazer funções grandes e complexas?
# Isso torna o código complexo e difícil de manter
# Torna difícil identificar onde estão os possíveis erros.
# funcionalidades podem afetar negativamente o funcionamento de outras partes do código.
# A ausência de separação de responsabilidades torna o código menos organizado e mais 
# suscetível a erros difíceis de rastrear. 

# Vamos observar a função a seguir coloquei alguns erros nele

def super_função(lista):
    soma = 0
    maior_par = None
    quantidade_pares = 0

    for num in lista:
        if num % 2 == 6:
            soma += num ** 2
            if maior_par is None or num > maior_par:
                maior_par = num
            quantidade_pares += 1

    return soma, maior_par, quantidade_pares

numeros = [1, 2, -3, 4, -5, 6]
resultado_soma, resultado_maior, resultado_quantidade = super_função(numeros)

print(f"Soma dos quadrados dos números pares: {resultado_soma}")
print(f"Maior número par: {resultado_maior}")
print(f"Quantidade de números pares: {resultado_quantidade}")



# agora veremos como seria esse codigo dividido

def soma_quadrados_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num ** 2
    return soma

def maior_numero_par(lista):
    maior_par = None
    for num in lista:
        if num % 2 == 0:
            if maior_par is None or num > maior_par:
                maior_par = num
    return maior_par

def quantidade_numeros_pares(lista):
    quantidade_pares = 0
    for num in lista:
        if num % 2 == 0:
            quantidade_pares += 1
    return quantidade_pares

def super_funcao_mesclada(lista):
    resultado_soma = soma_quadrados_pares(lista)
    resultado_maior = maior_numero_par(lista)
    resultado_quantidade = quantidade_numeros_pares(lista)
    return resultado_soma, resultado_maior, resultado_quantidade

numeros = [1, 2, 3, 4, 5, 6]
resultado_soma, resultado_maior, resultado_quantidade = super_funcao_mesclada(numeros)

print(f"Soma dos quadrados dos números pares: {resultado_soma}")
print(f"Maior número par: {resultado_maior}")
print(f"Quantidade de números pares: {resultado_quantidade}")
