
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Text, Button, PhotoImage
import tkinter as tk
import ttkbootstrap as ttk
from input_text import display_date, display_clock, main_gui, connect_to_db


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_LP = OUTPUT_PATH / Path(r"/Users/stanmerlijn/PycharmProjects/pythonProject4/proj/assets/frame0")
ASSETS_PATH_PC = OUTPUT_PATH / Path(r"C:\Users\smerl\PycharmProjects\StationsZuil\proj\assets\frame0  ")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH_LP / Path(path)


# this function returns the correct name of the user
def get_name():
    if name_var.get() == 1:
        entry_name.configure(foreground="grey")
        entry_name["state"] = "disabled"
        return "anonymous"
    elif name_var.get() == 0:
        entry_name["state"] = "normal"
        entry_name.configure(foreground="#000716")
        return user_name.get()


# this function gets the name and message. will display message if one is empty
def get_data():
    entered_text = entry_message.get("1.0", tk.END)
    name = get_name()
    message_len = len(entered_text.replace("\n", ""))

    canvas.itemconfig(message_error, text="")
    canvas.itemconfig(name_error, text="")

    empty_return = False, None, None

    # displays message if no name is given.
    if name == "":
        canvas.itemconfig(name_error, text="One of the above must be checked /filled in!")

    # displays message if entry message is empty.
    if entered_text == "\n":
        canvas.itemconfig(message_error, text="Message cannot be empty!")

    if message_len > 140:
        canvas.itemconfig(message_error, text="message has to be less than 140 characters!")
        return empty_return

    # if the data fields are not empty it will return them.
    if entered_text == "\n" or name == "":
        return empty_return

    return True, name, entered_text


# this function sends the data to the database
def send_data(cur, con):
    bool_data, name, message = get_data()
    if bool_data:
        # prepare and commit all data to database
        main_gui(cur, name, message)

        # reset inputs to prepare for new message
        entry_name.configure(state="normal")
        entry_name.configure(foreground="black")
        entry_name.delete(0, tk.END)

        entry_message.delete("1.0", tk.END)
        name_var.set(value=0)

    con.commit()


window = Tk()

conn = connect_to_db()
cursor = conn.cursor()

window.geometry("960x540")
window.title("NS message")

canvas = Canvas(
    window,
    bg="#E6E6E9",
    height=540,
    width=960,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.create_rectangle(-1, 0.0, 960, 600, fill="#E6E6E9")
canvas.place(x=0, y=0)

canvas.create_rectangle(1158.0, 61.0, 1179.0, 70.0, fill="#000000", outline="")
canvas.create_rectangle(0.0, 41.0, 960.0, 171.0, fill="#FFC917", outline="")
canvas.create_rectangle(55.0, 131.0, 905.0, 540.0, fill="#FFFFFF", outline="")

canvas.create_text(
    125.0,
    310.199951171875,
    anchor="nw",
    text="message\n",
    fill="#003082",
    font=("Open Sans", 11 * -1)
)

canvas.create_text(
    140.0,
    214.0,
    anchor="nw",
    text="name\n",
    fill="#003082",
    font=("Open Sans", 11 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_exit = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_exit.place(x=679.0, y=475.0, width=60.0, height=33.0)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_send = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: send_data(cursor, conn),
    relief="flat"
)
button_send.place(x=199.0, y=475.0, width=60.0, height=33.0)

canvas.create_rectangle(0.0, 0.0, 960.0, 45.0, fill="#FFFFFF", outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    90.0,
    22.0,
    image=image_image_1
)

date_var = tk.StringVar()
label_date = ttk.Label(
    canvas,
    textvariable=date_var,
    foreground="#003082",
    font=("OpenSansRoman SemiBold", 11 * -1)
)
label_date.place(x=227.0, y=151)

time_var = tk.StringVar()
label_time = ttk.Label(
    canvas,
    textvariable=time_var,
    foreground="#003082",
    font=("OpenSansRoman SemiBold", 11 * -1)
)
label_time.place(x=365.0, y=151)


name_var = tk.IntVar(value=0)
button_name = ttk.Checkbutton(canvas, command=get_name, variable=name_var, offvalue=0, onvalue=1)
button_name.place(x=199.0, y=214.0, width=17.0, height=16.32000732421875)

canvas.create_text(
    233.0,
    215.0,
    anchor="nw",
    text="anonymous",
    fill="#000000",
    font=("OpenSansRoman Regular", 11 * -1)
)

canvas.create_text(
    55.0,
    66.0,
    anchor="nw",
    text="write your message",
    fill="#003082",
    font=("OpenSansRoman SemiBold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    206.5,
    161.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    347.0,
    161.0,
    image=image_image_3
)

canvas.create_text(
    443.0,
    15.0,
    anchor="nw",
    text="welcome to NS",
    fill="#003082",
    font=("OpenSansRoman ExtraBold", 13 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    469.0,
    380.5000305175781,
    image=entry_image_1
)

entry_message = Text(bd=0, bg="#F0F0F2", fg="#000716", highlightthickness=0)
entry_message.place(x=199.60000002384186, y=310.0000305175781, width=538.7999999523163, height=139.0)

entry_image_name = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_name = canvas.create_image(
    298.9000015258789,
    264.5,
    image=entry_image_name
)

style = ttk.Style()
style.configure("Disabled.TEntry", foreground="#000716", background="#F0F0F2")

user_name = tk.StringVar()
entry_name = ttk.Entry(canvas, textvariable=user_name, style="Disabled.TEntry")
entry_name.place(x=199.60000002384186, y=252.0, width=198.6000030040741, height=25.0)

name_error = canvas.create_text(
    199.0,
    285.0,
    anchor="nw",
    text="",
    fill="#DB0029",
    font=("OpenSansRoman Light", 9 * -1)
)

message_error = canvas.create_text(
    199.0,
    458.0,
    anchor="nw",
    text="",
    fill="#DB0029",
    font=("OpenSansRoman Light", 9 * -1),
    state="disabled"
)

display_date(date_var, window, "%B %d", 1000*60*60)
display_clock(time_var, window, "%H:%M", 1000)
window.resizable(False, False)
window.mainloop()

cursor.close()
conn.close()
