def calculator():
    print("Welcome to the calculator.") #Welcomes the user to the Calculator in Terminal/Interactive Window

    while True:
        try:
            num1 = float(input("Enter the first number: ")) #Asks user for first input value
            operator = input("Choose an operator (+, -, *, /): ") #Asks user operator
            num2 = float(input("Enter the second number: ")) #Asks user for second input value

            if operator == '+': 
                result = num1 + num2 #Runs this line if the user wants to add the numbers
            elif operator == '-':
                result = num1 - num2 #Runs this line if the user wants to subtract the numbers
            elif operator == '*':
                result = num1 * num2 #Runs this line if the user wants to multiply the numbers
            elif operator == '/': 
                if num2 == 0:
                    print("You tried to divide by zero. Invalid.") #Since a number cannot be divided by zero, the calculator produces a error message when the user inputs 0 as a value when dividing
                    continue
                result = num1 / num2 #Runs this line if the user wants to divide the numbers
            else:
                print("Invalid operator. Try again.") #Prints this if the user asks with a operator that is not +,-,*, or /
                continue

            print(f"The result is: {result}") #Prints the result of whatever operation is performed

        except ValueError:
            print("That’s not a number. Try again.") #When user inputs something that is not a number in the first and third inputs

        cont = input("Do you want to calculate something else? (yes/no): ").lower() #Asks the user if they want to calculate anything else, returns the value even if the user uses uppercase or random casing
        if cont != 'yes':
            print("Goodbye.") #Prints if the user does not want to further calculate
            break #Ends the function to avoid looping

calculator() #Runs the function defined above