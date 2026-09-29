# Hardware Setup

Intended hardware: ESP32 development board, analog soil-moisture sensor, relay module, water pump, and suitable power supply.

Connect the sensor to an ESP32 ADC-capable input and calibrate dry/wet values from the actual sensor. Drive the relay from an appropriate GPIO. Do not power a pump directly from an ESP32 GPIO.

Pin numbers are intentionally not claimed because wiring depends on the exact boards and modules used.
