import csv
from email import header
import shutil
import os

DATA_FILE = "TRACKER.csv"
BACKUP_FILE = "TRACKER_backup.csv"
header = ["Amount", "Category", "Date", "Description"]

def save_expense(expense):
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if os.path.getsize(DATA_FILE) == 0:
            writer.writerow(header)
        writer.writerow(expense.to_list())

def read_expenses():
    expenses = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            reader = csv.reader(file)
        
            
            for row in reader:
                expenses.append(row)
    return expenses

def backup_data():
    shutil.copy(DATA_FILE, BACKUP_FILE)

def restore_data():
    shutil.copy(BACKUP_FILE, DATA_FILE)
