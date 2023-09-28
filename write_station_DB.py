import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="test data",
    user="postgres",
    password="Whynow3421!"
)

curser = conn.cursor()

with open("stations.txt", "r") as file:
    for lines in file:
        words = lines.strip()
        curser.execute("INSERT INTO places (place_name) VALUES (%s)", (words,))
    conn.commit()
curser.close()
conn.close()


cursers = conn.cursor()
cursers.execute("SELECT COUNT(*) FROM station;")
row_count = cursers.fetchone()[0]
cursers.close()
conn.close()
print(row_count)