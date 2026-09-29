# System Architecture

Soil Moisture Sensor -> ESP32 ADC -> Moisture Conversion -> Irrigation Controller -> Relay -> Water Pump

The software separates sensing, decision logic, and actuation. Simulated sensor and relay models provide repeatable automated tests.
