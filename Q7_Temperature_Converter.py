

def temperature_converter():

    while True:
        print("\n===== TEMPERATURE CONVERTER =====")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 7:
                print("Exiting program...")
                break

            temperature_value = float(input("Enter temperature value: "))

            # Perform conversion based on choice
            if user_choice == 1:
                result = (temperature_value * 9/5) + 32
            elif user_choice == 2:
                result = (temperature_value - 32) * 5/9
            elif user_choice == 3:
                result = temperature_value + 273.15
            elif user_choice == 4:
                result = temperature_value - 273.15
            elif user_choice == 5:
                result = (temperature_value - 32) * 5/9 + 273.15
            elif user_choice == 6:
                result = (temperature_value - 273.15) * 9/5 + 32
            else:
                print("Invalid choice.")
                continue

            print("Converted Temperature:", round(result, 2))

        except Exception:
            print("Invalid input! Please try again.")
#call the function 
temperature_converter()