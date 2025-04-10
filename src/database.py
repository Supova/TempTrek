import sqlite3

def setup_database(db_name="sensor_data.db"):
    """
    Initializes the SQLite database and creates the temperature_data table if it doesn't exist.

    Parameters:
    db_name (str): The name of the SQLite database file (default is 'sensor_data.db').
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS temperature_data (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   temperature real,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
    """)
    
    conn.commit()
    conn.close()


def insert_data(temperature, db_name="sensor_data.db"):
    """
    Inserts temperature data into the temperature_data table in the SQLite database.

    Parameters:
    temperature (float): The temperature value to store.
    db_name (str): The name of the SQLite database file (default is 'sensor_data.db').
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO temperature_data (temperature)
            VALUES (?)
        """, (temperature,))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()