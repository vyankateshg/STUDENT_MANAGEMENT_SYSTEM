
# import sqlite3
# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
# from tkcalendar import DateEntry
# from datetime import datetime, timedelta

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

# def mark_attendance(selected_date):
#     """Save the marked attendance to the database for the selected date."""
#     conn = sqlite3.connect("attendance.db")
#     cursor = conn.cursor()

#     for roll_no, var in attendance_vars.items():
#         status = 'Present' if var.get() else 'Pass'
#         cursor.execute("INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)", (roll_no, selected_date, status))
    
#     conn.commit()
#     conn.close()
#     messagebox.showinfo("Success", f"Attendance marked successfully for {selected_date}!")

# def view_attendance(selected_date):
#     """Fetch and display attendance for the selected date."""
#     conn = sqlite3.connect("attendance.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT roll_no, status FROM attendance WHERE date = ?", (selected_date,))
#     records = cursor.fetchall()

#     conn.close()

#     # Clear previous records in the treeview
#     for row in tree.get_children():
#         tree.delete(row)

#     # Insert new records into the treeview
#     for roll_no, status in records:
#         tree.insert("", "end", values=(roll_no, selected_date, status))
    
# def view_30_days_attendance(roll_no):
#     """Fetch and display attendance for a specific student over the last 30 days."""
#     conn = sqlite3.connect("attendance.db")
#     cursor = conn.cursor()

#     end_date = datetime.now().date()
#     start_date = (end_date - timedelta(days=30)).strftime("%Y-%m-%d")
#     end_date = end_date.strftime("%Y-%m-%d")

#     cursor.execute("""
#         SELECT date, status FROM attendance
#         WHERE roll_no = ? AND date BETWEEN ? AND ?
#         ORDER BY date
#     """, (roll_no, start_date, end_date))
#     records = cursor.fetchall()

#     conn.close()

#     # Clear previous records in the treeview
#     for row in tree.get_children():
#         tree.delete(row)

#     # Insert new records into the treeview
#     for date, status in records:
#         tree.insert("", "end", values=(roll_no, date, status))

# def create_gui():
#     """Create the Tkinter GUI for marking and viewing attendance."""
#     root = tk.Tk()
#     root.title("Student Attendance System")

#     tk.Label(root, text="Student Attendance System", font=("Helvetica", 16, "bold"), pady=10).pack()

#     # Date picker
#     date_frame = ttk.LabelFrame(root, text="Date Selection", padding=10)
#     date_frame.pack(pady=10, fill="x")

#     tk.Label(date_frame, text="Select Date:", font=("Helvetica", 12)).pack(side="left", padx=5)
#     date_picker = DateEntry(date_frame, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern='yyyy-MM-dd')
#     date_picker.pack(side="left", padx=5)

#     # Attendance checkboxes with scrollbar
#     attendance_frame = ttk.LabelFrame(root, text="Mark Attendance", padding=10)
#     attendance_frame.pack(pady=10, fill="both", expand=True)

#     canvas = tk.Canvas(attendance_frame)
#     scrollbar = ttk.Scrollbar(attendance_frame, orient="vertical", command=canvas.yview)
#     scrollable_frame = ttk.Frame(canvas)

#     scrollable_frame.bind(
#         "<Configure>",
#         lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#     )

#     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#     canvas.configure(yscrollcommand=scrollbar.set)

#     canvas.pack(side="left", fill="both", expand=True)
#     scrollbar.pack(side="right", fill="y")

#     global attendance_vars
#     attendance_vars = {}

#     # for roll_no in range(1301, 1373):
#     #     var = tk.BooleanVar(value=True)  # Default to checked (Pass)
#     #     attendance_vars[roll_no] = var
#     #     tk.Checkbutton(scrollable_frame, text=f"Roll No: {roll_no}", variable=var).pack(anchor="w")
 
#     for roll_no in range(1301, 1373):
#         var = tk.BooleanVar(value=True)  # Default to checked (Pass)
#         attendance_vars[roll_no] = var
#         tk.Checkbutton(
#             scrollable_frame, 
#             text=f"Roll No: {roll_no}", 
#             variable=var, 
#             anchor="center",  # Center-align the text
#             width=20  # Set a fixed width to ensure consistent alignment
#         ).pack(anchor="w")

#     # Save Attendance Button
#     tk.Button(root, text="Save Attendance", command=lambda: mark_attendance(date_picker.get()), bg="green", fg="white", font=("Helvetica", 12)).pack(pady=10)

#     # View Attendance Section
#     view_frame = ttk.LabelFrame(root, text="View Attendance", padding=10)
#     view_frame.pack(pady=10, fill="both", expand=True)

#     tk.Button(view_frame, text="View Attendance for Selected Date", command=lambda: view_attendance(date_picker.get()), bg="blue", fg="white", font=("Helvetica", 12)).pack(pady=5)

#     tk.Label(view_frame, text="Enter Roll No to View Last 30 Days Attendance:", font=("Helvetica", 12)).pack(pady=5)
#     roll_no_entry = tk.Entry(view_frame, font=("Helvetica", 12))
#     roll_no_entry.pack(pady=5)

#     tk.Button(view_frame, text="View 30 Days Attendance", 
#               command=lambda: view_30_days_attendance(roll_no_entry.get()), 
#               bg="orange", fg="white", font=("Helvetica", 12)).pack(pady=5)

#     # Frame for Treeview with Scrollbar
#     tree_frame = ttk.LabelFrame(root, text="Attendance Records", padding=10)
#     tree_frame.pack(pady=10, fill="both", expand=True)

#     tree_scroll = ttk.Scrollbar(tree_frame)
#     tree_scroll.pack(side="right", fill="y")

#     global tree
#     columns = ("Roll No", "Date", "Status")
#     tree = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
#     tree.heading("Roll No", text="Roll No")
#     tree.heading("Date", text="Date")
#     tree.heading("Status", text="Status")
#     tree.pack(fill="both", expand=True)

#     tree_scroll.config(command=tree.yview)

#     root.geometry("1000x700")  # Adjust window size
#     root.mainloop()

# if __name__ == "__main__":
#     initialize_database()
#     create_gui()

import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta

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

def mark_attendance(selected_date):
    """Save the marked attendance to the database for the selected date."""
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    for roll_no, var in attendance_vars.items():
        status = 'Present' if var.get() else 'Pass'
        cursor.execute("INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)", (roll_no, selected_date, status))

    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Attendance marked successfully for {selected_date}!")

def view_30_days_attendance(roll_no):
    """Fetch and display attendance for a specific student over the last 30 days."""
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    end_date = datetime.now().date()
    start_date = (end_date - timedelta(days=30)).strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT date, status FROM attendance
        WHERE roll_no = ? AND date BETWEEN ? AND ?
        ORDER BY date
    """, (roll_no, start_date, end_date))
    records = cursor.fetchall()

    conn.close()

    # Clear previous records in the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insert new records into the treeview
    for date, status in records:
        tree.insert("", "end", values=(roll_no, date, status))

def create_gui():
    """Create the Tkinter GUI for marking and viewing attendance."""
    root = tk.Tk()
    root.title("Student Attendance System")

    tk.Label(root, text="Student Attendance System", font=("Helvetica", 16, "bold"), pady=10).pack()

    # Date picker
    date_frame = ttk.LabelFrame(root, text="Date Selection", padding=10)
    date_frame.pack(pady=10, fill="x")

    tk.Label(date_frame, text="Select Date:", font=("Helvetica", 12)).pack(side="left", padx=5)
    date_picker = DateEntry(date_frame, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern='yyyy-MM-dd')
    date_picker.pack(side="left", padx=5)

    # Attendance checkboxes with scrollbar
    attendance_frame = ttk.LabelFrame(root, text="Mark Attendance", padding=10)
    attendance_frame.pack(pady=10, fill="both", expand=True)

    canvas = tk.Canvas(attendance_frame)
    scrollbar = ttk.Scrollbar(attendance_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    global attendance_vars
    attendance_vars = {}

    for roll_no in range(1301, 1373):
        var = tk.BooleanVar(value=True)  # Default to checked (Pass)
        attendance_vars[roll_no] = var
        tk.Checkbutton(
            scrollable_frame, 
            text=f"Roll No: {roll_no}", 
            variable=var, 
            anchor="center",  # Center-align the text
            width=20  # Set a fixed width to ensure consistent alignment
        ).pack(anchor="w")

    # Save Attendance Button
    tk.Button(root, text="Save Attendance", command=lambda: mark_attendance(date_picker.get()), bg="green", fg="white", font=("Helvetica", 12)).pack(pady=10)

    # View Attendance Section
    view_frame = ttk.LabelFrame(root, text="View Attendance", padding=10)
    view_frame.pack(pady=10, fill="both", expand=True)

    tk.Label(view_frame, text="Enter Roll No to View Last 30 Days Attendance:", font=("Helvetica", 12)).pack(pady=5)
    roll_no_entry = tk.Entry(view_frame, font=("Helvetica", 12))
    roll_no_entry.pack(pady=5)

    tk.Button(view_frame, text="View 30 Days Attendance", 
              command=lambda: view_30_days_attendance(roll_no_entry.get()), 
              bg="orange", fg="white", font=("Helvetica", 12)).pack(pady=5)

    # Frame for Treeview with Scrollbar
    tree_frame = ttk.LabelFrame(root, text="Attendance Records", padding=10)
    tree_frame.pack(pady=10, fill="both", expand=True)

    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side="right", fill="y")

    global tree
    columns = ("Roll No", "Date", "Status")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
    tree.heading("Roll No", text="Roll No")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")
    tree.pack(fill="both", expand=True)

    tree_scroll.config(command=tree.yview)

    root.geometry("1000x700")  # Adjust window size
    root.mainloop()

if __name__ == "__main__":
    initialize_database()
    create_gui()