# Задание 1

import datetime

def working_hours_decorator(func):
    def wrapper(*args, **kwargs):
        current_hour = datetime.datetime.now().hour
        if 9 <= current_hour < 18:
            return func(*args, **kwargs)
        else:
            print("Функция может быть выполнена только в рабочие часы (с 9 до 18).")
    return wrapper

@working_hours_decorator
def my_function():
    print("Функция выполняется в рабочие часы.")

my_function()

# Задание 2

def check_type_decorator(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(isinstance(arg, expected_type) for arg in args) and all(isinstance(arg, expected_type) for arg in kwargs.values()):
                return func(*args, **kwargs)
            else:
                print("Bad type")
        return wrapper
    return decorator

@check_type_decorator(int)
def my_function(arg1, arg2):
    print("Оба аргумента являются целыми числами.")

my_function(10, 20)