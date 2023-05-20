''' Python already supports math, whereby you can write code to add, subtract, multiply, or divide values 
and even variables. But let's write a program that enables users to do math, even without knowing Python. '''

user_input = input("Expression: ").strip()

left_value, operator, right_value = user_input.split(" ")

match operator:
    case "+":
        print(f"{float(left_value) + float(right_value):.1f}")
    case "-":
        print(f"{float(left_value) - float(right_value):.1f}")
    case "*":
        print(f"{float(left_value) * float(right_value):.1f}")
    case "/":
        print(f"{(float(left_value) / float(right_value)):.1f}")