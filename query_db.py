import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# Fetch all records from the weather_forecasts table
cursor.execute("SELECT * FROM weather_forecasts")
rows = cursor.fetchall()

# Print the fetched records
for row in rows:
    print(row)

# Close the connection
conn.close()
