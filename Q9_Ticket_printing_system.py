
def ticket_pricing():
    try:
        age = int(input("Enter age: "))
        day = input("Enter day of week: ").lower()
        number_of_tickets = int(input("Enter number of tickets: "))

        # Determine base price
        if age < 3:
            base_price = 0
        elif 3 <= age <= 12:
            base_price = 150
        elif 13 <= age <= 59:
            base_price = 300
        else:
            base_price = 200

        total_price = base_price * number_of_tickets

        # Weekend discount
        if day in ["friday", "saturday", "sunday"]:
            discount = total_price * 0.20
        else:
            discount = 0

        final_price = total_price - discount

        print("Base Price:", total_price)
        print("Discount:", discount)
        print("Final Amount:", final_price)

    except Exception:
        print("Invalid input.")
#calling the function
ticket_pricing()