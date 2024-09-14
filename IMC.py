
funcionarios = ['ana', 'marcos', 'alice', 'pedro', 'sophia', 'bruno', 'melissa']
turno_dia = ['ana', 'marcos', 'alice', 'melissa']
turno_noite = ['pedro', 'sophia', 'bruno']
tem_carro = ['marcos', 'alice', 'bruno', 'melissa']

#lista 1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

#lista 2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

#lista 3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
'''
'''
peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual o sua altura em cm? '))

def IMC():
    IMC = peso / (altura/100)**2
    print(IMC)
    if IMC < 18.5:
        print('MAGREZA')
    elif IMC >= 18.5 <= 24.9:
        print('NORMAL')
    elif IMC >= 25 <= 29.9:
        print('SOBREPESO')
    elif IMC >= 30 <= 39.9:
        print('OBESIDADE')
    else:
        print('OBESIDADE GRAVE')

IMC()


