from flask import Flask, render_template, request, make_response
from db.model import get_orders, create_client, delete_order, update_order, create_order, get_clients

app = Flask(__name__)


@app.route("/", methods=["GET"])
def tabl():
    list_orders = get_orders()
    return render_template("index.html", orders=list_orders)


@app.route("/client", methods=["GET", "POST"])
def new_client():
    if request.method == "POST":
        client_name = request.form.get("name")
        if not client_name:
            return make_response("Name cannot be empty!", 400)
        create_client(client_name)
        return make_response("Created", 201)

    clients = get_clients()
    return render_template("client.html", clients=clients)


@app.route("/delete_order", methods=["POST"])
def delete_order_api():
    order_id = request.form.get("order_id")
    if not order_id:
        return make_response("Order ID required", 400)
    if delete_order(order_id):
        return make_response("Order deleted", 200)
    else:
        return make_response("Order not found", 404)


@app.route("/update_order", methods=["POST"])
def update_order_api():
    order_id = request.form.get("order_id")
    name = request.form.get("name")
    cost = request.form.get("cost")
    if not order_id:
        return make_response("Order ID required", 400)
    if not name and not cost:
        return make_response("At least one field required", 400)
    if update_order(order_id, name, cost):
        return make_response("Order updated", 200)
    else:
        return make_response("Order not found", 404)


@app.route("/add_order", methods=["POST"])
def add_order():
    name = request.form.get("name")
    cost = request.form.get("cost")
    client_id = request.form.get("client_id")
    if not name or not cost or not client_id:
        return make_response("Name, cost, and client ID required", 400)
    create_order(name, cost, client_id)
    return make_response("Order added", 201)


if __name__ == "__main__":
    app.run()
