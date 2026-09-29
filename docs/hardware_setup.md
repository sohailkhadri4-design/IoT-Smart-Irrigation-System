# Hardware Setup

Intended hardware:
- ESP32 development board
- Analog soil moisture sensor
- Relay module
- Water pump and suitable power supply

Connect the sensor output to an ESP32 ADC-capable input and calibrate dry/wet values from the actual sensor. Drive the relay from an appropriate ESP32 GPIO. Do not power a pump directly from an ESP32 GPIO.

Pin numbers are intentionally not claimed because wiring depends on the exact ESP32 board and modules used.
