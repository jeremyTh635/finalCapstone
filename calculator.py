# Import os to delete text files when all is finished.
import os

print("Enter two numbers and perform a calculation on them.")
# State condition to exit loop.
print("\nWhen you've finished enter 00 to exit the calculator.")

# Loop enables user to perform as many calculations as they want.
while True:

# Loop and try/except statement in case user enters string or float.
    while True:
        try:
            number_1 = int(input("\nEnter your first number:\t"))
            break
        except ValueError:
            print("Please enter only a whole number:\t")
            continue
# Enable user to stop entering calculations and move on.
    if number_1 == 00:
        break

    while True:
        try:
            number_2 = int(input("\nEnter another number:\t\t"))
            break    
        except ValueError:
            print("Please only enter a whole number.")
            continue
    if number_2 == 00:
        break

# Instructions for choosing which type of calculation to perform.
    print("\nEnter the letter for the calculation  you want to perform.")
    calculation = input("\nAddition = 'a'\tSubtraction = 's'\tMultiplication   =  'm'\t Division = 'd':\n\n\t")

# if/elif statements for different calculations.
    if calculation == "a" :
        equation = str(number_1) + " + "  + str(number_2)

# Method for printing to file from https://www.askpython.com/python/built-in-methods/python-print-to-file
        print(equation, file=open("equations.txt", 'a'))

# Display result of calculation.
        result = number_1 + number_2
        print(f"\nThe answer is {result}")

    elif calculation == "s":
        equation = str(number_1) + " - " + str(number_2)
        print(equation, file=open("equations.txt", 'a'))
        result = number_1 - number_2
        print(f"\nThe answer is {result}")

    elif calculation == "m":
        equation = str(number_1) + " x " + str(number_2)
        print(equation, file=open("equations.txt", 'a'))
        result = number_1 * number_2
        print(f"\nThe answer is {result}")

    elif calculation == "d":
        equation = str(number_1) + " ÷ " + str(number_2)
        print(equation, file=open("equations.txt", 'a'))
        result = number_1 / number_2
        print(f"\nThe answer is {result}")

# else statement flags invalid entry, enables user to restart calculation.  
    else:
        print("\nOnly enter letters a, s, m, or d:\t")
        continue

# Display user’s calculations and close file.
print("\nHere are your calculations.")
file = open("equations.txt", 'r')
print(file.read())
file.close()

# Invite user to create a new file with variable for filename.
print("Now we're going to make a new file for your next calculations.")
filename = input("\nFirst, give your file a name. Don't forget to type .txt at the end.\n")
file = open(filename, 'w')

# Perform more calculations using procedure as above.
print("\nFirst, let's do some more calculations the same way as before.")

while True:

    while True:
        try:
            number_1 = int(input("\nEnter your first number:\t"))
            break
        except ValueError:
            print("Please enter only a whole number:\t")
            continue
    if number_1 == 00:
        break

    while True:
        try:
            number_2 = int(input("\nEnter another number:\t\t"))
            break    
        except ValueError:
            print("Please only enter a whole number.")
            continue
    if number_2 == 00:
        break

    print("\nEnter the letter for the calculation you want to perform.")
    calculation = input("\nAddition = 'a'\tSubtraction = 's'\tMultiplication   =  'm'\t Division = 'd':\n\n\t")

    if calculation == "a" :
        equation = str(number_1) + " + "  + str(number_2)
        result = number_1 + number_2

# This time programme prints results to file instead of displaying.
        print(f"\n{equation} = {result}", file = open(filename, 'a'))

    elif calculation == "s":
        equation = str(number_1) + " - " + str(number_2)
        result = number_1 - number_2
        print(f"\n{equation} = {result}", file = open(filename, 'a'))

    elif calculation == "m":
        equation = str(number_1) + " x " + str(number_2)
        result = number_1 * number_2
        print(f"\n{equation} = {result}", file = open(filename, 'a'))

    elif calculation == "d":
        equation = str(number_1) + " ÷ " + str(number_2)
        result = number_1 / number_2
        print(f"\n{equation} = {result}", file = open(filename, 'a'))

    else:
        print("\nOnly enter letters a, s, m, or d:\t")
        continue

# Close file to avoid exception when user ties to open it.
file.close()

# Prompt user to open their file.
# While loop and try/except statements to avoid File not Found Error. 
while True:
        try:
            file = open(input("Enter the name of the file you created to see your calculations.\t"))
            print(file.read())
            break
        except FileNotFoundError:
            print("Please enter the filename exactly as you created it.")
        continue

file.close()

# Delete files to provide clean start for next use of app.
os.remove("equations.txt")
os.remove(filename)





    

    
                
              
            
        
            



















        




