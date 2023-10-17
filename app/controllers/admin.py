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

def get_config(name: str):
    config = taqueria_db.fetch_one(
        sql='SELECT * FROM configs WHERE `name` = %s',
        params=(name,)
    )

    if not config:
        raise Exception("No se encontró la configuración")

    return config['value']
