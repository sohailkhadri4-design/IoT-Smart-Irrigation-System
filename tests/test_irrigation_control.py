from src.control.irrigation_controller import IrrigationController, IrrigationState

def test_dry_starts_watering():
    d = IrrigationController().decide(20)
    assert d.state == IrrigationState.WATERING and d.pump_on

def test_hysteresis():
    c = IrrigationController()
    assert c.decide(20).pump_on
    assert c.decide(45).pump_on
    assert not c.decide(55).pump_on

def test_fault_stops_pump():
    c = IrrigationController()
    assert c.decide(10, sensor_ok=False).state == IrrigationState.SENSOR_FAULT
    assert not c.decide(10, sensor_ok=False).pump_on
