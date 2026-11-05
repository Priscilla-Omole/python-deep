#Decorators supercharge our function adding extra functionality to it.

#Higher Order Function HOC- it is a function that accepts another function
#  as a parameter or a function that returns another function.


def my_decorator(func):
    def wrap_function(*args, **kwargs):
        print('************')
        func(*args, **kwargs)
        print('************')
    return wrap_function

@my_decorator
def hello():
    print("hello")

@my_decorator
def bye():
    print("bye")

hello()
bye()
hello()
