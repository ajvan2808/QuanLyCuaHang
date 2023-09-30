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
