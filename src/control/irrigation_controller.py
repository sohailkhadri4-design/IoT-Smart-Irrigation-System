from dataclasses import dataclass
from enum import Enum

class IrrigationState(str, Enum):
    OFF="OFF"
    WATERING="WATERING"
    SENSOR_FAULT="SENSOR_FAULT"

@dataclass(frozen=True)
class IrrigationDecision:
    state:IrrigationState
    pump_on:bool
    reason:str

class IrrigationController:
    def __init__(self,start_below=35.0,stop_at=55.0):
        if not 0<=start_below<stop_at<=100: raise ValueError("Expected 0 <= start_below < stop_at <= 100")
        self.start_below,self.stop_at=start_below,stop_at
        self._watering=False
    def decide(self,moisture_percent,sensor_ok=True):
        if not sensor_ok:
            self._watering=False
            return IrrigationDecision(IrrigationState.SENSOR_FAULT,False,"Invalid soil-moisture reading")
        if self._watering:
            if moisture_percent>=self.stop_at: self._watering=False
        elif moisture_percent<self.start_below: self._watering=True
        if self._watering: return IrrigationDecision(IrrigationState.WATERING,True,"Soil moisture below start threshold")
        return IrrigationDecision(IrrigationState.OFF,False,"Soil moisture adequate")
