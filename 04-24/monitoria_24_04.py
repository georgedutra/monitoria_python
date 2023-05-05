# Terceira monitoria de Python, do dia 24 de abril
# Descomente as linhas de print() para ver o resultado no terminal.

# tipos de variaveis
# bool, int, float, string

# condicional
# if, (elif), else

# Laços/loops/estruturas de repetição:

# while (CONDICAO):
#     CASO A CONDICAO SEJA VERDADE

# for ELEMENTO in LISTA:
#     CASO A CONDICAO SEJA VERDADE

"""
Introduziremos hoje o conceito de iteráveis: todo objeto em python que contém elementos que podem ser acessados um a um, é chamado de iterável
Iteração ou iterar é a ação de acessar ou manipular os elementos de um objeto, um por um
O processo de iteração mais básico que temos é o laço de repetição for
"""

alfabeto = ["A", "B", "C", "D"]
alfabeto_grego = ["alpha", "beta", "gamma", "phi", "delta"]

# FUNCIONA, MAS NAO PARA ESSE CENARIO
# for i in alfabeto:
#     for j in alfabeto_grego:
#         print(i, j)

# NAO FUNCIONA
# for i, j in alfabeto, alfabeto_grego:
#     print(i, j)

# FUNCIONA MESMO PRA LISTAS COM TAMANHOS DIFERENTES
# for letra_normal, letra_grega in zip(alfabeto, alfabeto_grego):
#     print(letra_normal, letra_grega)

#####################################################################################################################

"""
Um slice é um PEDAÇO de um iterável. Ainda que esse pedaço possua somente um elemento, ele ainda é um iterável.
Ou seja, qualquer slice de uma lista é uma lista menor, e definimos seu tamanho pelos índices
Estrutura de um slice:

lista[START (inclusivo) : STOP (não inclusivo) : STEP (padrão é 1)]

"""

# pixel = [R, G, B]
verde_musgo = [92, 107, 39]

# print("Canal vermelho:", verde_musgo[0])
# print("Canais vermelho e azul:", verde_musgo[0], verde_musgo[2])

# Slices são FECHADOS à esquerda e ABERTOS à direita, portanto se queremos os dois primeiros elementos:
# INCORRETO: 
# print("Canais vermelho e verde:", verde_musgo[0:1]) 
# CORRETO:
# print("Canais vermelho e verde:", verde_musgo[0:2])

# print("Todos os canais:", verde_musgo[0:3])
# print("Todos os canais a partir do segundo:", verde_musgo[1:3])

"""
Observação: temos uma função que retorna um inteiro correspondente ao número de elementos de um iterável, ou seja, seu tamanho.
Essa é a função len(). Nesse caso, teríamos: len(verde_musgo), que retorna 3.
"""

# Slice sem fim definido -> percorre até o final
# print(verde_musgo[1:])
# Slice sem incio definido -> percorre desde o início
# print(verde_musgo[:2])

# Slice somente com step definido -> percorre todo o iterável, com o incremento especificado (nesse caso, de 2 em 2)
# print(verde_musgo[::2])

# INTERESSANTE: Se tentamos acessar um mesmo elemento duas vezes num slice, como estamos incluindo e excluindo ele ao mesmo tempo, o python opta por excluí-lo:
# print(verde_musgo[0:0])
# Mas perceba que o resultado não é "nada", é uma LISTA VAZIA, ou seja, AINDA É UM PEDAÇO, apenas um pedaço vazio 

"""
range é uma função que pode receber um start (inclusivo), um stop (exclusivo), e um step. 
Ela retorna uma lista de inteiros começando no start, terminando um elemento antes do stop, com intervalos do tamanho do step.
"""

# ITERAR SOBRE TODOS OS ELEMENTOS DO RANGE (indo de 0 até 99, um por um)
# for elemento in range(0, 100):
#     print(elemento)

# ITERAR SOBRE TODOS OS ELEMENTOS PARES DO RANGE (indo de 0 a 99, de dois em dois)
# for elemento in range(0, 100, 2):
#     print(elemento)

# ITERAR SOBRE TODOS OS ELEMENTOS IMPARES DO RANGE (indo de 1 a 99, de dois em dois)
# for elemento in range(1, 100, 2):
#     print(elemento)

letras = ["A", "B", "C", "D", "E", "F"]

# for valor in letras[::2]: # IMPRIME SOMENTE OS VALORES DE ÍNDICE PAR
#     print(valor)

# for index in range(0, len(letras), 2):
#     # print(index) # IMPRIME SOMENTE OS INDICES
#     print(letras[index]) # IMPRIME OS VALORES DA LISTA UTILIZANDO OS ÍNDICES PARES

# INDICES NEGATIVOS
# print(letras[-3]) # Saída: D

# Como já vimos anteriormente, a indexação negativa indica o último elemento com -1, e decresce conforme retornamos na lista
#  A   B   C   D   E   F
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

# print(letras[-1:]) # Percorre a lista a partir do -1 (F), mas mantém o step
# Saída: ['F']

# print(letras[-1::-1]) # Percorre a lista a partir de -1 (F), mas no sentido contrário (STEP = -1)
# Saída: ['F', 'E', 'D', 'C', 'B', 'A']

#####################################################################################################################
"""
for elemento in lista:
    print(elemento)

# SAÍDA:
A
B
C
D
E
F

===============================
for elemento in lista:
    print(elemento, end=", ")

# SAÍDA:
A, B, C, D, E, F,
"""

idade = 16

# TEXTO RIGIDO
# print("Tenho 15 anos")

# MANIPULANDO O PRINT
# print("Tenho", idade, "anos")

# STRING FORMATADA
# print(f"Tenho {idade} anos")

#####################################################################################################################
"""
in: OPERADOR DE PERTENCIMENTO
"""

alunos = ["Almir", "Adalberto", "Ademar", "Oracio", "Edwaldo", "Itamar"]

# Podemos procurar um elemento iterando pela lista
# for elemento in alunos:
#     if elemento == "Beatriz":
#         print("ACHEI!!")
#         break

# Mas o operador in facilita o processo
# if "Beatriz" in alunos:
#     print("ACHEI!!")
# else:
#     print("NAO ACHEI :(")

# if "Itamar" in alunos:
#     print("ACHEI!!")
# else:
#     print("NAO ACHEI :(")

# E para procurar mais de uma string?
# if ["Beatriz", "Itamar"] in alunos:
#     print("ACHEI!!")
# else:
#     print("NAO ACHEI :(")

# if ["Adalberto", "Itamar"] in alunos:
#     print("ACHEI!!")
# else:
#     print("NAO ACHEI :(")

"""
Estranho não? Deu errado em ambos os casos. Acontece que quando usamos o operador in, passamos para ele exatamente o que queremos achar.
Ou seja, ele não está procurando por duas strings, está procurando por uma LISTA que CONTÉM essas duas strings.
Vamos modificar a lista de forma que ele encontre o que está procurando:
"""
# alunos.append(["Adalberto", "Itamar"])
# print(alunos)

# if ["Adalberto", "Itamar"] in alunos:
#     print("ACHEI!!")
# else:
#     print("NAO ACHEI :(")

"""
Se queremos procurar mais de um elemento, usamos os operadores lógicos: OR e AND
"""
# if "Adalberto" and "Itamar" in alunos:
#     print("ACHEI!!")
# else:
#     print("NAO ACHEI :(")

# /\ /\ /\ EQUIVALENTES \/ \/ \/

# if "Adalberto" in alunos and "Itamar" in alunos:
#     print("ACHEI!!")
# else:
#     print("NAO ACHEI :(")

#####################################################################################################################
"""
Qual a diferença de um MÉTODO e uma FUNÇÃO?
O que define um processo INPLACE?
"""

# FUNÇÃO x MÉTODO

# Função: algo INDEPENDENTE que pode ou não receber parâmetros/argumentos, e pode ou não retornar algo
    # Ex: print("Almir")
# A função print recebe o que deve ser impresso, e não retorna nada, portanto não precisamos atribuí-la a nenhuma variável, basta chamá-la de forma avulsa
# Ela também não depende de outros objetos, perceba que podemos até chamá-la sem passar nada, e ela ainda funciona! (e imprimirá um espaço vazio no terminal)

# Método: algo DEPENDENTE que pode ou não receber parâmetros/argumentos, e pode ou não retornar algo
    # Ex: lista.sort()
# O método sort só pode ser chamado a partir de uma lista, pois ele é um método delas. Ele não recebe parâmetros, e não retorna nada, então o que ele faz?
# Chamamos sort de um método INPLACE, pois ele realiza uma alteração DIRETA no objeto que o chama

lista = [1,7,2,5,3,4,8,6,9]

# print("Lista antes do sort:", lista)
lista.sort() # Operação INPLACE (que altera a variavel original)
# print("Lista depois do sort:", lista)
# Perceba que também chamamos sort de forma avulsa, pois esse método não RETORNA nada

# Apresentando a função sorted: ela não é exclusiva da lista, mas aceita listas como parâmetro (assim como qualquer iterável)
# Ela também não é uma operação inplace, portanto se a chamarmos de forma avulsa:
lista = [1,7,2,5,3,4,8,6,9]
sorted(lista)
# print("Lista depois do sorted:", lista)
# NADA acontece. Ela não altera a lista, mas cria e RETORNA uma cópia ordenada dela. Portanto, devemos ATRIBUÍ-LA a uma variável

lista_ordenada = sorted(lista) # Operação que não é inplace (que preserva a variavel original)
# print("Lista:", lista)
# print("Lista ordenada:", lista_ordenada)

# Também podemos usar a cópia da lista apenas para o print, sem atribuí-la, e logo em seguida a descartamos
# print("Lista temporariamente ordenada:", sorted(lista))

#####################################################################################################################

"""
O que são SHALLOW COPIES e DEEP COPIES? 
"""

# print("Adicionando elementos à lista original")
# lista.append(10)
# print("Lista:", lista)
# print("Lista ordenada:", lista_ordenada)

# Perceba que alterando a lista original, a lista ordenada não se altera. Isso acontece pois dizemos que a função sorted(), que NÃO É INPLACE, cria uma DEEP COPY, ou CÓPIA PROFUNDA
# Isso significa que criamos uma cópia VERDADEIRA E INDEPENDENTE da versão original.

# DEEP COPY
copia_lista = lista.copy() # O método copy() cria uma deep copy
# print(id(lista), id(copia_lista)) # A função id cria um identificador numérico para o local da memória na qual aquela variável está alocada
# Perceba que os ids são diferentes, portanto são objetos diferentes. Repetindo o teste:
# lista.append(11)
# print("Lista:", lista)
# print("Copia:", copia_lista)

# Quando fazemos uma cópia rasa, ou SHALLOW COPY, criamos uma nova forma de nos referir ao mesmo objeto. Ou seja, apenas PARECE que criamos uma cópia, quando na verdade, ela
# ainda está ligada ao objeto original, e DEPENDE dele. Por isso o nome se traduz para "raso" ou "superficial".

# SHALLOW COPY
copia_lista = lista # Se apenas atribuímos um mesmo objeto em outra variável, ambas nos levarão no MESMO local de memória
# print(id(lista), id(copia_lista))

# lista.append(11)
# print("Lista:", lista)
# print("Copia:", copia_lista)

# INPLACE -> shallow copy (cópia superficial)
# NOT INPLACE -> deep copy (cópia profunda)
