# Segunda monitoria de Python, do dia 27 de março
# Descomente as linhas de print() para ver o resultado no terminal.
"""
if, elif, else

for, while

break, continue

"""

"""
Estruturas Condicionais e Operadores Lógicos

Temos em python as estruturas:
if
elif
else

As quais chamamos de estruturas condicionais. Queremos usá-las quando temos ESCOLHAS a serem feitas, pois passamos condições que devem ou não ser atendidas (intuitivo, não?).
Essas estruturas ainda são apoiadas por operadores lógicos que ampliam suas funções: and, or e not.
"""

idade = 17
# idade = 30
# idade = 65

# if idade >= 18:
#     # O bloco de código escrito dentro de um if só é executado se a operação ternária escrita na frente do "if" retornar True
#     print("Você pode se embriagar (Aproveite)")

# elif idade >= 60:
#     # Já no bloco elif, o código só é compilado se o ternário DIRETAMENTE ANTERIOR a ele retornar False, mas o dele retornar True.   
#     print("Você pode se aposentar (e se embriagar tambem)")

# else: 
#     # O bloco else é compilado caso NENHUM dos ternários antes dele retornarem True. Como ele só depende disso, não possui ternário.
#     print("Você não pode beber ;-;")

"""
É importante perceber algumas coisas na sintaxe das estruturas condicionais em python:
- Elas seguem um padrão de fila: o código é compilado de cima para baixo, e a estrutura para no primeiro ternário a retornar True
- Usar elif e else é opcional, mas cada estrutura condicional PRECISA iniciar com if
- Podemos colocar uma estrutura condicional dentro da outra, causando várias recursões de condições 

Em muitos casos, porém, se queremos "empilhar" várias condições, podemos usar operadores lógicos:
"""

# if idade >= 18 and idade < 60:
#     # Com o 'and', TODAS as condições devem retornar True para o código ser compilado
#     print("Você pode se embriagar (Aproveite)")

# elif idade == 60 or idade > 60:
#     # Com o 'or', o código será executado se pelo menos UMA (ou mais) das condições retornar True
#     print("Você pode se aposentar (e se embriagar tambem)")

# else:
#     print("Você não pode beber ;-;")

# # Temos ainda o not, que vem logo antes da operação ternária e INVERTE a lógica da condicional
# idade = 2000
# if not idade < 1000:
#     # Nesse caso, o ternário que retornaria False retornará True!
#     print("Caramba, você deve ser Matusalém! (e pode beber!)") 

"""
RESUMO DE CONDICIONAIS:
==================================
if CONDIÇÃO:
    SE A CONDIÇÃO FOR VERDADEIRA
==================================
if CONDIÇÃO:
    SE A CONDIÇÃO FOR VERDADEIRA
else:
    SE A CONDIÇÃO FOR FALSA
==================================
if CONDIÇÃO_1:
    SE A CONDIÇÃO_1 FOR VERDADEIRA
elif CONDIÇÃO_2:
    SE AS CONDIÇÕES ANTERIORES FOREM FALSAS E A CONDIÇÃO_2 FOR VERDADEIRA
else:
    SE NENHUMA CONDIÇÃO FOR VERDADEIRA
==================================

TABELA AND/OR:
-----------------------------------------------------
| X |   CONDIÇÃO_1    |   CONDIÇÃO_2    | RESULTADO |
-----------------------------------------------------
|   |     TRUE        |      TRUE       |   TRUE    | 
|AND|     TRUE        |      FALSE      |   FALSE   |
|   |     FALSE       |      FALSE      |   FALSE   |
-----------------------------------------------------
|   |     TRUE        |      TRUE       |   TRUE    |
|OR |     TRUE        |      FALSE      |   TRUE    |
|   |     FALSE       |      FALSE      |   FALSE   |
-----------------------------------------------------
"""

aluno_1 = "Guilherme"
aluno_2 = "Almir"

# Perceba que os operadores ternários são capazes de comparar strings!
# if aluno_1 == aluno_2:
#     print("Alunos iguais")
# else:
#     print("Alunos diferentes")

# Muitas classes tem um valor Booleano intrínseco. Por exemplo, um inteiro vale False se for igual a 0, e True caso contrário. Qualquer iterável vale False se estiver vazio, e True se possuir algum conteúdo. A classe especial de python None representa a ausência de dados, e sempre vale False.

# if None:
#     print("SIM")
# else:
#     print("NÃO")

################################################################################################################

"""
Listas e Laços de Repetição

Listas são uma classe de objeto que, resumindo, armazena outros objetos sem necessariamente atribuí-los a uma variável.
Elas são classes muito complexas e com muitas funcionalidades, mas vamos explorá-las melhor no futuro.

Na maioria das linguagens, existem estruturas para executar um código várias vezes consecutivas. Chamamos essas estruturas de laços de repetição, ou simplesmente Loops.
Existem dois loops principais no python:
for
while

E ambos são apoiados por duas flags muito utilizadas: continue e break.
"""

lista = ["A", "B", "C", "D", "E"]

# Utilizando o laço for, estamos fazendo com que o bloco de código dentro do laço seja executado uma vez para cada item DENTRO da lista  
# for elemento in lista:
#     print(elemento)

"""
O laço while recebe uma operação ternária que retorne True. Toda vez que o bloco de código termina, ele verifica se a ternária ainda é True, e em caso afirmativo, repetirá o laço.
CUIDADO! Caso você não faça com que essa operação ternária mude em algum momento, o loop do while se repetirá eternamente, fazendo com que você tenha que parar o código manualmente. Vamos mostrar isso numa função que imprime todos os números pares de 1 até 100.
""" 

i = 0

while True: # Perceba que o laço não para nunca, pois True nunca deixará de valer True
    i += 1

    if i % 2 != 0 and i <= 100:
        # A flag continue, quando executada, interrompe ESSA execução do loop e pula para a próxima, não importando se tem mais código no bloco
        continue

    # print(f"{i} é par")

    if i >= 100:
        # A flag break por outro lado, interrompe de vez o loop e ENCERRA o while nessa linha, independente da ternária ter mudado ou não
        break

"""
Como introduzimos listas, vamos falar um pouco sobre como acessá-las. Já que não demos uma variável para cada item, precisamos de uma forma de acessar os itens diretamente. No momento da criação de uma lista, é atribuído a cada item da lista um índice, mais comumente chamado de INDEX.
Os indexes de uma lista são números inteiros crescentes começando do 0, distribuídos na ordem de atribuição. 
"""
# INDEX:         0    1    2 
lista_letras = ["A", "B", "C"]

# print(lista_letras)

# Para acessar um item específico, chamamos o nome da lista, e passamos um índice entre colchetes
# print(lista_letras[2])

# Se passarmos um inteiro NEGATIVO, o python entende que estamos contando a lista de trás para frente, sendo o ÚLTIMO ITEM da lista o índice -1
# print(lista_letras[-2])

# Podemos ainda SUBSTITUIR um item da lista
# Perceba que uma lista pode conter vários tipos diferentes de objetos
lista_letras[1] = 42

# Se quisermos adicionar um item, chamamos o método list.append(), e passamos para ele UM objeto a ser adicionado
lista_letras.append("D")

# Para remover um item da lista, chamamos o método list.pop(), e passar para ele o índice do item. Se não passarmos um index, ele remove o último
a = lista_letras.pop()
# print(lista_letras)

# O método pop não só altera a lista original, mas RETORNA o item removido, e dessa forma podemos salvar esse item numa variável 
# print(a)

# Podemos fazer algo bem interessante: adicionar uma lista dentro da outra
lista_letras.append(["D1", "D2"])
# print(lista_letras)

# Além disso, podemos ACESSAR a lista dentro da lista
# print(lista_letras[3][1])

# Vamos brincar um pouco com o conceito de listas dentro de listas para criar uma estrutura parecida com uma matriz:
matriz = [["a", "b", "c"], ["d", "e", "f"], ["e", "f", "g"]]
# print(matriz[1][2]) # Perceba que com esse acesso, parece que estamos passando qual linha e depois qual coluna queremos

# for linha in matriz:
#     for elemento in linha:
#         print(elemento, end=" ")
#     print("")

# Bônus: Apresentamos alguns métodos de listas na monitoria de hoje! Lembra como se faz para perguntar para uma classe o que ela sabe fazer?
# Descomente a linha abaixo e veja se reconhece alguns dos métodos que vimos hoje!!

# print(lista_letras.__dir__())

