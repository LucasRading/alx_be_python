# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # Optional return if needed in future calculations

# Part 2: Calculate a future date
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Run the script
if __name__ == "__main__":
    # Show current date and time
    display_current_datetime()
    
    # Prompt user for number of days
    try:
        user_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
