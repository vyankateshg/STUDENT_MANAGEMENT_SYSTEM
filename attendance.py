# import sqlite3
# import tkinter as tk
# from tkinter import messagebox
# from datetime import datetime

# def initialize_database():
#     """Initialize the SQLite database and create the attendance table."""
#     conn = sqlite3.connect("attendance.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS attendance (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             roll_no INTEGER,
#             date TEXT,
#             status TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# def mark_attendance():
#     """Save the marked attendance to the database with the current date."""
#     conn = sqlite3.connect("attendance.db")
#     cursor = conn.cursor()
#     current_date = datetime.now().strftime("%Y-%m-%d")

#     for roll_no, var in attendance_vars.items():
#         status = 'Present' if var.get() else 'Pass'
#         cursor.execute("INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)", (roll_no, current_date, status))

#     conn.commit()
#     conn.close()
#     messagebox.showinfo("Success", "Attendance marked successfully for today!")

# def create_gui():
#     """Create the Tkinter GUI for marking attendance."""
#     root = tk.Tk()
#     root.title("Student Attendance System")

#     tk.Label(root, text="Student Attendance System", font=("Helvetica", 16, "bold"), pady=10).pack()

#     canvas = tk.Canvas(root)
#     frame = tk.Frame(canvas)
#     scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
#     canvas.configure(yscrollcommand=scrollbar.set)

#     scrollbar.pack(side="right", fill="y")
#     canvas.pack(side="left", fill="both", expand=True)
#     canvas.create_window((0, 0), window=frame, anchor="nw")

#     def on_frame_configure(event):
#         canvas.configure(scrollregion=canvas.bbox("all"))

#     frame.bind("<Configure>", on_frame_configure)

#     # Create checkboxes for roll numbers
#     global attendance_vars
#     attendance_vars = {}

#     for roll_no in range(1301, 1373):
#         var = tk.BooleanVar()
#         attendance_vars[roll_no] = var
#         tk.Checkbutton(frame, text=f"Roll No: {roll_no}", variable=var).pack(anchor="w")

#     # Save button
#     tk.Button(root, text="Save Attendance", command=mark_attendance, bg="green", fg="white", font=("Helvetica", 12)).pack(pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     initialize_database()
#     create_gui()

import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def initialize_database():
    """Initialize the SQLite database and create the attendance table."""
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no INTEGER,
            date TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def mark_attendance():
    """Save the marked attendance to the database with the current date."""
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    # current_date = datetime.now().strftime("%Y-%m-%d")
    current_date = '2025-01-25'

    for roll_no, var in attendance_vars.items():
        status = 'Present' if var.get() else 'Absent'
        cursor.execute("INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)", (roll_no, current_date, status))

    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Attendance marked successfully for today!")

def create_gui():
    """Create the Tkinter GUI for marking attendance."""
    root = tk.Tk()
    root.title("Student Attendance System")

    tk.Label(root, text="Student Attendance System", font=("Helvetica", 16, "bold"), pady=10).pack()

    canvas = tk.Canvas(root)
    frame = tk.Frame(canvas)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="n")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", on_frame_configure)

    # Create checkboxes for roll numbers
    global attendance_vars
    attendance_vars = {}

    for roll_no in range(1301, 1373):
        var = tk.BooleanVar(value=True)  # Default to checked (Pass)
        attendance_vars[roll_no] = var
        tk.Checkbutton(frame, text=f"Roll No: {roll_no}", variable=var, ).pack(anchor="center")
    # Save button
    tk.Button(root, text="Save Attendance", command=mark_attendance, bg="green", fg="white", font=("Helvetica", 12)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    initialize_database()
    create_gui()
