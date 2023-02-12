import mysql.connector
from mysql.connector import errorcode

""" db config """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    # Connect to the db
    db = mysql.connector.connect(**config)

    # Create cursor object
    cursor = db.cursor()

    # Get the player and teamd ata
    cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # Get results
    players = cursor.fetchall()

    print("\n-- DISPLAYING PLAYER RECORDS --")
    
    # Loop and print
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
    input("\n\nPress any key to continue... ")

except mysql.connector.Error as error:
    print("Error: {}".format(error))

finally:
    cursor.close()
    db.close()
