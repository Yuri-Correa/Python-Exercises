pessoas = {'nome': 'yuri', 'sexo': 'M', 'Idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
'''for v in pessoas.values():
    print(v)'''
'''for k,v in pessoas.items():
    print(f'{k} = {v}')''' 