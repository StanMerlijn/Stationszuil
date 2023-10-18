from input_text import get_time_date, write_data_to_db, get_random_station, connect_to_db
import time


def write_shit(cur, conn):
    name = "anonymous"
    start = time.time()
    for i in range(1, 1001):
        start = time.time()
        message = i
        time_now, date_now = get_time_date()
        random_station = get_random_station(cur)
        message_data = name, date_now, time_now, message, random_station
        write_data_to_db(cur, message_data, conn)
    end = time.time()
    print(f"time elapsed = {end - start}")


if __name__ == '__main__':
    with connect_to_db() as conn, conn.cursor() as cursor:
        write_shit(cursor, conn)