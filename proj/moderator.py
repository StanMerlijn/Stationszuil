from proj.input_text import *
import ttkbootstrap as ttk
import pprint as p
import requests


# Function to check if file is not empty
def file_not_empty():
    with open(file_messages) as csv_file:
        lines = csv_file.readlines()
        return len(lines) != 0


# Function to write data to a clean file
def write_to_clean_file(filename, data_to_file):
    with open(filename, "w") as csv_file:
        for item in data_to_file:
            csv_file.write(f"{item}\n")


# Function to prepare user data for insertion into the database
def prepare_user_data(message_data):
    insert_script = ("INSERT INTO message_mod ("
                     "mod_email, mod_name, "
                     "mod_date, mod_time, "
                     "approval, message_id) "
                     "VALUES (%s, %s, %s, %s, %s, %s)")

    # The data to write to the DB
    insert_values = (*message_data.values(),)
    return insert_script, insert_values


# function to initialize data from gui
def initialize_data_gui(cursor, mod_data, message_id):
    current_time, current_date = get_time_date()
    approval, mod_name, mod_email = mod_data

    message_data = {
        'mod_email': mod_email,
        'mod_name': mod_name,
        'current_date': current_date,
        'current_time': current_time,
        'approval': approval,
        'message_id': message_id
        }

    insert_script, insert_value = prepare_user_data(message_data)
    cursor.execute(insert_script, insert_value)


# Function to initialize data and handle moderation
def initialize_data(cursor, line, mod_data):
    current_time, current_date = get_time_date()
    name_user, message, date_message, time_message, station = line.strip().split(", ")
    mod_name, mod_email = mod_data

    user_input = input(f"Is this text by {name_user} valid: {message}: ")

    # if moderator agrees that the text is valid, it will be written into the database
    if is_input_yes(user_input):
        bool_approved = 1

        message_data = {
            'name_user': name_user,
            'date_message': date_message,
            'time_message': time_message,
            'message': message,
            'station': station,
            'mod_email': mod_email,
            'mod_name': mod_name,
            'current_date': current_date,
            'current_time': current_time,
            'message_id': bool_approved
        }

        # insert user data into the ns_user table
        insert_script, insert_value = prepare_user_data(message_data)
        cursor.execute(insert_script, insert_value)
        return True, user_input

    return False, user_input


# Function to write data to the database or a clean file
def write_data(connection, cursor, filename, mod_data):
    # puts all lines from the csv file into a list
    with open(filename) as csv_file:
        all_messages = [line.strip() for line in csv_file.readlines()]

    len_messages = len(all_messages)
    lines_index = 0

    # when a list is moderated, lines_index will increase by 1
    while lines_index < len_messages:
        line = all_messages[lines_index]
        bool_approved, user_input = initialize_data(cursor, line, mod_data)

        # commits to DB if message = valid
        if bool_approved:
            connection.commit()
        # clears file if all messages are moderated
        elif (lines_index + 1) == len_messages:
            print("There are no more messages to moderate")
            clear_file(filename)
        # if user inputs exit when asked if text is valid, it will return every message back to file
        elif user_input.lower() == "exit":
            data_back_to_file = all_messages[lines_index:]
            write_to_clean_file(filename, data_back_to_file)
            break

        lines_index += 1


# Function to send data for moderation
def send_data(filename, mod_data):
    if file_not_empty():
        with connect_to_db() as connection, connection.cursor() as cursor:
            write_data(connection, cursor, filename, mod_data)
    else:
        print("There are no more messages to moderate")


# function to call all data from the station_service table
def get_stations_data(cursor):
    query_station = "SELECT * FROM station_service"
    cursor.execute(query_station)
    stations = cursor.fetchall()
    return stations


def get_new_messages(cursor):
    # Query to get data from message_send
    # if it's not already moderated(message_id is not in message_mod)
    query_not_exists = (
        "SELECT t1.name_user, t1.message_column , t1.message_id "
        "FROM message_send as t1 "
        "WHERE NOT EXISTS ( "
        "SELECT 1 "
        "FROM message_mod "
        "WHERE message_mod.message_id = t1.message_id)")

    cursor.execute(query_not_exists)
    messages = cursor.fetchall()
    return messages


def get_newest_messages_moderated(cursor, approval_values, limit_value):
    # Query to get all data for a message
    # sorted by newest which are all approved
    query_get_messages = (
        "SELECT t1.name_user, t1.message_column, t1.date_message, t1.time_message, t2.mod_time, t2.message_id "
        "FROM message_send as t1 "
        "LEFT JOIN message_mod as t2 "
        "ON t1.message_id = t2.message_id "
        "WHERE t2.message_id IS NOT NULL and t2.approval IN %s "
        "ORDER BY t2.mod_date DESC, t2.mod_time DESC "
        "LIMIT %s;")
    cursor.execute(query_get_messages, (tuple(approval_values), limit_value,))
    messages = cursor.fetchall()
    return messages


def get_newest_messages_station(cursor, limit_value):
    # Query to get all data for a message
    # sorted by newest which are all approved
    query_get_messages = (
        "SELECT t1.name_user, t1.message_column, t1.date_message, t1.time_message, t1.station_city, "
        "t2.mod_time, t2.message_id "
        "FROM message_send as t1 "
        "LEFT JOIN message_mod as t2 "
        "ON t1.message_id = t2.message_id "
        "WHERE t1.station_city = 'Alkmaar' AND "
        "t2.message_id IS NOT NULL and t2.approval = 'approved'"
        "ORDER BY t2.mod_date DESC, t2.mod_time DESC "
        "LIMIT %s;")
    cursor.execute(query_get_messages, (limit_value,))
    messages = cursor.fetchall()
    return messages


def display_messages(var, root, limit_messages, time_int, cursor):
    approval_val = ["approved", "not approved"]

    messages = get_newest_messages_moderated(cursor, approval_val, limit_messages)

    new_text = ""
    for message in messages:
        formatted_time_mod = (message[4]).strftime("%H:%M")
        new_text += (f"\nMessage by {message[0]:>5} - time: {formatted_time_mod:<5}"
                     f"\nMessage: {message[1]}\n")

    var.set(new_text)

    root.after(time_int, display_messages, var, root, limit_messages, time_int, cursor)


def truncate_text(text):

    max_length = 40  # Set the maximum length you want

    if len(text) > max_length:
        truncated_text = text[:max_length] + "..."
    else:
        truncated_text = text + "..."

    return truncated_text


def create_update_messages(x_pos, y_pos, messages, root):

    root.delete("text_to_delete")

    for index, message in enumerate(messages, start=0):
        print(message)
        formatted_time_mod = (message[4]).strftime("%H:%M")

        # display name and time
        root.create_text(
            x_pos + 35,
            y_pos,
            text=f"{message[0]:<15} - {formatted_time_mod:>15}",
            font=("Open Sans bold", 11 * -1),
            tags="text_to_delete"
        )

        root.create_rectangle(
            x_pos - 20,
            y_pos + 36,
            x_pos + 150,
            y_pos + 39,
            fill="#FFC917",
            outline="",
            tags="text_to_delete"
        )
        hello = "sssdfasdsasssdfasdsasssdfasdsasssdfasdsasssdfasdsasssdfasdsasssdfasdsa"
        # display the message
        root.create_text(
            x_pos + 15,
            (y_pos + 25),
            text=f"{truncate_text(hello)}",
            font=("Open Sans ", 9 * -1),
            tags="text_to_delete"
        )

        y_pos += 60


def display_latest_messages(root, limit_messages, cursor, x_pos, y_pos):
    approval_val = ["approved", "not approved"]
    messages = get_newest_messages_moderated(cursor, approval_val, limit_messages)

    create_update_messages(x_pos, y_pos, messages, root)

    root.after(6000, display_latest_messages, root, limit_messages, cursor, x_pos, y_pos)


def display_latest_messages_station(root, limit_messages, cursor, x_pos, y_pos):
    messages = get_newest_messages_station(cursor, limit_messages)

    create_update_messages(x_pos, y_pos, messages, root)

    root.after(6000, display_latest_messages_station, root, limit_messages, cursor, x_pos, y_pos)


def get_weather_geolocation(lat, long):
    api_key = '164897825d4c9c6d19f032047061bfbf'

    url = (f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}"
           f"&exclude=hourly&appid={api_key}&units=metric")

    response = requests.get(url)
    data = response.json()
    return data


# Main block
if __name__ == "__main__":
    file_messages = "../old_proj/text.csv"

    with connect_to_db() as conn, conn.cursor() as cur:
        # p.pprint(get_stations_data(cur))
        approval_val = ["approved", "not approved"]
        messages1 = get_newest_messages_moderated(cur, approval_val, 5)
        print(messages1)
        messages = get_newest_messages_station(cur, 5)
        print(messages)
        data = get_newest_messages_station(cur, 5)
        print(data)
