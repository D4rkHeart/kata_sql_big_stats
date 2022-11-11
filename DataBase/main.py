import sqlite3
from sqlite3 import Error

# Create a connexion to the database 
def connectionCreation (dbName):
    connection = None
    try :
        connection = sqlite3.connect(dbName)
    except Error as error:
        print(error)
    return connection

def genericQuerie(connection,statement):
    #invoke methods that execute SQLite statements
    cursor = connection.cursor()
    # Execute the statement 
    cursor.execute(statement)
    #Saves all transactions to the database 
    connection.commit()