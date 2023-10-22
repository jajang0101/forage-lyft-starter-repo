from abc import ABC
from datetime import datetime


class SpindlerBattery(ABC):
    def __init__(self, date_current, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return (datetime.today().date() - self.last_service_date > 2)