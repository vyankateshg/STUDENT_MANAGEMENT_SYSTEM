# import tkinter as tk
# from tkinter import Scrollbar, Text

# class ChatBotApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chatbot")

#         # Create chat window
#         self.chat_area = Text(root, wrap=tk.WORD, width=60, height=20, bg="#f0f0f0", padx=10, pady=10)
#         self.chat_area.configure(state=tk.DISABLED)
#         self.chat_area.grid(row=0, column=0, columnspan=2)

#         # Scrollbar for chat area
#         scrollbar = Scrollbar(root, command=self.chat_area.yview)
#         self.chat_area['yscrollcommand'] = scrollbar.set
#         scrollbar.grid(row=0, column=2, sticky='ns')

#         # Message entry box
#         self.entry_box = tk.Entry(root, width=45)
#         self.entry_box.grid(row=1, column=0, padx=10, pady=5)

#         # Send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_message)
#         self.send_button.grid(row=1, column=1, padx=5, pady=5)

#     def send_message(self):
#         user_message = self.entry_box.get().strip()
#         if user_message:
#             self.display_message(user_message, "user")
#             response = self.get_bot_response(user_message)
#             self.display_message(response, "bot")
#         self.entry_box.delete(0, tk.END)

#     def display_message(self, message, sender):
#         self.chat_area.configure(state=tk.NORMAL)
#         if sender == "user":
#             self.chat_area.insert(tk.END, f"\n{' ' * 50}{message}\n")
#         else:
#             self.chat_area.insert(tk.END, f"Bot: {message}\n")
#         self.chat_area.configure(state=tk.DISABLED)
#         self.chat_area.see(tk.END)

#     def get_bot_response(self, user_message):
#         # Simple responses for demo
#         responses = {
#             "hello": "Hi there! How can I help you?",
#             "how are you": "I'm just a bot, but I'm doing well!",
#             "bye": "Goodbye! Have a great day!",
#         }
#         return responses.get(user_message.lower(), "I'm not sure how to respond to that.")


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ChatBotApp(root)
#     root.mainloop()

import tkinter as tk
from tkinter import Scrollbar, Text, Canvas

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")

        # Create chat window
        self.chat_area = Text(root, wrap=tk.WORD, width=60, height=20, bg="#f0f0f0", padx=10, pady=10, borderwidth=0, highlightthickness=0)
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.grid(row=0, column=0, columnspan=2)

        # Scrollbar for chat area
        scrollbar = Scrollbar(root, command=self.chat_area.yview)
        self.chat_area['yscrollcommand'] = scrollbar.set
        scrollbar.grid(row=0, column=2, sticky='ns')

        # Message entry box
        self.entry_box = tk.Entry(root, width=45)
        self.entry_box.grid(row=1, column=0, padx=10, pady=5)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=5, pady=5)

    def send_message(self):
        user_message = self.entry_box.get().strip()
        if user_message:
            self.display_message(user_message, "user")
            response = self.get_bot_response(user_message)
            self.display_message(response, "bot")
        self.entry_box.delete(0, tk.END)

    def display_message(self, message, sender):
        self.chat_area.configure(state=tk.NORMAL)

        if sender == "user":
            message_box = f"\n{' ' * 30}┌{'─' * (len(message) + 2)}┐\n{' ' * 30}| {message} |\n{' ' * 30}└{'─' * (len(message) + 2)}┘\n"
            self.chat_area.insert(tk.END, message_box, "right")
        else:
            message_box = f"┌{'─' * (len(message) + 2)}┐\n| {message} |\n└{'─' * (len(message) + 2)}┘\n"
            self.chat_area.insert(tk.END, message_box, "left")

        self.chat_area.tag_config("right", justify="right")
        self.chat_area.tag_config("left", justify="left")
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def get_bot_response(self, user_message):
        # Simple responses for demo
        responses = {
            "hello": "Hi there! How can I help you?",
            "how are you": "I'm just a bot, but I'm doing well!",
            "bye": "Goodbye! Have a great day!",
        }
        return responses.get(user_message.lower(), "I'm not sure how to respond to that.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()