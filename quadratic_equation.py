import math

print("Here is the quadratic equation model below:")
print("ax² + bx + c = 0")
print("Please replace the values above with the ones from your problem right after the prompt.")
proceed = input("Can we proceed? (Y/N) ").upper()

if proceed == "N":
    print("Restart the program if you change your mind.")

else:
    while True:
        a = float(input("What is the value of A? "))
        b = float(input("What is the value of B? "))
        c = float(input("What is the value of C? "))

        delta = (b ** 2) - (4 * a * c)

        if delta < 0:
            #Here I want to set a system which you can see the negative roots
            print("Negative discriminant, there are no real roots.")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            print(f"The roots are: x1 = {x2} and x2 = {x1}")

        question = input("Do you want to calculate other equations? (Y/N) ").upper()
        if question == "N":
            break
        else:
            print("- - -")


