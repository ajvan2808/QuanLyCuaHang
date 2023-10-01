import sys
from tkinter import ttk
import app
import tkinter as tk
import tkinter.font as tkFont


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Quản Lý Kho Hàng')
        self.geometry('2560x1600')
        self.config(background="#5ce1e6", width=200)
        self.resizable(True, True)

        self.heading = tk.Label(self)
        self.img_logo = tk.PhotoImage(
            file="data/logo.png")
        self.heading.config(
            anchor="nw",
            background="#5ce1e6",
            font="{San Francisco} 25 {}",
            image=self.img_logo,
            justify="center",
            relief="flat",
            text='pic')
        self.heading.place(anchor="nw", height=438, width=478, x=480, y=160, relx=0.0, rely=0.0)

        # Create the buttons
        self.login_button = tk.Button(self, text="Đăng nhập", command=self.open_login_window,
                                      activebackground="#34a3b0", activeforeground="#ffffff",
                                      borderwidth=0, cursor="pointinghand", font="{San Francisco} 15 {}", relief="flat")
        self.register_button = tk.Button(self, text="Đăng ký", command=self.open_register_window,
                                         activebackground="#34a3b0", activeforeground="#ffffff", borderwidth=0,
                                         cursor="pointinghand", font="{San Francisco} 15 {}",)
        self.exit_button = tk.Button(self, text="Thoát", command=self.exit_window,
                                       activebackground="#34a3b0", activeforeground="#ffffff",
                                       borderwidth=0, cursor="pointinghand", font="{San Francisco} 15 {}", relief="flat",)

        # # Align button
        self.login_button.place(anchor="nw", height=40, width=150, x=430, y=450)
        self.register_button.place(anchor="nw", height=40, relx=0.14, width=150, x=430, y=450)
        self.exit_button.place(anchor="nw", height=40, relx=0.27, width=150, x=450, y=450)

        # Create sub frames
        # self.register_frame = tk.Frame(self)
        # self.logout_frame = tk.Frame(self)

        # Place the frames in the main window
        # self.login_frame.grid(row=0, column=0)
        # self.register_frame.grid(row=1, column=0)
        # self.logout_frame.grid(row=2, column=0)

    def open_login_window(self):
        if app.DangNhapWindow():
            self.destroy()

    def open_register_window(self):
        # Create a new register window
        if app.RegisterWindow():
            self.deiconify()

    def exit_window(self):
        self.destroy()
        sys.exit()


if __name__ == "__main__":
    main_application = MainApplication()
    main_application.mainloop()
