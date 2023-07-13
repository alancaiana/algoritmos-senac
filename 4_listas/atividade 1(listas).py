numeros = []
par = []
impar = []

for i in range (5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Números digitasdos: ", numeros)
print("Números pares: ", par)
print("Números ímpares:", impar)