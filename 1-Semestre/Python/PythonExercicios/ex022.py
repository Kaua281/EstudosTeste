frase = str(input('Digite seu nome:')).strip()
print('Analizando seu nome...')
print('Seu nome em maiscúlas é {}'.format(frase.upper()))
print('Seu nome em minúsculas é {}'.format(frase.lower()))
print('Seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))
dividida = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividida[0] , len(dividida[0])))