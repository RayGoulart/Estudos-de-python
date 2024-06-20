# importar módulos 

# import: importa todas as funcionalidades dentro de um modulo
# from: importa apenas as que eu escolher.
#ceil: arredonda o numero para cima
#floor:arredondar para baixo
#random: gera um numero 
# trunc: mostra a porção inteira de um numero sem suas casas decimais
#  função random.choice é chamada passando uma sequência como argumento, e ela retorna um elemento aleatório dessa sequência. 

# import math
# num = int(input("digite um numero: "))
# raiz = math.sqrt(num)
# print(f"A raiz de {num} é igual a {math.ceil(raiz)}")



# from math import sqrt, floor
# num = int(input("digite um numero: "))
# raiz = sqrt(num)
# print(f"A raiz de {num} é igual a {floor(raiz)}")





# desafio 16
# from math import trunc
# num = float(input('digite um numero para saber sua porção inteira: '))

# print(f"A porção inteira do numero {num} vai ser: {trunc(num)}")







# exercicio 17

# catetoOposto = float(input("escreva o valor do cateto oposto: "))

# catetoAdjacente = float(input("escreva o valor do cateto adjacente: "))

# from math import pow, sqrt
# oposto = pow(catetoOposto, 2)

# adjacente = pow(catetoAdjacente, 2)

# soma = oposto + adjacente
# result = sqrt(soma)
# print(f"O valor da hipotenusa é: {round(result, 2)}")







# exercicio 18

# angulo = float(input("digite um angulo para saber o sen, coss e tangente: "))

# from math import radians, sin, cos, tan
# AnguloRadiais = radians(angulo)

# seno = sin(AnguloRadiais)
# cosseno = cos(AnguloRadiais)
# tangente = tan(AnguloRadiais)

# print(f"O seno, cosseno e tangente do numero {angulo}° é igual a:\nseno: {round(seno,2)}\ncosseno: {round(cosseno, 2)}\ntangente: {round(tangente,2)}")






# exercicio 19
# import random
# # from random import choice

# aluno1 = str(input("primeiro aluno: "))
# aluno2 = str(input("segundo aluno: "))
# aluno3 = str(input("terceiro aluno: "))
# aluno4 = str(input("quarto aluno: "))

# lista = [aluno1, aluno2, aluno3, aluno4]

# escolhido = random.choice(lista)

# print(f"O aluno escolhido é: {escolhido}")





# exercicio 20
aluno1 = str(input("primeiro aluno: "))
aluno2 = str(input("segundo aluno: "))
aluno3 = str(input("terceiro aluno: "))
aluno4 = str(input("quarto aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]

from random import shuffle

shuffle(lista)

print(lista)




