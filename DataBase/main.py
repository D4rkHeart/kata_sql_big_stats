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

def genericQueries(connection,statement):
    #invoke methods that execute SQLite statements
    cursor = connection.cursor()
    # Execute the statement 
    cursor.execute(statement)
    #Saves all transactions to the database 
    # connection.commit()

# Create the insert statement
def insertInto(connection,statement):
    sqlStatement = '''INSERT INTO Probe(ID,Name,Value,Date) VALUES(?,?,?,?)'''
    #invoke methods that execute SQLite statements
    cursor = connection.cursor()
    # Execute the statement 
    cursor.execute(sqlStatement,statement)
    #Saves all transactions to the database 
    # connection.commit()


def main():
    dataBase = "sensorRecord.db"
    i = 0
    connection = connectionCreation(dataBase)
    genericQueries(connection,'''DROP TABLE IF EXISTS Probe''')
    genericQueries(connection,'''CREATE TABLE Probe ( ID INTEGER PRIMARY KEY, Name TEXT NOT NULL, Value TEXT NOT NULL, Date TEXT NOT NULL )''')
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
            
            if i%10000 == 0:
                print(f"yaaay i made {i}")
                connection.commit()
            i +=1
            # print(contents[0],contents[2],contents[3],contents[7])
    # i = 0
    # while i == 2:
    #     for filename in dataBase:
    #         print(contents[0],contents[2],contents[3],contents[7])
    #         i = i+1
    
 
        

main()
