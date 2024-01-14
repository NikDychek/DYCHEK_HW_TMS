
# Задание 1
"""Декодировать в строку байковое значение: b’r\xc3\xa9sum\xc3\xa9’.
 Затем результат преобразовать в байковый вид в кодировке ‘Latin1’ и затем результат снова декодировать в строку
 (результаты всех преобразований выводить на экран). """
print("######Задание 1######")

byte_value = b'r\xc3\xa9sum\xc3\xa9' # Декодирование байтового значения

decoded_value = byte_value.decode()

latin1_bytes = decoded_value.encode('latin1') # Преобразование в байты в кодировке 'Latin1'

decoded_latin1_value = latin1_bytes.decode('latin1') # Декодирование обратно в строку

# Вывод результатов
print("Исходное байтовое значение:", byte_value)
print("Декодированное значение:", decoded_value)
print("Закодированное в 'latin1' значение:", latin1_bytes)
print("Декодированное обратно в строку:", decoded_latin1_value)



# Задание 2

print("######Задание 2######")
# Чтение строк с клавиатуры
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
str3 = input("Введите третью строку: ")
str4 = input("Введите четвертую строку: ")

# Запись первых двух строк в файл
with open('myfile.txt', 'w') as file:
    file.write(str1 + '\n' + str2)

# Дозапись оставшихся двух строк в файл
with open('myfile.txt', 'a') as file:
    file.write('\n' + str3 + '\n' + str4)

# Задание 3

import json

# Создание словаря
dictionary = {
    123456: ('IVAN', 25),
    654321: ('MARIA', 30),
    987654: ('ALEKSEY', 40),
    246813: ('ELENA', 35),
    135792: ('PETR', 28)
}

# Запись словаря в json-файл
with open('data.json', 'w') as file:
    json.dump(dictionary, file)

# Задание 4

import csv
import json

with open('data.json', 'r') as file:
    data = json.load(file)

num = ("273-43-25", "214-65-76", "733-25-99-", "431-27-92", "725-93-30")

for i, (key, value) in enumerate(data.items()):
    value = list(value)
    value.append(num[i])
    data[key] = tuple(value)

with open("data.json", "w") as file:
    json.dump(data, file)


with open('data.csv', 'w', newline='') as file: # Запись данных в CSV-файл
    writer = csv.writer(file)


    writer.writerow(['ID', 'NAME', 'AGE', 'NUMBER'])     # Запись заголовков столбцов

    # Запись данных
    for id, (name, age, phone_number) in data.items():
        writer.writerow([id, name, age, phone_number])


import pandas as pd

# Чтение CSV-файла
data = pd.read_csv('data.csv')

# Удаление столбца с возрастом
data = data.drop('AGE', axis=1) #параметр 'axis' используем  для удаления столбца

# Сохранение данных в Excel-файл
data.to_excel('data.xlsx', index=False) #Параметр 'index' указывает, что не нужно сохранять индексы строк в Excel-файле.