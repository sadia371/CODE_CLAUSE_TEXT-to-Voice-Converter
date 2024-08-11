import tkinter as tk
from tkinter import ttk
import pyttsx3
from threading import Thread

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")

        self.engine = pyttsx3.init()

        # Header
        header = tk.Label(root, text="Text to Speech Converter", font=("Helvetica", 18, "bold"), bg="#1abc9c", fg="white", pady=10)
        header.pack(fill=tk.X)

        # Create and place widgets with styling
        text_label = tk.Label(root, text="Enter Text Below:", font=("Helvetica", 14), bg="#2c3e50", fg="white")
        text_label.pack(pady=10)

        self.text_entry = tk.Text(root, wrap=tk.WORD, width=50, height=5, font=("Helvetica", 12), bd=2, relief=tk.GROOVE)
        self.text_entry.pack(pady=10, padx=20)

        voice_label = tk.Label(root, text="Select Voice:", font=("Helvetica", 14), bg="#2c3e50", fg="white")
        voice_label.pack(pady=10)

        voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in voices]

        self.voice_combobox = ttk.Combobox(root, values=voice_names, state="readonly", font=("Helvetica", 12))
        self.voice_combobox.current(0)
        self.voice_combobox.pack(pady=10, padx=20)

        rate_label = tk.Label(root, text="Adjust Speech Rate:", font=("Helvetica", 14), bg="#2c3e50", fg="white")
        rate_label.pack(pady=10)

        self.rate_slider = tk.Scale(root, from_=50, to=300, orient=tk.HORIZONTAL, font=("Helvetica", 10), bg="#2c3e50", fg="white", troughcolor="#1abc9c", command=self.update_rate)
        self.rate_slider.set(150)
        self.rate_slider.pack(pady=10, padx=20)

        self.speak_button = tk.Button(root, text="Speak", command=self.start_speaking, font=("Helvetica", 14), bg="#1abc9c", fg="white", bd=0, activebackground="#16a085", cursor="hand2")
        self.speak_button.pack(pady=20)

        # Footer
        footer = tk.Label(root, text="© 2024 Text to Speech Converter", font=("Helvetica", 10), bg="#2c3e50", fg="white", pady=10)
        footer.pack(side=tk.BOTTOM, fill=tk.X)

    def update_rate(self, _):
        new_rate = self.rate_slider.get()
        self.engine.setProperty('rate', new_rate)

    def start_speaking(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        if text:
            voice_index = self.voice_combobox.current()
            self.engine.setProperty('voice', self.engine.getProperty('voices')[voice_index].id)
            self.engine.setProperty('rate', self.rate_slider.get())
            speech_thread = Thread(target=self.speak, args=(text,))
            speech_thread.start()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Initialize the main window
root = tk.Tk()
app = TextToSpeechApp(root)
root.mainloop()
