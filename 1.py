from tkinter import *
from tkinter import messagebox
import base64
import os




def encode():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("450x500")

        message = text1.get("1.0", END)
        encode_message = message.encode('ascii')
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode('ascii')

        Label(screen1, text="Encoded Message", fg="black", font=("Arial", 13, "bold")).pack(pady=10)
        text2 = Text(screen1, font='Roboto 15 bold', height=10, width=50, bg="#FF4136", fg="black", relief=GROOVE, bd=5)
        text2.place(x=10, y=50, width=430, height=180)
        text2.insert(END, encrypt)
    else:
        messagebox.showerror("Error", "Invalid Key! Please enter the correct key.")

def decode():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("450x500")

        message = text1.get("1.0", END)
        try:
            base64_bytes = base64.b64decode(message)
            decrypt = base64_bytes.decode('ascii')
        except Exception as e:
            decrypt = "Invalid encoded message!"

        Label(screen2, text="Decoded Message", fg="black", font=("Arial", 13, "bold")).pack(pady=10)
        text3 = Text(screen2, font='Roboto 15 bold', height=10, width=50, bg="#007BFF", fg="black", relief=GROOVE, bd=5)
        text3.place(x=10, y=50, width=430, height=180)
        text3.insert(END, decrypt)
    else:
        messagebox.showerror("Error", "Invalid Key! Please enter the correct key.")

def main_screen():
    global screen
    global text1
    global code

    screen = Tk()
    screen.geometry("450x500")

    # icon
    if os.path.exists("OIP.png"):
        image_icon = PhotoImage(file="OIP.png")
        screen.iconphoto(False, image_icon)

    screen.title("Encoder/Decoder")

    def reset():
        text1.delete("1.0", END)
        code.set("")
        messagebox.showinfo("Reset", "All fields have been reset")

    Label(screen, text="Welcome to Encoder/Decoder", fg="black", font=("Arial", 13, "bold")).pack(pady=10)
    Label(screen, text="Enter the text to be encoded/decoded", fg="black", font=("Arial", 10)).pack(pady=10)

    text1 = Text(font='Roboto 15 bold', height=10, width=50, bg="ivory", fg="black", relief=GROOVE, bd=5)
    text1.place(x=10, y=50, width=430, height=180)

    Label(text='Enter the key', fg="black", font=("Arial", 10)).place(x=10, y=250)

    code = StringVar()
    Entry(textvariable=code, width=30, font='Roboto 15 bold', bg="ivory", fg="black", relief=GROOVE, bd=5).place(x=10, y=280)

    Button(text="ENCRYPT", width=20, height=2, bg="#4E5863", fg="white", font=("Arial", 10, "bold"), command=encode).place(x=10, y=350)
    Button(text="DECRYPT", width=20, height=2, bg="black", fg="white", font=("Arial", 10, "bold"), command=decode).place(x=240, y=350)
    Button(text="RESET", width=50, height=2, bg="#063970", fg="white", font=("Arial", 10, "bold"), command=reset).place(x=18, y=420)

    screen.mainloop()

main_screen()