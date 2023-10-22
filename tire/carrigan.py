class Carrigan:
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.tire_worn = [0, 0, 0, 0]
    def tire_should_be_serviced(self):
        result = False
        for i in range(4):
            if (self.tire.worn[i] >= 0.9):
                result = True
        return result
