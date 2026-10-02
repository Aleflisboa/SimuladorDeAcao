import mysql.connector

def get_conexao():
    return mysql.connector.connect(
       host ="localhost", 
       user ="root",
       password ="12345678",
       database ="DatabaseAcao",
       autocommit=True

)