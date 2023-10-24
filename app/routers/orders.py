from email.quoprimime import body_check
from fastapi import APIRouter
from app.controllers.order import create_order, edit_quantity_product, delete_product_in_order, add_product_to_order, get_orders, get_order, delete_order

def nada():
    return None

router = APIRouter(prefix="/order")

router.post("/create_order")(create_order) #create order
router.post("/edit_quantity_product")(edit_quantity_product) #edit_quantity_product
router.post("/add_product_to_order")(add_product_to_order)
router.delete("/delete_product_in_order")(delete_product_in_order)
router.get("/get_orders")(get_orders)
router.get("/get_order")(get_order)
router.delete("/delete_order")(delete_order)
router.head("/None")(nada)

