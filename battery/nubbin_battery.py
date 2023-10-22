from abc import ABC
from utils import add_years_to_date



class NubbinBattery(ABC):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        return (self.current_date > add_years_to_date(self.last_service_date, 4))