import time

def timing_decorator(func):
  def wrapper():
    start_time = time.time()
    result = func()
    end_time = time.time()
    print(f"Function {func.__name__} took {end_time - start_time} seconds")
    return result
  return wrapper

@timing_decorator
def my_function():
  # Simulate some work
  time.sleep(1)
  return "Done!"

my_function()

