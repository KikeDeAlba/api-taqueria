from services.db import taqueria_db

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
        raise Exception(f"Product with id {id} not found")
    
    return product