#Verificar se um número é par ou ímpar: Neste exercício, você deve desenvolver um programa que recebe um número como entrada e determina se ele é par ou ímpar.
numero = int(input( 'me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print("o numero {} e par".format(numero))
else:
    print('o numero {} e impar'.format(numero))

