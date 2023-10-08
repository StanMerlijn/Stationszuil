import tkinter as tk
import ttkbootstrap as ttk

root = ttk.Window(themename="darkly")
root.title("entering message")

root.geometry("300x150")

title_label = ttk.Label(master=root, text="write your message here")
entry_message = ttk.Entry(root, width=20)
entry_name = ttk.Entry(root, width=20)

entry_name.pack()
entry_message.pack(side="left")

# entry_message.grid(row=1, column=1, columnspan=3, padx=10, pady=10, )
# entry_name.grid(row=0, column=1, columnspan=1, padx=10, pady=10, )


def get_user_data():
    message = entry_message.get()
    name = entry_name.get()

    if name == "":
        name = "anonymous"
    entry_name.delete(0, tk.END)
    entry_message.delete(0, tk.END)

    print(f"{message} by {name}")


button_send = ttk.Button(root, text="send message", command=get_user_data)
# button_send.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

button_send.pack(side="left", padx=10)

root.mainloop()
