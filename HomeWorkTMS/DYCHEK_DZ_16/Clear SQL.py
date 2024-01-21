# С использованием чистого SQL:

import sqlite3

# Создание соединения с базой данных SQLite
con = sqlite3.connect('HomeWork_16_1.db')
cur = con.cursor()

# Функция для создания таблиц
def create_tables():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cost INTEGER,
            name TEXT,
            client_id INTEGER,
            FOREIGN KEY (client_id) REFERENCES Clients (id)
        )
    ''')

# Функция для добавления данных
def populate_data():
    clients_data = [
        {'name': 'Клиент 1'},
        {'name': 'Клиент 2'},
        {'name': 'Клиент 3'},
        {'name': 'Клиент 4'}
    ]

    orders_data = [
        {'cost': 100, 'name': 'Заказ 1', 'client_id': 1},
        {'cost': 200, 'name': 'Заказ 2', 'client_id': 1},
        {'cost': 300, 'name': 'Заказ 3', 'client_id': 2},
        {'cost': 400, 'name': 'Заказ 4', 'client_id': 2},
        {'cost': 500, 'name': 'Заказ 5', 'client_id': 2},
        {'cost': 600, 'name': 'Заказ 6', 'client_id': 3},
        {'cost': 700, 'name': 'Заказ 7', 'client_id': 3},
        {'cost': 800, 'name': 'Заказ 8', 'client_id': 3},
        {'cost': 900, 'name': 'Заказ 9', 'client_id': 3},
        {'cost': 1000, 'name': 'Заказ 10', 'client_id': 4}
    ]

    for data in clients_data:
        cur.execute("INSERT INTO Clients (name) VALUES (?)", (data['name'],))

    for data in orders_data:
        cur.execute("INSERT INTO Orders (cost, name, client_id) VALUES (?, ?, ?)", (data['cost'], data['name'], data['client_id'],))

    con.commit()

# Создание таблиц и добавление данных
create_tables()
populate_data()

# Получение списка заказов каждого клиента
cur.execute('''
    SELECT Clients.name, Orders.name, Orders.cost
    FROM Clients
    INNER JOIN Orders ON Clients.id = Orders.client_id
    ORDER BY Clients.id ASC, Orders.id ASC
''')

rows = cur.fetchall()
current_client_name = ""
for row in rows:
    client_name, order_name, order_cost = row
    if client_name != current_client_name:
        current_client_name = client_name
        print(f"\nЗаказы клиента '{client_name}':")
    print(f"Заказ {order_name}, стоимость: {order_cost}")

con.close()