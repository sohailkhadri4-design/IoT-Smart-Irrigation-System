# IoT Smart Irrigation System

ESP32-based smart irrigation system using soil-moisture sensing and automated water-pump control.

## Project Overview

This project models a practical embedded IoT irrigation workflow:

**Soil Moisture Sensor -> ESP32 ADC -> Moisture Conversion -> Irrigation Controller -> Relay -> Water Pump**

### Features

- Analog soil-moisture reading and calibration
- Configurable dry/wet ADC range
- Moisture percentage conversion
- Automatic watering with hysteresis
- Relay/pump abstraction
- Sensor-fault handling that forces the pump OFF
- Deterministic simulation example
- Unit and integration tests
- GitHub Actions CI
- Hardware setup and control-logic documentation

## Control Logic

The example controller starts watering below **35%** moisture and stops at **55%**. Separate start/stop thresholds reduce rapid relay switching around a single threshold.

These values are example parameters, not experimentally validated settings for a particular crop or soil type.

## Repository Structure

```text
src/
  sensors/soil_moisture.py
  control/irrigation_controller.py
  actuators/pump_relay.py
  application/irrigation_system.py
tests/
examples/
docs/
.github/workflows/tests.yml
```

## Hardware Notes

Intended hardware includes an ESP32, analog soil-moisture sensor, relay module, water pump, and suitable power supply. Pin numbers are intentionally not claimed because wiring depends on the exact boards and modules used.

The pump must use an appropriate external power path. Do not drive a pump directly from an ESP32 GPIO.

## Testing

The automated tests use software sensor and relay models, so they do not require physical hardware. Hardware measurements or physical validation are not claimed by this repository.

Run locally with:

```bash
pip install -r requirements.txt
pytest -q
```

See [system architecture](docs/system_architecture.md), [hardware setup](docs/hardware_setup.md), and [control logic](docs/control_logic.md).

## ESP32 Arduino / PlatformIO Firmware

A reference ESP32 firmware implementation is included under PlatformIO using the Arduino framework.

### Firmware features

- 12-bit ESP32 ADC soil-moisture sampling
- Calibrated ADC-to-moisture percentage conversion
- 35% watering start threshold
- 55% watering stop threshold with hysteresis
- Fail-safe pump OFF behavior on invalid sensor readings
- Active-low relay support, configurable in include/config.h
- UART telemetry at 115200 baud
- Reference pinout: GPIO34 for soil moisture and GPIO26 for relay control

### Build

Install PlatformIO, then run:

    pio run
    pio run -t upload
    pio device monitor -b 115200

The PlatformIO build is also configured in GitHub Actions.

See [ESP32 firmware](docs/esp32_firmware.md) and [hardware setup](docs/hardware_setup.md) for the reference configuration.

> The ESP32 implementation is a reference firmware design. Physical wiring, sensor calibration, relay polarity, pump behavior, and hardware measurements have not been validated or claimed in this repository.
\n