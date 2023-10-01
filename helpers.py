from typing import Tuple, Any

from sqlalchemy.orm import sessionmaker
from data.models import *

import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='quanlykhohang',
    port=3306
)

cursor = mydb.cursor()


def check_login_info(username, pwd):
    # session.query(NhanVien).filter_by(ho_ten=username).first()
    query_str = f"SELECT * FROM NhanVien WHERE ho_ten = '{username}' AND ma_nhan_vien = '{pwd}'"
    cursor.execute(query_str)
    user = cursor.fetchone()
    if user:
        return user
    else:
        return False


def create_user(ma_nv, ho_ten, sdt, dia_chi, ngay_lam, vi_tri):
    insert_str = "INSERT INTO NhanVien (ma_nhan_vien, ho_ten, dien_thoai, dia_chi, ngay_vao_lam, chuc_vu) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_str, (ma_nv, ho_ten, sdt, dia_chi, ngay_lam, vi_tri))

    try:
        mydb.commit()
    except pymysql.err.OperationalError as e:
        # The commit operation failed, so rollback the transaction
        mydb.rollback()
        return False

    query_str = f"SELECT * FROM NhanVien WHERE ma_nhan_vien = '{ma_nv}'"
    cursor.execute(query_str)
    user = cursor.fetchone()
    return user


def read():
    sql = "SELECT* FROM SanPham"
    cursor.execute(sql)
    rows = cursor.fetchall()
    mydb.commit()
    mydb.close()
    return rows


def add_data_admin(ma_sp):
    sql = "SELECT * FROM SanPham WHERE ma_san_pham = '%s' "
    cursor.execute(sql, ma_sp)
    result = cursor.fetchall()
    return result


def create_product(ma_sp, ten_sp, dvt, nuoc_sx, hsd, gia):
    sql = "INSERT INTO SanPham (ma_san_pham, ten_san_pham, don_vi_tinh, nuoc_san_xuat, han_su_dung, gia) VALUES (?,?,?,?,?,?)"
    cursor.execute(sql, (ma_sp, ten_sp, dvt, nuoc_sx, hsd, gia))
    mydb.commit()


def get_product(ma_sp):
    sql = "SELECT*from SanPham where ma_san_pham = ?"
    cursor.execute(sql, ma_sp)
    result = cursor.fetchall()
    return result


def update_product(ten_sp, dvt, nuoc_sx, hsd, gia, ma_sp):
    sql = "UPDATE SanPham SET ten_san_pham =?,don_vi_tinh=?,nuoc_san_xuat=?,han_su_dung=?, gia=?  WHERE ma_san_pham =? "
    cursor.execute(sql, (ten_sp, dvt, nuoc_sx, hsd, gia, ma_sp))
    if mydb.commit():
        return True
    else:
        return False


def delete_product(ma_sp):
    sql = "DELETE FROM SanPham WHERE ma_san_pham = ? "
    cursor.execute(sql, ma_sp)
    mydb.commit()


def search_product_by_id(ma_sp):
    sql = "SELECT ma_san_pham,ten_san_pham,don_vi_tinh,nuoc_san_xuat,han_su_dung, gia FROM SANPHAM WHERE ma_san_pham LIKE ? "
    cursor.execute(sql, ma_sp)
    result = cursor.fetchall()
    return result


def search_product_by_name(ten_sp):
    sql = "SELECT ma_san_pham,ten_san_pham,don_vi_tinh,nuoc_san_xuat,han_su_dung, gia FROM SANPHAM WHERE ten_san_pham LIKE ? "
    cursor.execute(sql, ten_sp)
    result = cursor.fetchall()
    return result
