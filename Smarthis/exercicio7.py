# Exercicio 7

# Resolver por código:
# Hora de programar um jogo! Seu código deve gerar um número aleatório dentro de um
# intervalo escolhido pelo próprio jogador, que servirá como resposta, e solicitar que o
# usuário tente adivinhá-lo. A partir da resposta do usuário:

# a. Se o palpite do usuário for errado, o jogo deve informar ao usuário se foi maior ou
# menor que a resposta correta e solicitar um novo chute.
# b. Se o palpite for correto, o jogo deve avisar ao usuário que ele acertou e informar o
# número de tentativas utilizadas.


import random

def jogo_simples():
    # Define o intervalo
    inicio = int(input("Número inicial: "))
    fim = int(input("Número final: "))

    # Sorteia o número
    secreto = random.randint(inicio, fim)
    tentativas = 0

    print(f"\nAdivinhe o número entre {inicio} e {fim}!")

    # Loop de palpites
    while True:
        palpite = int(input("Seu palpite: "))
        tentativas += 1

        if palpite < secreto:
            print("Maior!")
        elif palpite > secreto:
            print("Menor!")
        else:
            print(f"\nAcertou! Número: {secreto}")
            print(f"Tentativas: {tentativas}")
            break

# Jogar
jogo_simples()
