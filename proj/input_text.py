import random
import psycopg2
from datetime import datetime
import time


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


# Bool function to check if the id is already in the database
def is_user_id_unique(user_id, cursor):
    cursor.execute("SELECT COUNT(*) FROM message_send WHERE message_id=%s", (user_id,))
    count = cursor.fetchone()[0]
    return count == 0


# Function to generate a unique ID
def generate_user_id():
    return random.randint(1, 999999999)


def create_new_id(cursor):
    while True:
        new_id = generate_user_id()
        if is_user_id_unique(new_id, cursor):
            return new_id


# Function to get the current time and date
def get_time_date():
    """this function gets the formatted time and date"""
    date = datetime.now().date()
    time = datetime.now().time().strftime("%X")
    return time, date


# Function to display the date in a specific format and update it every hour
def display_date(label, root, format_date, time_int):
    label.configure(text=f"{time.strftime(format_date, time.localtime())}")
    root.after(time_int, display_date, label, root, format_date, time_int)


# Function to display the clock time in a specific format and update it every minute
def display_clock(label, root, format_time, time_int):
    try:
        label.configure(text=f"{time.strftime(format_time, time.localtime())}")
    except TypeError:
        pass
    root.after(time_int, display_clock, label, root, format_time, time_int)


def get_random_station(cursor):
    cursor.execute("SElECT (station_city) FROM station_service")
    row_data = cursor.fetchall()
    stations = [row[0] for row in row_data]
    random_station = random.choice(stations)
    return random_station


# Function to prepare the message data for insertion into the database
def get_insert_script():
    insert_script = ("INSERT INTO message_send (name_user, date_message, time_message, "
                     "message_column, station_city, message_id)"
                     "VALUES (%s, %s, %s, %s, %s, %s)")
    return insert_script


# Function to write message data to the database
def write_data_to_db(cursor, message_data):
    cursor.execute(get_insert_script(), message_data)


def main_gui(cursor, name, message):
    # getting all data to insert into database
    time_now, date_now = get_time_date()
    random_station = get_random_station(cursor)

    # creating new unique message id
    message_id = create_new_id(cursor)

    message_data = name, date_now, time_now, message, random_station, message_id
    write_data_to_db(cursor, message_data)


