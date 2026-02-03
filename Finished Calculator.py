import time

def slow_print(text, delay=0.3):
    print(text)
    time.sleep(delay)

def slower_print(text, delay=1.0):
    print(text)
    time.sleep(delay)


def main():
    print("")
    slow_print("Welcome to Grandpa Roob's Calculator!")
    print("")
    slow_print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    slow_print("")
    operation = input("Input corresponding number: ").strip().lower()
    if operation in ['1', '2', '3', '4']:
        print("")
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("")
            slow_print("Error: Invalid Input. Please input a number")
            slower_print("Restarting Calculator...")
            print("")
            return main()
        if operation == '1':
            result = num1 + num2
            slow_print(f"Sum = {result}")
            endmsg()
        elif operation == '2':
            result = num1 - num2
            slow_print(f"Difference = {result}")
            endmsg()
        elif operation == '3':
            result = num1 * num2
            slow_print(f"Product = {result}")
            endmsg()
        elif operation == '4':
            if num2 == 0:
                print("")
                slow_print("Error: DIV/0")
                slower_print("Restarting Calculator...")
                print("")
                while True:
                    main()
            else:
                result = num1 / num2
                slow_print(f"Quotient = {result}")
                endmsg()
    else: 
        print("")
        slow_print("Error: Invalid Operation. Please choose one of the four options provided.")
        slower_print("Restarting Calculator...")
        print("")
        while True:
            main()

def endmsg():
    print("")
    slow_print("Thank you for using Grandpa Roob's Calculator!")
    slower_print("Click here for mac and cheese: https://streamable.com/lf027o")
    print("")

main()
        