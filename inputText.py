import random
from datetime import datetime

yes_bool = "yesYesYy1jaJa"

def get_time_date():
    """this function retrieves the current time and date when called"""
    current_date = datetime.now().date()
    current_time = datetime.now().time().strftime("%X")
    return current_time, current_date


while True:

    randomNr = int(random.random())
    wants_write = input("do you want to write a message? ")
    time_now, date_now = get_time_date()
    # checks if user wants to write a message. and if the user wants to input his/her name
    if wants_write in yes_bool:
        wantsName = input("Do you want to use your name(yes or no): ")
        if wantsName in yes_bool:
            name = input("What is your name: ")
        else:
            name = "anonymous"
        with open("stations.txt", "r") as file:
            lines = file.readlines()
        random_line_number = random.randint(0, len(lines) - 1)
        station = lines[random_line_number].strip()

        # here the user inputs there message
        message = input("write your message here: ")
        if len(message) >= 140:
            print("your message should be less than 140 characters")
            message = input("write your message here again: ")
        if len(message) <= 140:
            with open("text.txt", "a") as file:
                file.write(f"{name}, {message}, {date_now}, {time_now}, {station}\n")
    else:
        break
