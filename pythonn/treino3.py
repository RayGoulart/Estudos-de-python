# name = 'Rayssa'
# print(f'Olá, {name}!') 

# nome = 'Rayssa Goulart'
# idade = 18
# caracteristicasSigno = 'vingativos'
# signo = 'escorpião'
# print(f'Ela se chama {nome}, possui {idade} anos de idade e seu signo é uns dos mais {caracteristicasSigno} do zoadico, mas conhecido como {signo}')






# menu = int(input('====menu====\n1-cadastrar perguntas e respostas\n2-iniciar jogo\n3- sair do jogo\nEscolha uma opção:'))


# contador = 0


# if menu == 1:
#     while contador < 5:
#         contador = contador + 1
#         pergunta = str(input('cadastre sua pergunta: '))
#         resposta = str(input('cadastre sua resposta: '))
    
# elif menu == 3:
#     print('encerrando jogo...')


menu = int(input('====menu====\n1-cadastrar perguntas e respostas\n2-iniciar jogo\n3- sair do jogo\nEscolha uma opção:'))

def mostrar_menu():
    print('====menu====')
    print('1- cadastrar perguntas e respostas')
    print('2- iniciar jogo')
    print('3- sair do jogo')
    escolha = int(input("escolha uma opção: "))
    return escolha

def limite_escolhas():
    contador = 0
    while contador < 5:
        contador = contador + 1




