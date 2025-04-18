import tkinter as tk
from tkinter import messagebox, scrolledtext
import speech_recognition as sr
import threading

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            output_box.insert(tk.END, text + "\n")
        except sr.WaitTimeoutError:
            messagebox.showerror("Timeout", "Listening timed out. Please try again.")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the audio.")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results from Google Speech Recognition service.")
        finally:
            status_label.config(text="Idle")

def start_recognition():
    threading.Thread(target=recognize_speech, daemon=True).start()

# GUI setup
app = tk.Tk()
app.title("Speech Recognition App")
app.geometry("500x400")

frame = tk.Frame(app)
frame.pack(pady=10)

status_label = tk.Label(frame, text="Idle", fg="blue")
status_label.pack()

start_btn = tk.Button(frame, text="Start Listening", command=start_recognition)
start_btn.pack(pady=5)

output_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=15)
output_box.pack(padx=10, pady=10)

app.mainloop()