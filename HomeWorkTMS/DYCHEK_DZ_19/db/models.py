from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Создание подключения к базе данных SQLite
engine = create_engine('sqlite:///database.db')
Base = declarative_base()

# Определение модели таблицы "Клиенты"
class Client(Base):
    __tablename__ = 'Clients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

    orders = relationship("Order", back_populates="client")

# Определение модели таблицы "Заказы"
class Order(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cost = Column(Integer)
    name = Column(String(20))
    client_id = Column(Integer, ForeignKey('Clients.id'))

    client = relationship("Client", back_populates="orders")

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Создание сессии для добавления данных
Session = sessionmaker(bind=engine)
session = Session()

# Добавление данных
clients_data = [
    {'name': 'Клиент 1'},
    {'name': 'Клиент 2'},
    {'name': 'Клиент 3'},
    {'name': 'Клиент 4'}
]

orders_data = [
    {'cost': 100, 'name': 'Заказ 1', 'client_id': 1},
    {'cost': 200, 'name': 'Заказ 2', 'client_id': 1},
    {'cost': 150, 'name': 'Заказ 3', 'client_id': 2},
    {'cost': 250, 'name': 'Заказ 4', 'client_id': 2},
    {'cost': 120, 'name': 'Заказ 5', 'client_id': 3},
    {'cost': 180, 'name': 'Заказ 6', 'client_id': 3},
    {'cost': 300, 'name': 'Заказ 7', 'client_id': 3},
    {'cost': 170, 'name': 'Заказ 8', 'client_id': 4},
    {'cost': 220, 'name': 'Заказ 9', 'client_id': 4},
    {'cost': 190, 'name': 'Заказ 10', 'client_id': 4}
]

for client_data in clients_data:
    client = Client(**client_data)
    session.add(client)

for order_data in orders_data:
    order = Order(**order_data)
    session.add(order)

session.commit()
session.close()