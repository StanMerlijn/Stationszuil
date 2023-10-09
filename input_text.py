import random
import psycopg2
from datetime import datetime


def connect_to_db():
    # connecting to the database. local
    connection = psycopg2.connect(
        host="localhost",
        database="NS messages",
        user="postgres",
        password="Whynow3421!"
    )
    return connection


def is_station_in_db(cursor, station_name):
    """"boolean function to check if a station is already in the database"""
    cursor.execute("SELECT COUNT(*) FROM station WHERE station_name = %s", (station_name,))
    data = cursor.fetchone()[0]
    return data > 0


def clear_file(filename):
    with open(filename, "w") as file:
        file.truncate()


def is_input_yes(input_text):
    yes_bool = ["yes", "y", "ye"]
    return input_text.lower() in yes_bool


def get_time_date():
    """this function gets the formatted time and date"""
    date = datetime.now().date()
    time = datetime.now().time().strftime("%X")
    return time, date


def prepare_message_data(cursor, message_data):
    random_station = message_data[4]
    # data to insert into DB
    insert_script = ("INSERT INTO ns_user (name_column, date_column, time_column, "
                     "message_column, station_name, bool_approved)"
                     "VALUES (%s, %s, %s, %s, %s, %s)")
    if not is_station_in_db(cursor, random_station):
        cursor.execute("INSERT INTO station (station_name) VALUES (%s)", (random_station,))

    return insert_script


def collect_user_input():
    time_now, date_now = get_time_date()
    print("-" * 50)
    if is_input_yes(input(f"do you want to write a message (yes or no): ")):
        bool_approved = False

        if is_input_yes(input("Do you want to use your name (yes or no): ")):
            name = input("What is your name: ")
        else:
            name = "anonymous"
        with open("stations.txt") as file:
            stations = [line.strip() for line in file]
        random_station = random.choice(stations)  # chooses a random station from file
        message = input("write your message here: ")

        message_data = name, date_now, time_now, message, random_station, bool_approved
        return True, message_data
    return False, None


def write_data_to_file(output_file):
    while True:
        user_data = collect_user_input()
        if user_data:
            name, message, random_station, time_now, date_now = user_data
            if len(message) >= 140:
                print("your message should be less than 140 characters")
            else:
                with open(output_file, "a") as csv_file:
                    csv_file.write(f"{name}, {message}, {date_now}, {time_now}, {random_station}\n")
        else:
            break


def write_data_to_db():
    while True:
        bool_val, message_data = collect_user_input()

        if bool_val:
            with connect_to_db() as connection, connection.cursor() as cursor:
                insert_script = prepare_message_data(cursor, message_data)
                cursor.execute(insert_script, message_data)
                connection.commit()
        else:
            break


if __name__ == "__main__":
    file_messages = "text.csv"
    # write_data_to_file(file_messages)
    write_data_to_db()

