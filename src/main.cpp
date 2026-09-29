#include <Arduino.h>
#include <math.h>

#include "config.h"

namespace {

enum class IrrigationState {
    OFF,
    WATERING,
    SENSOR_FAULT
};

struct MoistureReading {
    int raw;
    float percent;
    bool valid;
};

class SoilMoistureSensor {
public:
    explicit SoilMoistureSensor(uint8_t pin) : pin_(pin) {}

    void begin() const {
        pinMode(pin_, INPUT);
    }

    MoistureReading read() const {
        const int raw = analogRead(pin_);

        if (raw < 0 || raw > config::ADC_MAX) {
            return {raw, NAN, false};
        }

        const float span = static_cast<float>(config::ADC_DRY - config::ADC_WET);
        if (span <= 0.0f) {
            return {raw, NAN, false};
        }

        float percent =
            (static_cast<float>(config::ADC_DRY - raw) / span) * 100.0f;

        percent = constrain(percent, 0.0f, 100.0f);
        return {raw, percent, true};
    }

private:
    uint8_t pin_;
};

class PumpRelay {
public:
    explicit PumpRelay(uint8_t pin) : pin_(pin) {}

    void begin() {
        pinMode(pin_, OUTPUT);
        off();
    }

    void on() {
        digitalWrite(pin_, config::RELAY_ON_LEVEL);
        state_ = true;
    }

    void off() {
        digitalWrite(pin_, config::RELAY_OFF_LEVEL);
        state_ = false;
    }

    bool isOn() const {
        return state_;
    }

private:
    uint8_t pin_;
    bool state_ = false;
};

class IrrigationController {
public:
    IrrigationState update(const MoistureReading& reading) {
        if (!reading.valid || isnan(reading.percent)) {
            return IrrigationState::SENSOR_FAULT;
        }

        if (state_ == IrrigationState::WATERING) {
            if (reading.percent >= config::STOP_THRESHOLD_PERCENT) {
                state_ = IrrigationState::OFF;
            }
        } else if (reading.percent < config::START_THRESHOLD_PERCENT) {
            state_ = IrrigationState::WATERING;
        } else {
            state_ = IrrigationState::OFF;
        }

        return state_;
    }

private:
    IrrigationState state_ = IrrigationState::OFF;
};

const char* stateToString(IrrigationState state) {
    switch (state) {
        case IrrigationState::OFF:
            return "OFF";
        case IrrigationState::WATERING:
            return "WATERING";
        case IrrigationState::SENSOR_FAULT:
            return "SENSOR_FAULT";
    }
    return "UNKNOWN";
}

SoilMoistureSensor sensor(config::SOIL_MOISTURE_PIN);
PumpRelay pump(config::PUMP_RELAY_PIN);
IrrigationController controller;

uint32_t lastSampleMs = 0;

void runControlCycle() {
    const MoistureReading reading = sensor.read();
    const IrrigationState state = controller.update(reading);

    if (state == IrrigationState::WATERING) {
        pump.on();
    } else {
        pump.off();
    }

    Serial.print("raw=");
    Serial.print(reading.raw);
    Serial.print(", moisture=");

    if (reading.valid) {
        Serial.print(reading.percent, 1);
        Serial.print("%");
    } else {
        Serial.print("INVALID");
    }

    Serial.print(", state=");
    Serial.print(stateToString(state));
    Serial.print(", pump=");
    Serial.println(pump.isOn() ? "ON" : "OFF");
}

}

void setup() {
    Serial.begin(115200);
    delay(200);

    analogReadResolution(12);
    sensor.begin();
    pump.begin();

    Serial.println();
    Serial.println("ESP32 Smart Irrigation System");
    Serial.println("Reference firmware starting...");
    Serial.println("WARNING: verify pinout, relay polarity, sensor calibration, and pump power path.");
}

void loop() {
    const uint32_t now = millis();

    if (now - lastSampleMs >= config::SAMPLE_INTERVAL_MS) {
        lastSampleMs = now;
        runControlCycle();
    }
}
