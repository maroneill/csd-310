import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "toorpassword",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

try:

    cursor = db.cursor()

    query = "SELECT * FROM team"
    
    cursor.execute(query)
    
    teams = cursor.fetchall()
    
    print("\n -- DISPLAYING TEAM RECORDS --")
    
    for team in teams:
        print("Team ID:", team[0])
        
        print("Team Name:", team[1])
        
        print("Mascot:", team[2])

    query = "SELECT * FROM player"
    
    cursor.execute(query)
    
    players = cursor.fetchall()
    
    print("\n -- DISPLAYING PLAYER RECORDS --")
    
    for player in players:
      
        print("Player ID:", player[0])
        
        print("First Name:", player[1])
        
        print("Last Name:", player[2])
        
        print("Team ID:", player[3])

except mysql.connector.Error as err:
  
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      
        print("The specified database does not exist")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      
        print("The specified database does not exist")

    else:
      
        print(err)

finally:
  
    cursor.close()
    
    db.close()
