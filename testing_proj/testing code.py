import time
from input_text import connect_to_db


def get_data_row(cursor):
    value = "anonymous"
    cursor.execute("SELECT * FROM message_send WHERE name_user = %s", (value,))
    rows = cursor.fetchone()
    #filtered_rows = [row for row in rows if row != ('anonymous',)]
    #print(filtered_rows)
    print(rows)


def get_data_all_rows(cursor):
    cursor.execute("SELECT * FROM message_send")
    rows = cursor.fetchall()
    # filtered_rows = [row for row in rows if row != ('anonymous',)]
    # print(filtered_rows)
    print(rows)


def get_data_column(cursor):
    cursor.execute("SELECT name_user FROM message_send")
    rows = cursor.fetchall()
    #filtered_rows = [row for row in rows if row != ('anonymous',)]
    # print(filtered_rows)
    print(rows)


def get_data_columns(cursor):
    cursor.execute("SELECT name_user, date_message, time_message FROM message_send")
    rows = cursor.fetchall()
    #filtered_rows = [row for row in rows if row != ('anonymous',)]
    # print(filtered_rows)
    print(rows)


def get_time(func, cur):
    start_time = time.time()
    func(cur)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


if __name__ == '__main__':
    with connect_to_db() as conn, conn.cursor() as cursor:
        print(f"all rows time = {get_time(get_data_all_rows, cursor)}")
        print(f"column time = {get_time(get_data_column, cursor)}")
        print(f"columns time= {get_time(get_data_columns, cursor)}")
        print(f"row time = {get_time(get_data_row, cursor)}")

        conn.commit()
