class Vehicle:
    college_name="ACE ENGINEERING COLLEGE"
    total_vehicles=0
def __init__(self,vehicle_id,vehicle_type,capacity):
    self.vehicle_id = vehicle_id
    self.vehicle_type = vehicle_type
    self.capacity = capacity
    Vehicle.total_vehicles += 1
def get_total_vehicles(cls):
    print(cls.total_vehicles)
def validate_method(vehicle_id):
    return vehicle_id[:5]=="TS33G"
def display_info(self):
    print("Vehicle type: ",self.vehicle_type)
    print("Vehicle id: ",self.vehicle_id)
    print("Capacity: ",self.capacity)

class Bus(Vehicle):