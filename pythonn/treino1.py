# print(7 + 4)
# print("7" + "4")




# toda variavel é um objeto pro python
# toda variavel recebe algum valor

# nome = input('qual o seu nome?')
# idade = input("qual a sua idade?")
# signo = input("qual o seu signo?")

# print(nome, idade, signo)




# nome = input("Qual o seu nome?")
# print("ola " + nome + "!" + " " + "Seja bem-vinda!" )




# dia = input("Qual o dia do seu aniversario?")
# mes = input("qual o mes do seu aniversario?")
# ano = input("E o ano?")

# print("você nasceu no dia" , dia , "de" , mes , 'de' , ano + '. Correto?')

# A ',' da espaço e o "+" junta as palavras




num1 = int(input("digite o primeiro numero: ")) #tem que usar int para entender que num1 e num2 é um numero.
num2 = int(input("digite o segundo numero: ")) #tudo que esta dentro do parentese roxo, vai ser convertido para numero

resultado = num1 + num2

print("A soma desses numeros é igual a:" , resultado )
print("A soma entre os numeros {} e {} vale {}".format(num1, num2, resultado))