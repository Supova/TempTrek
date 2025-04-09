const int thermistorPin = A0;  // Pin connected to thermistor
const int R1 = 10000;          // Fixed resistor value (10kΩ)
const float T0 = 298.15;       // Reference temperature in Kelvin (25°C)
const float B = 3950;          // Beta constant for thermistor

void setup() { 
    Serial.begin(9600); 
}

void loop() {
  // Read analog input and calculate thermistor resistance
  int adcValue = analogRead(thermistorPin);
  float resistance = R1 * (1023.0 / adcValue - 1);

  // Calculate temperature in Kelvin using the Beta formula
  float temperatureK = 1.0 / (1.0 / T0 + log(resistance / R1) / B);

  // Convert Kelvin to Celsius then to Fahrenheit
  float temperatureC = temperatureK - 273.15;
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

  Serial.print("Temperature (°F): ");
  Serial.println(temperatureF);

  delay(1000);
}
