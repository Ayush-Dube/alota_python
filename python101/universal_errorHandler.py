# try:
#     print(')

# except Exception as e:
#     print(f'this {} occurred.')

# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("Please enter a valid number.")

# try:
#     print()
# except Exception as e:
#     print(f'This {e.__class__.__name__} occurred.')

# try and except blocks do not handle syntax errors that occur during parsing (before the code even runs).


# Why?
# Python processes your code in two steps:

# 1.Parsing (compile time) — checks for syntax errors.

# 2.Execution (run time) — where exceptions can be caught using try/except.

# print(')
# ...is a syntax error, not a runtime error. Python can't even start running the code because it's invalid syntax — so the try block is never reached.

"""
1. Division by Zero
try:
    num = 10 / 0
except ZeroDivisionError as e:
    print(f"Can't divide by zero: {e}")


2. File Handling
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")


3. Invalid Type Conversion
try:
    num = int("abc")
except ValueError as e:
    print(f"Invalid input: {e}")


4. List Index Error
try:
    items = [1, 2, 3]
    print(items[5])
except IndexError as e:
    print(f"Index error: {e}")


5. Key Not Found in Dictionary
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError as e:
    print(f"Missing key: {e}")


6. Multiple Exception Types
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Division by zero occurred")


7. Generic Exception Handling
try:
    # any risky code
    open('nope.txt')
except Exception as e:
    print(f"Something went wrong: {e}")


8. Handling User Input Safely
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")


9. Using else and finally
try:
    print("Trying something safe.")
except Exception:
    print("Something went wrong.")
else:
    print("No error occurred.")
finally:
    print("This always runs.")


"""