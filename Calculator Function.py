# This program asks the user for two numbers and performs basic arithmetic operations.


def main():
    number = float(input("Enter a number: "))
    squared = number ** 2
    square_root = number ** 0.5
    print(f"Square: {squared}")
    print(f"Square Root: {square_root}")

main()