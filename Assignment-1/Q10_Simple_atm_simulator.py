
def atm_simulator():
   
    balance = 10000
    transaction_history = []

    # Keep showing menu until user chooses Exit
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. View Transaction History\n5. Exit")
        choice = input("Enter choice: ")

        # Option 1: display current balance
        if choice == "1":
            print("Current Balance:", balance)
            transaction_history.append(f"Balance checked: ₹{balance}")

        # Option 2: Add money to account
        elif choice == "2":
            try:
                deposit_amount = float(input("Enter amount to deposit: "))
                balance += deposit_amount
                print("Updated Balance:", balance)
                transaction_history.append(f"Deposited: ₹{deposit_amount} | Balance: ₹{balance}")
            except:
                print("Invalid input.")

        # Option 3: Withdraw money while keeping minimum ₹500 balance
        elif choice == "3":
            try:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if balance - withdraw_amount >= 500:
                    balance -= withdraw_amount
                    print("Withdrawal successful.")
                    print("Updated Balance:", balance)
                    transaction_history.append(f"Withdrew: ₹{withdraw_amount} | Balance: ₹{balance}")
                else:
                    print("Minimum ₹500 balance required.")
                    transaction_history.append(
                        f"Withdrawal failed (₹{withdraw_amount}) | Balance unchanged: ₹{balance}"
                    )
            except:
                print("Invalid input.")

        # Option 4: Show complete transaction history
        elif choice == "4":
            if transaction_history:
                print("\n===== TRANSACTION HISTORY =====")
                for index, record in enumerate(transaction_history, start=1):
                    print(f"{index}. {record}")
            else:
                print("No transactions yet.")

        # Option 5: Exit the ATM simulator loop
        elif choice == "5":
            break
        else:
            # Handles choices other than 1, 2, 3, 4, or 5
            print("Invalid choice.")

# calling the function
atm_simulator()