# Logging decorator

import time

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} returned {result} in {end_time - start_time:.4f} seconds")
        return result
    return wrapper
@logging_decorator
def add(a, b):
    return a + b

add(2, 3)

# Authentication

def authentication_decorator(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated", False):
            raise PermissionError("User is not authenticated!")
        return func(user, *args, **kwargs)
    return wrapper

@authentication_decorator
def view_account_details(user):
    return f"Account details for {user['name']}"

user = {"name": "John Doe", "is_authenticated": True}
print(view_account_details(user))


#Adapter
class USB:
    def connect_with_usb(self):
        return "Connected with USB"

class USBToLightningAdapter:
    def __init__(self, usb_device):
        self.usb_device = usb_device

    def connect_with_lightning(self):
        return self.usb_device.connect_with_usb().replace("USB", "Lightning")

usb_device = USB()
adapter = USBToLightningAdapter(usb_device)
print(adapter.connect_with_lightning())

# FCache

from functools import lru_cache

@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))

#


def call_counter(func):
    count = 0  # This variable keeps track of the number of calls.

    def wrapper(*args, **kwargs):
        nonlocal count  # Allows access to the variable outside the inner function.
        count += 1
        print(f"{func.__name__} has been called {count} times.")
        return func(*args, **kwargs)

    return wrapper

# Example usage:
@call_counter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")



# Order calle

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def reverse_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

@reverse_decorator
@uppercase_decorator
def say_hello():
    return "hello world"

print(say_hello())


# Parametrized decorator

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()


## Preserver metadata

from functools import wraps

def preserve_metadata(decorator):
    def wrapper_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return decorator(func)(*args, **kwargs)
        return wrapper
    return wrapper_decorator

@preserve_metadata
def my_decorator(func):
    @wraps(func)  # Ensures metadata of `func` is preserved here too
    def wrapper(*args, **kwargs):
        """This is the wrapper function."""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # Output: "add"
print(add.__doc__)   # Output: "Add two numbers."
