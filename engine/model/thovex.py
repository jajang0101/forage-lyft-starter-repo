from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery
from car import Car

class Thovex(Car, CapuletEngine, NubbinBattery):
    pass

def create_thovex(date_current, last_service_date, current_mileage, last_service_mileage):
    new_car = Thovex(date_current, last_service_date, current_mileage, last_service_mileage)
    
    return new_car
