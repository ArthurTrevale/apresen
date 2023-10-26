# a mesma lógica se aplica a funções quando não sabemos do que se trata
# é bem mais complexo ver o por que daquela função existir

import exemplos

def função(a,b):
    c = exemplos.Exemplo2(a)
    d=b/c
    print(d)

# agora faremos a mesma função de forma descritiva


def Calcular_IMC(altura,peso):
    altura_elevada = exemplos.Elevar_pelo_quadrado(altura)
    imc = peso/altura_elevada
    print(imc)