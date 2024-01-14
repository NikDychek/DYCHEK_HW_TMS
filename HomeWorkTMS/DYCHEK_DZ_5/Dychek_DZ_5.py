#Задание 1
def factorial(n):  #n! = 1*2*3*..*n - факториат числа
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Введите число: "))
result = factorial(n)
print(f"Факториал числа {n} равен {result}")

#Задание 2
import time
from datetime import datetime

def generate_list(n):
    new_list = []
    for i in range(n):
        time.sleep(1)  # Задержка в 1 секунду
        current_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        new_list.append(current_time)
    return new_list

n = int(input("Введите количество элементов списка: "))
result = generate_list(n)
print(result)