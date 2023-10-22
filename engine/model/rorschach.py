from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from car import Car

class Rorschach(Car, WilloughbyEngine, NubbinBattery):
    pass

def create_rorschach(date_current, last_service_date, current_mileage, last_service_mileage):
    new_car = Rorschach(date_current, last_service_date, current_mileage, last_service_mileage)
    
    return new_car