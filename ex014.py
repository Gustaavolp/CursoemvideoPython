# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
c = float(input('Informe a temperatura em °C: '))
print('A temperatura de {}°C corresponde a {}°F!'.format(c, ((c * 9) / 5) + 32))
