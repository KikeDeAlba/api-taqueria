import  mysqlclientpy

taqueria_db =  mysqlclientpy.DB(
    host="127.0.0.1",
    database= "taqueria_db",
    password= "12345678",
    user= "root",
)