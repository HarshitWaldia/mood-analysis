# Prepare the SQL statement
sql = "INSERT INTO users (name, age, gender, address, mood) VALUES (%s, %s, %s, %s, %s)"
values = (name, age, gender, address, mood)

# Execute the SQL statement using prepared statements
cursor.execute(sql, values)
with mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harshit",
    database="healthsys"
) as mydb:
    # Create a cursor using a context manager
    with mydb.cursor() as cursor:
        # Execute the SQL statement using prepared statements
        sql = "INSERT INTO users (name, age, gender, address, mood) VALUES (%s, %s, %s, %s, %s)"
        values = (name, age, gender, address, mood)
        cursor.execute(sql, values)

    # Commit the transaction
    mydb.commit()
