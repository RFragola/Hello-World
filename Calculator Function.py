# This program asks the user for two numbers and performs basic arithmetic operations.


def main():
    number = float(input("Enter a number: "))
    squared = number ** 2
    square_root = number ** 0.5

x = float(input("Number 1: "))
y = float(input("Number 2: "))

# Calculate the answer and round to 2 decimal places
z = round(x + y , 2)
print(f"Sum = {z}")