# As variáveis devem possuir nomes intuitivos para facilitar sua compreensão.

# Quando uma variável não possui um nome intuitivo é difícil definir do que ela se trata,
# e isso impacta diretamente na legibilidade do código que posteriormente impactara na manutenção do mesmo.

# Vamos ver um exemplo simples para melhor compreensão.

# Ex 1:

import exemplos

x = exemplos.Exemplo1()

# Mas se mudarmos o nome dá varivel sua compreenção fica tão nitida
# quanto a luz do dia...


data_atual= exemplos.Exemplo1()

data_atual_centralizada = " " * 10 + data_atual + " " * 10

print("="*30)
print(data_atual_centralizada)
print("="*30)