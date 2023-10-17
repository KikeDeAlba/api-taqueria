from services.db import taqueria_db
from models.order import Order, OrderProduct
from app.controllers.admin import get_config
#
def create_order(order: Order):
    config_num_of_tables = int(get_config(name='number_of_tables'))

    if order.table_number > config_num_of_tables:
        raise Exception(f"Table number {order.table_number} not found")

    order_id = taqueria_db.insert(
        table="orders",
        data={
            "client_name": order.client_name,
            "type_id": order.type_id,
            "table_number" : order.table_number,
            "adress" : order.adress
        }
    )
        
    for product in order.products:
        taqueria_db.insert(
            table="order_products",
            data={
                "order_id": order_id,
                "product_id": product.product_id,
                "quantity": product.quantity
            }
        )

    return {
        "message": "Order created successfully",
    }

def edit_quantity_product(order_id: int, product_id: int, quantity: int):
    taqueria_db.update(
        table="order_products",
        where=f"order_id = {order_id} and product_id = {product_id}",
        data={
            "quantity": quantity
        }
    )

    return {
        "message": "Quantity updated successfully",
    }


def delete_product_in_order(order_id: int, product_id: int):
    taqueria_db.execute(
        sql="DELETE FROM order_products WHERE order_id = %s and product_id = %s;",
        params=(order_id,product_id)
    )
    return {
        "message": "Product in order delete successfully",
    }


def add_product_to_order(order_id:int, product: OrderProduct):
    taqueria_db.insert(
        table="order_products",
        data={
            "order_id": order_id,
            "product_id": product.product_id,
            "quantity": product.quantity
        }
    )
    
    return {
        "message":"Add Product In Order Successfully"
    }

def get_orders():
    orders = taqueria_db.fetch_all(
            sql="SELECT * FROM orders;"
    )
    return orders


def get_order(order_id:int):
    orders = taqueria_db.fetch_one(
            sql="SELECT * FROM orders;",
              params=(order_id,)
    )
    
    if not orders:
        raise Exception(f"Order with id {id} not found")
    return orders


def delete_order(order_id:int):
    taqueria_db.execute(
        sql="DELETE FROM orders WHERE order_id = %s;",
        params=(order_id,)
    )
    return {
        "message":"Delete Order Successfully"
    }




#TODO CHECK funciones para agregar o eliminar un producto 
#TODO CHECK function para obtener ordenes 
#TODO CHECK funcion para eliminar una orden 
#
# CREATE TABLE IF NOT EXISTS order_products (
#     order_id INT NOT NULL,
#     product_id INT NOT NULL,
#     quantity INT NOT NULL,
#     PRIMARY KEY(order_id, product_id),
#     FOREIGN KEY (order_id) REFERENCES orders(id),
#     FOREIGN KEY (product_id) REFERENCES products(id),
#     CHECK (quantity > 0)
# );



# CREATE TABLE IF NOT EXISTS orders (
#     id INT NOT NULL AUTO_INCREMENT,
#     created_date DATETIME NOT NULL DEFAULT (NOW()),
#     client_name VARCHAR(50) NOT NULL,
#     adress VARCHAR(50),
#     status_id INT NOT NULL DEFAULT (1),
#     type_id INT NOT NULL,
#     table_number INT NOT NULL,
#     PRIMARY KEY(id),
#     FOREIGN KEY (status_id) REFERENCES status_order(id),
#     FOREIGN KEY (type_id) REFERENCES type_order(id)
# );