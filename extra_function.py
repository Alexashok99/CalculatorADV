import time
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.root.configure(background="#222831")

        self.input_var = ttk.StringVar()
        self.output_var = ttk.StringVar()

        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        # Clock
        self.clock_label = ttk.Label(
            self.root,
            font=("DS-Digital", 50),
            foreground="cyan",
            background="black"
        )
        self.clock_label.pack(pady=20)

        # Title
        title = ttk.Label(
            self.root,
            text="Mile to Kilometer Converter",
            font=("Calibri", 20, "bold"),
            foreground="blue",
            background="#222831"
        )
        title.pack(pady=5)

        # Input Frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=15)

        self.entry = ttk.Entry(input_frame, textvariable=self.input_var, font=("Arial", 12), width=18)
        self.entry.pack(side=LEFT, padx=10)
        self.input_var.trace_add("write", self.auto_clear)

        convert_btn = ttk.Button(input_frame, text="Convert", command=self.convert)
        convert_btn.pack(side=LEFT, padx=5)

        # Buttons Frame
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        clear_btn = ttk.Button(btn_frame, text="Clear", bootstyle=SECONDARY, command=self.clear)
        clear_btn.pack(side=LEFT, padx=10)

        # Output
        output_label = ttk.Label(
            self.root,
            textvariable=self.output_var,
            font=("Arial", 14, "bold"),
            foreground="red",
            background="#222831"
        )
        output_label.pack(pady=20)

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def convert(self):
        try:
            mile = float(self.input_var.get().strip())
            km = round(mile * 1.60934, 4)
            self.output_var.set(f"{mile} miles = {km} km")
        except ValueError:
            self.output_var.set("⚠️ Enter a valid number")

    def clear(self):
        self.input_var.set("")
        self.output_var.set("")

    def auto_clear(self, *args):
        self.output_var.set("")


if __name__ == "__main__":
    app = ttk.Window(themename="solar")  # Choose from: litera, darkly, cyborg, flatly, etc.
    ConverterApp(app)
    app.mainloop()
