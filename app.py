import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from abc import ABC, abstractmethod
from helpers import *
from PIL import ImageTk, Image

from main import MainApplication

globrole = 1


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
        self.user_type_dropdown = tk.OptionMenu(self, self.user_role_var, *self.user_role_options)

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

        self.login_succeed = False

        self.mainloop()

    def on_login(self):
        ten_dang_nhap = self.username_entry.get()
        mat_khau = self.password_entry.get()
        chuc_vu = self.user_role_var.get()

        nguoi_dung = check_login_info(username=ten_dang_nhap, pwd=mat_khau)
        if nguoi_dung is not None:
            if nguoi_dung[5] == chuc_vu:
                messagebox.showinfo('OK', f'Đăng nhập {chuc_vu} thành công')
                self.destroy()
                admin_window = AdminWindow()
                admin_window.deiconify()
            else:
                messagebox.showinfo('Error', f'Chức vụ không đúng!')
        else:
            messagebox.showerror("Error", "Đăng nhập không thành công! Tên hoặc mật khẩu không đúng")

    def on_exit(self):
        self.destroy()
        

class RegisterWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.configure(background="#f6f9fd", borderwidth=0)
        self.geometry("700x500")
        self.resizable(True, True)
        self.title("Đăng Ký")

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

        self.mainloop()

    def on_register(self):
        ma_nv = self.ma_nv_entry.get()
        ho_ten = self.ten_nv_entry.get()
        sdt = self.sdt_entry.get()
        dia_chi = self.dia_chi_entry.get()
        ngay_lam = self.ngay_lam_entry.get()
        vi_tri = self.role_var.get()

        new_user = create_user(ma_nv, ho_ten, sdt, dia_chi, ngay_lam, vi_tri)
        if new_user is not None:
            messagebox.showinfo('Thành công', f'Mã nhân viên: {new_user[0]}'
                                                            f'Tên nhân viên: {new_user[1]}')
            self.destroy()
        else:
            messagebox.showerror('Tạo nhân viên không thành công!')

    def on_cancel(self):
        self.destroy()


# ADMIN WINDOW
class AdminWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(self, bg="#006400")
        self.frame.pack()
        self.Frame1 = tk.LabelFrame(self.frame, bg="white", height=180, width=700, borderwidth=2)
        self.Frame1.grid(row=0, column=0, sticky="w", padx=0, pady=0)
        self.photo = Image.open("data/hinhnen.jpg")
        self.photo.resize((700, 400))
        self.image = ImageTk.PhotoImage(self.photo)
        self.imageLable = tk.Label(self.Frame1, image=self.image, height=190, width=700)
        self.imageLable.pack()

        self.frame2 = tk.LabelFrame(self.frame, bg="white", text="Thông tin", borderwidth=5)
        self.frame2.grid(row=1, column=0, sticky="w", padx=10)

        self.mspLabel = tk.Label(self.frame2, text="MÃ SẢN PHẨM", font=("Time New Roman", 10), bg="white", anchor="w",
                              width=15)
        self.tenLabel = tk.Label(self.frame2, text="TÊN SẢN PHẨM", font=("Time New Roman", 10), bg="white", anchor="w",
                              width=15)
        self.giaLabel = tk.Label(self.frame2, text="GIÁ", anchor="w", font=("Time New Roman", 10), bg="white", width=15)
        self.nuocsxLabel = tk.Label(self.frame2, text="NƯỚC SẢN XUẤT", font=("Time New Roman", 10), bg="white", anchor="w",
                                 width=15)
        self.hsdLabel = tk.Label(self.frame2, text="HẠN SỬ DỤNG", font=("Time New Roman", 10), bg="white", anchor="w",
                              width=15)
        self.dvtLabel = tk.Label(self.frame2, text="ĐƠN VỊ TÍNH", font=("Time New Roman", 10), bg="white", anchor="w",
                              width=15)

        self.mspLabel.grid(row=0, column=0, padx=10)
        self.tenLabel.grid(row=1, column=0, padx=10)
        self.giaLabel.grid(row=2, column=0, padx=10)
        self.nuocsxLabel.grid(row=3, column=0, padx=10)
        self.hsdLabel.grid(row=4, column=0, padx=10)
        self.dvtLabel.grid(row=5, column=0, padx=10)

        self.mspEntry = tk.Entry(self.frame2, width=58)
        self.tenEntry = tk.Entry(self.frame2, width=58)
        self.giaEntry = tk.Entry(self.frame2, width=58)
        self.nuocsxEntry = tk.Entry(self.frame2, width=58)
        self.hsdEntry = tk.Entry(self.frame2, width=58)
        self.dvtEntry = tk.Entry(self.frame2, width=58)

        self.mspEntry.grid(row=0, column=2, padx=5, pady=5)
        self.tenEntry.grid(row=1, column=2, padx=5, pady=5)
        self.giaEntry.grid(row=2, column=2, padx=5, pady=5)
        self.nuocsxEntry.grid(row=3, column=2, padx=5, pady=5)
        self.hsdEntry.grid(row=4, column=2, padx=5, pady=5)
        self.dvtEntry.grid(row=5, column=2, padx=5, pady=5)

        self.frame3 = tk.LabelFrame(self.frame,bg="white", borderwidth=2)
        self.frame3.grid(row=1, column=0, sticky="w", padx=570, pady=10)

        self.addButton = tk.Button(self.frame3, text="Thêm",relief="ridge",activeforeground="black",width=6, borderwidth=3,font=("Time New Roman",10), bg="#a0522d", fg='white', command=self.add)
        self.updateButton = tk.Button(self.frame3, text="Sửa",relief="ridge",activeforeground="black", width=6, borderwidth=3, bg="#a0522d",font=("Time New Roman",10), fg='white', command=self.update)
        self.deleteButton = tk.Button(self.frame3, text="Xoá",relief="ridge",activeforeground="black", width=6, borderwidth=3,font=("Time New Roman",10), bg="#a0522d", fg='white', command=self.delete)
        self.findButton = tk.Button(self.frame3, text="Tìm kiếm",relief="ridge",activeforeground="black", width=6, borderwidth=3,font=("Time New Roman",10), bg="#a0522d", fg='white', command=self.find)
        self.veiwButton = tk.Button(self.frame3, text="Xem",relief="ridge",activeforeground="black", width=6, borderwidth=3,font=("Time New Roman",10), bg="#a0522d", fg='white', command=self.view)

        self.addButton.grid(row=0, column=1, padx=4, pady=4)
        self.veiwButton.grid(row=1, column=1, padx=4, pady=4)
        self.updateButton.grid(row=2, column=1, padx=4, pady=4)
        self.deleteButton.grid(row=3, column=1, padx=4, pady=4)
        self.findButton.grid(row=4, column=1, padx=4, pady=4)

        self.my_tree = ttk.Treeview(self.frame, columns=("MASP", "TENSP", "DVT", "NUOCSX", "HANSD", "GIA"),
                                    show='headings', height=12)
        self.my_tree.grid(row=2, column=0, sticky="w", padx=0, pady=0)

        self.my_tree.column("MASP", anchor='w', width=100)
        self.my_tree.column("TENSP", anchor='w', width=160)
        self.my_tree.column("DVT", anchor='w', width=110)
        self.my_tree.column("NUOCSX", anchor='w', width=110)
        self.my_tree.column("HANSD", anchor='w', width=110)
        self.my_tree.column("GIA", anchor='w', width=110)

        self.my_tree.heading("MASP", text="MÃ SẢN PHẨM", anchor='w')
        self.my_tree.heading("TENSP", text="TÊN SẢN PHẨM", anchor='w')
        self.my_tree.heading("DVT", text="ĐƠN VỊ TÍNH", anchor='w')
        self.my_tree.heading("NUOCSX", text="NƯỚC SẢN XUẤT", anchor='w')
        self.my_tree.heading("HANSD", text="HẠN SỬ DỤNG", anchor='w')
        self.my_tree.heading("GIA", text="GIÁ", anchor='w')

        self.mainloop()

        if globrole == 0:
            self.updateButton.destroy()
            self.deleteButton.destroy()
            self.addButton.destroy()
        else:
            pass


    def view(self):
        for data in self.my_tree.get_children():
            self.my_tree.delete(data)
        for row in read():
            row_to_list = [row[0], row[1], row[2], row[3], row[4], row[5]]
            self.my_tree.insert('', 'end', iid=row[0], values=row_to_list, tags="bg")
            self.my_tree.tag_configure("bg", background="#f0fff0")

    def add(self):
        maSP = str(self.mspEntry.get()).strip()
        tenSP = str(self.tenEntry.get()).strip()
        dvt = str(self.dvtEntry.get()).strip()
        gia = str(self.giaEntry.get()).strip()
        nuocSX = str(self.nuocsxEntry.get()).strip()
        hsd = str(self.hsdEntry.get()).strip()

        if not maSP or not tenSP or not dvt or not gia or not nuocSX or not hsd:
            messagebox.showwarning("Thông báo", "Điền đầy đủ thông tin")
            return
        try:
            result = add_data_admin(ma_sp=maSP)
            if result is not None:
                messagebox.showwarning("Thông báo", "Mã sản phẩm này đã tồn tại")
                return
            else:
                if create_product(maSP, tenSP, dvt, nuocSX, hsd, gia):
                    messagebox.showinfo("Thông báo", "Đã thêm dữ liệu")
                    for data in self.my_tree.get_children():
                        self.my_tree.delete(data)
                    for row in read():
                        row_to_list = [row[0], row[1], row[2], row[3], row[4], row[5]]
                        self.my_tree.insert('', 'end', iid=row[0], values=row_to_list, tags='bg')
                        self.my_tree.tag_configure("bg", background="#f0fff0")
        except InterruptedError:
            messagebox.showwarning("Thông báo", "Lỗi")
            return

    def update(self):
        maSP = str(self.mspEntry.get()).strip()
        tenSP = str(self.tenEntry.get()).strip()
        dvt = str(self.dvtEntry.get()).strip()
        gia = str(self.giaEntry.get()).strip()
        nuocSX = str(self.nuocsxEntry.get()).strip()
        hsd = str(self.hsdEntry.get()).strip()

        if not maSP or not tenSP or not dvt or not gia or not nuocSX or not hsd:
            messagebox.showwarning("Thông báo", "Điền đầy đủ thông tin!")
            return
        sp_hien_tai = get_product(maSP)
        if sp_hien_tai is not None:
            messagebox.showwarning("Thông báo", "Không tồn tại mã sản phẩm này")
            return
        else:
            try:
                if update_product(tenSP, dvt, nuocSX, hsd, gia, maSP):
                    messagebox.showinfo("Thông báo", "Cập nhật thành công")
                    for data in self.my_tree.get_children():
                        self.my_tree.delete(data)
                    for row in read():
                        row_to_list = [row[0], row[1], row[2], row[3], row[4], row[5]]
                        self.my_tree.insert('', 'end', iid=row[0], values=row_to_list, tags="bg")
                        self.my_tree.tag_configure("bg", background="#f0fff0")
                else:
                    messagebox.showwarning("Thông báo", "Cập nhật không thành công")
            except InterruptedError:
                messagebox.showwarning("Thông báo", "Lỗi")

    def delete(self):
        try:
            if (self.my_tree.selection()[0]):
                result = messagebox.askquestion("Xoá sản phẩm", "Bạn muốn xoá dữ liệu này?", icon='warning')
                if (result != 'yes'):
                    return
                else:
                    san_pham = self.my_tree.selection()[0]
                    maSP = str(self.my_tree.item(san_pham)['values'][0])
                    if delete_product(maSP):
                        messagebox.showinfo("Thông báo", "Dữ liệu đã xoá")
                        self.my_tree.delete(san_pham)
        except InterruptedError:
            messagebox.showinfo("Thông báo", "Chưa chọn dữ liệu")

    def find(self):
        maSP = str(self.mspEntry.get()).strip()
        tenSP = str(self.tenEntry.get()).strip()
        sp = tuple()

        if maSP:
            sp = search_product_by_id(maSP)

        elif tenSP:
            sp = search_product_by_name(tenSP)

        try:
            for data in self.my_tree.get_children():
                self.my_tree.delete(data)
            if not sp:
                messagebox.showwarning("Thông báo", "Không tìm được dữ liệu")
            else:
                for row in sp:
                    row_to_list = [row[0], row[1], row[2], row[3], row[4], row[5]]
                    self.my_tree.insert(parent='', index='end', iid=row, text="", values=row_to_list, tag="bg")
                    self.my_tree.tag_configure("bg", background="#f0fff0")
        except InterruptedError:
            messagebox.showinfo("Thông báo", "Điền vào mã sản phẩm hoặc tên sản phẩm")