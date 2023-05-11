# Quinta monitoria de Python, do dia 10/05
# Descomente as linhas de print() para ver o resultado no terminal.

""" 
Outros tipos de iteráveis!

Na aula de funções falamos muito de tuplas, mas afinal o que elas são? O que são ITERÁVEIS?
Iteráveis são objetos em python que armazenam elementos, e possibilitam o processo de ITERAÇÃO.
Iterar é o ato de acessar um iterável elemento por elemento, visualizando-os e/ou manipulando-os um por um.
Dentre as principais classes de iteráveis, temos no python base:

- Listas
- Tuplas
- Dicionários
- Conjuntos
"""

# Definição de lista
lista = []

# Definição de tupla
tupla = ()

# Definição de set (conjunto)
conjunto = {}

# Definição de dicionario
dicionario = {}

# Estranho... sets e dicionarios são definidos da mesma forma?

###############################################################################################################

"""
Tuplas possuem muito em comum com listas: 
- Seus elementos são ordenados, e podem ser acessados com indexação e slicing;
- Consegue guardar elementos de diferentes tipos;
- Permite duplicatas;
- Suporta iterações com laços (for, while).

Porém, possuem uma diferença crucial: uma vez criadas, tuplas são imutáveis!!!
"""

lista = [1,2,3, "EMAp", True]
tupla = (1,2,3,3,3, "EBAPE", False) 

# A principal diferença é que representamos tuplas entre parênteses ao invés de colchetes
# print(lista, tupla)
# print(type(lista), type(tupla))

# Indexação e slicing funciona da exata mesma forma!
# print(tupla[0], tupla[6])
# print(tupla[0:5])

# Podemos alterar listas:
lista.remove(2)
# print(lista)
lista.append(42)
# print(lista)
# Mas não podemos alterar tuplas :(

# Em IDE's com extensões de python como o Pylance do VSCode, se escrevermos algo como a linha abaixo:
# lista. 
# Podemos ver que uma lista possui vários métodos de alteração, como o .remove e o .append

# Uma tupla no entanto, ao escrevermos a mesma coisa:
# tupla.
# Percebemos que não sabe fazer quase nada :(

"""
Isso decorre do fato de que tuplas são definidas com o objetivo de transportar e visualizar dados, 
portanto uma vez criadas, não podemos alterar seu conteúdo ou seu tamanho.

Por consequência do menor número de métodos, uma tupla é mais prática que uma lista, mas menos útil.
Além disso, ela tem a utilidade de proteger seu conteúdo da influência do usuário. 
"""

###############################################################################################################

"""
Dicionários são estruturas muito importantes e úteis. Eles possuem poucas semelhanças com seus antecessores,
mas carregam muitas utilidades. Em resumo, são estruturas poderosíssimas. Entre suas principais características:

- Não possuem uma ordenação natural, portanto não temos como acessá-lo por indexação ou slicing;
- Carregam dentro de si dois objetos com objetivos diferentes: Chaves e Valores, que juntos formam pares chamados de Itens;
- Não são homogêneos, portanto aceitam objetos de qualquer tipo como chaves e como valores;
- Não aceitam repetição de chaves, mas aceitam de valores;
- Aceitam iteração de elementos com laços de repetição.

Dito isso, vamos aprender na prática:
"""

# Sintaxe:
# nome_do_dict = {Chave : Valor, Chave : Valor}
dicionario = {1 : "EMAp", "dois" : "CdD", False : "MAp", (4,6,8) : [1,2,3,4,5]}

# Perceba que de fato podemos usar QUALQUER COISA como chave, e naturalmente, como valor também
# print(dicionario)
# print(type(dicionario))

# Para acessar um dicionário, chamamos uma chave dentro de colchetes
# print(dicionario["dois"])
# print(dicionario[False])

# Recursão: Podemos colocar um dicionário dentro do outro
dicionario_2 = {1: "FGV", 2: {"um": "EMAp", "dois": "CPDOC"}}
# print(dicionario_2[1])
# print(dicionario_2[2]["um"])

# Para adicionar um elemento, "acessamos" uma chave que não existe ainda, e atribuímos algum valor
aluno = {} 
aluno["Nome"] = "Tio"
aluno["Sobrenome"] = "Rafa"
aluno["Idade"] = 38
aluno["Naturalidade"] = "MS"
# print(aluno)

# Perceba que não tem como atribuir uma chave sem valor, nem um valor sem chave. Eles são pares inseparáveis!

# Para alterar um valor, atribuímos um valor acessando uma chave que já existe
aluno["Idade"] = 20
# print(aluno)

# Perceba que não temos como criar chaves repetidas! Se ela já existe, só será alterada.

"""
Dicionários sabem fazer muitas coisas interessantes através de seus MÉTODOS
"""

# dict1.update(dict2) recebe um dicionário, e insere seus dados no dicionário original
dados_extras = {"Nacionalidade": "brasileiro", "Religião": "paganismo nórdico"}
aluno.update(dados_extras)
#print(aluno)

# Se uma chave do segundo dicionário já existe, o valor do dicionário original é atualizado
dados_extras = {"Idade": "21"}
aluno.update(dados_extras)
# print(aluno)

# dict.get(key) retorna o valor correspondente à chave passada
valor = aluno.get("Nacionalidade")
# print(valor)
# print(cartao.get("Essa chave não existe", -1)) # Podemos escolher o valor retornado caso a chave não exista

# dict.pop() remove itens específicos pela chave
# removido = aluno.pop("Religião") # Remove o valor da chave passada, e o retorna
# del aluno["Religião"] # Funciona mas não é o usual

# dict.items() retorna uma lista com tuplas, cada tupla contendo um item (ou seja, um par (chave, valor))
itens = aluno.items()
# print(type(itens))
# print(itens)
# OBS: na verdade, retorna um objeto do tipo "dict_items", que pode ser convertido para listas usando "list()"

# dict.keys() retorna um iterável das chaves de dict
keys = aluno.keys()
# print(keys)
keys = list(aluno.keys())
# print(keys[0])

# dict.values() retorna um iterável dos valores de dict
values = aluno.values()
# print(values)

# dict.clear() esvazia completamente o dicionário
aluno.clear()
# print(aluno)

###############################################################################################################

"""
Conjuntos são uma classe de iterável bastante incomum.
Imagine-os como dicionários sem chave:

- Não possuem ordem nem índices;
- Não são homogêneos;
- Não permitem repetição;
- Não suportam nenhum acesso ou loop diretamente. Se tentarmos, o python faz um loop sobre uma lista criada por cima do conjunto.

Em suma, não temos como acessar um set de nenhuma forma. Seu único objetivo é transportar dados.
Ainda assim, existem algumas utilidades para ele, como remover duplicatas.
"""

myset = {"apple", "banana", "cherry"}
# print(myset)

"""
Quando imprimimos um set, o python o ordena de forma aleatória (ou de forma a economizar memória se for homogêneo)
Por isso, toda vez que rodamos um print(set), podemos ver um resultado diferente
"""

# Tanto dicts como sets são indicados com chaves, por isso para iniciar um vazio, é melhor utilizar set()
empty_set = set()

# Inicialização de um set a partir de uma lista
number_list = list(range(0, 100))
number_set = set(number_list)
# print(number_set)

# Usando sets para remover duplicatas
lista_pares = [2, 0, 4, 6, 8, 2, 10, 4]
lista_sem_duplicatas = list(set(lista_pares))
# print(lista_sem_duplicatas)

# Dict ou Set?? Eis a questão

# Inicialização ambígua
qualquer_coisa = {}

# Inicialização clara
novo_set = set()
novo_dicionario = dict()

# Qual o resultado da inicialização ambígua?
# print(type(qualquer_coisa)) 

# Transformando set em dict
new_set = {"A", "E", "I", "O", "U"}
# new_dict = dict(new_set) # -> Falha, porque nao existem chaves pra esses valores

new_keys = {1, 2, 3, 4, 5}
new_dict = dict(zip(new_set, new_keys))
# print(new_dict)

# Como podemos ver, é bem complicado transformar um set em dicionário, por isso a inicialização ambígua
# cria um dicionário, pois é mais fácil convertê-lo em conjunto do que o caminho inverso. 

"""
A principal utilidade dos conjuntos são seus métodos que abordam a lógica de conjuntos matemáticos,
como união, interseção, diferença de conjuntos, etc. Apesar de ser útil, tudo isso pode ser feito em
poucas linhas de código com listas e loops de repetição.

Em suma, a maior vantagem dos conjuntos é seu baixo custo computacional.
"""
