# manipulando texto(string)

# exercico 22
# nome = str(input("Digite o seu nome completo: ")).strip()

# print(f"Seu nome completo em letra maiuscula: {nome.upper()}\nSeu nome completo em letra minuscula: {nome.lower()}\nletras ao todo sem contar os espaços: {len(nome)-nome.count(' ')}\nQuantidade de Letras do primeiro nome: {(nome.find(' '))}")

# # ou

# separado = nome.split()
# print(f'quantidade de letras do primeiro nome: {len(separado[0])}')









# exercicio 23

# numero = int(input('Digite um numero de 1 a 9999: '))
# if numero > 9999:
#     print('digite um numero menor!!!!!')
# elif numero >= 100 and numero < 1000:
#     num = str(numero)
#     print(f'O numero {numero} separado:\ncentena: {num[0:1]}\ndezena: {num[1:2]}\nunidade: {num[2:3]}')
# elif numero >= 0 and numero <=99:
#     num = str(numero)
#     print(f'O numero {numero} separado:\ndezena: {num[0:1]}\nunidade: {num[1:2]}')
# elif numero >= 1000 and numero <=9999:
#     num = str(numero)
#     print(f'O numero {numero} separado:\nmilhar: {num[0:1]}\ncentena: {num[1:2]}\ndezena: {num[2:3]}\nunidade: {num[3:4]}')


# ou


# laco = True
# while laco:
#     numero = int(input('Digite um número entre 1 e 9999: '))
#     if numero < 1 or numero > 9999:
#         print('Digite um número entre 1 e 9999!')
#     else:
#         num = str(numero).zfill(4)  # Garante que todos os números tenham 4 dígitos
#         print(f'O número {numero} separado de acordo com unidade, dezena, centena e milhar:')
#         print(f'Milhar: {num[0]}')
#         print(f'Centena: {num[1]}')
#         print(f'Dezena: {num[2]}')
#         print(f'Unidade: {num[3]}')
#         laco = False  # Sai do loop



# OU
#utilizando matematica e trabalhando com int




# numero = int(input('digite um numero entre 1 e 9999: '))
# u = numero // 1 % 10 # % mostra o resto 
# d = numero // 10 % 10
# c = numero // 100 % 10
# m = numero // 1000 % 10

# print(f'milhar: {m}\ncentena: {c}\ndezena: {d}\nunidade: {u}')






# exercicio 24
# cidade = str(input('digite o nome de uma cidade: ')).split()

# if cidade[0] == 'santo':
#     print('Essa cidade começa com SANTO')
# else:
#     print('nao começa com SANTO')

# ou

# cidade = str(input('Digite o nome da sua cidade: ')).strip()

# print(cidade[0:5].upper() == 'SANTO')







# exercicio 25
# nome = str(input('Digite o seu nome: ')).upper()

# if 'SILVA' in nome:
#     print('O seu nome contem silva')
# else:
#     print('o seu nome nao contem silva')





# frase = str(input('Escreva uma frase: '))

# fraseSemEspacos = frase.replace(' ', '') #está substituindo todas as ocorrências de espaços na string frase por uma    string vazia '', ou seja, está removendo todos os espaços da string original.
# qtd = fraseSemEspacos.count('a')
# posicaoP = fraseSemEspacos.find('a')
# posicaoU = fraseSemEspacos.rfind('a')

# print(f'A letra (a) aparece {qtd} vezes')
# print(f'A primeira letra (a) esta na posição {posicaoP}')
# print(f'A ultima letra (a) esta na posição {posicaoU}')

