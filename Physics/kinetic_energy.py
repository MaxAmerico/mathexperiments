import math

print('Welcome to kinetic energy solver')

system = input('What system do you use? ft and lb(FB) or kg and m/s(KS)?').upper()
if system == 'FB':
    
    while True:
     lb = float(input('How many pounds does the body weigh?'))
     if lb < 0:
        print('Sorry, the weigh cannot be a negative weigh')
        continue
     else:
        ft = float(input('The body moves yourself how many ft/s?'))
        if ft < 0:
           print('Sorry, but is not allowed negative velocity in classic physics')
        else:
           ke = (lb*(ft**2))/2
           print(f'The kinetic energy of the body is {ke:.2f} joules')
           wish = input('Do you wish calcule other body?(S/N)').upper()
           if wish == 'S':
              continue
           else:
              print('Turning off...')

        break
         
else:
   while True:
      kg = float(input('How many kilograms does the body weigh?'))
      if kg < 0:
         print('Sorry, the weigh cannot be a negative weigh')
         continue
      else:
         ms = float(input('The body moves yourself how many m/s?'))
         if ms < 0:
            print('Sorry, but is not allowed negative velocity in classic physics')
         else:
            ke2 = (kg*(ms**2))/2
            print(f'The kinetic energy of the body is {ke2:.2f} joules')
            wish = input('Do you wish calcule other body?(S/N)').upper()
            if wish == 'S':
               continue
            else:
               print('Turning off...')
            break
