import app
import tkinter as tk


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Quản Lý Kho Hàng')
        self.geometry('2560x1600')

        # Create the frames
        # self.login_frame = tk.Frame(self)
        # self.register_frame = tk.Frame(self)
        # self.logout_frame = tk.Frame(self)

        # Create the buttons
        self.login_button = tk.Button(self, text="Đăng nhập", command=self.open_login_window)
        self.register_button = tk.Button(self, text="Đăng ký", command=self.open_register_window)
        self.logout_button = tk.Button(self, text="Đăng xuất", command=self.open_logout_window)

        # Connect the buttons to functions
        self.login_button.grid(row=1, column=1)
        self.register_button.grid(row=1, column=2)
        self.logout_button.grid(row=1, column=3)

        # Place the frames in the main window
        # self.login_frame.grid(row=0, column=0)
        # self.register_frame.grid(row=1, column=0)
        # self.logout_frame.grid(row=2, column=0)

    @staticmethod
    def open_login_window():
        app.DangNhapWindow()
        # login_window.mainloop()

    @staticmethod
    def open_register_window():
        # Create a new register window
        register_window = app.RegisterWindow()
        # Start the mainloop for the register window
        register_window.mainloop()

    @staticmethod
    def open_logout_window():
        # Create a new logout window
        logout_window = app.LogOutWindow()
        # Start the mainloop for the logout window
        logout_window.mainloop()


if __name__ == "__main__":
    main_application = MainApplication()
    main_application.mainloop()
