import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID
import uuid


class GUID(TypeDecorator):
    """Platform-independent GUID type.
    Uses PostgreSQL's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.
    """

    impl = CHAR
    cache_ok = True

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == "postgresql":
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            if not isinstance(value, uuid.UUID):
                value = uuid.UUID(value)
            return value


class KhachHang(Base):
    __tablename__ = 'KhachHang'
    ma_khach_hang = Column(String(200), nullable=False, primary_key=True)
    ten_khach_hang = Column(String(200), nullable=False)
    dien_thoai = Column(String(20), nullable=False)
    dia_chi = Column(String(200), nullable=True)
    ngay_sinh = Column(String(200), nullable=True)
    doanh_thu = Column(Integer(), nullable=True)
    don_hang = relationship('DonHang', back_populates='khach_hang_dh')

    def __str__(self):
        return f"Khách hàng {self.ten_khach_hang} - Mã khách hàng: {self.ma_khach_hang}"


class NhanVien(Base):
    __tablename__ = 'NhanVien'
    ma_nhan_vien = Column(String(50), nullable=False, primary_key=True)
    ho_ten = Column(String(200), nullable=False)
    dien_thoai = Column(String(50), nullable=False)
    dia_chi = Column(String(200), nullable=True)
    ngay_vao_lam = Column(String(200), nullable=False)
    don_hang = relationship('DonHang', back_populates='nhan_vien_dh')

    def __str__(self):
        return (f"Nhân viên: {self.ho_ten}\n"
                f"Số điẹn thoại: {self.dien_thoai}\n"
                f"Địa chỉ: {self.dia_chi}\n"
                f"Ngày vào làm: {self.ngay_vao_lam}")


class DonHang(Base):
    __tablename__ = 'DonHang'
    ma_don_hang = Column(String(200), nullable=False, primary_key=True)
    ngay_tao_dh = Column(String(200), nullable=False)
    tong_so_luong = Column(Integer(), nullable=False)
    tong_tien = Column(Integer(), nullable=False)
    ma_kh = Column(String(200), ForeignKey('KhachHang.ma_khach_hang'), nullable=False)
    ma_nv = Column(String(50), ForeignKey('NhanVien.ma_nhan_vien'), nullable=False)
    khach_hang = relationship('KhachHang', back_populates='don_hang_kh')
    nhan_vien = relationship('NhanVien', back_populates='don_hang_nv')

    def __str__(self):
        return f"Đơn hàng {self.ma_don_hang} - Ngày tạo: {self.ngay_tao_dh}"


class SanPham(Base):
    __tablename__ = 'SanPham'
    ma_san_pham = Column(String(200), nullable=False, primary_key=True)
    ten_san_pham = Column(String(200), nullable=False)
    don_vi_tinh = Column(String(50), nullable=True)
    nuoc_san_xuat = Column(String(50), nullable=True)
    han_su_dung = Column(Integer(), nullable=True)
    gia = Column(Integer(), nullable=False)
    ctdh = relationship('ChiTietDonHang', back_populates='san_pham_ctdh')


class ChiTietDonHang(Base):
    __tablename__ = 'ChiTietDonHang'
    ma_chi_tiet_dh = Column(GUID(), primary_key=True, default=uuid.uuid4)
    so_luong_sp = Column(Integer(), nullable=False)
    ma_dh = Column(String(200), ForeignKey('DonHang.ma_don_hang'), nullable=False)
    ma_sp = Column(String(200), ForeignKey('SanPham.ma_san_pham'), nullable=False)
    san_pham = relationship('SanPham', back_populates='chi_tiet_don_hang_sp')
    don_hang = relationship('DonHang', backref='chi_tiet_don_hang')


class KhoHang(Base):
    __tablename__ = 'KhoHang'
    stt = Column(Integer(), primary_key=True)   # default auto increment
    ten_san_pham = Column(String(200), nullable=False)
    don_vi_tinh = Column(String(50), nullable=True)
    nuoc_san_xuat = Column(String(50), nullable=True)
    han_su_dung = Column(Integer(), nullable=True)
    gia = Column(Integer(), nullable=True)
    so_luong = Column(Integer(), nullable=False)
    trang_thai = Column(String(50), nullable=True)
    ma_sp = Column(String(200), ForeignKey('SanPham.ma_san_pham'), nullable=False)
    san_pham = relationship('SanPham', backref='kho_hang')

    def __str__(self):
        return self.__tablename__


engine = create_engine("mysql+pymysql://root@localhost:3306/quanlykhohang", echo=True)
Base.metadata.create_all(engine)
print('Data engine connected')
