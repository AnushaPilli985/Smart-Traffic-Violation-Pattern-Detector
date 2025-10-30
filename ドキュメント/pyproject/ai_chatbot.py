import tkinter as tk
from tkinter import filedialog, scrolledtext, END
from transformers import pipeline
import os

# Load a pre-trained QA/Chat model
chatbot = pipeline("text-generation", model="gpt2")  # You can replace with a bigger model

# ---- Chatbot Response ----
def get_response(user_input):
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

# ---- Send message ----
def send_message():
    user_input = entry.get()
    if not user_input:
        return
    
    chat_window.insert(END, "You: " + user_input + "\n")
    entry.delete(0, END)

    response = get_response(user_input)
    chat_window.insert(END, "Bot: " + response + "\n\n")
    chat_window.yview(END)

# ---- Upload Image ----
def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
    )
    if file_path:
        chat_window.insert(END, f"You uploaded an image: {os.path.basename(file_path)}\n")
        chat_window.insert(END, "Bot: I received your image, but I can’t analyze it yet.\n\n")
        chat_window.yview(END)

# ---- Tkinter Window ----
root = tk.Tk()
root.title("AI Chatbot with Image Upload")
root.geometry("600x500")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, state="normal")
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
