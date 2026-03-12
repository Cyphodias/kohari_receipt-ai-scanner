import psycopg2

conn = psycopg2.connect(
    database="receipts",
    user="postgres",
    password="password",
    host="localhost"
)

def save_receipt(items,total):

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO receipts(total) VALUES(%s)",
        (total,)
    )

    conn.commit()
