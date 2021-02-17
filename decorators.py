# functions in python are first-class objects

# Decorator is a function that takes another function as an argument
# and explicitly extends the behvaior of this function without
# explicitly modifying it.
# if is expressed as @<decorator_function_name>

# usage of decorators
# timer, debug, check, plug_ins, cache return_values, update the state

import functools


# Decorator function
# pass function as argument (func).
# Have an inner wrapper function that can do something (extend) before/after
# calling the function (func) on which the decorator is to be applied.
# This decorator will only work on functions with no arguments
def start_end_decorator(func):

    # inner function
    def wrapper():
        # do something before
        print("\nstart")
        func()
        # do something after
        print("end\n")

    return wrapper


# Decorator function
# To work on functions with argument, the inner wrapper function
# must be of form <wrapper_func_name>(*args, **kwargs).
# func called inside the wrapper_func should also have (*args, **kwargs)
# To work on func with return values, <return_value> = func(*args, **kwargs)
# To preserve the info of function func, use functools.wrap(func)
# functools.wrap() used for help(func), func.__name__
def add_decorator(func):

    @functools.wraps(func)
    # inner function
    def wrapper(*args, **kwargs):
        # do something before
        print("\nstart")
        result = func(*args, **kwargs)
        # do something after
        print("end\n")
        return result

    return wrapper


# Decorator function
# To pass arguments firectly to a decorator function,
# we need an inner function inside an inner function
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


# Decorator function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        # prints information about the name, args, keyword args and func name
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)

        # prints the return type of the funciton
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper


# Class Decorator
# used to maintain and update a state
# ex: how many times a function is executed
class CountCalls:

    # func is saved as class variable
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    # same as the inner function of the function decorator
    # __call__() allows to execute an object of this class just like a function
    def __call__(self, *args, **kwargs):
        print('Hi there')


# Class Decorator
# used to maintain and update a state
# ex: how many times a function is executed
class CountCalls_v2:

    # func is saved as class variable
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    # same as the inner function of the function decorator
    # pass *args, **kwargs to it
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


def print_name():
    print("Vibha")


@start_end_decorator
def print_name_v2():
    print("Vibha")


@start_end_decorator
def add(x):
    return x + 5


@add_decorator
def add_v2(x):
    return x + 5


@repeat(num_times=4)
def greet(name):
    greeting = f"Hello {name}"
    print(greeting)


# stacking decorator functions executes them in the order they are listed
@debug
@add_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


# calling class decorator
@CountCalls
def say_hi(name):
    print(f'hello {name}')


# calling class decorator
@CountCalls_v2
def say_hi_v2(name):
    print(f'hello {name}')


# print_name()

# print_name = start_end_decorator(print_name)

# print_name()

# print_name_v2()

# add(5)

# result = add_v2(5)
# print(result)

# print(help(add))
# print(add.__name__)

# print(help(add_v2))
# print(add_v2.__name__)

# greet("vibha")

# say_hello("vibha")

# cc = CountCalls(None)
# cc()

# say_hi_v2("vibha"), say_hi_v2("vibha")

'''
################
Vibha
################

start
Vibha
end

################

start
Vibha
end

################
Traceback (most recent call last):
  File "/home/vibha/visual_studio/decorators.py", line 43, in <module>
    add(5)
TypeError: wrapper() takes 0 positional arguments but 1 was given
################
start
end

10
################
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)
    # inner function

None
wrapper
################
Help on function add_v2 in module __main__:

add_v2(x)
    # to preserve the identity of function func

None
add_v2
################
Hello vibha
Hello vibha
Hello vibha
Hello vibha
################
Calling say_hello('vibha')

start
Hello vibha
end

say_hello returned 'Hello vibha'
################
Hi there

################
This is executed 1 times
hello vibha
This is executed 2 times
hello vibha

################
'''
