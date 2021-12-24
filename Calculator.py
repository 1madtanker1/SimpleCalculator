#this calculator can do addition, subtraction, multipulication, and division
#I mainly coded this project because of the if statement practice

num1 = float(input("Enter your first number > "))
op = input("Enter the operator for this equation > ")
num2 = float(input("Enter another number > "))

#If statement
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "x":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
    
