from src.actuators.pump_relay import PumpRelay, SimulatedRelay
from src.application.irrigation_system import IrrigationSystem
from src.control.irrigation_controller import IrrigationController
from src.sensors.soil_moisture import SoilMoistureSensor

system = IrrigationSystem(SoilMoistureSensor(3000, 1000), IrrigationController(), PumpRelay(SimulatedRelay()))
for raw in [2600, 2400, 1800, 1200, 1000]:
    r = system.process_raw_adc(raw)
    print(f"ADC={raw} moisture={r.moisture_percent:.1f}% state={r.decision.state.value} pump={system.pump.pump_on}")
