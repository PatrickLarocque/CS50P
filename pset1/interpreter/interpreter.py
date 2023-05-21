''' Python already supports math, whereby you can write code to add, subtract, multiply, or divide values 
and even variables. But let's write a program that enables users to do math, even without knowing Python. '''

# Get input from the user, stripped of leading or trailing white spaces.
user_input = input("Expression: ").strip()

# Seperate the user's expression into 3 variables, seperated after each white space.
left_value, operator, right_value = user_input.split(" ")

# Based on the operator variable, preform the appropriate operation.
match operator:
    case "+":
        print(f"{(float(left_value) + float(right_value)):.1f}")
    case "-":
        print(f"{(float(left_value) - float(right_value)):.1f}")
    case "*":
        print(f"{(float(left_value) * float(right_value)):.1f}")
    case "/":
        print(f"{(float(left_value) / float(right_value)):.1f}")