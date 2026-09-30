import tkinter as tk

window = tk.Tk()
window.title("a special message!")
window.geometry("600x400")

title = tk.Label(
    window,
    text="a special message!",
    font=("Arial", 24,"bold"),
    fg="#ff4da6",
    bg="#1b1035"
)
title.pack(pady=35)

name_label = tk.Entry(
    window,
    font=("Arial", 18),
    justify="center",
    bg="#fff0f8",
    fg="#ff4da6",
    width=30
)
name_label.pack(pady=20)

message_label = tk.Label(
    window,
    text="enter your name",
    font=("Arial", 18, "bold"),
    fg="#ff4da6",
    bg="#1b1035",
    justify="center"
)
message_label.pack(pady=35)

def surprise():
    name = name_label.get()

    if name:
        message_label.config(
text=f"Hello, {name}! You are amazing!"
"you are a wonderful person."
"keep smiling and keep shining!"
        )
    else: 
        message_label.config(
text="Please enter your name to receive a special message!"
        )
        button = tk.Button(
    window,
    text="open the surprise",
    font=("Arial", 18, "bold"),
    bg="#ff4da6",
    fg="#white",
    activebackground="#ff80bf",
    activeforeground="#1b1035",
    command=surprise
        )


footer= tk.Label(
    window,
    text="made with love by [alfred]",
    font=("Arial", 25),
    fg="#ffd700",
    bg="#1b1035"
)
footer.pack(side="bottom", pady=20) 

window.mainloop()