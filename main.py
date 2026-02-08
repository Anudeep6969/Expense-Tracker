from Expense import Expense
from utils import validate_amount, validate_date, validate_text
from file_manager import save_expense, read_expenses, backup_data, restore_data
from reports import generate_report
from menu import show_menu

def main():
    while True:
        choice = show_menu()

        try:
            if choice == "1":
                amount = validate_amount(input("Amount: "))
                category = validate_text(input("Category: "))
                date = validate_date(input("Date (YYYY-MM-DD): "))
                description = validate_text(input("Description: "))

                expense = Expense(amount, category, date, description)
                save_expense(expense)
                print("Expense added successfully ✅")

            elif choice == "2":
                expenses = read_expenses()
                generate_report(expenses)
                print("Report generated 📊")

            elif choice == "3":
                backup_data()
                print("Backup completed 💾")

            elif choice == "4":
                restore_data()
                print("Data restored 🔄")

            elif choice == "5":
                print("Goodbye 👋")
                break

            else:
                print("Invalid option ❌")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
