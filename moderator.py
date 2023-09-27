import psycopg2

# connecting to the database
connection = psycopg2.connect(
    host="localhost",
    database="NS messages",
    user="postgres",
    password="Whynow3421!"
)
email = "idkman@hello.com"

yes_bool = "yesYesYy1jaJajJOKok"
input_file_messages = "text.txt"


def clear_file(input_file):
    """"this function clears the file when its called"""
    with open(input_file, "w"):
        return


with open("text.txt", "r+") as file:
    for line in file:
        name_user, message, date_now, time_now, station = line.strip().split(", ")
        valid_text = input(f"Is this text by {name_user} valid: {message}: ")
        listt = name_user, message, date_now, time_now, station
        print(listt)

        # if moderator agrees that the text is valid it will be writen into the database
        if valid_text in yes_bool:
            cur = connection.cursor()
            cur.execute("INSERT INTO station (station_name) VALUES (%s)", (station,))
            insert_script = ("INSERT INTO ns_user (name_column, email_column, date_column,"
                             "time_column, message_column, station_name) "
                             "VALUES (%s, %s, %s, %s, %s, %s)")
            insert_values = (name_user, email, date_now, time_now, message, station)
            cur.execute(insert_script, insert_values)
            connection.close()

# clear_file(input_file_messages)
