
from rental import Rental
from vehicle import EconomyCar, SUV, LuxuryCar

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


    def search_vehicles(self, vehicle_type=None, max_daily_rate=None):
            types = {"Economy": EconomyCar, "SUV": SUV, "Luxury": LuxuryCar}

            if vehicle_type is not None and vehicle_type not in types:
                raise ValueError(f"Unknown vehicle type: {vehicle_type}")

            found = False
            for vehicle in self.vehicles:
                if not vehicle.is_available():
                    continue
                if vehicle_type is not None and not isinstance(vehicle, types[vehicle_type]):
                    continue
                if max_daily_rate is not None and vehicle.daily_rate > max_daily_rate:
                    continue

                found = True
                print(f"{vehicle.make} {vehicle.model}")
                print(f"   Registration: {vehicle.registration_number}")
                print(f"   Rate: KSh {vehicle.daily_rate:,}/day")

            if not found:
                print("No vehicles match your search.")
        


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





    def show_active_rentals(self):
        print("ACTIVE RENTALS")
        found = False
        for rental in self.rentals:
            if rental.status == "ACTIVE":
                found = True
                print(f"{rental.rental_id}: {rental.customer.name} has "
                f"{rental.vehicle.make} {rental.vehicle.model}"
                f"({rental.vehicle.registration_number}) for "
                f"{rental.rental_days} days")
        if not found:
            print("No active rentals")


    def show_completed_rentals(self):
        print("COMPLETED RENTALS")
        found = False
        for rental in self.rentals:
            if rental.status == "COMPLETED":
                found = True
                print(f"{rental.rental_id}: {rental.customer.name} has "
                      f"{rental.vehicle.make} {rental.vehicle.model}"
                      f"({rental.vehicle.registration_number}) for "
                      f"{rental.rental_days} days "
                      f"total KSh {rental.calculate_total():,}, paid: {rental.is_paid()}")
        if not found:
            print("No active rentals")

    def process_payment(self,payment):
        if payment.rental.status  != "COMPLETED":
            raise ValueError("A rental can only be paid after it is completed.")

        if payment.rental.is_paid():
            raise ValueError("This rental has already been paid.")

        success = payment.process_payment()

        if success:
            payment.rental.mark_as_paid()
            self.__revenue += payment.amount
            self.payments.append(payment)


        return success
                      



