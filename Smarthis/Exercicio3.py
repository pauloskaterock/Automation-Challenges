# Em uma mesa, existem 9 pedras, 8 com o mesmo peso e uma mais pesada que as
# demais. Nesta mesa, temos também uma balança de duas pás, que pode dizer se um
# dos lados é mais leve, mais pesado, ou possui o mesmo peso do outro. Usando apenas
# duas medidas na balança (ou seja, apenas podendo usá-la duas vezes), como podemos
# encontrar a pedra mais pesada?


# Divida as 9 pedras em 3 grupos de 3.
# 1ª pesagem: pese dois grupos.

# Se um lado pesar mais, a pedra pesada está ali.

# Se equilibrar, a pedra pesada está no grupo não pesado.
# 2ª pesagem: com as 3 pedras candidatas, pese duas delas.

# Se uma pesar mais, é ela.

# Se equilibrar, a terceira é a pesada.


# ------------------------------------------------------------------------

def encontrar_pesada_simples(pedras):
    # PRIMEIRA PESAGEM: compara grupos de 3
    if sum(pedras[0:3]) > sum(pedras[3:6]):
        grupo = pedras[0:3]  # grupo da esquerda
        indices = [0, 1, 2]
    elif sum(pedras[3:6]) > sum(pedras[0:3]):
        grupo = pedras[3:6]  # grupo da direita
        indices = [3, 4, 5]
    else:
        grupo = pedras[6:9]  # grupo de fora
        indices = [6, 7, 8]

    # SEGUNDA PESAGEM: compara 2 pedras do grupo suspeito
    if grupo[0] > grupo[1]:
        return indices[0]
    elif grupo[1] > grupo[0]:
        return indices[1]
    else:
        return indices[2]

# Teste
pedras = [1,1,1, 1,1,1, 1,1,2]  # última é a mais pesada
print(f"A pedra mais pesada está no índice: {encontrar_pesada_simples(pedras)}")
