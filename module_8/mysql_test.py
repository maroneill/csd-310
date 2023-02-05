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
    

    db

    print("\n Database user {} connected to MySQL on host {} with database {}",format(config["user"]), config["host"], config["database"])

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The specified database does not exist")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
