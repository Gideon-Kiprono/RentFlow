
from rental import Rental
class CarRentalSystem:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.customers = []
        self.rentals = []
        self.payments = []
        self.__revenue = 0


    def add_vehicle(self, vehicle):
        if self.find_vehicle(vehicle.registration_number):
            raise ValueError("A vehicle with this registration number already exists.")
        self.vehicles.append(vehicle)


    def register_customer(self, customer):
        if self.find_customer(customer.customer_id):
            raise ValueError("A Customer with this customer_id already exists")
        self.customers.append(customer)


    def find_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle
        return None



    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None



    def show_available_vehicles(self):
        print("AVAILABLE VEHICLES")

        for vehicle in self.vehicles:
            if vehicle.is_available():
                vehicle.display_details()
                print("--------")
        


    @property
    def revenue(self):
        return self.__revenue


    def rent_vehicle(self,customer, vehicle, days):
        if not self.find_customer(customer.customer_id):
            raise ValueError("Customer must be registered before renting")
        if not self.find_vehicle(vehicle.registration_number):
            raise ValueError("Vehicle must be registered before renting")
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        if not vehicle.is_available():
            raise ValueError("Vehicle must be available before renting")

        rental_id = f"R{len(self.rentals) + 1:03d}"
        rental = Rental(rental_id, customer, vehicle, days)
        vehicle.mark_as_rented()
        self.rentals.append(rental)
        customer.add_rental(rental)
        return rental
        

    def return_vehicle(self, rental, actual_days, damage_charge=0):
        # Rule 7: the vehicle must currently be rented
        
        if rental.status == "COMPLETED":
            raise ValueError("This rental has already been completed.")
        if rental.vehicle.is_available():
            raise ValueError("This vehicle is not currently rented.")

        # Complete first: if it raises, the car must stay marked as rented
        rental.complete_rental(actual_days, damage_charge)

        # Only then free the car
        rental.vehicle.mark_as_available()
