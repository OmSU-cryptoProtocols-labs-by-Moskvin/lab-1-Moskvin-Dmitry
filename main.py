import tkinter as tk
from tkinter import scrolledtext

class ChatApp:
    def __init__(self, root, name):
        self.root = root
        self.name = name
        self.root.title("Chat App - " + self.name)

        # Text widgets for displaying chat history and entering messages
        self.chat_history = scrolledtext.ScrolledText(self.root, height=20, width=50)
        self.entry_field = tk.Entry(self.root, width=50)

        # Button for sending messages
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)

        # Grid layout setup
        self.chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        self.entry_field.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        self.send_button.grid(row=1, column=2, padx=10, pady=10)

    def send_message(self):
        message = self.entry_field.get()
        # Display the message in chat history
        self.chat_history.insert(tk.END, self.name + ": " + message + "\n")
        # Clear the entry field
        self.entry_field.delete(0, tk.END)
        # Send the message to the other user
        if self.other_user:
            self.other_user.chat_history.insert(tk.END, self.name + ": " + message + "\n")

    def set_other_user(self, other_user):
        self.other_user = other_user

if __name__ == "__main__":
    root1 = tk.Tk()
    root2 = tk.Tk()

    app1 = ChatApp(root1, "User 1")
    app2 = ChatApp(root2, "User 2")

    app1.set_other_user(app2)
    app2.set_other_user(app1)

    root1.mainloop()
    root2.mainloop()
