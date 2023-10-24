from ast import Div
from fastapi import APIRouter
from app.controllers.products import get_all_products, get_one_product, insert_product, update_product, delete_product
router = APIRouter(prefix="/product")
def nada():
    return None

router.get("/get_all_products")(get_all_products) #get_all_products
router.get("/get_one_product")(get_one_product) #get_one_product
router.post("/insert_product")(insert_product)
router.post("/update_product")(update_product)
router.delete("/delete_product")(delete_product)
router.get("/None")(nada)