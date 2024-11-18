import customtkinter as ctk
from tkinter import messagebox
from googletrans import Translator

def translate_text():
    input_text = input_entry.get("1.0", "end").strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return
    translator = Translator()
    try:
        translated_text = translator.translate(input_text, dest='ar').text
        output_entry.delete("1.0", "end")
        output_entry.insert("end", translated_text)
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred during translation: {e}")

# Create the main window
root = ctk.CTk()
root.title("English to Arabic Translator")

# Set the window size
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Change background color of the window
ctk.set_appearance_mode("dark")  # Set the appearance mode
root.configure(bg="#2b2b2b")

# Create title label
title_label = ctk.CTkLabel(root, text="English to Arabic Translator", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Create input and output frames and pack them side by side
frame_container = ctk.CTkFrame(root)
frame_container.pack(fill="both", expand=True, padx=20, pady=20)

input_frame = ctk.CTkFrame(frame_container)
input_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

output_frame = ctk.CTkFrame(frame_container)
output_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Create input label and text box
input_label = ctk.CTkLabel(input_frame, text="Enter English text:", font=("Arial", 18))
input_label.pack(anchor="w", padx=10, pady=10)
input_entry = ctk.CTkTextbox(input_frame, height=10, font=("Arial", 16))
input_entry.pack(fill="both", expand=True, padx=10, pady=10)

# Create output label and text box
output_label = ctk.CTkLabel(output_frame, text="Arabic translation:", font=("Arial", 18))
output_label.pack(anchor="w", padx=10, pady=10)
output_entry = ctk.CTkTextbox(output_frame, height=10, font=("Arial", 16))
output_entry.pack(fill="both", expand=True, padx=10, pady=10)

# Create translate button and place it at the bottom
translate_button = ctk.CTkButton(root, text="Translate", command=translate_text, font=("Arial", 18), fg_color="#1c7ed6")
translate_button.pack(pady=20)

# Set icon if exists
try:
    root.iconbitmap(default='1.ico')  # Ensure the path to your .ico file is correct
except Exception as e:
    print("Icon loading failed:", e)

# Start the Tkinter event loop
root.mainloop()
