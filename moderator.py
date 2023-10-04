import psycopg2
from datetime import datetime

# connecting to the database
connection = psycopg2.connect(
    host="localhost",
    database="NS messages",
    user="postgres",
    password="Whynow3421!"
)

file_messages = "text.csv"


def is_yes(input_text):
    yes_bool = "yesYesYy1jaJajJOKok"
    return input_text in yes_bool


def file_not_empty():
    with open(file_messages) as csv_file:
        lines = csv_file.readlines()
        return len(lines) != 0


def get_time_date():
    date = datetime.now().date()
    time = datetime.now().time().strftime("%X")
    return time, date


def clear_file(input_file):
    """"this function clears the file when called"""
    with open(input_file, "w"):
        return


def is_station_in_db(cursor, station_name):
    """"boolean function to check if a station is already in the database"""
    cursor.execute("SELECT COUNT(*) FROM station WHERE station_name = %s", (station_name,))
    data = cursor.fetchone()[0]
    return data > 0


if file_not_empty():
    email = input("before moderating could enter your email: ")


def write_data(cursor, mod_email, line):
    current_time, current_date = get_time_date()
    name_user, message, date_message, time_message, station = line.strip().split(", ")

    # if moderator agrees that the text is valid it will be writen into the database
    if is_yes(input(f"Is this text by {name_user} valid: {message}: ")):

        # if the random station is already in the DB it will not write it to it
        if is_station_in_db(cursor, station) is False:
            cursor.execute("INSERT INTO station (station_name) VALUES (%s)", (station,))

        # insert user data into the ns_user table
        insert_script = ("INSERT INTO ns_user (name_column, mod_email, date_column,"
                         "time_column, message_column, station_name, mod_date, mod_time) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        # The values that will be written to its respectable columns
        insert_values = (name_user, mod_email, date_message, time_message,
                         message, station, current_date, current_time)
        cursor.execute(insert_script, insert_values)
        return True
    return False


def write_to_db(filename):
    cursor = connection.cursor()
    while file_not_empty():
        with open(filename) as csv_file:
            for line in csv_file:
                if write_data(cursor, email, line):
                    connection.commit()
        clear_file(filename)
    cursor.close()
    connection.close()


write_to_db(file_messages)
