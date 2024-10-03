"Crie um programa que leia numero inteiros pelo teclado"
"O programa só vai parar quando o usuario digitar o valor 999"
"que a condicao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)."



num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999] para parar: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Voce Digitou {cont} numero e a soma deles foram {soma}')
    
print('-'*30)
print('Acabou')
print('-'*30)


""""n = 0
dig = 0
total = 0

while n != 999:
    n = int(input('digite um valor[digite 999 para parar]: '))
    if n != 999:
        total += n
        dig += 1
print(f'foram digitados \033[31m{dig}\033[m números \n'
      f'e a soma de todos eles é \033[31m{total}\033[m')"""