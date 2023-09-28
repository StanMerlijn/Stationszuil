import psycopg2

# connecting to the database
connection = psycopg2.connect(
    host="localhost",
    database="NS messages",
    user="postgres",
    password="Whynow3421!"
)

yes_bool = "yesYesYy1jaJajJOKok"
input_file_messages = "text.txt"


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


with open("text.txt", "r") as file:
    email = input("moderator email: ")
    for line in file:
        # extract data from the file
        name_user, message, date_now, time_now, station = line.strip().split(", ")

        # prompt for validation
        valid_text = input(f"Is this text by {name_user} valid: {message}: ")

        cur = connection.cursor()

        # if moderator agrees that the text is valid it will be writen into the database
        if valid_text in yes_bool:
            # if the random station is already in the DB it will not write it to it
            if is_station_in_db(station) is False:
                # insert station into station table
                sql_query = "INSERT INTO station (station_name) VALUES (%s)"
                cur.execute(sql_query, (station,))

            # insert user data into the ns_user table
            insert_script = ("INSERT INTO ns_user (name_column, email_column, date_column,"
                             "time_column, message_column, station_name) "
                             "VALUES (%s, %s, %s, %s, %s, %s)")
            insert_values = (name_user, email, date_now, time_now, message, station)
            cur.execute(insert_script, insert_values)
            connection.commit()
    cur.close()
    connection.close()
clear_file(input_file_messages)
