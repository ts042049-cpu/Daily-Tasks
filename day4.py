balance = 5000
pin = "1234"
history = []

print("================================")
print("        💳 MINI ATM")
print("================================")

# PIN Login
for attempt in range(3):
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == pin:
        print("\n✅ Login successful!")
        break
    else:
        print("❌ Wrong PIN!")

else:
    print("\n🚫 Too many wrong attempts.")
    exit()


while True:
    print("\n========== ATM MENU ==========")
    print("1. 💰 Check Balance")
    print("2. 💵 Deposit Money")
    print("3. 💸 Withdraw Money")
    print("4. 📜 Transaction History")
    print("5. 🚪 Exit")

    choice = input("\nChoose an option: ")

    # Check Balance
    if choice == "1":
        print(f"\n💰 Current Balance: ₹{balance:.2f}")

    # Deposit
    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: ₹"))

            if amount <= 0:
                print("❌ Enter a valid amount.")
            else:
                balance += amount
                history.append(f"Deposited ₹{amount:.2f}")
                print(f"✅ ₹{amount:.2f} deposited successfully.")

        except ValueError:
            print("❌ Please enter a valid number.")

    # Withdraw
    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("❌ Enter a valid amount.")

            elif amount > balance:
                print("❌ Insufficient balance.")

            else:
                balance -= amount
                history.append(f"Withdrawn ₹{amount:.2f}")
                print(f"✅ ₹{amount:.2f} withdrawn successfully.")

        except ValueError:
            print("❌ Please enter a valid number.")

    # History
    elif choice == "4":
        print("\n📜 TRANSACTION HISTORY")
        print("-----------------------")

        if len(history) == 0:
            print("No transactions yet.")

        else:
            for i, transaction in enumerate(history, 1):
                print(f"{i}. {transaction}")

    # Exit
    elif choice == "5":
        print("\n👋 Thank you for using Mini ATM!")
        print(f"💰 Final Balance: ₹{balance:.2f}")
        break

    else:
        print("❌ Invalid option. Try again.")