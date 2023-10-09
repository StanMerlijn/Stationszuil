import psycopg2
from input_text import get_time_date, is_input_yes, clear_file


def connect_to_db():
    # connecting to the database. local
    connection = psycopg2.connect(
        host="localhost",
        database="NS messages",
        user="postgres",
        password="Whynow3421!"
    )
    return connection


def file_not_empty():
    with open(file_messages) as csv_file:
        lines = csv_file.readlines()
        return len(lines) != 0


def write_to_clean_file(filename, data_to_file):
    with open(filename, "w") as csv_file:
        for item in data_to_file:
            csv_file.write(f"{item}\n")


def is_station_in_db(cursor, station_name):
    """"boolean function to check if a station is already in the database"""
    cursor.execute("SELECT COUNT(*) FROM station WHERE station_name = %s", (station_name,))
    data = cursor.fetchone()[0]
    return data > 0


def prepare_user_data(line, mod_email):
    current_time, current_date = get_time_date()
    name_user, message, date_message, time_message, station = line.strip().split(", ")

    insert_script = ("INSERT INTO ns_user (name_column, date_column,"
                     "time_column, message_column, station_name, mod_email, mod_date, mod_time) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    # The values that will be written to its respectable columns
    insert_values = (name_user, date_message, time_message,
                     message, station, mod_email, current_date, current_time)
    return insert_script, insert_values


def initialize_data(cursor, mod_email, line):
    name_user, message, date_message, time_message, station = line.strip().split(", ")

    user_input = input(f"Is this text by {name_user} valid: {message}: ")
    # if moderator agrees that the text is valid it will be writen into the database
    if is_input_yes(user_input):

        # if the random station is already in the DB it will not write it to it
        if not is_station_in_db(cursor, station):
            cursor.execute("INSERT INTO station (station_name) VALUES (%s)", (station,))

        # insert user data into the ns_user table
        insert_script, insert_value = prepare_user_data(line, mod_email)
        cursor.execute(insert_script, insert_value)
        return True, user_input
    return False, user_input


def write_data(connection, cursor, filename, email):
    with open(filename) as csv_file:
        all_messages = [line.strip() for line in csv_file.readlines()]

    len_messages = len(all_messages)
    lines_index = 0

    while lines_index < len_messages:
        line = all_messages[lines_index]
        bool_approved, user_input = initialize_data(cursor, email, line)

        # commits to DB if message = valid
        if bool_approved:
            connection.commit()

        # clears file if all messages are moderated
        if (lines_index + 1) == len_messages:
            print("There no more messages to moderate")
            clear_file(filename)

        # if user inputs exit when asked if text valid it will return every message back to file
        if user_input.lower() == "exit":
            data_back_to_file = all_messages[lines_index:]
            write_to_clean_file(filename, data_back_to_file)
            break

        lines_index += 1


def send_data(filename):
    if file_not_empty():

        email = input("before moderating could enter your email: ")
        with connect_to_db() as connection, connection.cursor() as cursor:
            write_data(connection, cursor, filename, email)
    else:
        print("there is no data to moderate")


if __name__ == "__main__":
    file_messages = "text.csv"
    send_data(file_messages)
