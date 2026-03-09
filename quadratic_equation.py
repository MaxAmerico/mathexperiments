import math
import cmath
#Functions
def calcule_quadratic(a,b,c):
        delta = (b ** 2) - (4 * a * c)

        if delta < 0:
            #Here I want to set a system which you can see the negative roots
            x1 = (-b - cmath.sqrt(delta)) / (2 * a)
            x2 = (-b + cmath.sqrt(delta)) / (2 * a)
            print(f'The complex roots are: x1 = {x1} and x2 = {x2}')
        else:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print(f"The roots are: x1 = {x1} and x2 = {x2}")


def main_code():
      while True:
        a = float(input("What is the value of A?: "))
        b = float(input("What is the value of B?: "))
        c = float(input("What is the value of C?: "))
   
        r = calcule_quadratic(a, b, c)
           
        question = input("Do you want to calculate other equations? (Y/N) ").upper()
        if question == 'Y':
             continue
        else:
             break
        
          
            
#Finish of functions
            
#Start of the code        

print("Here is the quadratic equation model below:")
print("ax² + bx + c = 0")
print("Please replace the values above with the ones from your problem right after the prompt.")

code = main_code()




