"""Serial reader module to read temperature data from serial port."""

import serial
import time


def read_temperature(serial_port: str, baud_rate: int) -> float | None:
    """
    Reads a temperature value from the specified serial port.

    Args:
        serial_port (str): The COM port to read from.
        baud_rate (int): The baud rate for the serial connection.

    Returns:
        float or None: The temperature in Fahrenheit, or None if reading failed.
    """
    try:
        connection = serial.Serial(serial_port, baud_rate)
        time.sleep(2)  # Wait for connection to stabilize
        line = connection.readline().decode().strip()
        connection.close()
        return float(line)
    except Exception as e:
        print(f"Error reading from serial: {e}")
        return None
    