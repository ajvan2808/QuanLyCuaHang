import csv
import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='quanlycuahang',
    port=3306
)

cursor = mydb.cursor()
# Nhap data tu customers.csv vao bang KhachHang
with open("customers.csv", mode='r') as custfile:
    reader = csv.reader(custfile)
    next(reader)  # skip header
    for row in reader:
        sql = "INSERT INTO KhachHang (ma_khach_hang, ten_khach_hang, dia_chi, dien_thoai, email) VALUES (%s, %s, %s, %s, %s)"
        val = (row[0], row[1], row[3], row[2], row[4])
        cursor.execute(sql, val)
        mydb.commit()

with open("orders.csv", mode='r') as odfile:
    reader = csv.reader(odfile)
    next(reader)  # skip header
    for row in reader:
        sql = "INSERT INTO DonHang (ma_don_hang, so_luong, tong_tien, ngay_dat_hang) VALUES (%s, %s, %s, %s)"
        val = (row[0], row[2], row[3], row[1])
        cursor.execute(sql, val)
        mydb.commit()

with open("order_details.csv", mode='r') as odtfile:
    reader = csv.reader(odtfile)
    next(reader)  # skip header
    for row in reader:
        sql = "INSERT INTO ChiTietDonHang (ma_thong_tin_dh, don_vi, gia) VALUES (%s, %s, %s)"
        val = (row[0], row[3], row[4])
        cursor.execute(sql, val)
        mydb.commit()

with open("products.csv", mode='r') as prodfile:
    reader = csv.reader(prodfile)
    next(reader)  # skip header
    for row in reader:
        sql = "INSERT INTO SanPham (ma_san_pham, ten_san_pham, phan_loai, gia, mo_ta, ngay_nhap_hang, ngay_xuat_hang) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (row[0], row[1], row[2], row[3], row[6], row[4], row[5])
        cursor.execute(sql, val)
        mydb.commit()


# for _ in range(2500):
#     with open("orders.csv", mode='r') as odtfile:
#         reader = csv.reader(odtfile)
#         next(reader)  # skip header
#         for row in reader:
#             sql = "SET FOREIGN_KEY_CHECKS=0; INSERT INTO ChiTietDonHang (ma_dh) VALUES ('', SELECT)"
#             val = (row[0])
#             cursor.execute(sql, val)
#             mydb.commit()
