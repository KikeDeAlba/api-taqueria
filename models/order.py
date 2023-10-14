from pydantic import BaseModel

class OrderProduct (BaseModel):
    product_id: int
    quantity: int

class Order (BaseModel):
    client_name: str
    table_number: int
    adress: str | None = None
    type_id: int
    products: list[OrderProduct]

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