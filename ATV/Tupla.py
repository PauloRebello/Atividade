#1. Crie uma lista com 5 números inteiros. Imprima o tamanho da lista.
numerosex1 = [1, 2, 3, 4, 5]
print("Ex1. Tamanho da lista:", len(numerosex1))
print(numerosex1 [1])

# 2. Solicite 5 nomes e imprima cada nome em uma linha.

nomes = []
for i in range (5):
    nome=input("Nomes:  ")
    nomes.append(nome)
print("Nomes digitados:  ")
for nome in nomes:
    print(nome)


# 3. Crie uma lista vazia e adicione 3 elementos usando append.

listavazia = []
for i in range (3):
    elementos=input("Digite os elementos:  ")
    listavazia.append(elementos)
print("Elementos adicionados:  ")
print(listavazia)


# 4. Tupla com dias da semana. Imprima o terceiro dia.
diasdasemana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
print(diasdasemana[2])

# 5. Remover o número 3 da lista
lista1_5 = [1,2,3,4,5]
lista1_5.remove(3)
print(lista1_5)

#6. Solicite 5 números e mostre o maior e o menor
listade5numeros = []
for i in range (5):
    n6=input("Digite 5 números:   ")
    listade5numeros.append(n6)
print("Número maior: ", max(listade5numeros))
print("Número menor: ", min(listade5numeros))


#7. Use while para imprimir elementos da lista


#8. Inserir "vermelho" na posição 1
listadecores = ["Amarelo","Azul","Verde"]
listadecores.insert(1,"Vermelho")
print(listadecores)

# 9. Ordenar a lista em ordem crescente e decrescente
listaforadeordem = [6,5,4,7,8,2,9]
listaforadeordem.sort()
print("Lista em ordem crescente: ", listaforadeordem)
listaforadeordem.reverse()
print("Lista em ordem decrescente: ",listaforadeordem)

#10. Juntar lista de palavras em string separada por vírgulas
listadepalavras = ["computador","mouse","teclado"]
ex10= ", " .join(listadepalavras)
print(ex10)

#11. Lista com 10 zeros usando for
listacomzero = []
for i in range (10):
    zero11=0
    listacomzero.append(zero11)
print(listacomzero)

#12. Verificar se cada número é maior que 10
listavazia12 = []
for i in range (5):
    n12=int(input("Digite um número: "))
    if n12 >10:
        print("Maior que 10")
    else:
        print("Menor que 10")
    listavazia12.append(n12)
print(listavazia12)


#13. Crie uma lista com os n´umeros de 1 a 10 usando range() e imprima somente os pares
lista= []
for i in range (1,11):
    lista.append(i)
for numero in lista:
    if numero %2 ==0:
        print(numero)

#14. Lista de frutas com insert no início
listadefrutas = ["maça","banana","uva"]
listadefrutas.insert(0,"Laranja")
print(listadefrutas)

#15Dada a lista ["A", "B", "C"], use pop para remover e imprimir o ´ultimo elemento.
lista15=["A", "B", "C"]
ultimo=lista15.pop()
print(ultimo)


#20. Crie uma lista de 5 letras e converta para uma ´unica string com join.
listadeletras = ["p","a","u","l","o"]
letras= "".join(listadeletras)
print(letras)

#21. Solicite ao usu´ario 10 n´umeros, armazene em uma lista e remova todos os n´umeros pares usando remove.
lista20 = []
for i in range (10):
    n21=int(input("Digite dez numeros:  "))
    lista20.append(n21)
    for n22 in lista20[:]:
        if n22 %2 ==0:
            lista20.remove(n22)
print(lista20)


#Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a ordem.
lista22 = ["Paulo","Vitor","Paulo", "Joao", "Miguel", "Vitor"]
listaf= []
for nome in lista22[:]:
    if nome not in listaf:
        listaf.append(nome)
print(listaf)




# Criando a lista
lista = [10, 20, 30, 40, 50]
# Substituindo o segundo elemento (índice 1) por 99
lista[1] = 99
print(lista)


17
# Criando a lista de 5 números
numeros = [10, 20, 30, 40, 50]
# Inicializando a variável para somar os números
soma = 0

# Usando o laço for para somar os números
for numero in numeros:
    soma += numero

# Calculando a média
media = soma / len(numeros)
print(f'Média: {media}')

# 18 Lista fornecida
lista = [3, 6, 9, 12]
# Verificando se o número 7 está na lista
if 7 in lista:
    print("O número 7 está na lista.")
else:
    print("O número 7 não está na lista.")

# 19 Criando uma lista para armazenar os nomes
nomes = []

# Loop para solicitar nomes
while True:
    nome = input("Digite um nome (ou 'sair' para terminar): ")
    if nome.lower() == 'sair':
        break
    nomes.append(nome)

# Imprimindo a lista de nomes
print("Lista de nomes:", nomes)

#20 Criando a lista de 5 letras
letras = ['a', 'b', 'c', 'd', 'e']
# Usando join para transformar a lista em uma única string
resultado = ''.join(letras)
print(resultado)




#30. Dada uma lista de strings, crie uma nova lista com o tamanho (numero de caracteres) de cada string.
def tamanhos_strings(lista_strings):
    return [len(s) for s in lista_strings]

#teste
strings = ["pc", "cadeira", "ram", "monitor"]
tamanhos = tamanhos_strings(strings)
print(tamanhos) 


#36 Crie uma funcao que retorne o segundo maior numero de uma lista
def segundo_maior(lista):
    if len(lista) < 2:
        return None  

    lista_unica = list(set(lista))

    if len(lista_unica) < 2:
        return None  

    lista_unica.sort(reverse=True)  
    return lista_unica[1]  


#34  Faca um programa que leia numeros do usuario ate digitar -1. Depois, imprima a media.
def calcular_media():
    numeros = []
    
    while True:
        try:
            numero = float(input("Digite um número (-1 para encerrar): "))
            if numero == -1:
                break
            numeros.append(numero)
        except ValueError:
            print("Digite um número válido.")

    if numeros:
        media = sum(numeros) / len(numeros)
        print(f"A média dos números digitados é: {media:.2f}")
    else:
        print("Não digitou número.")

calcular_media()

#revisar



# # 2. Solicite 5 nomes e imprima cada nome em uma linha.
# nomes = []
# print("\n2. Digite 5 nomes:")
# for _ in range(5):
#     nome = input("Nome: ")
#     nomes.append(nome)
# print("Nomes digitados:")
# for nome in nomes:
#     print(nome)

# # 3. Crie uma lista vazia e adicione 3 elementos usando append.
# lista_vazia = []
# lista_vazia.append("um")
# lista_vazia.append("dois")
# lista_vazia.append("três")
# print("\n3. Lista após append:", lista_vazia)

# # 4. Tupla com dias da semana. Imprima o terceiro dia.
# dias_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
# print("\n4. Terceiro dia da semana:", dias_semana[2])

# # 5. Remover o número 3 da lista
# numeros2 = [1, 2, 3, 4, 5]
# numeros2.remove(3)
# print("\n5. Lista após remover 3:", numeros2)

# # 6. Solicite 5 números e mostre o maior e o menor
# numeros3 = []
# print("\n6. Digite 5 números:")
# for _ in range(5):
#     n = int(input("Número: "))
#     numeros3.append(n)
# print("Maior número:", max(numeros3))
# print("Menor número:", min(numeros3))

# # 7. Use while para imprimir elementos da lista
# lista_while = [10, 20, 30, 40, 50]
# print("\n7. Elementos da lista com while:")
# i = 0
# while i < len(lista_while):
#     print(lista_while[i])
#     i += 1

# # 8. Inserir "vermelho" na posição 1
# cores = ["azul", "verde", "amarelo"]
# cores.insert(1, "vermelho")
# print("\n8. Lista de cores com vermelho na posição 1:", cores)

# # 9. Ordenar a lista em ordem crescente e decrescente
# lista_ordenar = [3, 1, 4, 1, 5, 9]
# lista_ordenar.sort()
# print("\n9. Ordem crescente:", lista_ordenar)
# lista_ordenar.sort(reverse=True)
# print("Ordem decrescente:", lista_ordenar)

# # 10. Juntar lista de palavras em string separada por vírgulas
# palavras = ["maçã", "banana", "uva"]
# frase = ", ".join(palavras)
# print("\n10. Frase unida por vírgulas:", frase)

# # 11. Lista com 10 zeros usando for
# zeros = []
# for _ in range(10):
#     zeros.append(0)
# print("\n11. Lista com 10 zeros:", zeros)

# # 12. Verificar se cada número é maior que 10
# print("\n12. Verifique se os números são maiores que 10:")
# for _ in range(5):
#     num = int(input("Digite um número: "))
#     if num > 10:
#         print(f"{num} é maior que 10")
#     else:
#         print(f"{num} não é maior que 10")

# # 13. Lista de 1 a 10 e imprimir apenas os pares
# numeros4 = list(range(1, 11))
# pares = [n for n in numeros4 if n % 2 == 0]
# print("\n13. Números pares de 1 a 10:", pares)

# # 14. Lista de frutas com insert no início
# frutas = ["maçã", "banana", "laranja"]
# frutas.insert(0, "morango")
# print("\n14. Lista de frutas após insert:", frutas)

# # 15. Remover e imprimir o último elemento com pop
# letras = ["A", "B", "C"]
# removido = letras.pop()
# print("\n15. Elemento removido com pop:", removido)
# print("Lista restante:", letras)