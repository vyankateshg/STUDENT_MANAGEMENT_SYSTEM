# import pyttsx3
# import speech_recognition as sr
# import tkinter as tk
# from tkinter import scrolledtext, messagebox, ttk
# import time
# import threading

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"Error in TTS: {e}")

# # Questions and answers
# questions = {
#     "python": {
#         "What is the keyword to define a function?": ["def", "func", "define", "lambda"],
#         "What is the output of print(2 + 2)?": ["4", "22", "8", "None"],
#         "What is the type of [1, 2, 3]?": ["list", "tuple", "set", "dictionary"],
#         "What is the keyword to define a class?": ["class", "def", "object", "init"],
#         "What method is used to add an item to a list?": ["append", "insert", "push", "add"]
#     },
#     "c": {
#         "What is the format specifier for an integer?": ["%d", "%f", "%c", "%s"],
#         "What is the keyword to include header files?": ["include", "import", "header", "load"],
#         "What is the result of 5 modulo 2?": ["1", "2", "0", "5"],
#         "What is the return type of the main function?": ["int", "void", "char", "float"],
#         "Which operator is used to access a pointer's value?": ["*", "&", "%", "@"]
#     },
#     "dsa": {
#         "What data structure uses FIFO?": ["Queue", "Stack", "Heap", "Tree"],
#         "What data structure uses LIFO?": ["Stack", "Queue", "Graph", "List"],
#         "What is the time complexity of binary search?": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
#         "What is a dynamic programming technique?": ["Memoization", "Sorting", "Searching", "Hashing"],
#         "What data structure is used for depth-first search?": ["Stack", "Queue", "Graph", "Array"]
#     }
# }

# def start_voice_viva():
#     global subject
#     subject = subject_entry.get().lower()
#     if subject in questions:
#         viva_window()
#     else:
#         messagebox.showerror("Invalid Subject", "Please choose Python, C, or DSA.")


# def viva_window():
#     global question_list, question_label, answer_var, question_index, log, next_button

#     question_list = list(questions[subject].items())
#     question_index = 0

#     # Hide subject selection window
#     main_window.withdraw()

#     # New window for viva
#     viva = tk.Toplevel(main_window)
#     viva.title("Voice Viva")

#     question_label = tk.Label(viva, text="Question will appear here.", wraplength=400, font=("Arial", 14))
#     question_label.pack(pady=10)

#     answer_var = tk.StringVar()

#     answer_frame = tk.Frame(viva)
#     answer_frame.pack(pady=10)

#     answer_checkboxes = []
#     for i in range(4):
#         cb = tk.Checkbutton(answer_frame, text="", variable=tk.StringVar(), font=("Arial", 12), anchor='w')
#         cb.pack(fill='x', padx=10, pady=2)
#         answer_checkboxes.append(cb)

#     next_button = tk.Button(
#         viva,
#         text="Next",
#         command=lambda: process_answer(answer_checkboxes, viva),
#         font=("Arial", 12),
#     )
#     next_button.pack(pady=10)

#     log = scrolledtext.ScrolledText(viva, wrap=tk.WORD, font=("Arial", 10), width=50, height=10)
#     log.pack(pady=10)

#     def delayed_question():
#         ask_question(answer_checkboxes)
#         next_button.config(state=tk.NORMAL)

#     threading.Thread(target=delayed_question).start()


# def ask_question(answer_checkboxes):
#     global question_index
#     if question_index < len(question_list):
#         question, options = question_list[question_index]
#         speak(question)
#         question_label.config(text=question)

#         # Set checkbox texts
#         for i, option in enumerate(options):
#             answer_checkboxes[i].config(text=option)
#     else:
#         speak("The viva is over. Thank you!")
#         messagebox.showinfo("Viva Complete", "You have completed the viva!")
#         main_window.deiconify()
#         question_label.master.destroy()


# def process_answer(answer_checkboxes, viva_window):
#     global question_index
#     if question_index >= len(question_list):
#         return

#     next_button.config(state=tk.DISABLED)

#     correct_answer = question_list[question_index][1][0]

#     # Find selected answer
#     selected_answer = None
#     for cb in answer_checkboxes:
#         if cb.var.get():
#             selected_answer = cb.cget("text")
#             break

#     with open("viva_answers.txt", "a") as file:
#         file.write(f"Question: {question_list[question_index][0]}\n")
#         file.write(f"Your Answer: {selected_answer}\n")
#         if selected_answer == correct_answer:
#             log.insert(tk.END, "Correct!\n")
#             file.write("Result: Correct\n\n")
#         else:
#             log.insert(tk.END, f"Wrong. Correct Answer: {correct_answer}\n")
#             file.write(f"Correct Answer: {correct_answer}\n")
#             file.write("Result: Wrong\n\n")

#     question_index += 1
#     time.sleep(1)
#     ask_question(answer_checkboxes)
#     next_button.config(state=tk.NORMAL)

# # Main Window
# main_window = tk.Tk()
# main_window.title("Voice Viva")

# # UI Elements
# tk.Label(main_window, text="Welcome to the Voice Viva!", font=("Arial", 16)).pack(pady=10)
# tk.Label(main_window, text="Choose a subject: Python, C, or DSA", font=("Arial", 12)).pack(pady=5)

# subject_entry = tk.Entry(main_window, font=("Arial", 12))
# subject_entry.pack(pady=5)

# start_button = tk.Button(main_window, text="Start Viva", command=start_voice_viva, font=("Arial", 12))
# start_button.pack(pady=20)

# main_window.mainloop()


# import pyttsx3
# import tkinter as tk
# from tkinter import scrolledtext, messagebox
# import time
# import threading

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"Error in TTS: {e}")

# # Questions and answers
# questions = {
#     "python": {
#         "What is the keyword to define a function?": ["def", "func", "define", "lambda"],
#         "What is the output of print(2 + 2)?": ["4", "22", "8", "None"],
#         "What is the type of [1, 2, 3]?": ["list", "tuple", "set", "dictionary"],
#         "What is the keyword to define a class?": ["class", "def", "object", "init"],
#         "What method is used to add an item to a list?": ["append", "insert", "push", "add"]
#     },
#     "c": {
#         "What is the format specifier for an integer?": ["%d", "%f", "%c", "%s"],
#         "What is the keyword to include header files?": ["include", "import", "header", "load"],
#         "What is the result of 5 modulo 2?": ["1", "2", "0", "5"],
#         "What is the return type of the main function?": ["int", "void", "char", "float"],
#         "Which operator is used to access a pointer's value?": ["*", "&", "%", "@"]
#     },
#     "dsa": {
#         "What data structure uses FIFO?": ["Queue", "Stack", "Heap", "Tree"],
#         "What data structure uses LIFO?": ["Stack", "Queue", "Graph", "List"],
#         "What is the time complexity of binary search?": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
#         "What is a dynamic programming technique?": ["Memoization", "Sorting", "Searching", "Hashing"],
#         "What data structure is used for depth-first search?": ["Stack", "Queue", "Graph", "Array"]
#     }
# }

# def start_voice_viva():
#     global subject
#     subject = subject_entry.get().lower()
#     if subject in questions:
#         viva_window()
#     else:
#         messagebox.showerror("Invalid Subject", "Please choose Python, C, or DSA.")

# def viva_window():
#     global question_list, question_label, question_index, log, next_button, answer_vars

#     question_list = list(questions[subject].items())
#     question_index = 0

#     # Hide subject selection window
#     main_window.withdraw()

#     # New window for viva
#     viva = tk.Toplevel(main_window)
#     viva.title("Voice Viva")

#     question_label = tk.Label(viva, text="Question will appear here.", wraplength=400, font=("Arial", 14))
#     question_label.pack(pady=10)

#     # Answer checkboxes
#     answer_frame = tk.Frame(viva)
#     answer_frame.pack(pady=10)

#     answer_vars = []  # List to hold StringVar for each checkbox
#     answer_checkboxes = []

#     for i in range(4):
#         var = tk.StringVar()  # Create a separate StringVar for each checkbox
#         cb = tk.Checkbutton(answer_frame, text="", variable=var, font=("Arial", 12), anchor='w', onvalue="selected", offvalue="")
#         cb.pack(fill='x', padx=10, pady=2)
#         answer_vars.append(var)
#         answer_checkboxes.append(cb)

#     next_button = tk.Button(
#         viva,
#         text="Next",
#         command=lambda: process_answer(answer_vars, viva),
#         font=("Arial", 12),
#     )
#     next_button.pack(pady=10)

#     log = scrolledtext.ScrolledText(viva, wrap=tk.WORD, font=("Arial", 10), width=50, height=10)
#     log.pack(pady=10)

#     def delayed_question():
#         ask_question(answer_checkboxes)
#         next_button.config(state=tk.NORMAL)

#     threading.Thread(target=delayed_question).start()

# # def ask_question(answer_checkboxes):
# #     global question_index
# #     if question_index < len(question_list):
# #         question, options = question_list[question_index]
# #         speak(question)
# #         question_label.config(text=question)

# #         # Set checkbox texts
# #         for i, option in enumerate(options):
# #             answer_checkboxes[i].config(text=option)
# #     else:
# #         speak("The viva is over. Thank you!")
# #         messagebox.showinfo("Viva Complete", "You have completed the viva!")
# #         main_window.deiconify()
# #         question_label.master.destroy()

# def ask_question(answer_checkboxes):
#     global question_index
#     if question_index < len(question_list):
#         question, options = question_list[question_index]
#         speak(question)
#         question_label.config(text=question)

#         # Set checkbox texts dynamically, ensuring no index out of range
#         for i in range(4):
#             if i < len(options):
#                 answer_checkboxes[i].config(text=options[i], state=tk.NORMAL)
#             else:
#                 answer_checkboxes[i].config(text="", state=tk.DISABLED)  # Disable unused checkboxes
#     else:
#         speak("The viva is over. Thank you!")
#         messagebox.showinfo("Viva Complete", "You have completed the viva!")
#         main_window.deiconify()
#         question_label.master.destroy()


# def process_answer(answer_vars, viva_window):
#     global question_index
#     if question_index >= len(question_list):
#         return

#     next_button.config(state=tk.DISABLED)

#     correct_answer = question_list[question_index][1][0]

#     # Find selected answer
#     selected_answer = None
#     for i, var in enumerate(answer_vars):
#         if var.get() == "selected":  # Check if the checkbox is selected
#             selected_answer = question_list[question_index][1][i]  # Get the corresponding answer
#             break

#     with open("viva_answers.txt", "a") as file:
#         file.write(f"Question: {question_list[question_index][0]}\n")
#         file.write(f"Your Answer: {selected_answer}\n")
#         if selected_answer == correct_answer:
#             log.insert(tk.END, "Correct!\n")
#             file.write("Result: Correct\n\n")
#         else:
#             log.insert(tk.END, f"Wrong. Correct Answer: {correct_answer}\n")
#             file.write(f"Correct Answer: {correct_answer}\n")
#             file.write("Result: Wrong\n\n")

#     question_index += 1
#     time.sleep(1)
#     ask_question([cb for cb in viva_window.winfo_children() if isinstance(cb, tk.Checkbutton)])
#     next_button.config(state=tk.NORMAL)

# # Main Window
# main_window = tk.Tk()
# main_window.title("Voice Viva")

# # UI Elements
# tk.Label(main_window, text="Welcome to the Voice Viva!", font=("Arial", 16)).pack(pady=10)
# tk.Label(main_window, text="Choose a subject: Python, C, or DSA", font=("Arial", 12)).pack(pady=5)

# subject_entry = tk.Entry(main_window, font=("Arial", 12))
# subject_entry.pack(pady=5)

# start_button = tk.Button(main_window, text="Start Viva", command=start_voice_viva, font=("Arial", 12))
# start_button.pack(pady=20)

# main_window.mainloop()


# import pyttsx3
# import speech_recognition as sr
# import tkinter as tk
# from tkinter import scrolledtext, messagebox
# import threading

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"Error in TTS: {e}")

# # Questions and answers
# questions = {
#     "python": {
#         "What is the keyword to define a function?": ["def", "func", "define", "lambda"],
#         "What is the output of print(2 + 2)?": ["4", "22", "8", "None"],
#         "What is the type of [1, 2, 3]?": ["list", "tuple", "set", "dictionary"],
#         "What is the keyword to define a class?": ["class", "def", "object", "init"],
#         "What method is used to add an item to a list?": ["append", "insert", "push", "add"]
#     },
#     "c": {
#         "What is the format specifier for an integer?": ["%d", "%f", "%c", "%s"],
#         "What is the keyword to include header files?": ["include", "import", "header", "load"],
#         "What is the result of 5 modulo 2?": ["1", "2", "0", "5"],
#         "What is the return type of the main function?": ["int", "void", "char", "float"],
#         "Which operator is used to access a pointer's value?": ["*", "&", "%", "@"]
#     },
#     "dsa": {
#         "What data structure uses FIFO?": ["Queue", "Stack", "Heap", "Tree"],
#         "What data structure uses LIFO?": ["Stack", "Queue", "Graph", "List"],
#         "What is the time complexity of binary search?": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
#         "What is a dynamic programming technique?": ["Memoization", "Sorting", "Searching", "Hashing"],
#         "What data structure is used for depth-first search?": ["Stack", "Queue", "Graph", "Array"]
#     }
# }

# def start_voice_viva():
#     global subject
#     subject = subject_entry.get().lower()
#     if subject in questions:
#         viva_window()
#     else:
#         messagebox.showerror("Invalid Subject", "Please choose Python, C, or DSA.")

# def viva_window():
#     global question_list, question_label, answer_vars, question_index, log, answer_checkboxes, next_button

#     question_list = list(questions[subject].items())
#     question_index = 0

#     # Hide subject selection window
#     main_window.withdraw()

#     viva = tk.Toplevel(main_window)
#     viva.title("Voice Viva")

#     question_label = tk.Label(viva, text="Question will appear here.", wraplength=400, font=("Arial", 14))
#     question_label.pack(pady=10)

#     answer_vars = [tk.StringVar() for _ in range(4)]  # Variables for checkboxes
#     answer_checkboxes = []

#     answer_frame = tk.Frame(viva)
#     answer_frame.pack(pady=10)

#     for i in range(4):
#         cb = tk.Checkbutton(answer_frame, text="", variable=answer_vars[i], font=("Arial", 12), anchor='w', onvalue="1", offvalue="0")
#         cb.pack(fill='x', padx=10, pady=2)
#         answer_checkboxes.append(cb)

#     next_button = tk.Button(
#         viva,
#         text="Next",
#         command=lambda: process_answer(answer_vars, viva),
#         font=("Arial", 12),
#     )
#     next_button.pack(pady=10)

#     log = scrolledtext.ScrolledText(viva, wrap=tk.WORD, font=("Arial", 10), width=50, height=10)
#     log.pack(pady=10)

#     ask_question(answer_checkboxes)

# def ask_question(answer_checkboxes):
#     global question_index
#     if question_index < len(question_list):
#         question, options = question_list[question_index]
#         speak(question)
#         question_label.config(text=question)

#         # Safely configure checkboxes based on options length
#         for i, cb in enumerate(answer_checkboxes):
#             if i < len(options):
#                 cb.config(text=options[i], state=tk.NORMAL)
#             else:
#                 cb.config(text="", state=tk.DISABLED)  # Disable extra checkboxes
#     else:
#         speak("The viva is over. Thank you!")
#         messagebox.showinfo("Viva Complete", "You have completed the viva!")
#         main_window.deiconify()
#         question_label.master.destroy()

# def process_answer(answer_vars, viva_window):
#     global question_index
#     if question_index >= len(question_list):
#         return

#     correct_answer = question_list[question_index][1][0]

#     # Get the selected answer from variables
#     selected_answer = None
#     for var in answer_vars:
#         if var.get() == "1":
#             selected_answer = var._name
#             break

#     with open("viva_answers.txt", "a") as file:
#         file.write(f"Question: {question_list[question_index][0]}\n")
#         file.write(f"Your Answer: {selected_answer}\n")
#         if selected_answer == correct_answer:
#             log.insert(tk.END, "Correct!\n")
#             file.write("Result: Correct\n\n")
#         else:
#             log.insert(tk.END, f"Wrong. Correct Answer: {correct_answer}\n")
#             file.write(f"Correct Answer: {correct_answer}\n")
#             file.write("Result: Wrong\n\n")

#     question_index += 1
#     ask_question(answer_checkboxes)

# # Main Window
# main_window = tk.Tk()
# main_window.title("Voice Viva")

# # UI Elements
# tk.Label(main_window, text="Welcome to the Voice Viva!", font=("Arial", 16)).pack(pady=10)
# tk.Label(main_window, text="Choose a subject: Python, C, or DSA", font=("Arial", 12)).pack(pady=5)

# subject_entry = tk.Entry(main_window, font=("Arial", 12))
# subject_entry.pack(pady=5)

# start_button = tk.Button(main_window, text="Start Viva", command=start_voice_viva, font=("Arial", 12))
# start_button.pack(pady=20)

# main_window.mainloop()



## well working one but only one issue 
# import pyttsx3
# import tkinter as tk
# from tkinter import scrolledtext, messagebox

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"Error in TTS: {e}")

# # Questions and answers
# questions = {
#     "python": {
#         "What is the keyword to define a function?": ["def", "func", "define", "lambda"],
#         "What is the output of print(2 + 2)?": ["22", "4", "8", "None"],
#         "What is the type of [1, 2, 3]?": ["list", "tuple", "set", "dictionary"],
#         "What is the keyword to define a class?": ["class", "def", "object", "init"],
#         "What method is used to add an item to a list?": ["append", "insert", "push", "add"]
#     },
#     "c": {
#         "What is the format specifier for an integer?": ["%d", "%f", "%c", "%s"],
#         "What is the keyword to include header files?": ["include", "import", "header", "load"],
#         "What is the result of 5 modulo 2?": ["1", "2", "0", "5"],
#         "What is the return type of the main function?": ["int", "void", "char", "float"],
#         "Which operator is used to access a pointer's value?": ["*", "&", "%", "@"]
#     },
#     "dsa": {
#         "What data structure uses FIFO?": ["Queue", "Stack", "Heap", "Tree"],
#         "What data structure uses LIFO?": ["Stack", "Queue", "Graph", "List"],
#         "What is the time complexity of binary search?": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
#         "What is a dynamic programming technique?": ["Memoization", "Sorting", "Searching", "Hashing"],
#         "What data structure is used for depth-first search?": ["Stack", "Queue", "Graph", "Array"]
#     }
# }

# def start_voice_viva():
#     global subject
#     subject = subject_entry.get().lower()
#     if subject in questions:
#         viva_window()
#     else:
#         messagebox.showerror("Invalid Subject", "Please choose Python, C, or DSA.")

# def viva_window():
#     global question_list, question_label, answer_vars, question_index, log, answer_checkboxes, next_button

#     question_list = list(questions[subject].items())
#     question_index = 0

#     # Hide subject selection window
#     main_window.withdraw()

#     viva = tk.Toplevel(main_window)
#     viva.title("Voice Viva")

#     question_label = tk.Label(viva, text="Question will appear here.", wraplength=400, font=("Arial", 14))
#     question_label.pack(pady=10)

#     answer_vars = [tk.StringVar(value="0") for _ in range(4)]  # Default unchecked state for checkboxes
#     answer_checkboxes = []

#     answer_frame = tk.Frame(viva)
#     answer_frame.pack(pady=10)

#     for i in range(4):
#         cb = tk.Checkbutton(answer_frame, text="", variable=answer_vars[i], font=("Arial", 12), anchor='w', onvalue="1", offvalue="0")
#         cb.pack(fill='x', padx=10, pady=2)
#         answer_checkboxes.append(cb)

#     next_button = tk.Button(
#         viva,
#         text="Next",
#         command=lambda: process_answer(answer_vars, viva),
#         font=("Arial", 12),
#     )
#     next_button.pack(pady=10)

#     log = scrolledtext.ScrolledText(viva, wrap=tk.WORD, font=("Arial", 10), width=50, height=10)
#     log.pack(pady=10)

#     ask_question(answer_checkboxes)

# def ask_question(answer_checkboxes):
#     global question_index
#     if question_index < len(question_list):
#         question, options = question_list[question_index]
#         speak(question)
#         question_label.config(text=question)

#         # Safely configure checkboxes based on options length
#         for i, cb in enumerate(answer_checkboxes):
#             if i < len(options):
#                 cb.config(text=options[i], state=tk.NORMAL)
#             else:
#                 cb.config(text="", state=tk.DISABLED)  # Disable extra checkboxes
#     else:
#         speak("The viva is over. Thank you!")
#         messagebox.showinfo("Viva Complete", "You have completed the viva!")
#         main_window.deiconify()
#         question_label.master.destroy()

# def process_answer(answer_vars, viva_window):
#     global question_index
#     if question_index >= len(question_list):
#         return

#     correct_answer = question_list[question_index][1][0]

#     # Get the selected answer from variables
#     selected_answer = None
#     for i, var in enumerate(answer_vars):
#         if var.get() == "1":  # If checkbox is selected
#             selected_answer = answer_checkboxes[i].cget("text")
#             break

#     with open("viva_answers.txt", "a") as file:
#         file.write(f"Question: {question_list[question_index][0]}\n")
#         file.write(f"Your Answer: {selected_answer}\n")
#         if selected_answer == correct_answer:
#             log.insert(tk.END, "Correct!\n")
#             file.write("Result: Correct\n\n")
#         else:
#             log.insert(tk.END, f"Wrong. Correct Answer: {correct_answer}\n")
#             file.write(f"Correct Answer: {correct_answer}\n")
#             file.write("Result: Wrong\n\n")

#     question_index += 1
#     ask_question(answer_checkboxes)

# # Main Window
# main_window = tk.Tk()
# main_window.title("Voice Viva")

# # UI Elements
# tk.Label(main_window, text="Welcome to the Voice Viva!", font=("Arial", 16)).pack(pady=10)
# tk.Label(main_window, text="Choose a subject: Python, C, or DSA", font=("Arial", 12)).pack(pady=5)

# subject_entry = tk.Entry(main_window, font=("Arial", 12))
# subject_entry.pack(pady=5)

# start_button = tk.Button(main_window, text="Start Viva", command=start_voice_viva, font=("Arial", 12))
# start_button.pack(pady=20)

# main_window.mainloop()

### fully working but root destroy for a second
# import pyttsx3
# import tkinter as tk
# from tkinter import scrolledtext, messagebox

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"Error in TTS: {e}")

# # Questions and answers
# questions = {
#     "python": {
#         "What is the keyword to define a function?": ["def", "func", "define", "lambda"],
#         "What is the output of print(2 + 2)?": ["4", "22", "8", "None"],
#         "What is the type of [1, 2, 3]?": ["list", "tuple", "set", "dictionary"],
#         "What is the keyword to define a class?": ["class", "def", "object", "init"],
#         "What method is used to add an item to a list?": ["append", "insert", "push", "add"]
#     },
#     "c": {
#         "What is the format specifier for an integer?": ["%d", "%f", "%c", "%s"],
#         "What is the keyword to include header files?": ["include", "import", "header", "load"],
#         "What is the result of 5 modulo 2?": ["1", "2", "0", "5"],
#         "What is the return type of the main function?": ["int", "void", "char", "float"],
#         "Which operator is used to access a pointer's value?": ["*", "&", "%", "@"]
#     },
#     "dsa": {
#         "What data structure uses FIFO?": ["Queue", "Stack", "Heap", "Tree"],
#         "What data structure uses LIFO?": ["Stack", "Queue", "Graph", "List"],
#         "What is the time complexity of binary search?": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
#         "What is a dynamic programming technique?": ["Memoization", "Sorting", "Searching", "Hashing"],
#         "What data structure is used for depth-first search?": ["Stack", "Queue", "Graph", "Array"]
#     }
# }

# def start_voice_viva():
#     global subject
#     subject = subject_entry.get().lower()
#     if subject in questions:
#         viva_window()
#     else:
#         messagebox.showerror("Invalid Subject", "Please choose Python, C, or DSA.")

# def viva_window():
#     global question_list, question_label, answer_vars, question_index, log, answer_checkboxes, next_button

#     question_list = list(questions[subject].items())
#     question_index = 0

#     # Hide subject selection window
#     main_window.withdraw()

#     viva = tk.Toplevel(main_window)
#     viva.title("Voice Viva")

#     question_label = tk.Label(viva, text="Question will appear here.", wraplength=400, font=("Arial", 14))
#     question_label.pack(pady=10)

#     answer_vars = [tk.StringVar(value="0") for _ in range(4)]  # Default unchecked state for checkboxes
#     answer_checkboxes = []

#     answer_frame = tk.Frame(viva)
#     answer_frame.pack(pady=10)

#     for i in range(4):
#         cb = tk.Checkbutton(answer_frame, text="", variable=answer_vars[i], font=("Arial", 12), anchor='w', onvalue="1", offvalue="0")
#         cb.pack(fill='x', padx=10, pady=2)
#         answer_checkboxes.append(cb)

#     next_button = tk.Button(
#         viva,
#         text="Next",
#         command=lambda: process_answer(answer_vars, viva),
#         font=("Arial", 12),
#     )
#     next_button.pack(pady=10)

#     log = scrolledtext.ScrolledText(viva, wrap=tk.WORD, font=("Arial", 10), width=50, height=10)
#     log.pack(pady=10)

#     ask_question(answer_checkboxes)

# def ask_question(answer_checkboxes):
#     global question_index
#     if question_index < len(question_list):
#         question, options = question_list[question_index]
#         speak(question)
#         question_label.config(text=question)

#         # Safely configure checkboxes based on options length
#         for i, cb in enumerate(answer_checkboxes):
#             if i < len(options):
#                 cb.config(text=options[i], state=tk.NORMAL)
#             else:
#                 cb.config(text="", state=tk.DISABLED)  # Disable extra checkboxes
#     else:
#         speak("The viva is over. Thank you!")
#         messagebox.showinfo("Viva Complete", "You have completed the viva!")
#         main_window.deiconify()
#         question_label.master.destroy()

# def process_answer(answer_vars, viva_window):
#     global question_index
#     if question_index >= len(question_list):
#         return

#     correct_answer = question_list[question_index][1][0]

#     # Get the selected answer from variables
#     selected_answer = None
#     for i, var in enumerate(answer_vars):
#         if var.get() == "1":  # If checkbox is selected
#             selected_answer = answer_checkboxes[i].cget("text")
#             break

#     with open("viva_answers.txt", "a") as file:
#         file.write(f"Question: {question_list[question_index][0]}\n")
#         file.write(f"Your Answer: {selected_answer}\n")
#         if selected_answer == correct_answer:
#             log.insert(tk.END, "Correct!\n")
#             file.write("Result: Correct\n\n")
#         else:
#             log.insert(tk.END, f"Wrong. Correct Answer: {correct_answer}\n")
#             file.write(f"Correct Answer: {correct_answer}\n")
#             file.write("Result: Wrong\n\n")

#     # Reset all checkboxes to unselected
#     for var in answer_vars:
#         var.set("0")

#     question_index += 1
#     ask_question(answer_checkboxes)

# # Main Window
# main_window = tk.Tk()
# main_window.title("Voice Viva")

# # UI Elements
# tk.Label(main_window, text="Welcome to the Voice Viva!", font=("Arial", 16)).pack(pady=10)
# tk.Label(main_window, text="Choose a subject: Python, C, or DSA", font=("Arial", 12)).pack(pady=5)

# subject_entry = tk.Entry(main_window, font=("Arial", 12))
# subject_entry.pack(pady=5)

# start_button = tk.Button(main_window, text="Start Viva", command=start_voice_viva, font=("Arial", 12))
# start_button.pack(pady=20)

# main_window.mainloop()


# import pyttsx3
# import tkinter as tk
# from tkinter import scrolledtext, messagebox

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"Error in TTS: {e}")

# # Questions and answers
# questions = {
#     "python": {
#         "What is the keyword to define a function?": ["def", "func", "define", "lambda"],
#         "What is the output of print(2 + 2)?": ["4", "22", "8", "None"],
#         "What is the type of [1, 2, 3]?": ["list", "tuple", "set", "dictionary"],
#         "What is the keyword to define a class?": ["class", "def", "object", "init"],
#         "What method is used to add an item to a list?": ["append", "insert", "push", "add"]
#     },
#     "c": {
#         "What is the format specifier for an integer?": ["%d", "%f", "%c", "%s"],
#         "What is the keyword to include header files?": ["include", "import", "header", "load"],
#         "What is the result of 5 modulo 2?": ["1", "2", "0", "5"],
#         "What is the return type of the main function?": ["int", "void", "char", "float"],
#         "Which operator is used to access a pointer's value?": ["*", "&", "%", "@"]
#     },
#     "dsa": {
#         "What data structure uses FIFO?": ["Queue", "Stack", "Heap", "Tree"],
#         "What data structure uses LIFO?": ["Stack", "Queue", "Graph", "List"],
#         "What is the time complexity of binary search?": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
#         "What is a dynamic programming technique?": ["Memoization", "Sorting", "Searching", "Hashing"],
#         "What data structure is used for depth-first search?": ["Stack", "Queue", "Graph", "Array"]
#     }
# }

# def start_voice_viva():
#     global subject
#     subject = subject_entry.get().lower()
#     if subject in questions:
#         viva_window()
#     else:
#         messagebox.showerror("Invalid Subject", "Please choose Python, C, or DSA.")

# def viva_window():
#     global question_list, question_label, answer_vars, question_index, log, answer_checkboxes, next_button

#     question_list = list(questions[subject].items())
#     question_index = 0

#     # Create a new top-level window for the viva
#     viva = tk.Toplevel(main_window)
#     viva.title("Voice Viva")

#     question_label = tk.Label(viva, text="Question will appear here.", wraplength=400, font=("Arial", 14))
#     question_label.pack(pady=10)

#     answer_vars = [tk.StringVar(value="0") for _ in range(4)]  # Default unchecked state for checkboxes
#     answer_checkboxes = []

#     answer_frame = tk.Frame(viva)
#     answer_frame.pack(pady=10)

#     for i in range(4):
#         cb = tk.Checkbutton(answer_frame, text="", variable=answer_vars[i], font=("Arial", 12), anchor='w', onvalue="1", offvalue="0")
#         cb.pack(fill='x', padx=10, pady=2)
#         answer_checkboxes.append(cb)

#     next_button = tk.Button(
#         viva,
#         text="Next",
#         command=lambda: process_answer(answer_vars, viva),
#         font=("Arial", 12),
#     )
#     next_button.pack(pady=10)

#     log = scrolledtext.ScrolledText(viva, wrap=tk.WORD, font=("Arial", 10), width=50, height=10)
#     log.pack(pady=10)

#     ask_question(answer_checkboxes)

# def ask_question(answer_checkboxes):
#     global question_index
#     if question_index < len(question_list):
#         question, options = question_list[question_index]
#         speak(question)
#         question_label.config(text=question)

#         # Safely configure checkboxes based on options length
#         for i, cb in enumerate(answer_checkboxes):
#             if i < len(options):
#                 cb.config(text=options[i], state=tk.NORMAL)
#             else:
#                 cb.config(text="", state=tk.DISABLED)  # Disable extra checkboxes
#     else:
#         speak("The viva is over. Thank you!")
#         messagebox.showinfo("Viva Complete", "You have completed the viva!")
#         question_label.master.destroy()

# def process_answer(answer_vars, viva_window):
#     global question_index
#     if question_index >= len(question_list):
#         return

#     correct_answer = question_list[question_index][1][0]

#     # Get the selected answer from variables
#     selected_answer = None
#     for i, var in enumerate(answer_vars):
#         if var.get() == "1":  # If checkbox is selected
#             selected_answer = answer_checkboxes[i].cget("text")
#             break

#     with open("viva_answers.txt", "a") as file:
#         file.write(f"Question: {question_list[question_index][0]}\n")
#         file.write(f"Your Answer: {selected_answer}\n")
#         if selected_answer == correct_answer:
#             log.insert(tk.END, "Correct!\n")
#             file.write("Result: Correct\n\n")
#         else:
#             log.insert(tk.END, f"Wrong. Correct Answer: {correct_answer}\n")
#             file.write(f"Correct Answer: {correct_answer}\n")
#             file.write("Result: Wrong\n\n")

#     # Reset all checkboxes to unselected
#     for var in answer_vars:
#         var.set("0")

#     question_index += 1
#     ask_question(answer_checkboxes)

# # Main Window
# main_window = tk.Tk()
# main_window.title("Voice Viva")

# # UI Elements
# tk.Label(main_window, text="Welcome to the Voice Viva!", font=("Arial", 16)).pack(pady=10)
# tk.Label(main_window, text="Choose a subject: Python, C, or DSA", font=("Arial", 12)).pack(pady=5)

# subject_entry = tk.Entry(main_window, font=("Arial", 12))
# subject_entry.pack(pady=5)

# start_button = tk.Button(main_window, text="Start Viva", command=start_voice_viva, font=("Arial", 12))
# start_button.pack(pady=20)

# main_window.mainloop()

import pyttsx3
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in TTS: {e}")

# Questions and answers
questions = {
    "python": {
        "What is the keyword to define a function?": ["def", "func", "define", "lambda"],
        "What is the output of print(2 + 2)?": ["4", "22", "8", "None"],
        "What is the type of [1, 2, 3]?": ["list", "tuple", "set", "dictionary"],
        "What is the keyword to define a class?": ["class", "def", "object", "init"],
        "What method is used to add an item to a list?": ["append", "insert", "push", "add"]
    },
    "c": {
        "What is the format specifier for an integer?": ["%d", "%f", "%c", "%s"],
        "What is the keyword to include header files?": ["include", "import", "header", "load"],
        "What is the result of 5 modulo 2?": ["1", "2", "0", "5"],
        "What is the return type of the main function?": ["int", "void", "char", "float"],
        "Which operator is used to access a pointer's value?": ["*", "&", "%", "@"]
    },
    "dsa": {
        "What data structure uses FIFO?": ["Queue", "Stack", "Heap", "Tree"],
        "What data structure uses LIFO?": ["Stack", "Queue", "Graph", "List"],
        "What is the time complexity of binary search?": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
        "What is a dynamic programming technique?": ["Memoization", "Sorting", "Searching", "Hashing"],
        "What data structure is used for depth-first search?": ["Stack", "Queue", "Graph", "Array"]
    }
}

def start_voice_viva():
    global subject, question_list, question_index, answer_vars, answer_checkboxes, log

    subject = subject_entry.get().lower()
    if subject in questions:
        # Clear main_window and show viva screen
        for widget in main_window.winfo_children():
            widget.destroy()

        question_list = list(questions[subject].items())
        question_index = 0

        question_label = tk.Label(main_window, text="Question will appear here.", wraplength=400, font=("Arial", 14))
        question_label.pack(pady=10)

        answer_vars = [tk.StringVar(value="0") for _ in range(4)]  # Default unchecked state for checkboxes
        answer_checkboxes = []

        answer_frame = tk.Frame(main_window)
        answer_frame.pack(pady=10)

        for i in range(4):
            cb = tk.Checkbutton(answer_frame, text="", variable=answer_vars[i], font=("Arial", 12), anchor='w', onvalue="1", offvalue="0")
            cb.pack(fill='x', padx=10, pady=2)
            answer_checkboxes.append(cb)

        next_button = tk.Button(
            main_window,
            text="Next",
            command=lambda: process_answer(question_label),
            font=("Arial", 12),
        )
        next_button.pack(pady=10)

        log = scrolledtext.ScrolledText(main_window, wrap=tk.WORD, font=("Arial", 10), width=50, height=10)
        log.pack(pady=10)

        ask_question(question_label, answer_checkboxes)
    else:
        messagebox.showerror("Invalid Subject", "Please choose Python, C, or DSA.")

def ask_question(question_label, answer_checkboxes):
    global question_index
    if question_index < len(question_list):
        question, options = question_list[question_index]
        speak(question)
        question_label.config(text=question)

        for i, cb in enumerate(answer_checkboxes):
            if i < len(options):
                cb.config(text=options[i], state=tk.NORMAL)
            else:
                cb.config(text="", state=tk.DISABLED)
    else:
        speak("The viva is over. Thank you!")
        messagebox.showinfo("Viva Complete", "You have completed the viva!")
        restart_to_main()

def process_answer(question_label):
    global question_index
    if question_index >= len(question_list):
        return

    correct_answer = question_list[question_index][1][0]

    # Get the selected answer
    selected_answer = None
    for i, var in enumerate(answer_vars):
        if var.get() == "1":  # If checkbox is selected
            selected_answer = answer_checkboxes[i].cget("text")
            break

    with open("viva_answers.txt", "a") as file:
        file.write(f"Question: {question_list[question_index][0]}\n")
        file.write(f"Your Answer: {selected_answer}\n")
        if selected_answer == correct_answer:
            log.insert(tk.END, "Correct!\n")
            file.write("Result: Correct\n\n")
        else:
            log.insert(tk.END, f"Wrong. Correct Answer: {correct_answer}\n")
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write("Result: Wrong\n\n")

    # Reset all checkboxes to unselected
    for var in answer_vars:
        var.set("0")

    question_index += 1
    ask_question(question_label, answer_checkboxes)

def restart_to_main():
    # Clear main_window and go back to subject selection
    for widget in main_window.winfo_children():
        widget.destroy()

    tk.Label(main_window, text="Welcome to the Voice Viva!", font=("Arial", 16)).pack(pady=10)
    tk.Label(main_window, text="Choose a subject: Python, C, or DSA", font=("Arial", 12)).pack(pady=5)

    global subject_entry
    subject_entry = tk.Entry(main_window, font=("Arial", 12))
    subject_entry.pack(pady=5)

    start_button = tk.Button(main_window, text="Start Viva", command=start_voice_viva, font=("Arial", 12))
    start_button.pack(pady=20)

# Main Window
main_window = tk.Tk()
main_window.title("Voice Viva")

restart_to_main()
main_window.mainloop()
