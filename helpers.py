from sqlalchemy.orm import sessionmaker
from data.models import *

Session = sessionmaker(bind=engine)
session = Session()


def check_login_info(username, pwd):
    user = session.query(NhanVien).filter_by(ho_ten=username).first()
    if user is not None and user.ma_nhan_vien == pwd:
        return user
    else:
        return False


def create_user(ma_nv, ho_ten, sdt, dia_chi, ngay_lam, vi_tri):
    new_user = NhanVien(ma_nhan_vien=ma_nv, ho_ten=ho_ten, dien_thoai=sdt, dia_chi=dia_chi, ngay_vao_lam=ngay_lam, chuc_vu=vi_tri)
    session.add(new_user)
    session.flush()
    if new_user.ma_nhan_vien:
        session.commit()
        return new_user
    else:
        session.rollback()
        return False
