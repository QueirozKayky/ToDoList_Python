"sequencia d fibonacci"

"Sequencia de Fibonacci é uma sequencia numerica em que cada termo, a partir do terceiro, a soma dos dois termos anteriores"

termo = int(input('Quantos termos você quer ?: '))

t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
cont = 3 
while cont <= termo:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont +=1 
print('FIM')