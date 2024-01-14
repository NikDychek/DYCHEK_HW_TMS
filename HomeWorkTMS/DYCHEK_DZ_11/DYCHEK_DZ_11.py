#Задание 1
print('######Задание№1######')

class Publication:
    publisher_name = "Издательство"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"Заголовок: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год выпуска: {self.year}")


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f"ISBN: {self.isbn}")


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        super().display()
        print(f"Номер выпуска: {self.issue_number}")


book = Book("Программирование на Python", "Иван Иванов", 2020, "978-5-93286-243-1")
magazine = Magazine("Журнал о программировании", "Петр Петров", 2021, 3)

book.display()
print()
magazine.display()

print()
print(Publication.publisher_name)

# Задание 2
print('######Задание№2######')

class BankAccount:
    def __init__(self, initial_balance, interest_rate):
        self.__balance = initial_balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Снятие: -{amount}")
        else:
            print("Недостаточно средств на счете")

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f"Начисление процентов: +{interest}")

    def history(self):
        for transaction in self.__transactions:
            print(transaction)

    def get_balance(self):
        return self.__balance



account = BankAccount(1000, 0.05)

account.deposit(500)
account.withdraw(200)
account.add_interest()

print("Баланс счета:", account.get_balance())
print("История операций:")
account.history()