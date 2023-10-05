import random
from datetime import datetime

file_messages = "text.csv"


def is_yes(input_text):
    yes_bool = "yesYesYy1jaJajJOKok"
    return input_text in yes_bool


def get_time_date():
    """this function gets the formatted time and date"""
    date = datetime.now().date()
    time = datetime.now().time().strftime("%X")
    return time, date


def collect_write_message(output_file):
    while True:
        time_now, date_now = get_time_date()
        if is_yes(input("do you want to write a message? ")):
            if is_yes(input("Do you want to use your name(yes or no): ")):
                name = input("What is your name: ")
            else:
                name = "anonymous"

            with open("stations.txt") as file:
                stations = [line.strip() for line in file]
            random_station = random.choice(stations)

            # here the user inputs there message
            message = input("write your message here: ")
            if len(message) >= 140:
                print("your message should be less than 140 characters")
            else:
                with open(output_file, "a") as csv_file:
                    csv_file.write(f"{name}, {message}, {date_now}, {time_now}, {random_station}\n")
            return True
        return False


# def write_data_to_file(name, message, random_station, outputfile):


print(collect_write_message(file_messages))
