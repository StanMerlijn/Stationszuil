
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import ttkbootstrap as ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/stanmerlijn/PycharmProjects/pythonProject4/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def button_click(event):
    print("Button clicked")


def get_name():
    # entry_name.delete(0, tk.END)
    if name_var.get() == 1:
        entry_name.configure(foreground="grey")
        entry_name["state"] = "disabled"
        return "anonymous"
    elif name_var.get() == 0:
        entry_name["state"] = "normal"
        entry_name.configure(foreground="#000716")
        return user_name.get()


# this function gets the name and message. will display message if empty
def get_data():
    entered_text = entry_message.get("1.0", tk.END)
    name = get_name()

    if name == "":
        canvas.itemconfig(name_error, text="One of the above must be checked /filled in!")
    else:
        canvas.itemconfig(name_error, text="")

    if entered_text == "\n":
        canvas.itemconfig(message_error, text="Message cannot be empty!")
    else:
        canvas.itemconfig(message_error, text="")

    if not name == "" and not entered_text == "\n":
        return name, entered_text


def send_data():
    get_data()


window = Tk()

window.geometry("960x540")
window.title("NS message")
window.configure(bg="#E6E6E9")


canvas = Canvas(window, bg="#E6E6E9", height=540, width=960, bd=0,
                highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)
canvas.create_rectangle(1158.0, 61.0, 1179.0, 70.0, fill="#000000", outline="")

canvas.create_rectangle(0.0, 41.0, 960.0, 171.0, fill="#FFC917", outline="")

canvas.create_rectangle(55.0, 131.0, 905.0, 540.0, fill="#FFFFFF", outline="")

canvas.create_text(125.0, 310.199951171875, anchor="nw", text="message\n",
                   fill="#003082", font=("Open Sans", 11 * -1))

canvas.create_text(140.0, 214.0, anchor="nw", text="name\n", fill="#003082", font=("Open Sans", 11 * -1))

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
    command=send_data,
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

canvas.create_rectangle(863.0, 28.20001220703125, 905.0, 31.20001220703125, fill="#FFC917", outline="")

canvas.create_text(227.0, 154.0, anchor="nw", text="today, mon 10",
                   fill="#003082", font=("OpenSansRoman SemiBold", 11 * -1))

canvas.create_text(365.0, 153.0, anchor="nw", text="10:40",
                   fill="#003082", font=("OpenSansRoman SemiBold", 11 * -1))

name_var = tk.IntVar(value=0)
button_name = ttk.Checkbutton(canvas, command=get_name, variable=name_var, offvalue=0, onvalue=1)
button_name.place(x=199.0, y=214.0, width=17.0, height=16.32000732421875)

canvas.create_text(233.0, 215.0, anchor="nw", text="anonymous",
    fill="#000000", font=("OpenSansRoman Regular", 11 * -1))

canvas.create_text(55.0, 66.0, anchor="nw", text="write your message",
    fill="#003082", font=("OpenSansRoman SemiBold", 20 * -1))

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    209.0,
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

canvas.create_text(443.0, 15.0, anchor="nw", text="welkom to NS",
                   fill="#003082", font=("OpenSansRoman SemiBold", 11 * -1))

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    469.0,
    380.5000305175781,
    image=entry_image_1)


entry_message = Text(bd=0, bg="#F0F0F2", fg="#000716", highlightthickness=0, )
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


button_8_image = PhotoImage(file=relative_to_assets("button_4.png"))

name_error = canvas.create_text(199.0,
                                285.0,
                                anchor="nw",
                                text="",
                                fill="#DB0029",
                                font=("OpenSansRoman Light", 9 * -1))

message_error = canvas.create_text(199.0,
                                   458.0,
                                   anchor="nw",
                                   text="",
                                   fill="#DB0029",
                                   font=("OpenSansRoman Light", 9 * -1),
                                   state="disabled")

# Create a Label to simulate the button
button_label = tk.Label(window, image=button_8_image)
button_label.bind("<Button-1>", button_click)

button_label.place(x=866.0, y=10.0, width=39.0, height=13.0)

window.resizable(False, False)
window.mainloop()
