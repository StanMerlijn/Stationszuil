import tkinter as tk
import ttkbootstrap as ttk


# save name
def get_user_data():
    user_message = entry_message.get()
    user_name = entry_name.get()

    if user_name == "":
        user_name = "anonymous"
    entry_name.delete(0, tk.END)
    entry_message.delete(0, tk.END)

    print(f"{user_message} by {user_name}")

# exit window
def exit_menu():
    window.destroy()


# window
window = ttk.Window(themename="darkly")
window.title("entering message")
window.geometry("800x500")

# entry fields
title_name = ttk.Label(master=window, text="Enter your name")
title_name.pack()

entry_name = ttk.Entry(master=window)
entry_name.pack()

title_message = ttk.Label(master=window, text="Enter your message")
title_message.pack()

entry_message = ttk.Entry(master=window)
entry_message.pack(ipadx=250)

# button
button_send_data = ttk.Button(master=window, text="send message", command=get_user_data)
button_send_data.pack(padx=10, pady=5)

button_exit = ttk.Button(master=window, text="exit", command=exit_menu)
button_exit.pack(padx=10)

# run
window.mainloop()
