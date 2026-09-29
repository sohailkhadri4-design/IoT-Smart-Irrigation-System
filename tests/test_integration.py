from src.actuators.pump_relay import PumpRelay, SimulatedRelay
from src.application.irrigation_system import IrrigationSystem
from src.control.irrigation_controller import IrrigationController, IrrigationState
from src.sensors.soil_moisture import SoilMoistureSensor

def make_system():
    return IrrigationSystem(SoilMoistureSensor(3000, 1000), IrrigationController(), PumpRelay(SimulatedRelay()))

def test_dry_enables_pump():
    s = make_system()
    r = s.process_raw_adc(2600)
    assert r.decision.state == IrrigationState.WATERING and s.pump.pump_on

def test_wet_disables_pump():
    s = make_system()
    s.process_raw_adc(2600)
    r = s.process_raw_adc(1000)
    assert r.decision.state == IrrigationState.OFF and not s.pump.pump_on

def test_invalid_disables_pump():
    s = make_system()
    s.process_raw_adc(2600)
    r = s.process_raw_adc(5000)
    assert r.decision.state == IrrigationState.SENSOR_FAULT and not s.pump.pump_on
