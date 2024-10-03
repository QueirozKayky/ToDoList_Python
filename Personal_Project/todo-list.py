#Aqui é o inicio para uma lista de tarefas. 

tasks = []
answer = 'Y'

while answer != 'N':
    
    tasks_user = input('what is your tasks today ? : ')
    tasks.append(tasks_user)
    answer = str(input("Do you want add other task? [Y/N]: ")).upper().split()[0]
       
    print('-'*30)
    print(tasks)
    print('-'*30)

#verifica se o usuario quer remover alguma tarefa
remove_task = input('Do you want to remove some task? [Y/N] : ').upper().split()[0]
if remove_task == 'Y':
    print('-' * 30)
    print('Which one? Here are your current tasks:')
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    print('-' * 30)

# Solicitar o número da tarefa a ser removida
try:
    task_number = int(input('Enter the task number to remove: ')) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task}' has been removed.")
    else:
        print("Invalid task number!")
except ValueError:
    print("Please enter a valid number.")

# Mostrar a lista final de tarefas
print('-' * 30)
print("Final list of tasks:", tasks)
print('-' * 30)