"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

from datetime import date

nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
print('O atleta tem {} anos.'.format(idade))
if idade < 10:
    print('Classificação: MIRIM')
elif idade < 15:
    print('Classificação: INFANTIL')
elif idade < 20:
    print('Classificação: JÚNIOR')
elif idade < 26:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
