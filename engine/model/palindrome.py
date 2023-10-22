from datetime import datetime

from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(Car, SternmanEngine, SpindlerBattery):
    pass

def create_palindrome(date_current, last_service_date, current_mileage, last_service_mileage):
    new_car = Palindrome(date_current, last_service_date, current_mileage, last_service_mileage)
    
    return new_car

