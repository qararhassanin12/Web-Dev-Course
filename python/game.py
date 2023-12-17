import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")

        # Initialize variables
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Create labels and entry widgets
        tk.Label(root, text="Username:").pack(pady=5)
        tk.Entry(root, textvariable=self.username_var).pack(pady=5)

        tk.Label(root, text="Password:").pack(pady=5)
        tk.Entry(root, textvariable=self.password_var, show='*').pack(pady=5)

        # Create login button
        tk.Button(root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        # Check if username and password are valid (for demonstration purposes)
        if username == "user" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    login_form = LoginForm(root)
    root.mainloop()
