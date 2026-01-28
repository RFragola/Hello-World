# This Program prompts the user for their name and greets them with a personalized message.
def main():
    name = input("What's your name? ")
    name = " ".join(name.split()).title() # Normalize whitespace and capitalize each word
    print(f"Hello, {name}!")

