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
