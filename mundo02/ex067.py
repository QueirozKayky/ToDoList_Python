"""
Faça um programa que mostre a tabuada de varios numeros um de cada vez, para cada valor digitado pelo usuario.
o programa sera interrompido quando o numero solicitado for negativo. 
"""
print("-------------------TABUADA-------------------")


while True:
    num = int(input('Digite um numero para sua tabuada: '))
    print('-'*30)
    if num < 0:
        print('[ERRO] não pode ter tabuada negativa.')
        break
    for c in range(1, 11):
        contador = 0
        contador += c 
        calc = num * contador
        print(f'{num} x {contador} = {calc}')
    print('-'*30)
    