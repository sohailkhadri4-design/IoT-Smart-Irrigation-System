# System Architecture

Soil Moisture Sensor -> ESP32 ADC -> Moisture Conversion -> Irrigation Controller -> Relay -> Water Pump

The software separates sensing, decision logic, and actuation. The repository uses simulated sensor and relay models for repeatable automated tests.
