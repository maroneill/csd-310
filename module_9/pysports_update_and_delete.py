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

def display_players(cursor, title):
    """ A function that performs an inner join between the player and team tables,
        and outputs the results to the terminal window.
    """

    # SQL query for the inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # Retrieve the results from the cursor object
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))

    # Loop through the player data and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ Exception handling for potential MySQL database errors """ 

    # Connect to the pysports database
    db = mysql.connector.connect(**config)

    # Obtain the cursor object
    cursor = db.cursor()

    # SQL query to insert a player record
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # Data for the new player
    player_data = ("Smeagol", "Shire Folk", 1)

    # Execute the insertion query
    cursor.execute(add_player, player_data)

    # Commit the insertion to the database
    db.commit()

    # Display all records in the player table
    display_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # SQL query to update the newly inserted player record
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # Execute the update query
    cursor.execute(update_player)

    # Display all records in the player table
    display_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # SQL query to delete a player record
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    # Execute the delete query
    cursor.execute(delete_player)

    # Display all records in the player table
    display_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ Error handling """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The provided username or password is incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The database specified does not exist")

    else:
        print(err)
finally:
    cursor.close()
    db.close()
