# from vehicle import Vehicle, EconomyCar,SUV,LuxuryCar


# # axio = EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000)
# # prado = SUV("KDJ 456B", "Toyota", "Prado", 2023, 8000)
# # merc = LuxuryCar("KDL 789C", "Mercedes-Benz", "E-Class", 2024, 15000)

# # for car in [axio, prado, merc]:
# #     print(f"{car.make} {car.model}: KSh {car.calculate_rental_cost(3):,}")


# axio = EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000)

# print(axio.is_available())   # what do you expect here?

# axio.mark_as_rented()
# print(axio.is_available())   # and here?

# axio.mark_as_available()
# print(axio.is_available())   # and here?

# # 1. Polymorphism: expect 12,000 / 26,000 / 49,500
# prado = SUV("KDJ 456B", "Toyota", "Prado", 2023, 8000)
# merc = LuxuryCar("KDL 789C", "Mercedes-Benz", "E-Class", 2024, 15000)

# for car in [axio, prado, merc]:
#     print(f"{car.make} {car.model}: KSh {car.calculate_rental_cost(3):,}")

# # 2. Negative rate: expect a clear error message, not a crash
# try:
#     EconomyCar("KDK 999Z", "Toyota", "Vitz", 2020, -500)
# except ValueError as error:
#     print(f"Error: {error}")

# # 3. Abstraction: expect a message, not a crash
# try:
#     Vehicle("KDK 123A", "Toyota", "Axio", 2022, 4000)
# except TypeError as error:
#     print(f"Error: {error}")


# axio.display_details()
# print()
# axio.mark_as_rented()
# axio.display_details()


from customer import Customer

# Checking valid customer
john = Customer("COO1", "John Kamau", "0712345678","12345678", "DL45821")
john.display_details()

# New customer has no history
john.view_rental_history()

# add_rental changes state
john.add_rental("test rental")
john.view_rental_history()

# Missing licence is rejected
for bad_licence in ["", "   "]:
    try:
        Customer("C002", "Jane Wanjiru", "0722222222", "87654321", bad_licence)
    except ValueError as error:
        print(f"Error: {error}")