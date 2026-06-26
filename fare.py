from abc import ABC,abstractmethod

class FareCalculator(ABC):
    def __init__(self,student_id,distance_km):
        self.student_id=student_id
        self.distance_km=distance_km

    @abstractmethod
    def calculate_fare(self):
        pass

    @abstractmethod
    def display_fare_summary(self):
        pass

    def apply_discount(self,amount,discount_percent):
        return amount-(amount*discount_percent/100)


class RouteFare(FareCalculator):
    def __init__(self,student_id,distance_km,pass_type):
        super().__init__(student_id,distance_km)
        self.pass_type=pass_type

    def calculate_fare(self):
        if self.pass_type=="Monthly":
            return self.distance_km*2.5
        elif self.pass_type=="Semester":
            return self.distance_km*12
        else:
            return 0

    def display_fare_summary(self):
        fare=self.calculate_fare()
        print("Student ID:",self.student_id)
        print("Distance:",self.distance_km)
        print("Pass Type:",self.pass_type)
        print("Fare:",fare)


class SpecialTripFare(FareCalculator):
    def __init__(self,student_id,distance_km,num_students):
        super().__init__(student_id,distance_km)
        self.num_students=num_students

    def calculate_fare(self):
        total=self.distance_km*5*self.num_students
        return total/self.num_students

    def display_fare_summary(self):
        fare=self.calculate_fare()
        print("Student ID:",self.student_id)
        print("Distance:",self.distance_km)
        print("Students:",self.num_students)
        print("Fare per Student:",fare)