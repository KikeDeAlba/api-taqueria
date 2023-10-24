from fastapi import APIRouter
from app.controllers.admin import change_maximum_tables, get_config
router = APIRouter(prefix="/admin")
def nada():
    return None

router.get("/config")(get_config) # /admin/config
router.post("/config/tables")(change_maximum_tables) # /admin/config/tables
router.get("/None")(nada)
