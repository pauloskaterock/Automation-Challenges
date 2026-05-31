# Exercicio 6

# 6- Resolver por código:
# Escreva um código para realizar o sorteio da mega-sena, que consiste na seleção de seis
# números diferentes compreendidos entre 1 e 60. Retorne o array contendo os números
# sorteados


import random

def mega_sena():
    """
    Realiza um sorteio da Mega-Sena.
    Retorna uma lista com 6 números aleatórios entre 1 e 60
    """
    # ------------Sorteia 6 números únicos entre 1 e 60
    numeros_sorteados = random.sample(range(1, 61), 6)

    # Ordena para ficar mais fácil de ler
    numeros_sorteados.sort()

    return numeros_sorteados


# Teste
print("---------- SORTEIO DA MEGA-SENA GOOD lUCK-----------\n")

for i in range(5):
    resultado = mega_sena()
    print(f"Sorteio {i+1}: {resultado}")
