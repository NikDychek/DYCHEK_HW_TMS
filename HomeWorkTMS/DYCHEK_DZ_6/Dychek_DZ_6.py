#Задание_1: Написать лямбда-функцию определяющую четное/нечетное.
print('Задание 1')
result = lambda x: "чётные" if x % 2 == 0 else "не чётные"
print(result(4))


# Задание_2 Дан список чисел. Вернуть список, где при помощи функции mар() каждое число переведено в строку. В качестве функции в mар использовать lambda.
print('Задание 2')
numbers = [1, 2, 3, 4, 5]
converted_numbers = list(map(lambda x: str(x), numbers))
print(converted_numbers)

# Задание_3 При помощи функции filter() из котрежа слов отфильтровать только те, которые являются полиндромами (которые читаются одинаково в обе стороны).
print('Задание 3 ')
words = ("level", "hello", "radar", "world")
palindromes = list(filter(lambda x: x == x[::-1], words))
print("Cлова:", palindromes)

# Задание_4: Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения. Подсказка: from datetime import datetime
# time = datetime.now
print('Задание 4')
from datetime import datetime
n = int(input('Введите число:'))
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        execution_time = datetime.now() - start_time
        print(f"Функция {func.__name__} выполнена за {execution_time.total_seconds()} секунд")
        return result
    return wrapper

@measure_time
def your_function():
    print('Func:Work')
your_function()

print(your_function()) # Пример использования декоратора

# Задание 5:
print('Задание 5')
def analyze_string(string):
    if string.isdigit():
        return f"Вы ввели положительное целое число: {int(string)}"
    elif string.startswith("-") and string[1:].isdigit():
        return f"Вы ввели отрицательное целое число: {int(string)}"
    elif string.startswith("-") and string[1:].replace(".", "", 1).isdigit():
        return f"Вы ввели отрицательное дробное число: {float(string)}"
    elif string.replace(".", "", 1).isdigit():
        return f"Вы ввели положительное дробное число: {float(string)}"
    else:
        return f"Вы ввели не корректное число: {string}"

# Пример использования функции
print(analyze_string("-6.7")) # Вы ввели отрицательное дробное число: -6.7
print(analyze_string("5")) # Вы ввели положительное целое число: 5
print(analyze_string("5.4r")) # Вы ввели не корректное число: 5.4r
print(analyze_string("-.777")) # Вы ввели отрицательное дробное число: -0.777