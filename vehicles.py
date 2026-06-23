class Vehicle:
    college_name="ACE ENGINEERING COLLEGE"
    total_vehicles=0
    def __init__(self,vehicle_id,vehicle_type,capacity):
        self.vehicle_id=vehicle_id
        self.vehicle_type=vehicle_type
        self.capacity=capacity
        Vehicle.total_vehicles+=1
    @classmethod
    def get_total_vehicles(cls):
        print(cls.total_vehicles)
    @staticmethod
    def validate_method(vehicle_id):
        return vehicle_id[:5] == "TS33G"
    def display_info(self):
        print("Vehicle type:",self.vehicle_type)
        print("Vehicle id:",self.vehicle_id)
        print("Capacity:",self.capacity)

class Bus(Vehicle):
    def __init__(self,vehicle_id,capacity,route_no,has_ac=False):
        super().__init__(vehicle_id, "Bus", capacity)
        self.route_no=route_no
        self.has_ac=has_ac
    def __str__(self):
        return f"Bus[{self.vehicle_id}]|Route:{self.route_no}|Capacity:{self.capacity}|AC:{'Yes' if self.has_ac else 'No'}"
    def __repr__(self):
         return f"Bus(vehicle_id='{self.vehicle_id}',route={self.route_no},capacity={self.capacity})"
    def display_route_info(self):
        print("Route Number :",self.route_no)
        print("AC Available :","Yes" if self.has_ac else "No")
    def display_info(self):
        print(self)
        self.display_route_info()
class MiniVan(Vehicle):
    def __init__(self,vehicle_id,capacity,trip_purpose):
        super().__init__(vehicle_id,"MiniVan",capacity)
        self.trip_purpose=trip_purpose
    def __str__(self):
        return f"MiniVan [{self.vehicle_id}] | Purpose: {self.trip_purpose}"
    def __repr__(self):
        return f"MiniVan(vehicle_id='{self.vehicle_id}',purpose='{self.trip_purpose}')"
    def display_info(self):
        print(self)
        print("Capacity :",self.capacity)
