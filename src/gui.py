import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image
import os
from fingering_generator import generate_fingering_sequence_multi_line
from translations import translations  # Import the translations dictionary

class FingeringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ocarina Fingering Generator")
        
        self.current_language = 'English'
        self.translations = translations[self.current_language]

        # Create the main frame
        self.mainframe = ttk.Frame(root, padding="10")
        self.mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid to make the widgets resize with the window
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(6, weight=1)

        # Language Selection
        self.language_label = ttk.Label(self.mainframe, text=self.translations['language'])  # Store label in self
        self.language_label.grid(row=0, column=0, sticky=tk.W)
        self.language_var = tk.StringVar(value=self.current_language)
        self.language_dropdown = ttk.Combobox(self.mainframe, textvariable=self.language_var)
        self.language_dropdown['values'] = ('English', '中文', '日本語')
        self.language_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.language_dropdown.bind("<<ComboboxSelected>>", self.change_language)

        # Key Label and Dropdown
        self.key_label = ttk.Label(self.mainframe, text=self.translations['select_key'])
        self.key_label.grid(row=1, column=0, sticky=tk.W)
        self.key_var = tk.StringVar()
        self.key_dropdown = ttk.Combobox(self.mainframe, textvariable=self.key_var)
        self.key_dropdown['values'] = ('G', 'C', 'D', 'F', 'A', 'bB', 'bE')
        self.key_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Input Label and Text Area
        self.notes_label = ttk.Label(self.mainframe, text=self.translations['enter_notes'])
        self.notes_label.grid(row=2, column=0, sticky=tk.W)
        self.text_area = tk.Text(self.mainframe, width=40, height=10)
        self.text_area.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Filename Label and Entry
        self.filename_label = ttk.Label(self.mainframe, text=self.translations['filename'])
        self.filename_label.grid(row=4, column=0, sticky=tk.W)
        self.filename_entry = ttk.Entry(self.mainframe, width=40)
        self.filename_entry.grid(row=5, column=0, padx=5, pady=5, columnspan=2, sticky=(tk.W, tk.E))
        self.filename_entry.insert(0, "output_fingering")  # Default filename

        # Generate Button
        self.generate_button = ttk.Button(self.mainframe, text=self.translations['generate_button'], command=self.generate_fingering)
        self.generate_button.grid(row=6, column=0, pady=10, columnspan=2)

        # Image Display Area
        self.image_label = ttk.Label(self.mainframe)
        self.image_label.grid(row=7, column=0, pady=5, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def change_language(self, event):
        self.current_language = self.language_var.get()
        self.translations = translations[self.current_language]
        self.update_labels()

    def update_labels(self):
        # Update all labels with the selected language
        self.key_label.config(text=self.translations['select_key'])
        self.notes_label.config(text=self.translations['enter_notes'])
        self.filename_label.config(text=self.translations['filename'])
        self.generate_button.config(text=self.translations['generate_button'])
        
        # Update the "Language" label
        self.language_label.config(text=self.translations['language'])

    def generate_fingering(self):
        # Get input from the text area
        user_input = self.text_area.get("1.0", tk.END).strip()
        note_sequences = [line.split() for line in user_input.splitlines() if line]
        
        if not note_sequences:
            messagebox.showerror(self.translations['input_error'], self.translations['input_error'])
            return
        
        # Get the filename from the entry box
        filename = self.filename_entry.get().strip()
        if not filename:
            messagebox.showerror(self.translations['filename_error'], self.translations['filename_error'])
            return
        
        # Ensure the filename has a .png extension
        if not filename.endswith(".png"):
            filename += ".png"
        
        # Get the selected key
        selected_key = self.key_var.get()
        if not selected_key:
            messagebox.showerror(self.translations['key_error'], self.translations['key_error'])
            return
        
        # Call the fingering generator function
        output_path = generate_fingering_sequence_multi_line(note_sequences, selected_key, output_path=filename)
        
        if output_path and os.path.exists(output_path):
            self.display_image(output_path)
        else:
            messagebox.showerror(self.translations['generation_error'], self.translations['generation_error'])
    
    def display_image(self, path):
        # Display the generated image in the GUI
        img = Image.open(path)
        img.thumbnail((800, 800))  # Increase the size for display (800x800 is an example, adjust as needed)
        photo = ImageTk.PhotoImage(img)
        
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = FingeringApp(root)
    root.mainloop()
