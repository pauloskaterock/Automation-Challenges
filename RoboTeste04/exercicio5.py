# Exercicio 5

#  Resolver por código:
# Um conjunto de caixas é numerado em ordem crescente usando adesivos que contém
# algarismos individuais. Para se numerar a caixa de índice 10, são usados 2 adesivos, por
# exemplo. O orçamento para a aquisição de adesivos é limitado, então deseja-se
# conhecer número máximo de caixas que podem ser numerados, de 1 até um
# determinado valor, sem pular nenhum número na contagem, dado esse limite. Escreva
# um algoritmo que receba o número total de adesivos disponíveis e retorne o número
# máximo de caixas que podem ser numerados.
# Ex: Se há 14 adesivos disponíveis, é possível numerar 11 caixas.



def contar_caixas(adesivos):
    """
    A lógica é ir consumindo os adesivos até não ser possível numerar a próxima caixa!
    """
    gasto = 0
    caixa = 1

    while gasto + len(str(caixa)) <= adesivos:
        gasto += len(str(caixa))
        caixa += 1

    return caixa - 1


# Teste
print(contar_caixas(14))  # 11
