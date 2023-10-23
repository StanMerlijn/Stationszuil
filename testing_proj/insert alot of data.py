import random

from proj.moderator import *
import time


def generate_random_name():
    length = random.randint(1, 10)  # Random length between 1 and 10
    name = ''.join(chr(random.randint(97, 122)) for _ in range(length))
    return name


def write_shit(cur):
    start = time.time()
    station = "Oss"
    names = "anonymous"
    time_now, date_now = get_time_date()

    for i in range(1, 1001):
        message = i

        message_id = create_new_id(cur)
        name = random.choices(names)
        message_data = name, date_now, time_now, message, station, message_id
        write_data_to_db(cur, message_data)

    end = time.time()
    print(f"time elapsed = {end - start}")


def write_shit_mod(cur):
    start = time.time()

    index = 0
    mod_email = "anal shit"
    mod_name = "stan"
    messages_ids = get_new_messages(cur)
    print(messages_ids)
    ids = []
    for t in messages_ids:
        ids.append(t[2])
    while index < len(ids):
        for i in range(1, 2):
            time_now, date_now = get_time_date()
            message_id = ids[index]
            index += 1

            message_data = {
                'mod_email': mod_email,
                'mod_name': mod_name,
                'current_date': date_now,
                'current_time': time_now,
                'approval': "aproved",
                'message_id': message_id
            }
            print(*message_data.values())
            insert_script, insert_value = prepare_user_data(message_data)
            cur.execute(insert_script, insert_value)

    end = time.time()

    print(f"time elapsed = {end - start}")


if __name__ == '__main__':
    with (connect_to_db() as conn, conn.cursor() as cursor):
        write_shit(cursor)
        # write_shit_mod(cursor)
        conn.commit()
