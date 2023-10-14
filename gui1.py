
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import ttkbootstrap as ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/stanmerlijn/PycharmProjects/pythonProject4/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def button_click(event):
    print("Button clicked")


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
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(x=199.0, y=475.0, width=60.0, height=33.0)

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

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(x=199.0, y=214.0, width=17.0, height=16.32000732421875)

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
    image=entry_image_1
)
entry_1 = Text(bd=0, bg="#F0F0F2", fg="#000716", highlightthickness=0)
entry_1.place(x=199.60000002384186, y=310.0000305175781, width=538.7999999523163, height=139.0)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    298.9000015258789,
    264.5,
    image=entry_image_2
)
entry_2 = Entry(bd=0, bg="#F0F0F2", fg="#000716", highlightthickness=0)
entry_2.place(x=199.60000002384186, y=252.0, width=198.6000030040741, height=23.0)

button_8_image = PhotoImage(file=relative_to_assets("button_4.png"))

# Create a Label to simulate the button
button_label = tk.Label(window, image=button_8_image)
button_label.bind("<Button-1>", button_click)

button_label.place(x=866.0, y=10.0, width=39.0, height=13.0)

window.resizable(False, False)
window.mainloop()
