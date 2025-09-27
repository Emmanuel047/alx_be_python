import datetime
from datetime import timedelta

current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {current_date}")

def display_current_datetime():
    Choice = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.datetime.now() + timedelta(days=Choice)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return

display_current_datetime()