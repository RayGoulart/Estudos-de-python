
# orientação a objeto é uma forma de codigficar de forma indireta, exemplo, criar uma classe e depois usar a função dessas classes. É uma forma de simplificar um codigo, usar uma class em outros objetos sem ter que ficar criando as mesmas funções, voce utiliza apenas uma para fazer determinada função. Tambem da de importar essa class. 

# __init__ : a função init inicializa a class
# self: faz referencia a alguma caracteristica do controle remoto

# class ControleRemoto:
#     #função das caracteristicas
#     def __init__(self, cor, altura, profundidade, largura):
#         self.cor = cor
#         self.altura = altura
#         self.profundidade = profundidade
#         self.largura = largura

#         #função de passar o canal do controle
#     def passar_canal(self, botao):
#         if botao == '+':
#             print('aumentar canal')
#         elif botao == '-':
#             print('diminuir canal')


# #duas intancias da classe ControleRemoto
# controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')
# print(controle_remoto.cor)
# controle_remoto.passar_canal('+')

# controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm')
# print(controle_remoto2.cor)
# controle_remoto2.passar_canal('-')












# class vendedor:
#     #atributos
#     def __init__(self, nome, idade, signo):
#         self.nome = nome
#         self.idade = idade
#         self.signo = signo
    
# #metodos
#     def Verificar_metas(self, vendidos, meta):
#         self.vendidos = vendidos
#         self.meta = meta

#         if vendidos > meta:
#             print('Você conseguiu atingir a meta!!')
#         elif vendidos < meta:
#             print('você não conseguiu atingir a meta!!')
    

# nome = str(input('Qual o seu nome? '))
# idade = str(input('Qual a sua idade? '))
# signo = str(input('Qual o seu signo? '))


# #vendedores = objeto ou instancia
# vendedores = vendedor(nome, idade, signo)
# print(f'O nome desse vendedor é {vendedores.nome}')
# print(f'Esse vendedor tem tem {vendedores.idade} anos')
# print(f'O signo dele é: {vendedores.signo}')



# vendidos = int(input('Quantos produtos voce conseguiu vender? '))
# meta = int(input('Qual a sua meta de vendas? '))

# vendedores.Verificar_metas(vendidos, meta)


















# class Vendedor:
#     def __init__(self, nome, idade, signo):
#         self.nome = nome
#         self.idade = idade
#         self.signo = signo
    
#     def verificar_metas(self, vendidos, meta):
#         if vendidos > meta:
#             print(f'{self.nome} conseguiu atingir a meta!!')
#         elif vendidos < meta:
#             print(f'{self.nome} não conseguiu atingir a meta!!')
#         else:
#             print(f'{self.nome} atingiu exatamente a meta!!')

# # Lista para armazenar os vendedores
# vendedores = []

# # Coletar dados e verificar metas para 100 vendedores
# for i in range(100):
#     print(f"\nDigite os dados do vendedor {i+1}:")
#     nome = input('Qual o seu nome? ')
#     idade = input('Qual a sua idade? ')
#     signo = input('Qual o seu signo? ')
    
#     # Criar um objeto Vendedor
#     vendedor = Vendedor(nome, idade, signo)
#     vendedores.append(vendedor)
    
#     # Coletar dados de vendas para o vendedor atual
#     vendidos = int(input('Quantos produtos você conseguiu vender? '))
#     meta = int(input('Qual a sua meta de vendas? '))
    
#     # Verificar metas para o vendedor atual
#     vendedor.verificar_metas(vendidos, meta)








# # vamos criar um site para os clientes da netflix

# class cliente:
#     #atributos
#     def __init__(self, nome, email):
#         self.nome = nome 
#         self.email = email
        
#     #métodos 
#     def PlanoValid_invalid(self, plano):
#         self.lista_planos = ['basic', 'premium']
        
#         if plano in self.lista_planos:
#             self.plano = plano
#             print(f'Plano escolhido: {plano}')
#         else:
#             print(f'erro: o plano {plano} é invalido')

#     def Mudar_plano(self, novo_plano):
#         if novo_plano in self.lista_planos:
#             self.plano = novo_plano
#             print(f'O seu novo plano agora é: {novo_plano}')
#         else:
#             print(f'plano {novo_plano} é invalido!')
    
#     def Ver_filme(self, filme, plano_filme):
#         if self.plano == plano_filme:
#             print(f'Ver filme {filme}')
#         elif self.plano == 'premium':
#             print('Ver filme {filme}')
#         elif self.plano == 'basic' and plano_filme == 'premium':
#             print(f'Você precisa ser premium para conseguir assistir o filme: {filme}. É necessario mudar o plano {self.plano} para premium')
#         else: 
#             print('plano invalido!!')



# #atributos(caracteristicas) do cliente
# cliente1 = cliente('Gustavo', 'gustavo@gmail.com')
# print(f'O nome do cliente é: {cliente1.nome}')
# print(f'O email do cliente {cliente1.nome} é: {cliente1.email}')

# #plano do cliente
# cliente1.PlanoValid_invalid('basic')

# #verfilme
# cliente1.Ver_filme('A Era do Gelo 3', 'premium')

# #mudar plano
# cliente1.Mudar_plano('premium')

# #tentar ver filme com novo plano
# cliente1.Ver_filme('A Era do Gelo 3', 'premium')
        














# class pessoa:
#     def __init__(self, nome, idade, email):
#         self.nome = nome
#         self.idade = idade
#         self.email = email

    
#     def ExibirDados(self):
#         print(f'O nome dessa pessoa é: {self.nome}\n{self.nome} tem {self.idade} anos\nO email cadastrado é: {self.email}')

#     def incrementando_idade(self):
#         self.idade = self.idade + 1 



# pessoa1 = pessoa('Rayssa', 18, 'rayssa2300@gmail.com')
# pessoa1.ExibirDados()
# pessoa1.incrementando_idade()
# pessoa1.ExibirDados()













# class Josue:
#     def __init__(self, nome, data, quilo, meta):
#         self.nome = nome
#         self.data = data
#         self.quilo = quilo
#         self.meta = meta


#     def AvisoPrevio(self):
#         if isinstance(self.quilo, str):
#             print(f'Por favor {self.nome}, digite um numero!')
#         elif self.quilo > self.meta: 
#             self.QntPrecisa = self.quilo - self.meta
#             print(f'{self.nome}, hoje é dia {self.data} e você ainda não atingiu sua meta de {self.meta} quilos. Ainda falta emagrecer {self.QntPrecisa} para atingir o seu objetivo. Mas não desista, sei que você consegue!')   
#         elif self.quilo == self.meta:
#             print(f'Parabens {self.nome}, você atingiu sua meta!')
#         elif self.quilo < self.meta:
#             print(f'O seu quilo esta abaixo de {self.meta}, cuidado para não emagrecer muito!!')
        
    
# nome = str(input('Qual o seu nome? '))
# data = str(input('Que dia é hoje? '))
# quilo = int(input('Quantos quilos você esta atualmente?'))
# meta = int(input('Qual a sua meta de peso a atingir? '))

# jojo = Josue(nome, data, quilo, meta)
# jojo.AvisoPrevio()












# class bola:
#     def __init__(self, cor, circuferencia, material):
#         self.cor = cor
#         self.circuferencia = circuferencia
#         self.material = material 


#     def TrocaCor(self, NovaCor):
#         self.cor = NovaCor
        

#     def MostrarCor(self):
#         return self.cor
    


# cliente1 = bola('verde', 40, 'plastico')
# print(cliente1.MostrarCor())
# cliente1.TrocaCor('rosa')
# print(cliente1.MostrarCor())

        

