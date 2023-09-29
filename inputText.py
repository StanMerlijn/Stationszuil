import random
import csv
from datetime import datetime

yes_bool = "yesYesYy1jaJajJOKok"


# creating a function to get the current time and date.
def get_time_date():
    current_date = datetime.now().date()
    current_time = datetime.now().time().strftime("%X")
    return current_time, current_date


while True:
    randomNr = int(random.random())
    wants_write = input("do you want to write a message? ")
    time_now, date_now = get_time_date()
    if wants_write in yes_bool:
        wantsName = input("Do you want to use your name(yes or no): ")
        if wantsName in yes_bool:
            name = input("What is your name: ")
        else:
            name = "anonymous"
        with open("stations.txt", "r") as file:
            lines = file.readlines()
        # generates a random number under the amount of lines in stations.txt. then retrieves a that random station
        random_line_number = random.randint(0, len(lines) - 1)
        station = lines[random_line_number].strip()

        # here the user inputs there message
        message = input("write your message here: ")
        if len(message) >= 140:
            print("your message should be less than 140 characters")
        if len(message) <= 140:

            fieldnames = ['name', 'message', 'date', 'time', 'station']

            data_for_file = {"ame": name, "message": message, "date": date_now, "time": time_now, "station": station}
            with open("text.csv", "w", newline='') as csv_file:
                if csv_file.tell() == 0:
                    writer = csv.writer(csv_file)
                    writer.writerow(fieldnames)

                writer.writerow(data_for_file)
    else:
        break

