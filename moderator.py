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
    """this function gets the formatted time and date"""
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


def initialize_data(cursor, mod_email, line):
    current_time, current_date = get_time_date()
    name_user, message, date_message, time_message, station = line.strip().split(", ")

    user_input = input(f"Is this text by {name_user} valid: {message}: ")
    # if moderator agrees that the text is valid it will be writen into the database
    if is_yes(user_input):

        # if the random station is already in the DB it will not write it to it
        if is_station_in_db(cursor, station) is False:
            cursor.execute("INSERT INTO station (station_name) VALUES (%s)", (station,))

        # insert user data into the ns_user table
        insert_script = ("INSERT INTO ns_user (name_column, date_column,"
                         "time_column, message_column, station_name, mod_email, mod_date, mod_time) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        # The values that will be written to its respectable columns
        insert_values = (name_user, date_message, time_message,
                         message, station, mod_email, current_date, current_time)
        cursor.execute(insert_script, insert_values)
        return True, user_input
    return False, user_input


def write_data(cursor, filename, email):
    exit_bool = False
    with open(filename) as csv_file:
        all_messages = csv_file.readlines()
        print(all_messages)
        while not exit_bool:
            for line in csv_file:
                bool_approved, user_input = initialize_data(cursor, email, line)
                if bool_approved:
                    connection.commit()
                    # all_messages.remove(f"{line}\\n")
                    # print(all_messages)
                elif user_input.lower() == "exit":
                    exit_bool = True
                    break


def write_to_db(filename):
    if file_not_empty():

        email = input("before moderating could enter your email: ")

        cursor = connection.cursor()
        write_data(cursor, filename, email)
        cursor.close()
        connection.close()
    else:
        print("there is no data to moderate")


write_to_db(file_messages)
