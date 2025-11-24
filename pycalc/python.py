#build a calculator
#take input from user
#output two numbers
#write code to do so

def calculator():
    num1 = float(input("Enter first digit: "))
    num2 = float(input("Enter second digit: "))
    op_choice = input("Choose an operator (+, -, *, /): ")

    match op_choice:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 // num2
        case _:
            result = "Invalid operator!"

    print("Sum:", result)

calculator()
