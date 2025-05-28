for i in (1, 2, 10, 4, 5, 6, 7, 8, 9):
    print(i)




#21. Solicite ao usu´ario 10 n´umeros, armazene em uma lista e remova todos os n´umeros pares usando remove.

lista21 = []
for i in range (10):
    n21=int(input("Digite dez números:   "))
    lista21.append(n21)
    if n21 %2 ==0:
        lista21.remove(n21)
print(lista21)