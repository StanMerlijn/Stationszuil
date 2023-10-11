from input_text import connect_to_db
import psycopg2


def get_stations(filename):
    with open(filename) as stations_file:
        stations = [station.strip() for station in stations_file.readlines()]
    return stations


def write_station(cursor, station):
    cursor.execute("INSERT INTO station (station_name) VALUES (%s)", (station, ))


def main(filename):
    with connect_to_db() as connection, connection.cursor() as cursor:
        for station in get_stations(filename):
            write_station(cursor, station)


if __name__ == "__main__":
    file_stations = "stations.txt"
    main(file_stations)