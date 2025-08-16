# 🔐 Text Encoder/Decoder (Tkinter GUI)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-Educational-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## 📌 Overview
This project is a **Python-based GUI application** that allows users to **encode and decode text messages** using **Base64 encoding**.  
It features a clean, interactive interface built with **Tkinter**, making it simple to enter text, protect it with a key, and either encrypt or decrypt the content.  

The tool demonstrates concepts of:
- GUI development in Python  
- Basic text encoding/decoding  
- User authentication with password validation  

---

## 🚀 Features
✅ **User-Friendly GUI** – Built with Tkinter, includes labels, text boxes, entry fields, and styled buttons  
✅ **Encode Messages** – Converts plain text into **Base64 encoded format**  
✅ **Decode Messages** – Restores encoded text back to the original form  
✅ **Password Protection** – Requires a secret key (`1234` by default) for both encryption and decryption  
✅ **Error Handling** – Alerts users when the key is invalid or when decoding fails  
✅ **Reset Option** – Clears all fields for a fresh start  

---

## 🖥️ How It Works
1. Run the script → The main **Encoder/Decoder** window opens.  
2. Enter your message in the text box.  
3. Type the **key** (`1234`) in the entry field.  
4. Click:  
   - 🔒 **ENCRYPT** → Encodes your message in Base64.  
   - 🔑 **DECRYPT** → Decodes the Base64 back to readable text.  
   - 🔄 **RESET** → Clears all input fields.  
5. If the wrong key is entered → An **error message box** is displayed.  

---

## 🛠️ Tech Stack
- **Python 3.x**  
- **Tkinter** → GUI components  
- **Base64** → Encoding/decoding  
- **OS module** → Handling optional app icon  

---

## 📂 File Structure
```
│── 1.py          # Main application file
│── OIP.png       # Optional window icon (if available)
```

---

## 📸 Screenshots (Conceptual)
- **Main Window**: Text input field, key entry, and buttons (Encrypt, Decrypt, Reset).  
- **Encryption Window**: Shows Base64 encoded message in red background.  
- **Decryption Window**: Shows decoded message in blue background.  

---

## ⚠️ Limitations
- Key is **hardcoded** (`1234`), not customizable.  
- Uses **Base64 encoding** (not secure encryption).  
- Only supports text (no file encoding).  
- Limited ASCII support (may break with special characters).  

---

## 🔮 Future Enhancements
- Implement stronger encryption (e.g., AES, Fernet).  
- Allow dynamic user-generated keys.  
- Add **copy-to-clipboard** for results.  
- Support **file upload & save** for encoded/decoded text.  
- Improve UI with **CustomTkinter** or modern frameworks.  

---

## ▶️ How to Run
1. Make sure you have **Python 3.x** installed.  
2. Save the file `1.py` and run it:
   ```bash
   python 1.py
   ```
3. The application window will launch.  

---

## 📜 License
This project is free to use for **educational purposes**.  
You may modify and extend it for your own projects.  

---

✨ **In short:** This is a beginner-friendly project that showcases **GUI development in Python with Tkinter** and introduces the concept of **encoding/decoding messages**. Perfect for learning or portfolio demonstration!  
