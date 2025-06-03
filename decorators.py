import functools
import time
import math
import random

PLUGINS = dict()

def register(func):
    """Register a function as a plugin."""
    PLUGINS[func.__name__] = func
    return func

# boiler plate
def decorator(func):
    """put content here"""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do someyhing after
        return value
    return wrapper_decorator

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} seconds.")
        return value
    return wrapper_timer

def debug(func):
    """Print the function signature and return value."""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} =  {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print (f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

def slow_down(func):
    """Sleep one second before calling function."""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


# try them out
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

print(waste_some_time(4))

@debug
def make_greeting(name, age=None):
    if age is None:
        return  f"Hello {name}"
    else:
        return f"Hello {name}! {age} you've grown up!"
    
print(make_greeting("Dave", 19))

# using a decorator with a built-in function.
math.factorial = debug(math.factorial)

def approximate_e(terms = 18):
    return sum(1 / math.factorial(n) for n in range(terms))

print(approximate_e(5))

@slow_down
def countdown(from_number):
    if from_number <1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
print(countdown(5))

@register
def say_hi_there(name):
    return f"HelloHi there {name}"

@register
def be_awesome(name):
    return f"Be awesome {name}!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
