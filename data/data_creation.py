import sqlite3
import os
import pandas as pd
from logs.logger import get_logger
logger= get_logger(__name__)
logger.info("Creating SQLite coffee database ☕")

DB_PATH = "data/coffee.db"

os.makedirs("data", exist_ok=True)

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS coffee_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    acidity REAL,
    aroma REAL,
    body REAL,
    flavor REAL,
    aftertaste REAL,
    balance REAL,
    quality INTEGER
)
""")

# Insert sample data (40 rows max)
coffee_samples = [
    (7.5, 8.0, 7.0, 8.2, 7.8, 8.0, 1),
    (6.0, 6.5, 6.2, 6.0, 6.1, 6.3, 0),
    (8.2, 8.5, 8.0, 8.7, 8.4, 8.6, 1),
    (5.8, 6.0, 5.9, 6.1, 6.0, 5.7, 0),
    (7.0, 7.2, 7.1, 7.4, 7.3, 7.0, 1),
    (6.2, 6.4, 6.3, 6.5, 6.2, 6.1, 0),
    (8.8, 9.0, 8.6, 9.1, 8.9, 9.0, 1),
    (5.5, 5.8, 5.6, 5.9, 5.7, 5.6, 0),
    (7.9, 8.1, 7.8, 8.3, 8.0, 8.2, 1),
    (6.1, 6.3, 6.0, 6.4, 6.2, 6.1, 0),
]

# Duplicate pattern to reach ~40 rows
coffee_samples = coffee_samples * 4

cursor.executemany("""
INSERT INTO coffee_data (
    acidity, aroma, body, flavor, aftertaste, balance, quality
) VALUES (?, ?, ?, ?, ?, ?, ?)
""", coffee_samples[:40])

connection.commit()
connection.close()

print("SQLite coffee database created successfully ☕")

def load_coffee_data(data_path = DB_PATH):
    connection = sqlite3.connect(data_path)
    query = "SELECT * FROM coffee_data"
    df = pd.read_sql_query(query,connection)
    
    connection.close()
    return df 
def export_sqlite_to_csv(db_path, csv_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM coffee_data", conn)
    conn.close()

    df.to_csv(csv_path, index=False)
    return csv_path
csv_path = "data/coffee_data.csv"
export_sqlite_to_csv(DB_PATH,csv_path)
print(f"Coffee data exported to CSV at {csv_path} ☕")