from random import *

nombre = input("Name: ")
print(f"Ok, {nombre}, I thought of a number between 0 and 100, you only have 8 tries to guess what this number is, ready?.")

tries = 8
intentos = 1
numguess = randint(1, 100)

# print(numguess)

number = int(input("Give me your number: "))

while numguess != number and tries > 0:

    print(f"Lets try again! You still have {tries} tries!")
    number = int(input("Give me another number: "))

    if number == numguess:
        print(f"Congratulations! You've guessed it in {intentos} tries!")
    elif number < numguess:
        print("Hint: Try a higher number.")
    elif number > numguess:
        print("Hint: Try a lower number. ")
        if tries <= 0:
            print("Its over!")

    tries -= 1
    intentos += 1







