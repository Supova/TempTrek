from src.serial_reader import read_temperature
from src.database import setup_database, insert_data

def collect_and_store_data():
    """
    Reads temperature data from the sensor and stores it in the database.
    
    This function sets up the database, retrieves the temperature data 
    from the sensor using the read_temperature function, and then 
    stores the data into the database using the insert_data function.
    """
    setup_database()
    temperature = read_temperature()
    insert_data(temperature)


def main():
    collect_and_store_data()


if __name__ == "__main__":
    main()