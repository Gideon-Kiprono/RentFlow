class   Customer:
    def __init__(self,customer_id, name, phone_number, national_id,driving_licence):

        if not driving_licence or not str(driving_licence).strip():
            raise ValueError("Driving Licence cannot be empty.")


        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.national_id = national_id
        self.driving_licence = driving_licence

        self.rentals = []

    def display_details(self):
        print(f"--- Customer Profile ({self.customer_id}) ---")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone_number}")
        print(f"National ID: {self.national_id}")
        print(f"Driving Licence: {self.driving_licence}")

    def add_rental(self, rental):
        self.rentals.append(rental)

    def view_rental_history(self):
        if not  self.rentals:
            print(f"No rental history for {self.name}")
            return


        for rental in self.rentals:
                print(rental)
