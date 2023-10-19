
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from gui1 import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_PC = OUTPUT_PATH / Path(r"C:\Users\smerl\PycharmProjects\StationsZuil\proj\assets\frame1 ")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH_PC / Path(path)


def main(cursor, conn):

    window = Tk()

    window.geometry("960x540")
    window.configure(bg="#E6E6E9")

    canvas = Canvas(
        window,
        bg="#E6E6E9",
        height=540,
        width=960,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        41.0,
        960.0,
        171.0,
        fill="#FFC917",
        outline="")

    canvas.create_rectangle(
        55.0,
        81.0,
        905.0,
        540.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        141.0,
        162.0,
        anchor="nw",
        text="email",
        fill="#003082",
        font=("Open Sans", 11 * -1)
    )

    canvas.create_text(
        112.0,
        277.0,
        anchor="nw",
        text="message by",
        fill="#003082",
        font=("Open Sans", 11 * -1)
    )

    canvas.create_text(
        127.0,
        330.0,
        anchor="nw",
        text="message",
        fill="#003082",
        font=("Open Sans", 11 * -1)
    )

    ass_shit = canvas.create_text(
        202.0,
        331.0,
        anchor="nw",
        text="547AWMdnhiu3hWwYVHDS6lUZgu\nbrhoE0sjIwamw1NVZcNwyZqNfwvkwwZ6\n"
             "R1y33zGBBI0VLaUt\nNpICZRKsim2u6EuS4tGXuygjbKHTmhIsgYo\n"
             "GkAhzx62pGXaOJ23KNeZFN66o8UlkOE\n",
        fill="#000000",
        font=("OpenSansRoman Regular", 11 * -1)
    )
    ass_shit.conjugate()

    canvas.create_text(
        566.0,
        125.0,
        anchor="nw",
        text="547AWMdnh\niu3hWwYVHDS6lUZgu\nbrhoE0sjIwa\nmw1NVZcNwyZqNfwvkwwZ6\n"
             "R1y33zGBBI0\nVLaUt\nNpICZRKsim2u6EuS\n"
             "4tGXuygjbKH\nTmhIsgYo\nGkAhzx62pGX\naOJ23KNeZF\nN66o8UlkOE\n",
        fill="#000000",
        font=("OpenSansRoman Regular", 11 * -1)
    )

    canvas.create_text(
        566.0,
        106.0,
        anchor="nw",
        text="latest messages moderated",
        fill="#003082",
        font=("OpenSansRoman Bold", 11 * -1)
    )

    canvas.create_text(
        202.0,
        276.0,
        anchor="nw",
        text="not defined ",
        fill="#000000",
        font=("OpenSansRoman Regular", 11 * -1)
    )

    canvas.create_text(
        141.0,
        112.0,
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
        command=lambda: connection_close(cursor, conn, window),
        relief="flat"
    )
    button_exit.place(
        x=738.0,
        y=475.0,
        width=60.0,
        height=33.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=202.0,
        y=473.0,
        width=90.0,
        height=33.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=324.0,
        y=473.0,
        width=90.0,
        height=33.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        960.0,
        45.0,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        90.0,
        22.0,
        image=image_image_1
    )

    canvas.create_text(
        420.0,
        15.0,
        anchor="nw",
        text="today, mon 10",
        fill="#003082",
        font=("OpenSansRoman Bold", 11 * -1)
    )

    canvas.create_text(
        512.0,
        15.0,
        anchor="nw",
        text="10:40",
        fill="#003082",
        font=("OpenSansRoman Bold", 11 * -1)
    )

    canvas.create_text(
        202.0,
        222.0,
        anchor="nw",
        text="message to moderate",
        fill="#003082",
        font=("OpenSansRoman Bold", 14 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        298.9000015258789,
        118.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F0F0F2",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=199.60000002384186,
        y=106.0,
        width=198.6000030040741,
        height=23.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        301.9000015258789,
        168.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#F0F0F2",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=202.60000002384186,
        y=156.0,
        width=198.6000030040741,
        height=23.0
    )
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    with connect_to_db() as conn, conn.cursor() as cursor:
        main(cursor, conn)