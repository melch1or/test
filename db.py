import pymysql

def create_database(host, username, password, database_name):
    # Connect to the MySQL database server
    conn = pymysql.connect(
        host=host,
        user=username,
        password=password
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the database
    cursor.execute(f"CREATE DATABASE {database_name}")

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print(f"Database '{database_name}' has been created successfully.")

# Provide your database credentials
host = "3dexperience.3ds.com"       # The host where the database server is running
username = "root"        # Your MySQL username
password = "password"    # Your MySQL password
database_name = "mydatabase"  # The desired name for your database

# Call the function to create the database
create_database(host, username, password, database_name)

# For test purpose only
