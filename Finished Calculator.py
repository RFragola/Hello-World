def main():
    print("")
    print("Welcome to Grandpa Roob's Calculator!")
    print("")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("")
    operation = input("Input corresponding number: ").strip().lower()
    if operation in ['1', '2', '3', '4']:
        print("")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if operation == '1':
            result = num1 + num2
            print(f"Sum = {result}")
            endmsg()
        elif operation == '2':
            result = num1 - num2
            print(f"Difference = {result}")
            endmsg()
        elif operation == '3':
            result = num1 * num2
            print(f"Product = {result}")
            endmsg()
        elif operation == '4':
            if num2 == 0:
                print("")
                print("Error: DIV/0")
                print("Restarting Calculator...")
                print("")
                main()
            else:
                result = num1 / num2
                print(f"Quotient = {result}")
                endmsg()
    else: 
        print("")
        print("Error: Invalid Operation. Please choose one of the four options provided.")
        print("Restarting Calculator...")
        print("")
        main()

def endmsg():
    print("")
    print("Thank you for using Grandpa Roob's Calculator!")
    print("Click here for mac and cheese: https://streamable.com/lf027o")
    print("")

main()
        