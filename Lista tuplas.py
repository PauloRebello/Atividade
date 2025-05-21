# 1. Crie uma lista com 5 números inteiros. Imprima o tamanho da lista.
# numerosex1 = [1, 2, 3, 4, 5]
# print("Ex1. Tamanho da lista:", len(numerosex1))
# print(numerosex1 [1])

# # 2. Solicite 5 nomes e imprima cada nome em uma linha.

# nomes = []
# for i in range (5):
#     nome=input("Nomes:  ")
#     nomes.append(nome)
# print("Nomes digitados:  ")
# for nome in nomes:
#     print(nome)


# # 3. Crie uma lista vazia e adicione 3 elementos usando append.

# listavazia = []
# for i in range (3):
#     elementos=input("Digite os elementos:  ")
#     listavazia.append(elementos)
# print("Elementos adicionados:  ")
# print(listavazia)


# # 4. Tupla com dias da semana. Imprima o terceiro dia.
# diasdasemana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
# print(diasdasemana[2])

# # 5. Remover o número 3 da lista
# lista1_5 = [1,2,3,4,5]
# lista1_5.remove(3)
# print(lista1_5)

# 6. Solicite 5 números e mostre o maior e o menor
# listade5numeros = []
# for i in range (5):
#     n6=input("Digite 5 números:   ")
#     listade5numeros.append(n6)
# print("Número maior: ", max(listade5numeros))
# print("Número menor: ", min(listade5numeros))


# 7. Use while para imprimir elementos da lista


# 8. Inserir "vermelho" na posição 1
# listadecores = ["Amarelo","Azul","Verde"]
# listadecores.insert(1,"Vermelho")
# print(listadecores)

# # 9. Ordenar a lista em ordem crescente e decrescente
# listaforadeordem = [6,5,4,7,8,2,9]
# listaforadeordem.sort()
# print("Lista em ordem crescente: ", listaforadeordem)
# listaforadeordem.reverse()
# print("Lista em ordem decrescente: ",listaforadeordem)

# 10. Juntar lista de palavras em string separada por vírgulas
# listadepalavras = ["computador","mouse","teclado"]
# ex10= ", " .join(listadepalavras)
# print(ex10)

# 11. Lista com 10 zeros usando for
# listacomzero = []
# for i in range (10):
#     zero11=0
#     listacomzero.append(zero11)
# print(listacomzero)

#12. Verificar se cada número é maior que 10
# listavazia12 = []
# for i in range (5):
#     n12=int(input("Digite um número: "))
#     if n12 >10:
#         print("Maior que 10")
#     else:
#         print("Menor que 10")
#     listavazia12.append(n12)
# print(listavazia12)


# 14. Lista de frutas com insert no início
listadefrutas = ["maça","banana","uva"]
listadefrutas.insert(0,"Laranja")
print(listadefrutas)




#20. Crie uma lista de 5 letras e converta para uma ´unica string com join.
listadeletras = ["p","a","u","l","o"]
letras= "".join(listadeletras)
print(letras)






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