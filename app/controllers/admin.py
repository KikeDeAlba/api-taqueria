from services.db import taqueria_db

def change_maximum_tables(number_of_tables: int):
    taqueria_db.update(
        table="configs",
        where="`name` = 'number_of_tables'",
        data={
            "`value`": number_of_tables
        }
    )
    
    return {
        "message": "Número de mesas actualizado correctamente"
    }