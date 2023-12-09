first = input("Enter first number")                        # This will ask the user to enter second number
Operator = input("Enter opeartor (+, -, *, /, %)")         # This will ask the user to choose arthematic operator
second = input("Enter second number")                      # This will ask the user to enter second number

if Operator == "+":                                                                  # check the operator
    print("The sum of two number is: " + str(int(first) + int(second)))              # Return the addition of two numbers.
elif Operator == "-":                                                                # check the operator
    print("The difference of two number is: " + str(int(first) - int(second)))       # Return the difference of two numbers.
elif Operator == "*":                                                                # check the operator
    print("The product of two number is: " + str(int(first) * int(second)))          # Return the product of two numbers.
elif Operator == "/":                                                                # check the operator
    print("The divison of two number is: " + str(int(first) / int(second)))          # Return the division of two numbers.
elif Operator == "%":                                                                # check the operator
    print("The modules of two number is: " + str(int(first) % int(second)))          # Return the modulus of two numbers.
else:
    print("Invalid Operator")                                                        # Return if entered operator is invalid.
