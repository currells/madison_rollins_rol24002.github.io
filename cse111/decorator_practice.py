"""Create a decorator that Memoizes the response from previous functions (caching) and gives rate 
limit to the function and how long it takes"""


"""My work down here"""
#Memoization Decorator 
def memoize():

    def dec(func): #memoizes the previous function calls
        cache = {}
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
                print("New input stored in Cache")
            return cache[args]
        return wrapper
    return dec

print(f"Your Cache is: {memoize}")

#Rate Limit Decorator
def rate_limit():
    import time
    def dec(func): #rate limits the function
        def wrapper(*args):
            start = time.time()
            func(*args)
            end = time.time()
            print(f"Time taken: {end - start}")
        return wrapper
    return dec
print(f"Your Rate Limit is: {rate_limit}")

#Time taken to run the function
def time_taken():
    import time
    def dec(func):
        def wrapper(*args):
            start = time.time()
            func(*args)
            end = time.time()
            print(f"Time taken: {end - start}")
        return wrapper
    return dec
print(f"Time taken to run the function is: {time_taken}")

@memoize()
#The AI generated function
def calculate_average(numbers):
    """Calculates the average of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The average of the numbers, or 0 if the list is empty.
    """
    if not numbers:  # Check for empty list to avoid division by zero
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

@memoize()
def greet(name, greeting="Hello"):
    """Greets a person with an optional greeting.

    Args:
        name: The name of the person to greet.
        greeting: The greeting to use (defaults to "Hello").

    Returns:
        A greeting string.
    """
    return f"{greeting}, {name}!"

@memoize()
def reverse_string(text):
    """Reverses a string.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.
    """
    return text[::-1]  # Efficient string reversal using slicing

@memoize() @rate_limit()
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
      n: A non-negative integer.

  Returns:
      The factorial of n, or 1 if n is 0.
      Raises ValueError if n is negative.
  """
  if n < 0:
      raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
      return 1
  else:
      result = 1
      for i in range(1, n + 1):
          result *= i


factorial(5)
factorial(5)