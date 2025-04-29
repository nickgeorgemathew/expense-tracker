import csv
from datetime import datetime, timedelta
import random

start_date = datetime(2024, 4, 28, 10, 0, 0)
num_days = 365 * 2
categories = ["Food", "Transport", "Entertainment", "Utilities", "Health", "Education", "Misc"]
descriptions = ["Lunch", "Bus fare", "Movie", "Electricity bill", "Doctor visit", "Books", "Gift"]

with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Amount", "Category", "Description"])
    for i in range(num_days):
        date = start_date + timedelta(days=i)
        for _ in range(random.randint(1, 3)):
            date_str = date.strftime("%d/%m/%y,%H:%M:%S")
            amount = round(random.uniform(10, 500), 2)
            category = random.choice(categories)
            description = random.choice(descriptions)
            writer.writerow([date_str, amount, category, description])
