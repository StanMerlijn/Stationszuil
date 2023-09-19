import random
from datetime import datetime


def get_date():
    current_date = datetime.now().date()
    return current_date


def get_time():
    current_time = datetime.now().time()
    return current_time


randomNr = int(random.random())
wantsName = input("Do you want to use your name(yes or no): ")


if wantsName == ("yes" or "Yes"):
    name = input("What is your name: ")
else:
    name = "anonymous"

message = input("write your message here: ")
print(len(message))


with open("stations.txt", "r") as file:
    lines = file.readlines()

random_line_number = random.randint(0, len(lines) - 1)
station = lines[random_line_number].strip()

if len(message) > 140:
    print("your message should be less than 140 characters")
else:
    file = open("text.txt", "a")
    file.write(f"{name}, {message}, {get_date()} {get_time()}, {station}\n")
    file.close()
