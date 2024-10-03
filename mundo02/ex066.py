"""
Crie um programa que leia varios numero inteiros,
o programa só vai parar quando o usuario digitar o valor "999"
que é a condição de parada.
no final, mostre quantos numeros foram digitados e qual foi a soma entre eles. (desconsiderando o flag)
"""
numero = 0 
soma = 0
quantidade = 0 

print("Caso Queira Parar, Digite [999]")

while numero != 999:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    quantidade += 1
    soma += numero
print(f'A soma dos {quantidade} Números é {soma}')        


