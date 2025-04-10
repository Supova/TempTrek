"""Main script to start temperature monitoring and data storage."""

from database import setup_database
from data_collector import collect_temperature_data

def main():
    """Setup database and start collecting temperature data."""
    db_path = "temperature_data.db"
    serial_port = "COM4"
    baud_rate = 9600

    setup_database(db_path)
    collect_temperature_data(serial_port, baud_rate, db_path)


if __name__ == "__main__":
    main()