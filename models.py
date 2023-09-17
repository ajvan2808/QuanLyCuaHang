from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Float, Integer, ForeignKey, create_engine, DECIMAL, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class KhachHang(Base):
    __tablename__ = 'KhachHang'
    ma_khach_hang = Column(String(200), nullable=False, primary_key=True)
    ten_khach_hang = Column(String(200), nullable=False)
    dia_chi = Column(String(200), nullable=False)
    dien_thoai = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)

    def __str__(self):
        return self.ho_ten


class DonHang(Base):
    __tablename__ = 'DonHang'
    ma_don_hang = Column(String(200), nullable=False, primary_key=True)
    so_luong = Column(Integer(), nullable=False)
    tong_tien = Column(DECIMAL(), nullable=False)
    ngay_dat_hang = Column(DateTime(), nullable=False)
    maKhachHang = Column(String(200), ForeignKey('KhachHang.ma_khach_hang'), nullable=True)
    khach_hang = relationship(KhachHang, backref='don_hang')

    def __str__(self):
        return self.ma_don_hang, self.ngay_dat_hang


class ChiTietDonHang(Base):
    __tablename__ = 'ChiTietDonHang'
    ma_thong_tin_dh = Column(String(200), primary_key=True)
    ma_dh = Column(String(200), ForeignKey('DonHang.ma_don_hang'), nullable=True)
    ma_sp = Column(String(200), ForeignKey('SanPham.ma_san_pham'), nullable=True)
    don_vi = Column(Integer(), nullable=False)
    gia = Column(DECIMAL(), nullable=False)
    product = relationship('SanPham', backref='chi_tiet_don_hang')
    order = relationship('DonHang', backref='don_hang')


class SanPham(Base):
    __tablename__ = 'SanPham'
    ma_san_pham = Column(String(200), nullable=False, primary_key=True)
    ten_san_pham = Column(String(200), nullable=False)
    phan_loai = Column(String(200), nullable=False)
    gia = Column(DECIMAL(), nullable=False)
    mo_ta = Column(String(300), nullable=True)
    ngay_nhap_hang = Column(DateTime(), nullable=False)
    ngay_xuat_hang = Column(DateTime(), nullable=False)

    def __str__(self):
        return self.ma_san_pham, self.ten_san_pham


engine = create_engine("mysql+pymysql://root@localhost:3306/quanlycuahang", echo=True)
Base.metadata.create_all(engine)
print('Data engine connected')
