# ESP32 Arduino / PlatformIO Firmware

The repository includes a reference ESP32 implementation using the Arduino framework through PlatformIO.

## Firmware flow

1. Read the analog soil-moisture sensor with the ESP32 ADC.
2. Convert the calibrated ADC value to a 0-100% moisture estimate.
3. Apply hysteresis control: below 35% starts watering; at or above 55% while watering stops it.
4. Drive the relay output.
5. On an invalid sensor reading, force the pump OFF.
6. Report raw ADC value, moisture percentage, controller state, and pump state over UART at 115200 baud.

## Reference pinout

| Function | ESP32 GPIO |
|---|---:|
| Soil moisture analog output | GPIO34 |
| Pump relay input | GPIO26 |
| UART telemetry | USB serial / Serial |

These pins are reference values for a generic ESP32 DevKit, not a claim about physical hardware. Verify the exact board, sensor module, relay module, and wiring before deployment.

## Calibration

The firmware uses ADC_DRY=3200, ADC_WET=1200, and a 12-bit ADC range of 0-4095.

The conversion is:

moisture_percent = (ADC_DRY - raw) / (ADC_DRY - ADC_WET) * 100

The result is clamped to 0-100%.

## Relay safety

The reference configuration assumes an active-low relay: LOW means pump ON and HIGH means pump OFF.

Change RELAY_ON_LEVEL and RELAY_OFF_LEVEL if the relay module uses opposite logic.

The pump must have an appropriate external power supply and switching path. Never drive a pump directly from an ESP32 GPIO.

## Build and upload

Install PlatformIO in VS Code or use the PlatformIO CLI.

    pio run
    pio run -t upload
    pio device monitor -b 115200

No physical hardware validation is claimed by this repository. The Python tests continue to validate the control model independently from the ESP32 toolchain.
