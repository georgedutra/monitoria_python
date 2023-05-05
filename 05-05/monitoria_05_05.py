# Quarta monitoria de Python, do dia 05/05
# Descomente as linhas de print() para ver o resultado no terminal.

"""
input
A função input(), quando executada, espera o usuário digitar algo no terminal e apertar enter.
Uma vez encerrada a espera, ela retorna uma string contendo tudo que o usuário inseriu no terminal.
Ela pode receber uma string, que é impressa no terminal logo antes da espera.
"""

# Esse código recebe um número do usuário, e imprime o número ao quadrado
# Repare que a input() sempre retorna uma STRING, portanto precisamos convertê-la para um int antes de manipulá-lo

# a = int(input("Digite um número: "))
# quadrado = a**2
# print(f"Seu quadrado é {quadrado}!")

# Não é possível receber uma string como '10.5' e convertê-la direto para int: primeiro convertemos para float, e depois para int
# a = int(float(input("Digite um float: ")))
# print(f"Seu float convertido em int é {a}!")

###########################################################################################

"""
Definição de Funções

Quando queremos reutilizar código definimos uma FUNÇÃO, que é chamada quando for necessário executar aquela porção de código. 
Função é um objeto independente que pode ou não receber parâmetros, e pode ou não retornar um resultado.

====================================
SINTAXE:
def nome_da_funcao(parametro):
    codigo
    codigo
    codigo

    return resultado
=====================================

Funções podem receber qualquer quantidade de parâmetros, e estes podem ser passados de algumas formas:

- Parâmetros posicionais x parâmetros nominais
- Parâmetros default
- Parâmetros de quantidade arbitrária
"""

# Diagamos que queremos imprimir os itens de algumas listas elevados ao quadrado
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = [11, 12, 13, 14, 15]

# JEITO RUIM >:(
# for num in lista1:
#     a = num**2
#     print(a)

# for num in lista2:
#     b = num**2
#     print(b)

# for num in lista3:
#     c = num**2
#     print(c)

# Perceba que escrevemos exatamente o mesmo código 3 vezes, mudando apenas a lista utilizada no processo... INACEITÁVEL!

# JEITO BOM :)
def imprimirquadrado(nomequalquer): # Perceba que o nome dado para um parâmetro é como uma variável: completamente arbitrário
    for num in nomequalquer:
        print(num**2)

# imprimirquadrado(lista1)
# imprimirquadrado(lista2)
# imprimirquadrado(lista3)
# É muito melhor simplesmente chamar a função várias vezes, sem ter que reescrever o código toda vez :D

# Aqui temos alguns exemplos de códigos que levantam erros:

# imprimirquadrado() # A função está preparada para receber um parâmetro, e aqui não passamos nenhum
# imprimirquadrado(lista1, lista2) # Já aqui, passamos mais parâmetros do que a função suporta
# print(nomequalquer) # Essa variável, criada dentro da função, não existe fora do escopo dela

# Função que não recebe nada:
def imprimeoi():
    print("oi galerinha :)")

# imprimeoi()

"""
Essa função acessa uma variável que não foi declarada dentro dela, nem foi passada como parâmetro.
Apesar de ser capaz disso, isso é uma PÉSSIMA prática, pois como mostrado a funcionalidade da função muda
conforme a variável muda, variável essa que não está no seu controle. 
Deve-se evitar ao MÁXIMO esse tipo de prática.
"""

# Função que acessa o que está fora dela:
def imprime_uai():
    print(uai)

uai = 5
# imprime_uai()

uai = True
# imprime_uai()

uai = "Uai sô!"
# imprime_uai()

#########################################################################################

"""
Funções podem receber nenhum, um ou vários parâmetros. 
Da mesma forma podem ou não retornar nada, ou retornar um ou vários objetos!
"""

# Função SEM retorno
def media3num(num1, num2, num3):
    soma = num1 + num2 + num3
    media = soma / 3
    print("Média =", media)

# media3num(5, 10, 15)

# Essa função não RETORNA nada, portanto se tentarmos atribuir sua chamada a uma variável...
# med = media3num(5, 10, 15)
# print(med)

# Função com UM retorno
def media_que_retorna(num1, num2, num3):
    soma = num1 + num2 + num3
    media = soma / 3
    return media

media_que_retorna(1, 10, 15) # Se só chamarmos ela sem salvar em uma variável, seu retorno é perdido 

resultado = media_que_retorna(5,10,15)
# print(resultado)
# print(type(resultado))

# Função com VÁRIOS retornos
def negativo(num1, num2, num3):
    a = num1 * -1
    b = num2 * -1
    c = num3 * -1
    return a, b, c # Essa função retorna TRÊS coisas

# Podemos atribuir sua chamada a uma única variável, e dessa forma seu retorno será uma TUPLA que contém os objetos retornados
neg = negativo(42, 666, 69)
# print(neg)

# Alternativamente, podemos atribuí-la no mesmo número de variáveis que o número de retornos
# Dessa forma cada variável referencia um objeto retornado, SEGUINDO A ORDEM DE LEITURA
x, y, z = negativo(42, 666, 69)
# print(x)
# print(y)
# print(z)

#########################################################################################

"""
Funções possuem várias alternativas para receber parâmetros
Uma delas são os Parâmetros Opcionais, mais conhecidos como Parâmetros Default 
"""

def potencia(base, expoente = 2):
    return base ** expoente

# O usuário pode escolher se quer passar ou não um expoente. Se escolher não passar nada,
# a função utilizará o valor default (padrão) passado na sua definição (nesse caso, 2).
# print(potencia(10))
# print(potencia(10, 5))

#########################################################################################
"""
Parâmetros posicionais X Parâmetros nominais  
Existem duas formas de passar um parâmetro: 
- através da sua posição decidida na definição da função;
- através do seu nome mostrado na definição da função.
"""

def funcaozinha1(num, soma = 1, mult = 2, exp = 3):
    result = num + soma
    result *= mult
    result **= exp
    return result

# Com os parâmetros default, posso passar somente o num
# print(funcaozinha1(5))

# Posso passar os parâmetros de forma posicional, ou seja, da esquerda pra direita
# print(funcaozinha1(5, -1, 10, 2))

# No entanto, se eu quiser passar um certo parâmetro sem passar outro que vem antes dele, preciso passá-lo pelo NOME
# print(funcaozinha1(5, 5, exp = 2)) # Parâmetros nominais

# Também posso passar TODOS os parâmetros de forma nominal
# print(funcaozinha1(num = 5, soma = 5, exp = 2))

# Uma vez que você passa um parâmetro nominal, você abdica de poder usar suas posições. Essa linha dará um ERRO:
# print(funcaozinha1(num = 5, 5, 2))

# Para parâmetros nominais, a ordem em que são passados não importa mais
# print(funcaozinha1(5, exp = 5, soma = 2))

#########################################################################################

"""
Parâmetros de quantidade arbitrária

Podemos definir uma função que recebe qualquer quantidade de parâmetros.
É útil quando não sabemos quantos parâmetros o usuário vai passar, ou quando a função tem mais de uma funcionalidade.
"""

def soma_arbitraria(*numeros):
    # A partir do momento que colocamos um asterisco, a variável numeros se torna uma TUPLA que contém todos os parâmetros passados
    result = 0
    for num in numeros:
        result += num
    
    return result

# Podemos passar qualquer quantidade de números para a função:
# print(soma_arbitraria(1,2,3,4,5,6,7,8,9,10))

# A função sum() do python possui uma funcionalidade parecida, mas ela recebe apenas dois parâmetros:
# Um iterável que CONTÉM os números, e um start opcional. Percebe a diferença?
# print(sum((1,2,3,4,5,6,7,8,9,10)))

numeros = (1,2,3,4,5,6,7,8,9,10)
# print(sum(numeros, 100)) # Esse funciona :)
# print(soma_arbitraria(numeros)) # Esse não :(

###################################################

# Quando temos um parâmetro de quantidade arbitrária, perceba que não conseguimos acessar quaisquer parâmetros
# posteriores de forma posicional, apenas os ANTERIORES. 
# Os parâmetros posteriores só podem ser passados de forma NOMINAL.
def soma2(inicio = 0, *numeros, a=1, b=2):
    for num in numeros:
        inicio += num
    
    return inicio

# print(soma2(-10, 1,2,3,4,5,6,7,8,9,10, a=5, b="biscoito"))

# Por conta disso, é uma boa prática sempre deixar parâmetros multivalorados como sendo o ÚLTIMO PARÂMETRO a ser passado

#########################################################################################

"""
EXTRA: Não vimos o seguinte em monitoria, mas é interessante de se saber :)

List Comprehension
É uma forma de se criar um iterável através de condições em outro iterável. Observe a construção:
nova_lista = [EXPRESSÃO for ELEMENTO in ITERÁVEL if CONDIÇÃO]
"""

# numeros = [0,1,2,3,45,6,7,89,65]

# quad_numeros = []
# for num in numeros:
#     quad_numeros.append(num**2)

# quad_numeros = [x**2 for x in numeros]
# print(quad_numeros)

# string = "Eu adoro a EMAp!"
# lista_da_string = [caractere for caractere in string]
# print(lista_da_string)

# comidas = ["Pizza", "Pastel", "Pão de Queijo", "Pavê", "Pudim"]
# comidas_maiusculas = [elemento.upper for elemento in comidas if "a" in elemento]
# print(comidas_maiusculas)

# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# matriz_achatada = []

# for linha in matriz:
#     for elemento in linha:
#         matriz_achatada.append(elemento)

# /\ Equivalentes \/

# matriz_achatada = [elemento for linha in matriz for elemento in linha]
# print(matriz_achatada)