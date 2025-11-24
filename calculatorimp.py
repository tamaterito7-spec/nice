# calculator 
# ask user for two numbers
# input value into variables
# store user operator choice
# use operator choice between selected numbers

num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter another number: "))

choice = input("Please enter 1, 2, 3, 4 (+, -, *, /): ")

if choice in ["1", "+"]:
	print(num1 + num2)

elif choice in ["2", "-"]:
	print(num1 - num2)
	
elif choice in ["3", "*"]:
	print(num1 * num2)
	
elif choice in ["4", "/"]:
	print(num1 // num2)

