from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Order

app = Flask(__name__)

# Настройка соединения с базой данных
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def index():
    # Получение всех записей из таблицы Orders
    orders = session.query(Order).all()

    # Отображение шаблона HTML-страницы с передачей списка заказов
    return render_template('orders.html', orders=orders)


if __name__ == '__main__':
    app.run()
