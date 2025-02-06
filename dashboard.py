# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
# import random
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# def on_button_click():
#     showinfo("Button Clicked", "You clicked the button!")


# # Generate random data for the chart
# def generate_random_data():
#     return [random.randint(1, 100) for _ in range(5)]


# # Create the main window
# root = tk.Tk()
# root.title("Dashboard Example")
# root.geometry("800x600")

# # Header Frame
# header_frame = tk.Frame(root, bg="#4CAF50", height=50)
# header_frame.pack(fill="x")

# header_label = tk.Label(
#     header_frame, text="Dashboard Example", bg="#4CAF50", fg="white", font=("Arial", 16)
# )
# header_label.pack(pady=10)

# # Sidebar Frame
# sidebar_frame = tk.Frame(root, bg="#f0f0f0", width=200)
# sidebar_frame.pack(side="left", fill="y")

# # Buttons in Sidebar
# button1 = ttk.Button(sidebar_frame, text="Button 1", command=on_button_click)
# button1.pack(pady=10, padx=10, fill="x")

# button2 = ttk.Button(sidebar_frame, text="Button 2", command=on_button_click)
# button2.pack(pady=10, padx=10, fill="x")

# button3 = ttk.Button(sidebar_frame, text="Button 3", command=on_button_click)
# button3.pack(pady=10, padx=10, fill="x")

# # Main Content Frame
# main_frame = tk.Frame(root, bg="white")
# main_frame.pack(side="right", expand=True, fill="both")

# # Generate a random bar chart
# data = generate_random_data()
# labels = ["A", "B", "C", "D", "E"]

# figure = Figure(figsize=(5, 4), dpi=100)
# chart = figure.add_subplot(111)
# chart.bar(labels, data, color=["blue", "green", "red", "orange", "purple"])
# chart.set_title("Random Data Chart")
# chart.set_xlabel("Categories")
# chart.set_ylabel("Values")

# # Embed the Matplotlib chart into Tkinter
# canvas = FigureCanvasTkAgg(figure, main_frame)
# canvas.get_tk_widget().pack(expand=True, fill="both")
# canvas.draw()

# # Run the application
# root.mainloop()
import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_excel_data():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        try:
            global df
            df = pd.read_excel(file_path)
            status_label.config(text=f"Data loaded successfully from {file_path}")
            show_pie_chart()
        except Exception as e:
            status_label.config(text=f"Error loading file: {e}")

def show_pie_chart():
    if df is not None:
        try:
            # Example: Assuming the first column contains labels and the second column contains values
            labels = df.iloc[:, 0]
            values = df.iloc[:, 1]

            # Creating a pie chart
            figure = Figure(figsize=(4, 4), dpi=100)
            ax = figure.add_subplot(111)
            ax.pie(values, labels=labels, autopct='%1.1f%%')
            ax.set_title("Pie Chart")

            # Embedding the chart into Tkinter
            canvas = FigureCanvasTkAgg(figure, master=main_frame)
            canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)
            canvas.draw()

        except Exception as e:
            status_label.config(text=f"Error creating pie chart: {e}")

# Initialize Tkinter window
root = tk.Tk()
root.title("Dashboard with Pie Chart")

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Load button
load_button = ttk.Button(main_frame, text="Load Excel Data", command=load_excel_data)
load_button.grid(row=0, column=0, padx=5, pady=5)

# Status label
status_label = ttk.Label(main_frame, text="No data loaded.")
status_label.grid(row=0, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
