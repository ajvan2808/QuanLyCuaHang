# import csv
# import uuid
import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='quanlykhohang',
    port=3306
)

cursor = mydb.cursor()
#
# '''
# Lưu ý:
# - Thứ tự tạo bảng và thêm data vào bảng do có ràng buộc foreign keys
# '''
#
# with open("KhachHang.csv", mode='r') as file1:
#     reader = csv.reader(file1)
#     next(reader)  # skip header
#     for row in reader:
#         sql = ("INSERT INTO KhachHang (ma_khach_hang, ten_khach_hang, dien_thoai, dia_chi, ngay_sinh, doanh_thu) "
#                "VALUES (%s, %s, %s, %s, %s, %s)")
#         val = (row[0], row[1], row[2], row[3], row[4], row[5])
#         cursor.execute(sql, val)
#         mydb.commit()
#
# with open("NhanVien.csv", mode='r') as file1:
#     reader = csv.reader(file1)
#     next(reader)  # skip header
#     for row in reader:
#         sql = ("INSERT INTO NhanVien (ma_nhan_vien, ho_ten, dien_thoai, dia_chi, ngay_vao_lam)"
#                "VALUES (%s, %s, %s, %s, %s)")
#         val = (row[0], row[1], row[2], row[3], row[4])
#         cursor.execute(sql, val)
#         mydb.commit()
#
# with open("DonHang.csv", mode='r') as dhfile:
#     reader = csv.reader(dhfile)
#     next(reader)  # skip header
#     for row in reader:
#         sql = "INSERT INTO DonHang (ma_don_hang, ngay_tao_dh, tong_so_luong, tong_tien, ma_kh, ma_nv) VALUES (%s, %s, %s, %s, %s, %s)"
#         val = (row[0], row[1], row[5], row[4], row[2], row[3])
#         cursor.execute(sql, val)
#         mydb.commit()
#
# with open("SanPham.csv", mode='r') as spfile:
#     reader = csv.reader(spfile)
#     next(reader)  # skip header
#     for row in reader:
#         sql = "INSERT INTO SanPham (ma_san_pham, ten_san_pham, don_vi_tinh, nuoc_san_xuat, han_su_dung, gia) VALUES (%s, %s, %s, %s, %s, %s)"
#         val = (row[0], row[1], row[2], row[3], row[4], row[5])
#         cursor.execute(sql, val)
#         mydb.commit()
#
#
# with open("ChiTietDonHang.csv", mode='r') as ctdhfile:
#     reader = csv.reader(ctdhfile)
#     next(reader)  # skip header
#     for row in reader:
#         sql = "INSERT INTO ChiTietDonHang (ma_chi_tiet_dh, so_luong, ma_dh, ma_sp) VALUES (%s,%s, %s, %s)"
#         val = (str(str(uuid.uuid4())[:8]), row[2], row[0], row[1])
#         cursor.execute(sql, val)
#         mydb.commit()
#
# with open("KhoHang.csv", mode='r') as khfile:
#     reader = csv.reader(khfile)
#     next(reader)  # skip header
#     for row in reader:
#         sql = "INSERT INTO KhoHang (ten_san_pham, don_vi_tinh, nuoc_san_xuat, han_su_dung, gia, so_luong, trang_thai, ma_sp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#         val = (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])
#         cursor.execute(sql, val)
#         mydb.commit()

sql = "ALTER TABLE NhanVien ADD COLUMN quan_ly BOOLEAN;"

