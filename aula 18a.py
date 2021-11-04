list = []
dados = []
person = []
for c in range(0, 5):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    person.append(int(input('Informe o peso: ')))
list.append(dados[:])
list.append(person[:])
print(list[0], '\n', dados, '\n', person)