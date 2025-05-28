'''
Dicionários
- é uma lista de associações compostas por uma chave "única"
- são mutáveis 
- 

listas= [1,2,3,4]

sintaxe:
listas
dicionario = {'a':( 1, 2, [1,2{1:20, 2:30}]), 'b':2, 'c':3}
'''
# dic = {'nome1': 'beto', 'nome2':'ana','nome3':'vitor'}

# dic['nota'] = 7.80

# tupla= ({2:30})

# # usando esse print para debug
# print(dic)

# #dic = {(1,2,3):'beto'} #pode! tupla é imutavel

# itens= dic.items()
# chaves = dic.keys()
# valores = dic.values()

# print(f'items = {itens}')
# print(f'chaves = {chaves}')
# print(f'valores = {valores}')

# # get

# for i, j in dic.items():
#     print(f'i={i}, j={j}')
'''
for i, j in dic.keys():
    print(f'i={i}, j={j}')

for i, j in dic.values():
    print(f'i={i}, j={j}')

leia o nome de 5 pessoas e armazene em um dicionário

crie um programa para gerar um dicionário com 20 número inteiros, mostre a soma de todos os elementos

'''
# nomes = {}
# for i in range (5):
#     n=int(input(f"Digite 5 nomes {i+1}: "))
#     nomes[i] =n
# print(nomes)

#nomes = {}
# for i in range (5):
#     cpf=input(f"Digite o CPF: "))
#     n=input(f"Digite 5 nomes {i+1}: "))
#     nomes[cpf] =n
# print(nomes)

# from random import randint
# ex2 = {}
# for i in range (20):
#     ex2[i] = randint(1, 50)
# soma = sum(ex2.values())
# print(f'Soma dos numeros do dicionairio= {soma}')


# from random import randint
# ex2 = {}
# soma = 0
# for i in range (20):
#     ex2[i] = randint(1, 50)
#     soma+=ex2.get(i)
# print(f'Soma dos numeros do dicionairio= {soma}')

# # compreensão de listas
# lista = [i**2 for i in range(5)]# -> [0,1,2,3,4,] 
# print(lista)

# for i in [0.2,0.3,0.4,0.5]:
#     pass

# pesquisa como trabalhar com compreensão de listas
#lista2= [x,y for x in range (3) if x > 10/ for y in range(6) if x == y: x+=2]

# print(dic.get('nome1'))

'''
Ex 3- crie um programa para ler o nome, a matrícula e as 4 notas de 5 alunos e armazene em um dicionario = [matricula:nome, notas: [n1,n2,n3.n4]]
as notas podem ser geradas de forma aleatória com o uso de compreensão de listas

alunos = {123: {'beto': [6,5,7,4]}

a) mostrar o aluno com maior média
b) a % de alunos com média maior que 8
c) a % de alunos que estariam reprovados, considerando média < 4
'''

notass=[]
for i in range (5):
        notass.append(i)
        from random import randint
        notas = []
        for _ in range (4):
            notas.append(randint(0,10))
print(notas)
print(notass)


dicf = {}
for i in range (5):
    nomess=input(f"Digite os nomes {i+1}:   ")
    dicf[i]=nomess
print(dicf)

matricular = {[dicf]}
for y in range (5):
    mat=input(f"As matriculas {i+1}:   ")
    matricular[y]=mat
print(matricular)
#dicionairo numero binario vai ser a chave e precisa ser a tupla, tuplas como chaves para usar na prova.