import serial
import time

serial_port = 'COM4'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate)
time.sleep(2)

def read_temperature():
    try:
        line = ser.readline().decode().strip()
        return float(line)

    except Exception as e:
        print(f"Error reading from serial: {e}")
        return None
    

def main():
    while True:
        temp = read_temperature()
        if temp is not None:
            print(f"Temperature: {temp} deg F")
        time.sleep(1)


if __name__ == "__main__":
    main()