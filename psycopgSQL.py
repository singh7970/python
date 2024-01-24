import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=school user=abc")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM school")

# Retrieve query results
records = cur.fetchall()