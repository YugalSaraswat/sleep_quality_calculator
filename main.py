import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class SleepQualityApp:
    """A Tkinter application to analyze sleep quality based on hours and disturbance."""

    def _init_(self, master):
        """Initializes the main application window and widgets."""
        self.master = master
        master.title("Sleep Quality Analyzer")
        master.geometry("400x300")
        
        # Configure the grid layout for responsiveness
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f4f8')
        self.style.configure('TLabel', background='#f0f4f8', foreground='#333333', font=('Inter', 10))
        self.style.configure('TButton', font=('Inter', 10, 'bold'), padding=8)
        self.style.configure('Result.TLabel', font=('Inter', 12, 'bold'), foreground='#007bff')

        # Variables to hold user input
        self.sleep_hours = tk.DoubleVar()
        self.disturbance_var = tk.StringVar(value="no") # Default to 'no'

        # Main frame for padding and background
        self.main_frame = ttk.Frame(master, padding="20 20 20 20")
        self.main_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

        # 1. Sleep Hours Input
        ttk.Label(self.main_frame, text="1. Enter your sleep hours:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.hours_entry = ttk.Entry(self.main_frame, textvariable=self.sleep_hours, width=10, justify='center')
        self.hours_entry.grid(row=0, column=1, sticky="ew", pady=5, padx=5)
        
        # 2. Disturbance Input
        ttk.Label(self.main_frame, text="2. Disturbance during sleep?").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        
        # Radio button frame
        radio_frame = ttk.Frame(self.main_frame)
        radio_frame.grid(row=1, column=1, sticky="ew", pady=5, padx=5)
        
        ttk.Radiobutton(radio_frame, text="No", variable=self.disturbance_var, value="no").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_frame, text="Yes", variable=self.disturbance_var, value="yes").pack(side=tk.LEFT, padx=15)

        # 3. Calculation Button
        self.calculate_button = ttk.Button(self.main_frame, text="Analyze Sleep Quality", command=self.calculate_quality)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew")

        # 4. Result Display
        self.result_text = tk.StringVar()
        self.result_label = ttk.Label(self.main_frame, textvariable=self.result_text, style='Result.TLabel', wraplength=350, justify=tk.CENTER)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

    def cal_hours(self, hours):
        """Analyzes sleep hours based on the original logic."""
        if 7.0 <= hours <= 8.0:
            return "Perfect Sleep"
        elif hours < 7.0:
            return "Need little bit more sleep for perfect"
        else:
            return "You can reduce your sleep hours if that affects your work life"

    def cal_disturbance(self, disturbance):
        """Analyzes sleep disturbance based on the original logic."""
        if disturbance.lower() == "no":
            return "well done, disturbance is low"
        else:
            return "disturbance is high"

    def determine_quality(self, sleep_status, disturbance_status):
        """Combines hours and disturbance analysis for the final quality score."""
        if sleep_status == "Perfect Sleep" and disturbance_status == "well done, disturbance is low":
            return "ELITE SLEEP! Everything is optimal."
        elif sleep_status == "Perfect Sleep" and disturbance_status == "disturbance is high":
            return "Good, but try to minimize disturbances to reach elite quality."
        elif sleep_status.startswith("Need") and disturbance_status == "well done, disturbance is low":
            return "Need improvement on duration, but disturbance is low."
        else:
            # Covers "Need more sleep" scenarios with high disturbance
            return "Need more sleep and significant improvement on disturbance control."

    def calculate_quality(self):
        """Retrieves input and calculates the final sleep quality."""
        try:
            # Safely retrieve hours from the entry widget
            A = self.sleep_hours.get()
            
            # Input validation for positive hours
            if A <= 0:
                messagebox.showerror("Invalid Input", "Sleep hours must be a positive number.")
                self.result_text.set("")
                return
            
            # Retrieve disturbance status
            B = self.disturbance_var.get()

            # Apply the original logic functions
            sleep_status = self.cal_hours(A)
            disturbance_status = self.cal_disturbance(B)
            final_quality = self.determine_quality(sleep_status, disturbance_status)

            # Update the result label
            self.result_text.set(f"Sleep Analysis: {final_quality}")

        except tk.TclError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for sleep hours.")
            self.result_text.set("")
        except Exception as e:
            messagebox.showerror("An Error Occurred", str(e))
            self.result_text.set("")

# Run the application
if __name__ == '_main_':
    root = tk.Tk()
    app = SleepQualityApp(root)
    root.maioop()