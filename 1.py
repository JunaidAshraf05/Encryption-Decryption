from tkinter import *
from tkinter import messagebox
import base64
import os

APP_BG = "#222831"
WIDGET_BG = "#393E46"
BTN_BG = "#00ADB5"
BTN_BG2 = "#393E46"
BTN_FG = "#EEEEEE"
ENTRY_BG = "#EEEEEE"
ENTRY_FG = "#222831"
LABEL_FG = "#00ADB5"
FONT_MAIN = ("Segoe UI", 14, "bold")
FONT_LABEL = ("Segoe UI", 11)
FONT_BTN = ("Segoe UI", 11, "bold")

def encode():
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption Result")
        screen1.configure(bg=APP_BG)
        screen1.geometry("500x300+600+300")
        screen1.resizable(False, False)

        message = text1.get("1.0", END).strip()
        encode_message = message.encode('utf-8')
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode('utf-8')

        Label(screen1, text="Encoded Message", fg=LABEL_FG, bg=APP_BG, font=FONT_MAIN).pack(pady=(20, 10))
        text2 = Text(screen1, font=FONT_LABEL, height=6, width=55, bg=ENTRY_BG, fg=ENTRY_FG, relief=GROOVE, bd=2, wrap=WORD)
        text2.pack(padx=20)
        text2.insert(END, encrypt)
        text2.config(state=DISABLED)
    else:
        messagebox.showerror("Error", "Invalid Key! Please enter the correct key.")

def decode():
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption Result")
        screen2.configure(bg=APP_BG)
        screen2.geometry("500x300+600+300")
        screen2.resizable(False, False)

        message = text1.get("1.0", END).strip()
        try:
            base64_bytes = base64.b64decode(message)
            decrypt = base64_bytes.decode('utf-8')
        except Exception:
            decrypt = "Invalid encoded message!"

        Label(screen2, text="Decoded Message", fg=LABEL_FG, bg=APP_BG, font=FONT_MAIN).pack(pady=(20, 10))
        text3 = Text(screen2, font=FONT_LABEL, height=6, width=55, bg=ENTRY_BG, fg=ENTRY_FG, relief=GROOVE, bd=2, wrap=WORD)
        text3.pack(padx=20)
        text3.insert(END, decrypt)
        text3.config(state=DISABLED)
    else:
        messagebox.showerror("Error", "Invalid Key! Please enter the correct key.")

def main_screen():
    global screen
    global text1
    global code

    screen = Tk()
    screen.title("Encoder/Decoder")
    screen.configure(bg=APP_BG)
    screen.geometry("600x500+500+200")
    screen.resizable(False, False)

    # icon
    if os.path.exists("OIP.png"):
        image_icon = PhotoImage(file="OIP.png")
        screen.iconphoto(False, image_icon)

    def reset():
        text1.delete("1.0", END)
        code.set("")
        messagebox.showinfo("Reset", "All fields have been reset")

    # Title
    Label(screen, text="Text Encoder / Decoder", fg=LABEL_FG, bg=APP_BG, font=("Segoe UI", 20, "bold")).pack(pady=(20, 10))

    # Text input
    Label(screen, text="Enter the text to encode or decode:", fg=LABEL_FG, bg=APP_BG, font=FONT_LABEL).pack(anchor="w", padx=40, pady=(10, 0))
    text_frame = Frame(screen, bg=APP_BG)
    text_frame.pack(padx=40, pady=(0, 10), fill="x")
    text1 = Text(text_frame, font=FONT_LABEL, height=8, width=60, bg=ENTRY_BG, fg=ENTRY_FG, relief=GROOVE, bd=2, wrap=WORD)
    text1.pack(side=LEFT, fill="both", expand=True)
    scroll = Scrollbar(text_frame, command=text1.yview)
    scroll.pack(side=RIGHT, fill="y")
    text1.config(yscrollcommand=scroll.set)

    # Key input
    Label(screen, text="Enter the key:", fg=LABEL_FG, bg=APP_BG, font=FONT_LABEL).pack(anchor="w", padx=40, pady=(10, 0))
    code = StringVar()
    Entry(screen, textvariable=code, width=30, font=FONT_LABEL, bg=ENTRY_BG, fg=ENTRY_FG, relief=GROOVE, bd=2, show="*").pack(padx=40, pady=(0, 20))

    # Buttons
    btn_frame = Frame(screen, bg=APP_BG)
    btn_frame.pack(pady=10)
    Button(btn_frame, text="ENCRYPT", width=15, height=2, bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, command=encode, bd=0, activebackground=BTN_BG2, activeforeground=BTN_FG).pack(side=LEFT, padx=10)
    Button(btn_frame, text="DECRYPT", width=15, height=2, bg=BTN_BG2, fg=BTN_FG, font=FONT_BTN, command=decode, bd=0, activebackground=BTN_BG, activeforeground=BTN_FG).pack(side=LEFT, padx=10)
    Button(screen, text="RESET", width=35, height=2, bg="#222831", fg=BTN_FG, font=FONT_BTN, command=reset, bd=0, activebackground=BTN_BG, activeforeground=BTN_FG).pack(pady=20)

    screen.mainloop()

main_screen()