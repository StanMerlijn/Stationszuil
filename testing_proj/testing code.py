import time
from proj.input_text import connect_to_db
import timeit
import sys


def get_data_row(cursor):
    value = "anonymous"
    cursor.execute("SELECT * FROM message_send WHERE name_user = %s", (value,))
    rows = cursor.fetchone()
    return rows
    # print(rows)


def get_data_all_rows(cursor):
    cursor.execute("SELECT * FROM message_send")
    rows = cursor.fetchall()
    return rows
    # print(rows)


def get_data_column(cursor):
    cursor.execute("SELECT name_user FROM message_send")
    rows = cursor.fetchall()
    return rows
    # print(rows)


def get_data_columns(cursor):
    cursor.execute("SELECT name_user, date_message, time_message FROM message_send")
    rows = cursor.fetchall()
    return rows
    # print(rows)


def filter_rows(rows):
    filtered_rows = [row for row in rows if row != ('anonymous',)]
    return filtered_rows


def get_time(func, cur):
    start_time = time.time()
    func(cur)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


def is_user_id_unique(user_id, cursor):
    cursor.execute("SELECT COUNT(*) FROM message_send WHERE name_user = %s", (user_id,))
    count = cursor.fetchone()[0]
    return count == 0


def name_in_set(list, target_value):
    list = set(list)
    if target_value in list:
        return True


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Target value found
        elif mid_val < target:
            start = mid + 1  # Search in the right half
        else:
            end = mid - 1  # Search in the left half

    return -1  # Target value not found


def time_set_sort(list, target_value):
    time_taken = timeit.timeit(
        stmt=lambda: name_in_set(list, target_value),
        number=10000
    )
    print(f"Average time taken for 1.000 .000 runs: {time_taken:.5f} seconds")


def time_binary_search(sorted_list, target_value):
    # sorted_list = [i for i in range(100000)]  # Generate a sorted list
    # target_value = 99999  # Target value to search for

    # Time the binary_search function
    time_taken = timeit.timeit(
        stmt=lambda: binary_search(sorted_list, target_value),
        number=1000000
    )
    print(f"Average time taken for bin 1.000 .000 runs: {time_taken:.5f} seconds")


def time_binary_search_set(sorted_list, target_value):
    s = time.time()
    sorted_list = set(sorted_list)
    sorted_list = list(sorted_list)
    e = time.time()
    c = e - s

    # Time the binary_search function
    time_taken = timeit.timeit(
        stmt=lambda: binary_search(sorted_list, target_value),
        number=1000000
    )
    print(f"Average time taken for bin set 1.000 .000 runs: {time_taken+ c:.5f} seconds")


def time_in_operation(names, target_name):
    time_taken = timeit.timeit(
        stmt=lambda: target_name in names,
        number=10000
    )
    print(f"Average time taken for 1.000 .000 runs: {time_taken:.10f} seconds")


def time_is_user_id_unique(cursor, user_id):
    time_taken = timeit.timeit(
        stmt=lambda: is_user_id_unique(user_id, cursor),
        number=1000
    )
    print(f"Average time taken for 1.000 .000 runs: {time_taken:.10f} seconds")


if __name__ == '__main__':
    with connect_to_db() as conn, conn.cursor() as cursor:
        print(f"all rows time = {get_time(get_data_all_rows, cursor)}")
        print(f"column time = {get_time(get_data_column, cursor)}")
        print(f"columns time= {get_time(get_data_columns, cursor)}")
        print(f"row time = {get_time(get_data_row, cursor)}")

        names = []
        rows = get_data_column(cursor)
        for row in rows:
            for name in row:
                names.append(name)

        names2 = [name for name in row for row in rows]
        # print(names2)

        size_list_names = sys.getsizeof(names)
        element_size = sys.getsizeof(names[3])
        total_size = size_list_names + len(names) * element_size

        size_set_names = sys.getsizeof(set(names))
        total_size_set = size_set_names + len(names) * element_size

        print(f"\nsize of list names {total_size}\nsize of set names {total_size_set}")

        #time_is_user_id_unique(cursor, "stan")
        #time_in_operation(names, "stan")
        time_binary_search(names, "stan")
        time_binary_search_set(names, "stan")
        #time_set_sort(names, "stan")

        conn.commit()
