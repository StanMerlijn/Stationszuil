import tkinter
from proj.input_text import *
import requests


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


# function to get the newest messages from a specific station in chronological order.
def get_newest_messages_station(cursor, limit_value, city_name):
    # Query to get all data for a message. sorted by newest which are all approved
    query_get_messages = (
        "SELECT t1.name_user, t1.message_column, t1.date_message, t1.time_message, "
        "t2.mod_time, t2.message_id "
        "FROM message_send as t1 "
        "LEFT JOIN message_mod as t2 "
        "ON t1.message_id = t2.message_id "
        "WHERE t1.station_city = %s AND "
        "t2.message_id IS NOT NULL and t2.approval = 'approved'"
        "ORDER BY t2.mod_date DESC, t2.mod_time DESC "
        "LIMIT %s;")
    cursor.execute(query_get_messages, (city_name, limit_value,))
    messages = cursor.fetchall()
    return messages


# function to trim down the length of a message
def truncate_text(text):

    max_length = 40  # Set the maximum length you want
    if len(text) > max_length:
        truncated_text = text[:max_length] + "..."
    else:
        truncated_text = text + "..."

    return truncated_text


# function to create and delete old messages
def create_update_messages(x_pos, y_pos, messages, root):

    root.delete("text_to_delete")

    for index, message in enumerate(messages, start=0):
        formatted_time_mod = (message[4]).strftime("%H:%M")
        stripped_messages = message[1].strip()

        title_message = f"{message[0]} - {formatted_time_mod}"

        # display name and time
        root.create_text(
            x_pos - 35,
            y_pos,
            text=f"{title_message}",
            font=("Open Sans bold", 11 * -1),
            tags="text_to_delete",
            fill="#000000",
            anchor=tkinter.W
        )

        # display the message
        root.create_text(
            x_pos,
            y_pos + 28,
            text=f"{stripped_messages}",
            font=("Open Sans ", 9 * -1),
            tags="text_to_delete",
            fill="#000000",
            width=270,
            anchor=tkinter.W
        )

        # displaying lines under messages
        if index < 4:
            offset = -30
            height = 3
            root.create_rectangle(
                x_pos + offset,
                y_pos + 50,
                x_pos + 260,
                y_pos + 50 + height,
                fill="#FFC917",
                outline="",
                tags="text_to_delete",
            )

        y_pos += 62


# function to display all moderated messages in chronological order
def display_latest_messages(root, limit_messages, cursor, x_pos, y_pos):
    approval_val = ["approved", "not approved"]
    messages = get_newest_messages_moderated(cursor, approval_val, limit_messages)

    create_update_messages(x_pos, y_pos, messages, root)

    root.after(6000, display_latest_messages, root, limit_messages, cursor, x_pos, y_pos)


city_name = "Apeldoorn"
def set_city(city):
    global city_name
    city_name = city


# function to display latest approved messages in chronological order from a specific station
def display_latest_messages_station(root, cursor, x_pos, y_pos):
    global city_name
    limit_messages = 5
    messages = get_newest_messages_station(cursor, limit_messages, city_name)

    create_update_messages(x_pos, y_pos, messages, root)

    root.after(1000, display_latest_messages_station, root, cursor, x_pos, y_pos)


# function to get weather forecast from geodata
def get_weather_geolocation(lat, long):
    api_key = '164897825d4c9c6d19f032047061bfbf'

    url = (f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}"
           f"&exclude=hourly&appid={api_key}&units=metric")

    response = requests.get(url)
    data = response.json()
    return data


# function to get all the useful forecast weather data
def get_current_weather(lat, lon):
    weather_data = get_weather_geolocation(lat, lon)

    weather_dates = []
    icons = []
    temp_forecast = []

    # loop to get the latest five weather data reports
    for i in range(0, 6):
        temp_forecast.append(weather_data["list"][i]["main"]["temp"])
        icons.append(weather_data["list"][i]["weather"][0]["icon"])
        weather_dates.append(weather_data["list"][i]["dt_txt"])

    weather = weather_data["list"][0]["weather"][0]["description"]
    wind = weather_data["list"][0]["wind"]["speed"]

    return temp_forecast, weather, wind, icons, weather_dates
