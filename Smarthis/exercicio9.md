Exercicio 9

Resolver por código:
Um cliente da SMARTHIS possui o seguinte processo de RPA: Todo dia um grupo de
notas fiscais, cada uma com um valor, chegam para serem processadas. O
processamento destas notas segue as seguintes regras:
Notas com valor abaixo de R$ 5.000 reais devem ter seu valor incluído no banco de
dados do cliente diretamente.
Notas acima de R$ 5.000 reais devem ter seu valor enviado por email para o centro de
custo do cliente, onde serão incluídas manualmente por eles.
Notas com valor R$ 0 não devem ser processadas e no final da automação, deve ser
enviado um email ao centro de custo informando a quantidade de notas com este valor.
A quantidade total de notas processadas (independente de valor) deve ser enviada por
e-mail para o centro de custo.
O pseudocódigo deste processo pode ser visto abaixo:
• Obter as notas a serem processadas no dia e criar um array de objetos que
representem essas notas fiscais.
• Enviar um e-mail para o centro de custo com a quantidade de itens desse array
(quantidade total de notas)
• Para cada nota:
o Se o valor da nota é igual a zero:
▪ Incrementa a contagem de notas zeradas
o Se o valor da nota é menor que R$ 5.000:
▪ Inclui os dados da nota fiscal no banco de dados
o Senão:
▪ Envia a nota fiscal por e-mail para o centro de custo
• Enviar um e-mail com a quantidade de notas fiscais com o valor igual a zero.
Recentemente, o cliente solicitou uma alteração no RPA. Eles querem que todos os
emails sejam mandados em sequência, sem que nenhuma inclusão no banco de dados
seja feita entre o envio de qualquer e-mail. Estas inclusões devem ser feitas antes ou
depois do envio de todos os emails.
Em outras palavras, entre os email de quantidade de notas, quantidade de notas zeradas
e notas acima de R$ 5.000, não podem existir inclusões no banco de dados.
Modifique o código para incluir esta regra nova
