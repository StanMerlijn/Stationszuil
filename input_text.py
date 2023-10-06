import random
from datetime import datetime


def is_input_yes(input_text):
    yes_bool = "yesYesYy1jaJajJOKok"
    return input_text in yes_bool


def get_time_date():
    """this function gets the formatted time and date"""
    date = datetime.now().date()
    time = datetime.now().time().strftime("%X")
    return time, date


def collect_user_input():
    print("-" * 50)
    if is_input_yes(input(f"do you want to write a message (yes or no): ")):
        if is_input_yes(input("Do you want to use your name (yes or no): ")):
            name = input("What is your name: ")
        else:
            name = "anonymous"
        with open("stations.txt") as file:
            stations = [line.strip() for line in file]
        random_station = random.choice(stations)  # chooses a random station from file
        message = input("write your message here: ")
        return name, message, random_station

    return False


def write_data_to_file(output_file):
    while True:
        time_now, date_now = get_time_date()
        user_data = collect_user_input()
        if user_data:
            name, message, random_station = user_data
            if len(message) >= 140:
                print("your message should be less than 140 characters")
            else:
                with open(output_file, "a") as csv_file:
                    csv_file.write(f"{name}, {message}, {date_now}, {time_now}, {random_station}\n")
        else:
            break


if __name__ == "__main__":
    file_messages = "text.csv"
    write_data_to_file(file_messages)
