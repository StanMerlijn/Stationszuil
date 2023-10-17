import random
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
                     "message, station_name)"
                     "VALUES (%s, %s, %s, %s, %s)")
    return insert_script


# Function to write message data to the database
def write_data_to_db(cursor, message_data, connection):
    insert_script = prepare_message_data()
    cursor.execute(insert_script, message_data)
    connection.commit()


def main_gui(cursor, connection, name, message):
    # getting all data to insert into database
    time_now, date_now = get_time_date()
    random_station = get_random_station(cursor)
    message_data = name, date_now, time_now, message, random_station

    write_data_to_db(cursor, message_data, connection)


if __name__ == "__main__":
    file_messages = "text.csv"
    # main(file_messages)
    # maingui()

