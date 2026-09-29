from src.sensors.soil_moisture import SoilMoistureSensor,SensorStatus
def test_conversion():
    r=SoilMoistureSensor(3000,1000).read_from_raw(2000)
    assert r.status==SensorStatus.OK and r.percentage==50.0
def test_clamping():
    s=SoilMoistureSensor(3000,1000)
    assert s.read_from_raw(3500).percentage==0.0 and s.read_from_raw(500).percentage==100.0
def test_invalid_adc():
    assert SoilMoistureSensor().read_from_raw(-1).status==SensorStatus.SENSOR_FAULT
