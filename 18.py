def say_hello():
    return "hello"
print(say_hello())

def outer():
    def inner():
        print("inner is called")
    inner()
outer()

def outer():
    def inner():
        print("inner is called")
        return inner
e = outer()
print(e)

# program 2
def decrarator_function(func):
    def wrapper_function():
        print("before is called")
        func()
        print("outer is called")
    return wrapper_function

@decrarator_function
def say_hello():
    print("hello ...")

# a = decorator_function(say_hello)
# print(a)
# a()

#program 2
def decorator(func):
    def wrapper(*args,**kwargs):
        print("Function is called ....")
        return func(*args,**kwargs)
    return wrapper

@decorator
def Calculate(*args,**kwargs):
    print(kwargs)
    print(args)

Calculate(1,2,3,4,5,a= "admin",b="manager")

# program 4
def upperCase_decorator(func):
    def wrapper(*args,**kwargs):
        e = func(*args,**kwargs)
        return e.upper()
    return wrapper

def start_decorator(func):
    def wrapper(*args,**kwargs):
        e = func(*args,**kwargs)
        return f'*** {e}****'
    return wrapper

@start_decorator
@upperCase_decorator
def greet(word):
    return f'hello,{word}'

print(greet("Vaibhav"))