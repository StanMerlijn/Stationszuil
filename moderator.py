import psycopg2
from datetime import datetime

# connecting to the database
connection = psycopg2.connect(
    host="localhost",
    database="NS messages",
    user="postgres",
    password="Whynow3421!"
)

yes_bool = "yesYesYy1jaJajJOKok"
file_messages = "text.csv"

email = input("before moderating could enter your email: ")

def get_time_date():
    date = datetime.now().date()
    time = datetime.now().time().strftime("%X")
    return time, date


def clear_file(input_file):
    """"this function clears the file when called"""
    with open(input_file, "w"):
        return


def is_station_in_db(station_name):
    """"boolean function to check if a station is already in the database"""
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM station WHERE station_name = %s", (station_name,))
    data = cursor.fetchone()[0]
    cursor.close()
    return data > 0


while True:
    current_time, current_date = get_time_date()
    with open(file_messages, "r") as file:
        cur = connection.cursor()
        for line in file:
            # extract data from the file
            name_user, message, date_message, time_message, station = line.strip().split(", ")

            # prompt for validation
            valid_text = input(f"Is this text by {name_user} valid: {message}: ")

            # if moderator agrees that the text is valid it will be writen into the database
            if valid_text in yes_bool:
                email = input("moderator email: ")

                # if the random station is already in the DB it will not write it to it
                if is_station_in_db(station) is False:
                    # insert station into station table
                    sql_query = "INSERT INTO station (station_name) VALUES (%s)"
                    cur.execute(sql_query, (station,))

                # insert user data into the ns_user table
                insert_script = ("INSERT INTO ns_user (name_column, email_column, date_column,"
                                 "time_column, message_column, station_name, mod_date, mod_time) "
                                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

                # The values that will be written to its respectable columns
                insert_values = (name_user, email, date_message, time_message,
                                 message, station, current_date, current_time)
                cur.execute(insert_script, insert_values)
                connection.commit()
            else:
                print("There are no text to moderate")
    cur.close()
    connection.close()
    break

clear_file(file_messages)
