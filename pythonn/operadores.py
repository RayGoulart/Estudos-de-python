#  operadores aritméticos:

#  + soma              
#  - subtração
#  * nultiplicação
#  / divisão 
#  ** potencia
#  // divisão inteira
#  % resto da divisão

# ordem de precedencia:
# 1- ()
# 2- **
# 3- *, /, //, %
# 4- +, -

# exercicio 5
# num = int(input('digite um numero: '))
# s = num + 1
# a = num - 1
# print("O sucessor do numero {} é {} e o antecessor é {}".format(num, s, a ))





# exercicio 6:
# laco = True
# while laco:
#     num = int(input('digite um numero: '))
#     d = num * 2
#     t = num * 3
#     r = num ** (1/2)
#     print('O dobro de {} é {}\nO triplo de {} é {}\nE a raiz quadrada de {} é {}'.format(num, d, num, t, num, r))





# exercico :7
# Nota1 = int(input("digite a primeira nota: "))
# Nota2 = int(input("digite a segunda nota: "))

# média = (Nota1 + Nota2) / 2

# if(média < 6):
#     print("sua média é {}, infelizmente você foi reprovado".format(média))
# elif(média >= 6):
#     print("sua média é {}, parabens!! Você passou!!".format(média))





# exercico 8:
# metros = int(input("digite um valor em metros: "))

# c = metros * 100
# m = metros * 1000

# print('{} metros em centimetros é igual a: {}\nE {} metros em milimetros é: {}'.format(metros, c, metros, m))





# exercicio 9:
# num = int(input("digite um numero para saber a tabuada: "))
# print("A tabuada do numero {} é: \n".format(num))

# for i in range(11):
#     result = num * i
#     print("{}x{}= {}".format(num, i, result))




# exercicio 10:
# num = float(input('Digite uma quantidade de dinheiro em reais para ver quantos dolares pode ser comprado: '))
# taxa_de_cambio = 3.27
# result = num / taxa_de_cambio
# result_arredondado = round(result, 2)
# print("Pode ser comprado {} US$".format(result_arredondado))





# exercicio 11

# largura = float(input("Qual a largura da sua parede? "))
# altura = float(input("qual a altura da sua parede? "))

# area = largura * altura

# print("A area da sua parede é {}".format(area))

# quantidade_de_tinta = area / 2

# print('vão ser necessarios {} litros de tinta para pintar uma area de {}'.format(quantidade_de_tinta, area))





# exercicio 11
# produto = float(input('digite o preço do ferreiro roche: '))
# porcentagem = 5/100
# desconto = produto * porcentagem
# novoPreço = produto - desconto

# print("o novo preço do ferreiro roche, com 5 porcento de desconto é {}".format(novoPreço))






# exercicio 12
laco = True
while laco:
    salario = float(input("Qual o seu salario? "))
    porcentagem = 15/100
    aumento = salario * porcentagem
    novoSalario = salario + aumento
    if(salario > 1 and salario <= 1500):
        print("O seu novo salario, com um aumento de 15 porcento é {}".format(novoSalario))
    else:
        print("ERRO, DIGITE UM NUMERO MAIOR MAZANZA!!")

    continuar = str(input("você ainda deseja continuar o programa?\n1- sim\n2-não\ndigite sua resposta: "))
    if(continuar == 'sim'):
        laco = True
    elif(continuar == 'não'):
        laco = False
        print("encerrando o programa...")
        

   