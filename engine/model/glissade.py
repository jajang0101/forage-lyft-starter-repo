from datetime import datetime

from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery

class Glissade(Car, WilloughbyEngine, SpindlerBattery):
    pass

def create_glissade(date_current, last_service_date, current_mileage, last_service_mileage):
    new_car = Glissade(date_current, last_service_date, current_mileage, last_service_mileage)
    
    return new_car