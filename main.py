import tkinter as tk
from gui import KeyloggerGUI

def main():
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()