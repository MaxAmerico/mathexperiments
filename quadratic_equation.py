import math

print('Segue o modelo da equação de segundo grau abaixo:')
print('ax²+bx+c=0')
print('Por favor, troque os valores acima pelos valores que está em sua questão logo depois da pergunta')
prossiga = input('Podemos prosseguir?(S/N)').upper()
if prossiga == 'N':
    print('Reinicie seu programa caso tenha mudado de ideia')

else:
  while True:
    a = float(input('Qual é o valor do A?'))
    b = float(input('Qual é o valor do B?'))
    c = float(input('Qual é o valor do C?'))

    delta = (b**2) - (4*a*c)
    if delta <0:
           print('Delta negativo, não há raízes reais')
    else:       
       

        bhaskaramais = (-b + math.sqrt(delta)) / (2*a)
        bhaskaramenos = (-b - math.sqrt(delta)) / (2*a)
        
        print(f'Os resultados da raiz são: x1 = {bhaskaramenos} e x2 = {bhaskaramais}')

    pergunta = input('Você deseja calcular outras equações?(S/N)').upper()
    if pergunta == 'N':
        break
    else:
       print('- - -')
