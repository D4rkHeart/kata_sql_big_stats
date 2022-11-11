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

# Create the insert statement
def insertInto(connection,statement):
    sqlStatement = '''INSERT INTO Probe(ID,Name,Value,Date) VALUES(?,?,?,?)'''
    #invoke methods that execute SQLite statements
    cursor = connection.cursor()
    # Execute the statement 
    cursor.execute(sqlStatement,statement)
    #Saves all transactions to the database 
    connection.commit()

def main():
    dataBase = "sensorRecord.db"
    connection = connectionCreation(dataBase)
    with connection:
        fullLine = ""
        db = open("./Data/states.csv")
        for line in db:
            fullLine += line
            contents = fullLine.split(",")
            insertInto(connection,[int(contents[0][1:-1]),contents[2][1:-1],contents[3][1:-1],contents[7][1:-1]])
main()