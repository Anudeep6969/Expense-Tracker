from datetime import datetime

def validate_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        raise ValueError("Amount must be a positive number")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def validate_text(text):
    if not text.strip():
        raise ValueError("Input cannot be empty")
    return text.strip()
