# command: python3 DecoratorFunctionsWithParameters.py

import time

# Example: Timing Function Execution
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")

        return result
    return wrapper

@timing_decorator
def calculate_sum(n):
    return sum(range(n))

print(calculate_sum(1000000))



# Example: Validating Inputs

def validate_non_negative(func):
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            raise ValueError("Negative values are not allowed!")
        return func(*args, **kwargs)
    return wrapper

@validate_non_negative
def multiply(a, b):
    return a * b

print(multiply(3, 5))  # Works fine
# print(multiply(3, -5))  # Raises ValueError


# 
# 
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)

