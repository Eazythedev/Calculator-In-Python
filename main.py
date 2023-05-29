import math

def main():
    print("This is Dat Calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("That ain't a valid input. Please enter a valid number.")
            continue
        
        operation = input("Enter the operation (+, -, *, /, %): ")
        
        if operation in ('+', '-', '*', '/'):
            try:
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("That ain't a valid input. Please enter a valid number.")
                continue
        
        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif operation == '%':
            if num1.is_integer() and num2.is_integer():
                print(f"{int(num1)} % {int(num2)} = {int(num1) % int(num2)}")
            else:
                print("Error: Modulus operation requires integer operands.")
        else:
            print("Invalid operation. Please enter a valid operation.")
        
        choice = input("Do you want to perform another calculation? (y/n): ")
        
        if choice.lower() != 'y':
            break
    
    print("Ok, peace!")

if __name__ == '__main__':
    main()
