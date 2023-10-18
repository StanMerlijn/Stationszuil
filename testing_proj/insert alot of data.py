import random

from input_text import get_time_date, write_data_to_db, get_random_station, connect_to_db
import time


def generate_random_name():
    length = random.randint(1, 10)  # Random length between 1 and 10
    name = ''.join(chr(random.randint(97, 122)) for _ in range(length))
    return name


def write_shit(cur):
    start = time.time()
    station = "Oss"
    name = "anonymous"
    for i in range(1, 5001):
        message = i
        time_now, date_now = get_time_date()
        message_data = name, date_now, time_now, message, station
        write_data_to_db(cur, message_data)

    end = time.time()
    print(f"time elapsed = {end - start}")


def write_ass(cur, data):
    write_data_to_db(cur, data)


if __name__ == '__main__':
    with (connect_to_db() as conn, conn.cursor() as cursor):

        write_shit(cursor)
        conn.commit()
