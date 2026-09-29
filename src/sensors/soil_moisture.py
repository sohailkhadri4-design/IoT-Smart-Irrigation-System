from dataclasses import dataclass
from enum import Enum

class SensorStatus(str, Enum):
    OK="OK"
    SENSOR_FAULT="SENSOR_FAULT"

@dataclass(frozen=True)
class SoilMoistureReading:
    raw_value:int
    percentage:float
    status:SensorStatus

class SoilMoistureSensor:
    def __init__(self,dry_raw=3200,wet_raw=1200,adc_max=4095):
        if not 0<=wet_raw<dry_raw<=adc_max: raise ValueError("Expected 0 <= wet_raw < dry_raw <= adc_max")
        self.dry_raw,self.wet_raw,self.adc_max=dry_raw,wet_raw,adc_max
    def read_from_raw(self,raw_value):
        if not 0<=raw_value<=self.adc_max: return SoilMoistureReading(raw_value,0.0,SensorStatus.SENSOR_FAULT)
        p=(self.dry_raw-raw_value)*100.0/(self.dry_raw-self.wet_raw)
        return SoilMoistureReading(raw_value,max(0.0,min(100.0,p)),SensorStatus.OK)
