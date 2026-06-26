from transport_manager import TransportManager
from vehicles import Bus,MiniVan
from drivers import Driver
from fare import RouteFare,SpecialTripFare

def display_main_menu():
    print("\n"+"="*55)
    print("ACE Engineering College Transportation Portal")
    print("="*55)
    print("1.Add New Bus")
    print("2.Add New MiniVan")
    print("3.Add New Driver")
    print("4.Display All Vehicles")
    print("5.Display All Drivers")
    print("6.Calculate Route Fare")
    print("7.Calculate Special Trip Fare")
    print("8.Search Vehicle by ID")
    print("9.Display Dashboard")
    print("0.Exit")

def main():
    manager=TransportManager("Mr.Ramesh")

    while True:
        display_main_menu()
        choice=input("Enter your choice:")

        if choice=="1":
            vehicle_id=input("Enter Vehicle ID:")
            capacity=int(input("Enter Capacity:"))
            route_no=int(input("Enter Route Number:"))
            ac=input("AC Bus?(yes/no):").lower()
            has_ac=True if ac=="yes" else False

            if Bus.validate_method(vehicle_id):
                bus=Bus(vehicle_id,capacity,route_no,has_ac)
                manager.add_bus(bus)
            else:
                print("Invalid Vehicle ID")

        elif choice=="2":
            vehicle_id=input("Enter Vehicle ID:")
            capacity=int(input("Enter Capacity:"))
            purpose=input("Enter Trip Purpose:")
            van=MiniVan(vehicle_id,capacity,purpose)
            manager.add_minivan(van)

        elif choice=="3":
            driver_id=input("Enter Driver ID:")
            name=input("Enter Driver Name:")
            license_number=input("Enter License Number:")
            contact=input("Enter Contact:")
            driver=Driver(driver_id,name,license_number,contact)
            manager.add_driver(driver)

        elif choice=="4":
            manager.display_all_vehicles()

        elif choice=="5":
            manager.display_all_drivers()

        elif choice=="6":
            student_id=input("Enter Student ID:")
            distance=float(input("Enter Distance:"))
            pass_type=input("Enter Pass Type:")
            fare=RouteFare(student_id,distance,pass_type)
            fare.display_fare_summary()

        elif choice=="7":
            student_id=input("Enter Student ID:")
            distance=float(input("Enter Distance:"))
            num_students=int(input("Enter Number of Students:"))
            fare=SpecialTripFare(student_id,distance,num_students)
            fare.display_fare_summary()

        elif choice=="8":
            vehicle_id=input("Enter Vehicle ID:")
            manager.search_vehicle(vehicle_id)

        elif choice=="9":
            manager.display_dashboard()

        elif choice=="0":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

if __name__=="__main__":
    main()