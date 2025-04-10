# TempTrek

## Project Overview

TempTrek uses an Arduino Uno and a thermistor to monitor temperature. The Arduino reads sensor data and sends it over USB serial to a Python script. The Python script stores this data in a SQL database and runs pytest for validation. Shell scripts automate starting/stopping the data collection, backups, and data cleaning.
