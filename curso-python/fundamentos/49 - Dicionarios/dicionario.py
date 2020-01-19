
pessoa = {'nome'   : 'Prof(a). Ana',
          'idade'  : 38,
          'cursos' : ['Inglês','Português']}

type(pessoa)
dir(dict)
len(pessoa)          

pessoa['nome']
pessoa['idade']
pessoa['cursos']

pessoa.keys()
pessoa.values()
pessoa.items()

pessoa.get('idade')
pessoa.get('tags', [])


# Parte II

pessoa = {'nome'   : 'Prof. Alberto',
          'idade'  : 43,
          'cursos' : ['React', 'Python']}

pessoa['idade'] =  44 
pessoa['cursos'].append('Angular')

pessoa['idade'].append('anos')

pessoa