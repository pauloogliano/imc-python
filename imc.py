__author__ = 'Damon Kohler <damonkohler@gmail.com>'
__copyright__ = 'Copyright (c) 2009, Google Inc.'
__license__ = 'Apache License, Version 2.0'

import sl4a

droid = sl4a.Android()
droid.ttsSpeak('Olá. Qual o seu nome?')
message = droid.dialogGetInput('Calculador de IMC', 'Qual o seu nome?').result
droid.ttsSpeak(message)
droid.ttsSpeak('Bem vindo ao Calculador de IMC em Python para Android!')

print('=========================')
print('CALCULO DE IMC EM PYTHON PARA ANDROID')
droid.ttsSpeak('Por favor, digite seu peso')
print('=========================')
peso = float(input('Digite seu peso: '))
print('=========================')
droid.ttsSpeak('Agora a sua altura')
altura = float(input('Agora informe sua altura: '))
print('=========================')
alt = altura*altura
imc = peso/alt
imcf = "%.2f"%(imc)
droid.ttsSpeak('Seu IMC é')
droid.ttsSpeak(imcf)
print('IMC: ',imcf)
print('=========================')
if imc < 15:
   droid.ttsSpeak('Extremamente abaixo do peso!')
   print('Extremamente abaixo do peso!')
elif imc >= 15 and imc <= 16:
   droid.ttsSpeak('Gravemente abaixo do peso!')
   print('Gravemente abaixo do peso!')
elif imc > 16 and imc <= 18.5:
   droid.ttsSpeak('Abaixo do peso ideal!')
   print('Abaixo do peso ideal!')
elif imc > 18.5 and imc <= 25:
   droid.ttsSpeak('Faixa de peso ideal!')
   print('Faixa de peso ideal!')
elif imc > 25 and imc <= 30:
   droid.ttsSpeak('Sobrepeso!')
   print('Sobrepeso!')
elif imc > 30 and imc <= 35:
   droid.ttsSpeak('Obesidade grau 1!')
   print('Obesidade grau I!')
elif imc > 35 and imc <= 40:
   droid.ttsSpeak('Obesidade grau 2. Grave!')
   print('Obesidade grau II (grave)!')
else:
   droid.ttsSpeak('Obesidade grau 3. Morbida!')
   print('Obesidade grau III (morbida)!')