from ParkingLot.Src.Models.Models import Vehicle

class VehicleRepo:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle_num, vehicle : Vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Invalid vehicle type")
        if vehicle_num in self.vehicles:
            raise ValueError(f"Vehicle with number {vehicle_num} already exists.")
        self.vehicles[vehicle_num] = vehicle
        return vehicle

    def get_vehicle(self, vehicle_num):
        if vehicle_num not in self.vehicles:
            raise ValueError(f"Vehicle with number {vehicle_num} does not exist.")
        return self.vehicles.get(vehicle_num)

    def remove_vehicle(self, vehicle_num):
        if vehicle_num in self.vehicles:
            del self.vehicles[vehicle_num]

    def list_vehicles(self):
        return self.vehicles.items()

