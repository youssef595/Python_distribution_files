import os
import datetime

# Get today's date as a string in the format "YYYY-MM-DD"
today_date = datetime.date.today().strftime('%Y-%m-%d')
def function2(today_date):
    # Create a path for the new folder
    new_folder_path = os.path.join('data', today_date)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)