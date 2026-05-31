
# # Exercicio 4

# Resolver por código:

# Um caixa eletrônico tem disponível apenas notas de R$ 5, R$ 20 e R$ 50. Crie um
# algoritmo que recebe como entrada o valor que se deseja sacar e retorne a menor
# quantidade de notas que o compõem, especificando a quantidade de cada nota.
# Atenção para os casos em que a entrada não é divisível pelo valor notas disponíveis.
# Ex1: para um saque de R$ 25, o algoritmo retornaria que são 2 notas, uma de 5 e uma
# de 20.
# Ex2: para um saque de R$ 175, o algoritmo retornaria que são 5 notas, três de 50, uma
# de 20 e uma de 5 -->





def saque(valor):
    # -----notas disponíveis
    notas = [50, 20, 5]
    resultado = {}

    for nota in notas:
        qtd = valor // nota
        if qtd > 0:
            resultado[nota] = qtd
            valor -= qtd * nota

    if valor != 0:
        return " ----------- O valor nao pode ser sacado -----------------"
    else:
        return resultado


# Exemplos de uso:
print(saque(25))   # {20: 1, 5: 1}
print(saque(175))  # {50: 3, 20: 1, 5: 1}
print(saque(18))   # Valor não pode ser sacado com as notas disponíveis.
