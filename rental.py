
class Rental:
    def __init__(self,rental_id, customer, vehicle, rental_days):

        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        self.rental_id = rental_id
        self.customer = customer
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.actual_days = None
        self.status = "ACTIVE"
        self.base_cost = self.vehicle.calculate_rental_cost(rental_days)
        self.late_fee = 0
        self.damage_charge = 0
        self.__paid = False


    def calculate_late_fee(self):
        late_days = max(0, self.actual_days - self.rental_days)
        return round(late_days * 0.20 * self.vehicle.daily_rate)


    def calculate_total(self):
        return self.base_cost + self.late_fee + self.damage_charge


    def complete_rental(self, actual_days, damage_charge = 0):
        if self.status == "COMPLETED":
            raise ValueError("This rental has already been completed.")
        
        if self.damage_charge < 0:
            raise ValueError("Damage charge must be greater than 0")

        self.actual_days = actual_days
        self.damage_charge = damage_charge

        self.late_fee = self.calculate_late_fee()

        self.status = "COMPLETED"


    def mark_as_paid(self):
        if not self.status == "COMPLETED":
            raise ValueError(" A rental can only be paid after it is completed.")

        if self.__paid:
            raise ValueError("This rental has already been paid.")
        self.__paid = True

        


    def is_paid(self):
        return self.__paid



    def display_rental_details(self):
        print(f"=" * 36)
        print("           SAFARIDRIVE RENTALS")
        print(f"=" * 36)
        print(f"Rental ID:        {self.rental_id}")
        print(f"Customer:         {self.customer.name}")
        print(f"Vehicle:          {self.vehicle.make} {self.vehicle.model}")
        print(f"Registration:     {self.vehicle.registration_number}")
        print(f"Rental Period:    {self.rental_days} days")
        print(f"Daily Rate:       KSh {self.vehicle.daily_rate:,}")
        print(f"Base Cost:        KSh {self.base_cost:,}")
        print(f"Late Fee:         KSh {self.late_fee:,}")
        print(f"Damage Charge:    KSh {self.damage_charge:,}")
        print("-" * 36)
        print(f"TOTAL:            KSh {self.calculate_total():,}")
        print(f"Status:           {self.status}")

        print(f"=" * 36)
       





