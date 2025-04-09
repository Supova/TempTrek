# Moist Mission

## Project Overview

Moist Mission uses an Arduino Uno and a DHT11 sensor to monitor temperature and humidity data in a closed environment. The Arduino reads sensor data and sends it over USB serial to a Python script. The Python script stores this data in a SQL database and runs pytest for validation. Shell scripts automate starting/stopping the data collection, backups, and data cleaning.
