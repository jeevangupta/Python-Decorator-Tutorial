
# command: python3 DecoratorBasicStructure.py

# Define the decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before the function runs.")
        result = func(*args, **kwargs)
        print("Something after the function runs.")
        return result
    return wrapper

# Apply the decorator
@my_decorator
def say_hello():
    print("Hello, World!")

# Call the decorated function
say_hello()

