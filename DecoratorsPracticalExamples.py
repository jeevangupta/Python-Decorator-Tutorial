# commond: python3 DecoratorsPracticalExamples.py

#
# 1. Logging Function Calls
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)



#
# 2. Enforcing Access Control
def requires_admin(func):
    def wrapper(user):
        if user != "admin":
            raise PermissionError("Access denied")
        return func(user)
    return wrapper

@requires_admin
def view_admin_dashboard(user):
    print("Welcome to the admin dashboard!")

# view_admin_dashboard("guest")  # Raises PermissionError
view_admin_dashboard("admin")  # Works



#
# 3. Memoization (Caching Results)
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

