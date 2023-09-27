yes_bool = "yesYesYy1"
input_messages = "text.txt"


def clear_file(input_file):
    """"this function clears the file when its called"""
    with open(input_file, "w"):
        return


with open("text.txt", "r+") as file:
    for line in file:
        unapproved_text = line.strip().split(", ")
        name, message, date_now, time_now, station = line.strip().split(", ")
        valid_text = input(f"Is this text by {name} valid: {unapproved_text[1]}: ")
        clear_file(input_messages)
        # if moderator agrees that the text is valid it will be writen into the database
        if valid_text in yes_bool:
            with open("approved_text.txt", "a") as write_file:
                unapproved_text.append("approved")
                write_file.write(f"{', '.join(unapproved_text)}\n")
