#pragma once

#include <Arduino.h>

// Reference pinout for a generic ESP32 DevKit.
// Verify GPIO availability and relay logic against the exact board/module.
namespace config {
constexpr uint8_t SOIL_MOISTURE_PIN = 34;
constexpr uint8_t PUMP_RELAY_PIN = 26;

constexpr uint8_t RELAY_ON_LEVEL = LOW;
constexpr uint8_t RELAY_OFF_LEVEL = HIGH;

constexpr int ADC_DRY = 3200;
constexpr int ADC_WET = 1200;
constexpr int ADC_MAX = 4095;

constexpr float START_THRESHOLD_PERCENT = 35.0f;
constexpr float STOP_THRESHOLD_PERCENT = 55.0f;

constexpr uint32_t SAMPLE_INTERVAL_MS = 2000;
}
