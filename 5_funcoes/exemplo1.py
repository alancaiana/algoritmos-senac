def soma(numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total

def maior(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

########################################################################

lista1 = [2, 14, 11]
lista2 = [2, 14, 11, 5, 1]

print(f"Resultado 1: {soma(lista1)}")
print(f"Resultado 2: {soma(lista2)}")

print(f"Maior: {maior(lista1)}")
print(f"Maior: {maior(lista2)}")

