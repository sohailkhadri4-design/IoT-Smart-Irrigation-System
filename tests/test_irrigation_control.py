from src.control.irrigation_controller import IrrigationController,IrrigationState
def test_dry_starts_watering():
    d=IrrigationController().decide(20)
    assert d.state==IrrigationState.WATERING and d.pump_on
def test_hysteresis():
    c=IrrigationController()
    assert c.decide(20).pump_on and c.decide(45).pump_on and not c.decide(55).pump_on
def test_fault_stops_pump():
    d=IrrigationController().decide(10,sensor_ok=False)
    assert d.state==IrrigationState.SENSOR_FAULT and not d.pump_on
