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

# Create the insert statement
def insertInto(connection,statement):
    sqlStatement = '''INSERT INTO Probe(ID,Name,Value,Date) VALUES(?,?,?,?)'''
    #invoke methods that execute SQLite statements
    cursor = connection.cursor()
    # Execute the statement 
    cursor.execute(sqlStatement,statement)

def main():
    dataBase = "sensorRecord.db"
    i = 0
    connection = connectionCreation(dataBase)
    genericQuerie(connection,'''DROP TABLE IF EXISTS Probe''')
    genericQuerie(connection,'''CREATE TABLE Probe ( ID INTEGER PRIMARY KEY, Name TEXT NOT NULL, Value TEXT NOT NULL, Date TEXT NOT NULL )''')
    with connection:
        fullLine = ""
        db = open("./Data/states.csv")
        for line in db:
            fullLine += line
            contents = fullLine.split(",")
            nbcontents = len(contents)
            if nbcontents >= 15:
                fullLine = ""
                insertInto(connection,[int(contents[0][1:-1]),contents[2][1:-1],contents[3][1:-1],contents[7][1:-1]])
    connection.commit()
            
main()