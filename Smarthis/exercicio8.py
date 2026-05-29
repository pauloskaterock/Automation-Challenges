# Exercico 8

# Resolver por código:
# Daniel, um programador jovem e cheio de vontade de aprender, precisava incorporar
# em seu código uma função que gerasse numeros aleatorios.
# Daniel queria, contudo, garantir que a função escolhida tivesse uma distribuição
# verdadeiramente aleatória.
# Ele decidiu montar o código conforme a imagem abaixo para testar a função random
# escolhida: em que Random(n) retorna um número inteiro, aleatoriamente, entre 1 e n,
# inclusos.
# A ideia do código era chamar a função randômica 1000 vezes e registrar o resultado
# em uma lista, salvando o valor em "Lista1" caso ele seja maior que 5 ou em "Lista2"
# caso seja menor ou igual.
# Com este experimento, Daniel esperava obter duas listas, cada uma com
# aproximadamente 500 elementos, em que Lista1 teria apenas números de 6 a 10 e
# Lista2 teria apenas números de 1 a 5.
# Ao final do experimento, Daniel verificou o tamanho das listas, e sucesso! Cada lista
# possuía aproximadamente 500 elementos. Ao ver o valor dos elementos, contudo,
# Daniel se surpreendeu.
# Ambas as listas possuíam números de 1 a 10!
# Qual correção deve ser feita no código de Daniel para corrigir este erro de lógica?


# -------------------------


# import random
# count = 0
# while count<1000:
#     if random(10) > 5:
#     Lista1 = Lista1 + random(10)  -----------
#     else:
#     Lista2 = Lista2 + random(10)
#     count = count + 1



# --------------------------------


# Daniel deve corrigir três coisas:

# Usar random.randint(1, 10) em vez de random(10)

# Armazenar o número gerado em uma variável e usar a MESMA variável tanto na condição quanto para adicionar à lista

# Usar append() para adicionar à lista, não concatenação com +



import random

Lista1 = []
Lista2 = []
count = 0

while count < 1000:
    numero = random.randint(1, 10)  # ← Gera uma vez só

    if numero > 5:
        Lista1.append(numero)       # ← Usa o mesmo número
    else:
        Lista2.append(numero)       # ← Usa o mesmo número

    count = count + 1
