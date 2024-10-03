import pandas as pd

pessoa = {
    'Nome' : ['Kayky', 'Gabrielly', 'Silas', 'João Vitor', 'Noah', 'Lohann'],
    'Sexo' : ['M', 'F', 'M', 'M', 'M', 'M'],
    'Idade' : [20, 20, 25, 26, 3, 1],
    'Cidade' : ['SJC','SJC','Paraibuna','SJC','SJC','SJC' ]
}

pessoainfo = pd.DataFrame(pessoa)
print(pessoainfo)


