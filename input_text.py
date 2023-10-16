import random
import psycopg2
from datetime import datetime


# Function to connect to the databasa
def connect_to_db():
    # Prompting for the database password
    db_password = input("DB password: ")

    # Establishing a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host="localhost",
        database="NS messages",
        user="postgres",
        password=db_password
    )
    return connection


# Function to clear a file
def clear_file(filename):
    with open(filename, "w") as file:
        file.truncate()


# Function to check if input corresponds to 'yes'
def is_input_yes(input_text):
    yes_bool = ["yes", "y", "ye"]
    return input_text.lower() in yes_bool


# Function to get the current time and date
def get_time_date():
    """this function gets the formatted time and date"""
    date = datetime.now().date()
    time = datetime.now().time().strftime("%X")
    return time, date


# Function to prepare the message data for insertion into the database
def prepare_message_data():
    insert_script = ("INSERT INTO message_send (name_user, date_message, time_message, "
                     "message, station_name)"
                     "VALUES (%s, %s, %s, %s, %s)")
    return insert_script


# Function to collect user input for writing messages
def collect_user_input():
    time_now, date_now = get_time_date()
    print("-" * 50)

    if is_input_yes(input(f"do you want to write a message (yes or no): ")):

        if is_input_yes(input("Do you want to use your name (yes or no): ")):
            name = input("What is your name: ")
        else:
            name = "anonymous"
        with open("stations.txt") as file:
            stations = [line.strip() for line in file]
        # chooses a random station from file
        random_station = random.choice(stations)
        message = input("write your message here: ")

        message_data = name, date_now, time_now, message, random_station
        return True, message_data
    return False, None


# Function to write message data to a file
def write_data_to_file(output_file):
    while True:
        is_valid, message_data = collect_user_input()
        if is_valid:
            name, date_now, time_now, message, random_station = message_data
            if len(message) >= 140:
                print("your message should be less than 140 characters")
            else:
                with open(output_file, "a") as csv_file:
                    csv_file.write(f"{name}, {message}, {date_now}, {time_now}, {random_station}\n")
        else:
            break


# Function to write message data to the database
def write_data_to_db(cursor, message_data, connection):
    insert_script = prepare_message_data()
    cursor.execute(insert_script, message_data)
    connection.commit()


# Main function
def main(filename):
    where_to_write = int(input("Write to DB else it will be file: "))
    if where_to_write == 1:
        with connect_to_db() as connection, connection.cursor() as cursor:
            while True:
                is_valid, message_data = collect_user_input()
                if is_valid:
                    write_data_to_db(cursor, message_data, connection)
                else:
                    break
    else:
        write_data_to_file(filename)


def main_gui(cursor, connection, name, message):
    time_now, date_now = get_time_date()

    # message_data = name, date_now, time_now, message, random_station
    cursor.execute("SElECT (station_city) FROM station_service")
    row_data = cursor.fetchall()
    stations = [row[0] for row in row_data]
    random_station = random.choice(stations)
    message_data = name, date_now, time_now, message, random_station
    write_data_to_db(cursor, message_data, connection)


if __name__ == "__main__":
    file_messages = "text.csv"
    # main(file_messages)
    main_gui("ass", "cheekcs")
