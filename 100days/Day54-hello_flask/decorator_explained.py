import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


def hello():
    print("Hello there")

@delay_decorator
def bye():
    print("Goodbye")


def greet():
    print("How are ya?")

hello()
bye() #delayed by 2 seconds but the order of execution is kept
greet()
