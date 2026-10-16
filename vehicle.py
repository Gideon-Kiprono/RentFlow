from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,registration_number, make, model, year, daily_rate):
        if daily_rate < 0:
            raise ValueError("Daily rate cannot be negative")

        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.__available = True   # private(Encapsulation concept)


    def display_details(self):
        status = "Available" if self.is_available() else "Rented"
        print(f"Type :                 {type(self).__name__}")
        print(f"Registration :         {self.registration_number}")
        print(f"Vehicle :              {self.make} {self.model} ({self.year})")
        print(f"Daily Rate :           Ksh {self.daily_rate:,}")
        print(f"Status :               {status}")

    
    def is_available(self):
        return self.__available

    def mark_as_rented(self):
        self.__available = False

    def mark_as_available(self):
        self.__available = True

    def extra_charge(self, days):
        return None

    

    @abstractmethod
    def calculate_rental_cost(self,days):
        pass

# Children classes
# Child class (Economy)
class EconomyCar(Vehicle):

    def calculate_rental_cost(self,days):
        return self.daily_rate * days

       
        

# Child class (SUV)

class SUV(Vehicle):

    SERVICE_CHARGE = 2000
    # calculate_rental_cost() method
    def calculate_rental_cost(self,days):
        return self.daily_rate * days + self.SERVICE_CHARGE

    def extra_charge(self, days):  
            return ("Service Charge", self.SERVICE_CHARGE)

# Child class (LUXURY)
class LuxuryCar(Vehicle):

    INSURANCE_RATE = 0.10

        # calculate_rental_cost() method
    def calculate_rental_cost(self,days):
        rental_charge = self.daily_rate * days
        insurance = rental_charge * self.INSURANCE_RATE
        return round(rental_charge + insurance)

    def extra_charge(self, days):
        amount = round(self.daily_rate * days * self.INSURANCE_RATE)
        return ("Insurance (10%)", amount)


