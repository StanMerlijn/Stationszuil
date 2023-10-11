from input_text import *


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
    insert_script = ("INSERT INTO message (name_user, date_message, time_message, "
                     "message, station_city, mod_email, mod_name, "
                     "mod_date, mod_time, bool_approved) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    # The data to write to the DB
    insert_values = (*message_data.values(),)
    return insert_script, insert_values


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
            'bool_approved': bool_approved
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


# Main block
if __name__ == "__main__":
    file_messages = "text.csv"
    mod_info = input("Moderator name: "), input("Moderator email: ")
    send_data(file_messages, mod_info)
