#Задание 1

sentence = "Привет пользователь"
word1, word2 = sentence.split()
formatted_sentence = "! " + word1 + "   " + word2 + " ⁣⁣⁣!"
print(formatted_sentence)

sentence = "Привет пользователь"
word1, word2 = sentence.split()
formatted_sentence = "!⁣⁣⁣{} ⁣⁣⁣!⁣⁣⁣{}".format(word1, word2)
print(formatted_sentence)

sentence = "Привет пользователь"
word1, word2 = sentence.split()
formatted_sentence = "!⁣⁣⁣ {}⁣⁣⁣⁣ ⁣{}".format(word1, word2)
print(formatted_sentence)

#Задание 2
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")

if not age.isdigit():
    print("Ошибка, повторите ввод.")
elif int(age) <= 0:
    print("Ошибка, повторите ввод.")
elif int(age) < 10:
    print(f"Привет, шкет {name}!")
elif int(age) <= 18:
    print(f"Как жизнь, {name}?")
elif int(age) < 100:
    print(f"Что желаете, {name}?")
else:
    print(f"{name}, Вы лжете - в наше время столько не живут…»")

# Задание 3-4
n = int(input("Введите целое число n: "))
sum_of_cubes = 0

i = 1
while i <= n:
    sum_of_cubes += i ** 3
    i += 1

    print(f"Сумма кубов чисел от 1 до {n} включительно: {sum_of_cubes}")

    n = int(input("Введите целое число n: "))
    sum_of_cubes = 0

    for i in range(1, n + 1):
        sum_of_cubes += i ** 3

    print(f"Сумма кубов чисел от 1 до {n} включительно: {sum_of_cubes}")
# выход из цикла = 0

# Задание 5 игра угадай число
import random

random_number = random.randint(1, 5)
user_number = input("Угадай число (от 1 до 5): ")

if user_number == random_number:
    print("Вы угадали!")
else:
    print("Вы проиграли! :( ")
    print(f"Было загадано число {random_number}")

