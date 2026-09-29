# Hardware Setup

## Reference hardware

- ESP32 DevKit-compatible board
- Analog soil-moisture sensor
- Relay module compatible with the ESP32 logic level
- Water pump with an appropriate external power supply
- Common ground where required by the selected modules

## Reference firmware pinout

- Soil-moisture analog output -> GPIO34
- Relay input -> GPIO26
- USB serial -> firmware telemetry at 115200 baud

The pinout is a reference configuration. Verify the exact ESP32 board and module datasheets before wiring.

## Important electrical considerations

- Do not power a pump directly from an ESP32 GPIO.
- Use a relay or suitable MOSFET/driver stage rated for the pump voltage and current.
- Check whether the relay input is active-low or active-high and update the firmware constants accordingly.
- Ensure the soil sensor output stays within the ESP32 ADC input voltage limits.
- If the sensor module can output more voltage than the ESP32 ADC safely accepts, use appropriate level scaling.
- Keep high-current pump wiring physically and electrically separated from low-voltage signal wiring where practical.
- Add suitable protection for inductive loads according to the pump/driver design.

Physical wiring and measured hardware behavior are not claimed by this repository.
