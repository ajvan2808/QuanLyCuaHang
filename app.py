import sys
import tkinter as tk
from tkinter import messagebox, Toplevel
# from sqlalchemy.orm import sessionmaker
# from data.models import *
from abc import ABC, abstractmethod
from main import MainApplication as root
from helpers import *

# Session = sessionmaker(bind=engine)
# session = Session()


# class CongCuQuanLy(ABC):
#     @abstractmethod
#     def __init__(self):
#         self.nhan_vien = NhanVien()
#         self.san_pham = SanPham()
#         self.khach_hang = KhachHang()
#         self.don_hang = DonHang()
#         self.ctdh = ChiTietDonHang()


class PhanMemQuanLy(ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        # self.data_nhan_vien = session.query(NhanVien).all()
        # self.data_khach_hang = session.query(KhachHang).all()
        # self.data_san_pham = session.query(SanPham).all()
        # self.data_don_hang = session.query(DonHang).all()
        # self.data_ctdh = session.query(ChiTietDonHang).all()


class DangNhapWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # GUI
        self.configure(background="#f6f9fd", borderwidth=0)
        self.geometry("700x400")
        self.resizable(True, True)
        self.title("Đăng nhập ")

        self.username_label = tk.Label(self)
        self.username_label.configure(
            text='Tên đăng nhập',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 18 {bold}",
            foreground="#04b4c3",
            justify="left")

        self.username_entry = tk.Entry(self)
        self.username_entry.configure(
            background="#efffff",
            borderwidth=0,
            font="{San Francisco} 14 {}",
            foreground="#445653",
            justify="center",
            selectbackground="#f6f9fd",
            selectborderwidth=0.2,
            width=30)

        self.password_label = tk.Label(self)
        self.password_label.configure(
            text='Mật khẩu',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 18 {bold}",
            foreground="#04b4c3",
            justify="left")
        self.password_entry = tk.Entry(self)
        self.password_entry.configure(
            background="#efffff",
            borderwidth=0,
            font="{San Francisco} 14 {}",
            foreground="#445653",
            justify="center",
            selectbackground="#f6f9fd",
            selectborderwidth=0.2,
            width=30)

        self.user_role_label = tk.Label(self)
        self.user_role_label.configure(
            text='Chức vụ',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 18 {bold}",
            foreground="#04b4c3",
            justify="left")

        self.user_role_var = tk.StringVar(value="Nhân viên")
        self.user_role_options = ["Quản lý", "Nhân viên"]
        self.user_type_dropdown = tk.OptionMenu(self, self.user_role_var, *self.user_role_options, command=None)

        self.login_button = tk.Button(self)
        self.login_button.configure(
            text='Đăng nhập',
            command=self.on_login,
            background="#5ce1e6",
            borderwidth=0,
            font="{San Francisco} 16 {}",
            justify="center")

        self.exit_button = tk.Button(self)
        self.exit_button.configure(
            text='Thoát',
            command=self.on_exit,
            background="#5ce1e6",
            borderwidth=0,
            font="{San Francisco} 16 {}",
            justify="center")

        # Grid the widgets
        self.username_label.place(anchor="nw", relx=0.1, rely=0.16, x=0, y=0)
        self.username_entry.place(anchor="nw", height=26, relx=0.36, rely=0.16, x=0, y=0)
        self.password_label.place(anchor="nw", relx=0.12, rely=0.30, x=0, y=0)
        self.password_entry.place(anchor="nw", height=26, relx=0.36, rely=0.29, x=0, y=0)
        self.user_role_label.place(anchor="nw", relx=0.12, rely=0.43, x=0, y=0)
        self.user_type_dropdown.place(anchor="nw",height=26,relx=0.36,rely=0.42,width=150,x=0,y=0)
        self.login_button.place(anchor="nw", height=30, relx=0.54, rely=0.7, width=100, x=0, y=0)
        self.exit_button.place(anchor="nw", height=30, relx=0.26, rely=0.7, width=100, x=0, y=0)

        self.mainloop()

    def on_login(self):
        ten_dang_nhap = self.username_entry.get()
        mat_khau = self.password_entry.get()
        chuc_vu = self.user_role_var.get()

        nguoi_dung = check_login_info(username=ten_dang_nhap, pwd=mat_khau)
        if nguoi_dung is not None:
            if nguoi_dung.chuc_vu == chuc_vu:
                messagebox.showinfo('OK', f'Đăng nhập {chuc_vu} thành công')
                self.destroy()
            else:
                messagebox.showinfo('Error', f'Chức vụ không đúng!')
        else:
            messagebox.showerror("Error", "Đăng nhập không thành công! Tên hoặc mật khẩu không đúng")

    def on_exit(self):
        self.destroy()


class LogOutWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text="Bạn muốn đăng xuất?")
        self.yes_button = tk.Button(self, text="Đồng ý", command=self.on_yes)
        self.no_button = tk.Button(self, text="Không", command=self.on_no)

        # Pack the widgets
        self.label.pack()
        self.yes_button.pack()
        self.no_button.pack()

    def on_yes(self):
        self.destroy()
        DangNhapWindow()

    def on_no(self):
        self.destroy()
        

class RegisterWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Đăng Ký")
        self.configure(
            background="#f6f9fd",
            borderwidth=0,)
        self.geometry("700x500")
        self.resizable(True, True)

        self.ma_nv_label = tk.Label(self)
        self.ma_nv_label.configure(
            text='Mã nhân viên',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 16 {bold}",
            foreground="#04b4c3",
            justify="left")

        self.ten_nv_label = tk.Label(self)
        self.ten_nv_label.configure(
            text='Họ tên nhân viên',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 16 {bold}",
            foreground="#04b4c3",
            justify="left")

        self.sdt_label = tk.Label(self)
        self.sdt_label.configure(
            text='Điện thoại',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 16 {bold}",
            foreground="#04b4c3",
            justify="left")

        self.dia_chi_label = tk.Label(self)
        self.dia_chi_label.configure(
            text='Địa chỉ',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 16 {bold}",
            foreground="#04b4c3",
            justify="left")

        self.ngay_lam_label = tk.Label(self)
        self.ngay_lam_label.configure(
            text='Ngày vào làm',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 16 {bold}",
            foreground="#04b4c3",
            justify="left")

        self.role_label = tk.Label(self)
        self.role_label.configure(
            text='Vị trí',
            background="#f6f9fd",
            borderwidth=0,
            font="{San Francisco} 18 {bold}",
            foreground="#04b4c3",
            justify="left")

        self.ma_nv_entry = tk.Entry(self)
        self.ma_nv_entry.configure(
            background="#efffff",
            borderwidth=0.5,
            font="{San Francisco} 16 {}",
            foreground="#445653",
            highlightthickness=0.5,
            justify="center",
            width=30)
        self.ten_nv_entry = tk.Entry(self)
        self.ten_nv_entry.configure(
            background="#efffff",
            borderwidth=0.5,
            font="{San Francisco} 16 {}",
            foreground="#445653",
            highlightthickness=0.5,
            justify="center",
            width=30)
        self.sdt_entry = tk.Entry(self)
        self.sdt_entry.configure(
            background="#efffff",
            borderwidth=0.5,
            font="{San Francisco} 16 {}",
            foreground="#445653",
            highlightthickness=0.5,
            justify="center",
            width=30)
        self.dia_chi_entry = tk.Entry(self)
        self.dia_chi_entry.configure(
            background="#efffff",
            borderwidth=0.5,
            font="{San Francisco} 16 {}",
            foreground="#445653",
            highlightthickness=0.5,
            justify="center",
            width=30)
        self.ngay_lam_entry = tk.Entry(self)
        self.ngay_lam_entry.configure(
            background="#efffff",
            borderwidth=0.5,
            font="{San Francisco} 16 {}",
            foreground="#445653",
            highlightthickness=0.5,
            justify="center",
            width=30)

        self.role_var = tk.StringVar(value="Nhân viên")
        self.role_options = ["Quản lý", "Nhân viên"]
        self.role_dropdown = tk.OptionMenu(self, self.role_var, *self.role_options, command=None)
        self.register_button = tk.Button(self)
        self.register_button.configure(
            text='Tạo tài khoản',
            command=self.on_register,
            background="#5ce1e6",
            borderwidth=0,
            font="{San Francisco} 16 {}",
            justify="center")
        self.cancel_button = tk.Button(self)
        self.cancel_button.configure(
            text='Hủy',
            command=self.on_cancel,
            background="#5ce1e6",
            borderwidth=0,
            font="{San Francisco} 16 {}",
            justify="center")

        # Place the widgets
        self.ma_nv_label.place(anchor="nw", relx=0.10, rely=0.16, x=0, y=0)
        self.ma_nv_entry.place(anchor="nw", height=25, relx=0.38, rely=0.15, x=0, y=0)
        self.ten_nv_label.place(anchor="nw", relx=0.10, rely=0.23, x=0, y=0)
        self.ten_nv_entry.place(anchor="nw", height=25, relx=0.38, rely=0.22, x=0, y=0)
        self.sdt_label.place(anchor="nw", relx=0.10, rely=0.30, x=0, y=0)
        self.sdt_entry.place(anchor="nw", height=25, relx=0.38, rely=0.29, x=0, y=0)
        self.dia_chi_label.place(anchor="nw", relx=0.10, rely=0.37, x=0, y=0)
        self.dia_chi_entry.place(anchor="nw", height=25, relx=0.38, rely=0.36, x=0, y=0)
        self.ngay_lam_label.place(anchor="nw", relx=0.10, rely=0.44, x=0, y=0)
        self.ngay_lam_entry.place(anchor="nw", height=25, relx=0.38, rely=0.43, x=0, y=0)
        self.role_label.place(anchor="nw", relx=0.10, rely=0.51, x=0, y=0)
        self.role_dropdown.place(anchor="nw", bordermode="ignore", height=26, relx=0.38, rely=0.50, width=150, x=0, y=0)
        self.register_button.place(anchor="nw", height=30, relx=0.45, rely=0.70, width=110, x=0, y=0)
        self.cancel_button.place(anchor="nw", height=30, relx=0.23, rely=0.70, width=100, x=0, y=0)

    def on_register(self):
        ma_nv = self.ma_nv_entry.get()
        ho_ten = self.ten_nv_entry.get()
        sdt = self.sdt_entry.get()
        dia_chi = self.dia_chi_entry.get()
        ngay_lam = self.ngay_lam_entry.get()
        vi_tri = self.role_var.get()

        new_user = create_user(ma_nv, ho_ten, sdt, dia_chi, ngay_lam, vi_tri)
        if new_user is not None:
            messagebox.showinfo('Thành công', f'{new_user.__str__()}')
            self.destroy()
        else:
            messagebox.showerror('Tạo nhân viên không thành công!')

    def on_cancel(self):
        self.destroy()
