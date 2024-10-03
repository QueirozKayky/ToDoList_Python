"""
Crie um programa que leia varios numero inteiros, e no final da execucao, mostre a media entre todos os valores
e qual foi o maior e o menor valor entre eles. O programa deve perguntar se o usuarios quer ou nao continuar digitando os valores. 
"""

resposta = "S"
soma = 0
quantidade = 0
media = 0
maior = 0
menor = 0

while resposta in "Ss":
    numero = int(input("Digite um numero: "))
    soma += numero
    quantidade +=1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    resposta = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
media = soma / quantidade 
print(f"Voce digitou {quantidade} Números e a Média deles foi {media}")
print(f"O maior numero é {maior} e o menor numero é {menor}")
