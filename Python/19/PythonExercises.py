import math

def ask_exponent():
    base = int(input("Enter a base number: "))
    exponent = int(input("Enter an exponent: "))
    result = base ** exponent
    print(f"{base}^{exponent} = {result}\n")

def ask_square_root():
    num = float(input("Enter a number to find the square root: "))
    if num < 0:
        print("Cannot calculate the square root of a negative number.\n")
        return
    result = round(math.sqrt(num), 2)
    print(f"√{num} = {result}\n")

def ask_division():
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    if denominator == 0:
        print("Division by zero is not allowed.\n")
        return
    result = round(numerator / denominator, 2)
    print(f"{numerator} ÷ {denominator} = {result}\n")

def main():
    print("Welcome to the Advanced Math Quiz!")
    print("Choose an option:")
    print("1. Exponentiation")
    print("2. Square Root")
    print("3. Division with Precision")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            ask_exponent()
        elif choice == '2':
            ask_square_root()
        elif choice == '3':
            ask_division()
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
