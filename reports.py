from collections import defaultdict

def generate_report(expenses):
    total = 0
    category_totals = defaultdict(float)

    for amount, category, _, _ in expenses:
        amount = float(amount)
        total += amount
        category_totals[category] += amount

    average = total / len(expenses) if expenses else 0

    with open("summary_report.txt", "w") as file:
        file.write(f"Total Expense: {total}\n")
        file.write(f"Average Expense: {average:.2f}\n\n")
        file.write("Category-wise Expenses:\n")
        for cat, amt in category_totals.items():
            file.write(f"{cat}: {amt}\n")
