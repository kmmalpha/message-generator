import tkinter as tk

class RomanticMessageGUI(tk.Frame):
    def _init_(self, master):
        super()._init_(master)
        self.master = master
        self.message_entry = tk.Entry(self)
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.message_entry.pack()
        self.send_button.pack()

    def send_message(self):
        message = self.message_entry.get()
        # Send the message to your loved one here
        # For example, you could send the message using SMS or WhatsApp

if __name__ == "__main__":
    root = tk.Tk()
    gui = RomanticMessageGUI(root)
    gui.pack()
    root.mainloop()