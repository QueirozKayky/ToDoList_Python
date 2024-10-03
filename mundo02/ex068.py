"""
Faça um programa que jogue PAR ou IMPAR com o computador, o jogo sera interrompido quando o jogador PERDER. 
mostrando o total das vitorias consecutivas que ele conquistou no final do jogo.    
"""
import random
vitoria = 0

print('-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-'*30)

while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0,10)
    total = jogador + computador
    
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    
    print(f'Você escolheu {jogador} e o Computador escolheu {computador} o numero é {total}')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')    
            vitoria +=1
        else:
            print('Você PERDEU')
            break
    
    
    
    
    
    
    """"if numero_jogador % 2 == 0 and decisao == "P":
        print('Voce escolehu PAR')"""
        
        
        

