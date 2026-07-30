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

def jogo_adivinhacao():
    """
    Jogo da adininhação
    """
    print("\n" + "=" * 50)
    print("--- BEM-VINDO AO JOGO DA ADIVINHAÇÃO")
    print("=" * 50)

    # Escolher intervalo
    print("\n---  DEFINA O INTERVALO DOS NÚMEROS:")

    while True:
        try:
            inicio = int(input("  Número inicial: "))
            fim = int(input("  Número final: "))

            if inicio >= fim:
                print("--- O número inicial deve ser MENOR que o final!\n")
                continue

            if inicio < 0 or fim < 0:
                print("--- Os números devem ser positivos!\n")
                continue

            break

        except ValueError:
            print("--- Digite apenas números inteiros!\n")

    # ----Gerar número secreto
    numero_secreto = random.randint(inicio, fim)
    tentativas = 0
    acertou = False

    print(f"\n--- Número sorteado entre {inicio} e {fim}!")
    print("--- Tente adivinhar...\n")

    # -----------------Loop de palpites
    while not acertou:
        try:
            palpite = int(input("--- Seu palpite: "))
            tentativas += 1

            if palpite < inicio or palpite > fim:
                print(f"--- O número deve estar entre {inicio} e {fim}!\n")

            elif palpite < numero_secreto:
                print(f"--- MAIOR! {palpite} é muito baixo.\n")

            elif palpite > numero_secreto:
                print(f"--- MENOR! {palpite} é muito alto.\n")

            else:
                acertou = True
                print("\n" + "---" * 15)
                print(f"--- PARABÉNS! VOCÊ ACERTOU!")
                print(f"--- Número secreto: {numero_secreto}")
                print(f"--- Tentativas: {tentativas}")

                # Mensagem especial baseada no desempenho
                if tentativas == 1:
                    print("--- PERFEITO! Acertou de primeira!")
                elif tentativas <= 3:
                    print("--- Muito bem! Poucas tentativas!")
                elif tentativas <= 7:
                    print("--- Bom trabalho! Continue praticando!")
                else:
                    print("--- Persistência é a chave! Parabéns!")

                print("---" * 15 + "\n")

        except ValueError:
            print("--- Digite apenas números inteiros!\n")

# Executar
if __name__ == "__main__":
    jogo_adivinhacao()
