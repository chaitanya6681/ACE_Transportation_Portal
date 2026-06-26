from vehicles import Bus,MiniVan
from drivers import Driver

class TransportManager:
    def __init__(self,manager_name):
        self.manager_name=manager_name
        self.buses=[]
        self.mini_vans=[]
        self.drivers=[]

    def add_bus(self,bus_obj):
        if isinstance(bus_obj,Bus):
            self.buses.append(bus_obj)

    def add_minivan(self,van_obj):
        if isinstance(van_obj,MiniVan):
            self.mini_vans.append(van_obj)

    def add_driver(self,driver_obj):
        if isinstance(driver_obj,Driver):
            self.drivers.append(driver_obj)

    def display_all_vehicles(self):
        all_vehicles=self.buses+self.mini_vans
        for vehicle in all_vehicles:
            vehicle.display_info()

    def display_all_drivers(self):
        for driver in self.drivers:
            driver.display_info()

    def search_vehicle(self,vehicle_id):
        all_vehicles=self.buses+self.mini_vans
        for vehicle in all_vehicles:
            if vehicle.vehicle_id==vehicle_id:
                vehicle.display_info()
                return
        print("Vehicle not found")

    def display_dashboard(self):
        print("Manager Name:",self.manager_name)
        print("Total Buses:",len(self.buses))
        print("Total MiniVans:",len(self.mini_vans))
        print("Total Drivers:",len(self.drivers))