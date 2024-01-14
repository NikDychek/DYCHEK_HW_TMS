
"""Задание 1
Реализуйте итератор колоды карт (52 штуки) CardDeck.
Каждая карта представлена в виде строки типа 2 Пик.
При вызове функции next() будет представлена следующая карта.
По окончании перебора всех элементов возникает ошибка StopIteration."""


class CardDeck:
    def __init__(self):
        self.suits = ['Пик', 'Треф', 'Бубен', 'Червей']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.current_card = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_card >= len(self.suits) * len(self.values):
            raise StopIteration
        else:
            suit_index = self.current_card // len(self.values)
            value_index = self.current_card % len(self.values)
            card = f"{self.values[value_index]} {self.suits[suit_index]}"
            self.current_card += 1
            return card

deck = CardDeck()
for card in deck:
    print(card)

print('#########@@########')

"""Задание 2
Числа Фибоначчи представляют последовательность, получаемую в результате сложения двух предыдущих элементов. 
Начинается коллекция с чисел 1 и 1. Она достаточно быстро растет, по этому вычисление больших значений занимает немало времени.
 Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов.
Для реализации этой функции потребуется обратиться к функции yield. 
Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность "доставать" промежуточные результаты по одному"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b

for num in fib(10):
    print(num)