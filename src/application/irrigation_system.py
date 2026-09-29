from dataclasses import dataclass
from src.sensors.soil_moisture import SensorStatus

@dataclass(frozen=True)
class IrrigationCycleResult:
    decision:object
    moisture_percent:float

class IrrigationSystem:
    def __init__(self,sensor,controller,pump): self.sensor,self.controller,self.pump=sensor,controller,pump
    def process_raw_adc(self,raw_value):
        reading=self.sensor.read_from_raw(raw_value)
        decision=self.controller.decide(reading.percentage,reading.status==SensorStatus.OK)
        self.pump.set_pump(decision.pump_on)
        return IrrigationCycleResult(decision,reading.percentage)
