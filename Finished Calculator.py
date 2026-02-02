def main():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Select operation (Type Corresponding Number): ").strip().lower()
    if operation in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if operation == '1':
            result = num1 + num2
            print(f"Sum = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"Difference = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"Product = {result}")
        elif operation == '4':
            if num2 == 0:
                print("Error: DIV/0")
            else:
                result = num1 / num2
                print(f"Quotient = {result}")
    else: print("Error: Invalid Operation. Please choose one of the four options above.")


main()
        