


def bill_splitter():
    try:
        total_bill_amount = float(input("Enter total bill amount: "))
        number_of_people = int(input("Enter number of people: "))
        tax_percentage = float(input("Enter tax percentage: "))
        tip_percentage = float(input("Enter tip percentage: "))

        if number_of_people <= 0:
            print("Number of people must be greater than 0")
            return

        # Calculate tax
        tax_amount = total_bill_amount * tax_percentage / 100

        # Bill after adding tax
        bill_after_tax = total_bill_amount + tax_amount

        # Calculate tip
        tip_amount = bill_after_tax * tip_percentage / 100

        # Final total
        final_bill = bill_after_tax + tip_amount

        # Per person share
        amount_per_person = final_bill / number_of_people

        print("\n===== BILL BREAKDOWN =====")
        print(f"Subtotal: ₹{total_bill_amount:}")
        print(f"Tax: ₹{tax_amount:}")
        print(f"After Tax: ₹{bill_after_tax:}")
        print(f"Tip: ₹{tip_amount:}")
        print(f"Total Bill: ₹{final_bill:}")
        print(f"Per Person: ₹{amount_per_person:}")

    except ValueError:
        print("Invalid input! Please enter correct values.")
#calling the function
bill_splitter()