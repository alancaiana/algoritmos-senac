#solicita a nota 1
nota1 = float(input("Digite a nota 1: "))

#solicita a nota 2 
nota2 = float(input("Digite a nota 2: "))

#solicita a nota 3
nota3 = float(input("Digite a nota 3: "))

# a media dos numero
media = (nota1 + nota2 + nota3)/3

#verifica se a media é maior ou igual a 70
aprovado = media >= 60
reprovado = media < 30

if aprovado:
    print("Parabéns, você foi aprovado!")
elif reprovado:
    print("Infelizmente você foi reprovado!")
else:
    print("Você está na 4° avaliação!")