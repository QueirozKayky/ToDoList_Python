""" 
crie um programa que leia a idade e o sexo de varias pessoas.
a cada pessoa cadastrada o programa devera perguntar se o USUARIO quer ou nao continuar... 
no final mostre. 

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados. 

C) Quantas mulheres tem menos de 20 anos. 
"""


sexof = 0
sexom = 0
idadefm = 0 

continuar = ''

while continuar != "N":
    sexo = str(input("Sexo: ")).upper().strip()[0]
    idade = int(input("Idade: "))
    continuar = str(input("Deseja cadastrar mais alguem? [S/N]: ")).upper().strip()[0]
    
    if sexo == "F" and idade < 20:
        idadefm += 1        
        
    
    
    
    
    
print(f"Tem {idadefm} meninas com menos de 20 anos ")
print("Muito obrigado! Até Mais...")