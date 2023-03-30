# Primeira monitoria de Python, do dia 24 de março
# Descomente as linhas de print() para ver o resultado no terminal.

"""
Importando bibliotecas em Python
Por convenção, sempre colocamos as linhas de importação de bibliotecas e módulos no começo dos arquivos!
Temos várias formas de importação em python, sendo algumas delas:
"""

import math # Importa uma biblioteca inteira, de forma que tudo utilizado dela deve levar seu nome como prefixo, como na linha 15
import math as ma # Igual ao anterior, mas usa um apelido como prefixo, ao invés do nome completo
from math import sqrt # Importa uma função, variável ou classe pelo nome INDIVIDUALMENTE, tirando a necessidade do prefixo
from math import * # Muito cuidado! Essa linha importa todo o conteúdo de uma biblioteca individualmente. Evite ao máximo!!! 

raiz_quadrada_1 = math.sqrt(1)
raiz_quadrada_2 = ma.sqrt(4)
raiz_quadrada_3 = sqrt(9)

# print(raiz_quadrada_1, raiz_quadrada_2, raiz_quadrada_3)

# Caso tenhamos arquivos python no mesmo diretório, podemos importar várias coisas de um para o outro, até mesmo variáveis!
import primeiro2 as p2 

# print(p2.variavel_para_importar)

#################################################################################

""" 
Operadores Matemáticos
Temos 6 operadores matemáticos principais:
+ Soma
- Subtração
* Multiplicação
/ Divisão
** Potência
% Resto
"""

x = 5
y = 10.0

# print(5 + x / y * 2 ** 2) 
# print(x % y)

# Repare que o python tenta seguir uma ordem de leitura (da esquerda pra direita),
# mas dá prioridade para os tipos de operação! (Potenciação > Multiplicação > Adição)

##############################################################################

"""
Multi-atribuição
Conseguimos usar a vírgula para atribuir múltiplas variáveis numa única linha, o que 
essencialmente dá na mesma que atribuir uma por vez. 
"""

a, b, c = 1, 2, 3

# print(c, b, a)

# Se atente à ordem de atribuição!
# É inútil, para atribuir valores iguais, tentar escrever algo como: 
# a, b, c = 1
# Essa linha levanta um erro, pois é necessário passar três valores para três variáveis

####################################################################################

"""
Operadores Ternários
Temos operadores que representam uma COMPARAÇÃO de valores:

> Maior que
< Menor que
>= Maior OU igual
<= Menor OU igual
== Igual
!= Diferente

Uma operação escrita com tais operadores retorna um objeto da classe Bool (True ou False)
de acordo com a validez da operação. E como objeto, ela pode ser atribuída a uma variável!
"""
z = 5
booleano = y < z

# print(booleano)

booleano = x == z

# print(booleano)

###################################################################

"""
Tipos e a função print()
Ao longo desse programa, criamos várias variáveis, mas o que diferencia elas uma da outra?
O que faz de Python uma linguagem FORTEMENTE TIPADA?
O que mais podemos fazer com a função print? E qual o poder das strings?
"""

# Vamos perguntar ao python qual a classe de algumas variáveis, utilizando a função type()

# print(type(a))
# print(type(y))
# print(type(booleano))
# print(type(p2.variavel_para_importar))

primeiro_nome = "George"
sobrenome = "Dutra"
idade = 19

# Podemos pedir para a função print() imprimir várias coisas, separando-as por vírgula:

# print("Meu nome completo é:", primeiro_nome, sobrenome, "e minha idade é:", idade)
# print("Ei, isso está na linha de baixo!\n")

"""
Perceba também que a função print automaticamente coloca um espaço entre cada impressão, e quando 
ela termina todas, pula uma linha automaticamente também. Isso não é mágica, são apenas os argumentos
pré-definidos sep e end! Chamamos esses argumentos de argumento default,
e nesse caso específico, precisamos chamar o argumento pelo nome para modificá-lo:
"""

# print("Meu nome completo é:", primeiro_nome, sobrenome, "e minha idade é:", idade, sep = "[:D]", end = " Ei, onde estão meus espaços!? ")
# print("Ei, isso NÃO está na linha de baixo!")

# É meio chato passar um argumento por vez não é? Pois bem, vou mostrar um SUPER-PODER da classe str:
f_string = f"Meu nome completo é {primeiro_nome} {sobrenome} e minha idade é {idade} anos!"

# print(f_string)

"""
Essa é uma string formatada, criada ao colocar um f antes da aspa inicial. Dentro dela, ao abrir chaves,
você pode passar variáveis que serão interpretadas como parte da string! E afinal, ela deixa de ser uma string?
"""

# print(type(f_string))

"""
A resposta é não, a string formatada nada mais é que um método da própria classe string. Classes em python são
carregadas de métodos, atributos, e características que fazem delas muito mais poderosas e complexas que em 
outras linguagens (e também mais pesadas!). Por isso dizemos que python é FORTEMENTE TIPADA.
"""
# Bônus: Para saber tudo que uma classe é capaz de fazer, use o método oculto __dir__():

# print(f_string.__dir__())






