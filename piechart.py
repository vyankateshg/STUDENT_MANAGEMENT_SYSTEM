import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

 # Sample Data
data = {
     'Roll No': [1301, 1302, 1303, 1304, 1305],
     '25-01-2025': ['P', 'P', 'A', 'P', 'A'],
     '26-01-2025': ['P', 'A', 'A', 'P', 'P'],
     '27-01-2025': ['P', 'P', 'A', 'P', 'A']
 }

#  Convert data into a DataFrame
df = pd.DataFrame(data)

# Calculate attendance summary for each student
def calculate_attendance(df):
    attendance_summary = []
    for index, row in df.iterrows():
        total_present = list(row[1:]).count('P')
        total_absent = list(row[1:]).count('A')
        attendance_summary.append((row['Roll No'], total_present, total_absent))
    return attendance_summary

attendance_summary = calculate_attendance(df)

# Create a function to display pie chart for a student
def show_pie_chart(roll_no):
    for student in attendance_summary:
        if student[0] == roll_no:
            present = student[1]
            absent = student[2]

            # Create pie chart
            fig = Figure(figsize=(4, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.pie(
                [present, absent],
                labels=['Present', 'Absent'],
                colors=['green', 'red'],
                autopct='%1.1f%%',
                startangle=90
            )
            ax.set_title(f"Attendance for Roll No: {roll_no}")

            # Display the chart in tkinter
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)
            canvas.draw()
            break

# Tkinter GUI
root = tk.Tk()
root.title("Student Attendance Dashboard")

# Dropdown menu to select student
ttk.Label(root, text="Select Roll No:").grid(row=0, column=0, padx=10, pady=10)

roll_no_var = tk.IntVar()
roll_no_menu = ttk.Combobox(root, textvariable=roll_no_var, values=[row[0] for row in attendance_summary])
roll_no_menu.grid(row=0, column=1, padx=10, pady=10)

# Button to show pie chart
ttk.Button(root, text="Show Attendance", command=lambda: show_pie_chart(roll_no_var.get())).grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()

# import tkinter as tk
# from tkinter import ttk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import pandas as pd

# # Load Excel data
# file_path = "student_attendance1.xlsx"  # Replace with your file path
# df = pd.read_excel(file_path)

# # Calculate attendance summary for each student
# def calculate_attendance(df):
#     attendance_summary = []
#     for index, row in df.iterrows():
#         total_present = list(row[1:]).count('P')
#         total_absent = list(row[1:]).count('A')
#         attendance_summary.append((row['Roll No'], total_present, total_absent))
#     return attendance_summary

# attendance_summary = calculate_attendance(df)

# # Create a function to display pie chart for a student
# def show_pie_chart(roll_no):
#     for student in attendance_summary:
#         if student[0] == roll_no:
#             present = student[1]
#             absent = student[2]

#             # Create pie chart
#             fig = Figure(figsize=(4, 4), dpi=100)
#             ax = fig.add_subplot(111)
#             ax.pie(
#                 [present, absent],
#                 labels=['Present', 'Absent'],
#                 colors=['green', 'red'],
#                 autopct='%1.1f%%',
#                 startangle=90
#             )
#             ax.set_title(f"Attendance for Roll No: {roll_no}")

#             # Display the chart in tkinter
#             canvas = FigureCanvasTkAgg(fig, master=root)
#             canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)
#             canvas.draw()
#             break

# # Tkinter GUI
# root = tk.Tk()
# root.title("Student Attendance Dashboard")

# # Dropdown menu to select student
# ttk.Label(root, text="Select Roll No:").grid(row=0, column=0, padx=10, pady=10)

# roll_no_var = tk.IntVar()
# roll_no_menu = ttk.Combobox(root, textvariable=roll_no_var, values=[row[0] for row in attendance_summary])
# roll_no_menu.grid(row=0, column=1, padx=10, pady=10)

# # Button to show pie chart
# ttk.Button(root, text="Show Attendance", command=lambda: show_pie_chart(roll_no_var.get())).grid(row=1, column=0, columnspan=2, pady=10)

# root.mainloop()
