# Day 6: Python Function Exercises - Error Handling and File I/O

# 1. Basic try-except block
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    return result

# 2. Try-except-else-finally block
def read_integer():
    try:
        value = int(input("Enter an integer: "))
    except ValueError:
        return "That's not an integer"
    else:
        return f"You entered: {value}"
    finally:
        print("Input attempt complete.")

# 3. Writing to a file
def write_to_file(filename, text):
    try:
        with open(filename, 'w') as f:
            f.write(text)
        return "Write successful"
    except Exception as e:
        return f"Write failed: {e}"

# 4. Reading from a file
def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

# 5. Append text to a file
def append_to_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        return "Append successful"
    except Exception as e:
        return f"Append failed: {e}"

# 6. Handling multiple exceptions
def safe_convert(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return "Conversion failed"

# 7. Custom exception example
class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot take square root of negative number")
    return x ** 0.5


# Example Tests
if __name__ == "__main__":
    print("Divide:", divide_numbers(10, 0))
    print("Safe Convert:", safe_convert("abc"))
    print("Write to file:", write_to_file("test_day6.txt", "Hello, world!\n"))
    print("Append to file:", append_to_file("test_day6.txt", "Appended line.\n"))
    print("Read from file:", read_from_file("test_day6.txt"))

    try:
        print("Square root:", square_root(-9))
    except NegativeNumberError as e:
        print("Error:", e)
