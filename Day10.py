import os
from Day10c import logo  

def clear():
    os.system('clear') 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Division by zero"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear()  # Clear the screen before starting
    
    print(logo)  # Print logo
    
    num1 = float(input("What is the first number? "))  # Get first number from user
    
    while True:
        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        
        if operation_symbol in operations:
            num2 = float(input("What's the next number? "))
            
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            
            print(f"{num1} {operation_symbol} {num2} = {answer}")
            
            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() != 'y':
                clear()
                break  
            else:
                num1 = answer  # Update num1 for further calculations
        else:
            print("Invalid operation symbol. Please choose a valid operation.")


calculator()
