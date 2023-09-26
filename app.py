import tkinter as tk
from tkinter import messagebox, Toplevel
from sqlalchemy.orm import sessionmaker
from data.models import *
from abc import ABC, abstractmethod

Session = sessionmaker(bind=engine)
session = Session()


class CongCuQuanLy(ABC):
    @abstractmethod
    def __init__(self):
        self.nhan_vien = NhanVien()
        self.san_pham = SanPham()
        self.khach_hang = KhachHang()
        self.don_hang = DonHang()
        self.ctdh = ChiTietDonHang()


class PhanMemQuanLy(CongCuQuanLy):
    def __init__(self):
        super().__init__()
        # self.data_nhan_vien = session.query(NhanVien).all()
        # self.data_khach_hang = session.query(KhachHang).all()
        # self.data_san_pham = session.query(SanPham).all()
        # self.data_don_hang = session.query(DonHang).all()
        # self.data_ctdh = session.query(ChiTietDonHang).all()


class DangNhapWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.Users = NhanVien()
        self.geometry("500x500")
        self.title("Đăng nhập")
        self.resizable(False, False)

        self.username_label = tk.Label(self, text="Tên đăng nhập")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Mật khẩu")
        self.password_entry = tk.Entry(self, show="*")

        self.user_role_label = tk.Label(self, text="Chức vụ")
        self.user_role_var = tk.StringVar(self)
        self.user_role_var.set("Nhân viên")  # Default value
        self.user_role_options = ["Nhân viên", "Quản lý"]
        self.user_type_dropdown = tk.OptionMenu(self, self.user_role_var, *self.user_role_options)
        self.login_button = tk.Button(self, text="Login", command=self.on_login)

        # Grid the widgets
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        self.password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        self.user_role_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
        self.user_type_dropdown.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        self.login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.mainloop()

    def on_login(self):
        ten_dang_nhap = self.username_entry.get()
        mat_khau = self.password_entry.get()
        nv_quan_ly = 1 if self.user_role_var.get() == "Quản lý" else 0
        nguoi_dung = session.query(NhanVien).filter_by(ma_nhan_vien=mat_khau, ho_ten=ten_dang_nhap, quan_ly=nv_quan_ly).first()

        if nguoi_dung is not None:
            if nv_quan_ly:
                pass
                # goi class tk cho trang cua quan ly
                # self.trang_quan_ly()
            elif not nv_quan_ly:
                pass
                # self.trang_chu()
        else:
            messagebox.showerror("Đăng nhập không thành công! Tên hoặc mật khẩu không đúng")
            self.on_register()

    @staticmethod
    def on_register():
        dang_ky_window = RegisterWindow()
        dang_ky_window.mainloop()


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
        

class RegisterWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(text="Tạo Tài Khoản Nhân Viên")

        self.ma_nv_label = tk.Label(self, text="Mã nhân viên")
        self.ma_nv_entry = tk.Entry(self)
        self.ten_nv_label = tk.Label(self, text="Họ tên nhân viên")
        self.ten_nv_entry = tk.Entry(self)
        self.sdt_label = tk.Label(self, text="Điện thoại")
        self.sdt_entry = tk.Entry(self)
        self.dia_chi_label = tk.Label(self, text="Địa chỉ")
        self.dia_chi_entry = tk.Entry(self)
        self.ngay_lam_label = tk.Label(self, text="Ngày bắt đầu")
        self.ngay_lam_entry = tk.Entry(self)

        self.role_label = tk.Label(self, text="Vị trí")
        self.role_var = tk.StringVar(self)
        self.role_var.set("Nhân viên")  # Default value
        self.role_options = ["Nhân viên", "Quản lý"]
        self.role_dropdown = tk.OptionMenu(self, self.role_var, *self.role_options)
        self.register_button = tk.Button(self, text="Register", command=self.tao_tai_khoan)

        # Grid the widgets
        self.ma_nv_label.grid(row=0, column=0)
        self.ma_nv_entry.grid(row=0, column=1)
        self.ten_nv_label.grid(row=1, column=0)
        self.ten_nv_entry.grid(row=1, column=1)
        self.sdt_label.grid(row=2, column=0)
        self.sdt_entry.grid(row=2, column=1)
        self.dia_chi_label.grid(row=3, column=0)
        self.dia_chi_entry.grid(row=3, column=1)
        self.ngay_lam_label.grid(row=4, column=0)
        self.ngay_lam_entry.grid(row=4, column=1)
        self.register_button.grid(row=5, column=1)

    def tao_tai_khoan(self):
        nhan_vien_moi = NhanVien()
        nhan_vien_moi.ma_nhan_vien = self.ma_nv_entry
        nhan_vien_moi.ho_ten = self.ten_nv_entry
        nhan_vien_moi.dien_thoai = self.sdt_entry
        nhan_vien_moi.dia_chi = self.dia_chi_entry
        nhan_vien_moi.ngay_vao_lam = self.ngay_lam_entry
        nhan_vien_moi.quan_ly = 1 if self.role_var == "Quản lý" else 0

        session.add(nhan_vien_moi)
        session.commit()

    # def xuat_tat_ca_san_pham(self):
    #     return session.query(SanPham).all()
    #
    # def tim_san_pham(self, id_san_pham: str):
    #     return session.query(SanPham).get(id_san_pham)
    #
    # def them_san_pham(self, san_pham_moi):
    #     if self.nguoi_dung_hien_tai and self.nguoi_dung_hien_tai.quan_ly == 1:
    #         session.add(san_pham_moi)
    #         session.commit()
    #     else:
    #         raise Exception('Không thể thực hiện! Vui lòng liên hệ Quản lý')
    #
    # def cap_nhat_san_pham(self, san_pham_can_cap_nhat):
    #     if self.nguoi_dung_hien_tai and self.nguoi_dung_hien_tai.quan_ly == 1:
    #         sp = session.query(SanPham).get(san_pham_can_cap_nhat.ma_san_pham)
    #         if sp:
    #             session.merge(san_pham_can_cap_nhat)
    #             session.commit()
    #         else:
    #             raise Exception('Sản phẩm không tồn tại!')
    #     else:
    #         raise Exception('Không thể thực hiện! Vui lòng liên hệ Quản lý')
    #
    # def xoa_san_pham(self, san_pham_moi):
    #     if self.nguoi_dung_hien_tai and self.nguoi_dung_hien_tai.quan_ly == 1:
    #         session.delete(san_pham_moi)
    #         session.commit()
    #     else:
    #         raise Exception('Không thể thực hiện! Vui lòng liên hệ Quản lý')
