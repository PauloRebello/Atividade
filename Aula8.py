lista = [1,2,3,4,5]
#map, filter, reduce
quadrado = [num**2 for num in lista]

pares = [x for x in lista if x % 2 == 0]
print(pares)
print(quadrado)

if True:
    x=10

def soma(x,y):
    return x + y
    # resultado = x + y
    # print(resultado)
    # #print(x + y)
    # return resultado


resultado = soma (2,4)
# soma(soma(1,3))
soma(2,5)
soma(2,4)
soma(3,3)
print(resultado)

def soma(a,b):
    return a+b
resultado = soma (8,18)
print(resultado)

def sub(a,b):
    return a-b
resultado = sub (6,10)
print(resultado)

def mult(a,b):
    return a*b
resultado = mult (6,10)
print(resultado)


def div(a,b):
    return a/b
resultado = div (6,10)
print(resultado)