import code
from services.db import taqueria_db
from models.product import Product
from fastapi import HTTPException


# Esta funcion debe traer todos los productos de la base de datos y devolverlos
def get_all_products():
    products = taqueria_db.fetch_all(
        sql="SELECT * FROM products;"
    )

    return products

# Esta funcion debe traer un producto especifico de la base de datos y devolverlo
def get_one_product(id: int):
    product = taqueria_db.fetch_one(
        sql="SELECT * FROM products WHERE id = %s;",
        params=(id,)
    )

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

# El nombre de la funcion que lo que hace el contrato
# Lo que hay entre parentesis es lo que se necesita para llevar acabo el contrato
def insert_product(product: Product):
    taqueria_db.insert(
        table="products",
        data={
            "name": product.name,
            "price": product.price,
        }
    )

    return {
        "message": "Product created"
    }

def update_product(id: int, product: Product):
    taqueria_db.update(
        table="products",
        where=f"id = {id}",
        data={
            "name": product.name,
            "price": product.price,
        }
    )

    return {
        "message": "Product updated"
    }

def delete_product(id: int):
    taqueria_db.execute(
        sql="DELETE FROM products WHERE id = %s;",
        params=(id,)
    )

    return {
        "message": "Product deleted"
    }

# Un contrato en la programacion, es el nombre de una funcion y lo que esta recibe
# Por ejemplo, si una funcion se llama insert_product y recibe un producto, el contrato
# seria insert_product(product: Product) y sabes que va a insertar un producto
# solo por el mero hecho del nombre y los parametros de la funcion