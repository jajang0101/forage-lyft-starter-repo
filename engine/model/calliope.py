from datetime import datetime

from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(Car, CapuletEngine, SpindlerBattery):
    pass

def create_calliope(date_current, last_service_date, current_mileage, last_service_mileage):
    new_car = Calliope(date_current, last_service_date, current_mileage, last_service_mileage)
    
    return new_car