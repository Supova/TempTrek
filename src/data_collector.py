"""Data collector module to read temperature and store it in database."""

from serial_reader import read_temperature
from database import insert_data


def collect_temperature_data(serial_port: str, baud_rate: int, db_path: str) -> None:
    """
    Continuously reads temperature data and stores it into the database.

    Args:
        serial_port (str): The COM port to read from.
        baud_rate (int): The baud rate for serial communication.
        db_path (str): Path to the SQLite database file.
    """
    while True:
        temperature = read_temperature(serial_port, baud_rate)
        if temperature is not None:
            insert_data(temperature, db_path)
