import random
import time

import psycopg2
from datetime import datetime


# Function to connect to the database
def connect_to_db():
    # Prompting for the database password
    while True:
        try:
            db_password = input("DB password: ")

            # Establishing a connection to the PostgreSQL database
            connection = psycopg2.connect(
                host="20.68.149.147",
                database="NS_messages",
                user="postgres",
                password=db_password
            )
            return connection
        except psycopg2.OperationalError as error:
            print("Error:", str(error))
            print("Invalid password. Please try again.")


# Function to clear a file
def clear_file(filename):
    with open(filename, "w") as file:
        file.truncate()


# Function to check if input corresponds to 'yes'
def is_input_yes(input_text):
    yes_bool = ["yes", "y", "ye"]
    return input_text.lower() in yes_bool


# Function to generate a unique ID
def generate_user_id():
    return random.randint(1, 11)


def get_message_ids(cursor):
    cursor.execute("SELECT message_id FROM message_send")
    data_ids = cursor.fetchall()
    message_ids = []

    for i in data_ids:
        for ids in i:
            message_ids.append(ids)
    return message_ids


def create_new_id(ids):
    while True:
        new_id = generate_user_id()
        if new_id not in ids:
            return new_id


# Function to get the current time and date
def get_time_date():
    """this function gets the formatted time and date"""
    date = datetime.now().date()
    time = datetime.now().time().strftime("%X")
    return time, date


def get_random_station(cursor):
    cursor.execute("SElECT (station_city) FROM station_service")
    row_data = cursor.fetchall()
    stations = [row[0] for row in row_data]
    random_station = random.choice(stations)
    return random_station


# Function to prepare the message data for insertion into the database
def prepare_message_data():
    insert_script = ("INSERT INTO message_send (name_user, date_message, time_message, "
                     "message_column, station_name, message_id)"
                     "VALUES (%s, %s, %s, %s, %s, %s)")
    return insert_script


# Function to write message data to the database
def write_data_to_db(cursor, message_data):
    insert_script = prepare_message_data()
    cursor.execute(insert_script, message_data)


def main_gui(cursor, name, message):
    # getting all data to insert into database
    time_now, date_now = get_time_date()
    random_station = get_random_station(cursor)

    # creating new unique message id
    message_ids = get_message_ids(cursor)
    message_id = create_new_id(message_ids)

    message_data = name, date_now, time_now, message, random_station, message_id
    write_data_to_db(cursor, message_data)


if __name__ == "__main__":
    with connect_to_db() as conn, conn.cursor() as cur:
        print(get_message_ids(cur))
