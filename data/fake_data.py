import csv
import datetime
import random
import uuid

from faker import Faker
import faker_commerce

fake = Faker('vi_VN')
fake.add_provider(faker_commerce.Provider)

with open('data/customers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ma_kh', 'ten_kh', 'so_dth', 'dia_chi', 'email'])
    for _ in range(1000):
        ma_kh = fake.vin()
        ten_kh = fake.name()
        so_dth = fake.phone_number()
        dia_chi = fake.address()
        email = fake.email()
        writer.writerow([ma_kh, ten_kh, so_dth, dia_chi, email])

with open('data/orders.csv', mode='w', newline='') as odfile:
    writer = csv.writer(odfile)
    writer.writerow(['ma_don_hang', 'ngay_dat_hang', 'so_luong', 'tong_tien', 'maKhachHang'])
    for _ in range(2500):
        ma_hoa_don = fake.uuid4()
        so_luong = random.randint(0, 20)
        tong_tien = 0.0
        ngay_dat_hang = fake.date_between(start_date='-1y', end_date='today')
        writer.writerow([ma_hoa_don, ngay_dat_hang, so_luong, tong_tien, ''])

with open('data/order_details.csv', mode='w', newline='') as odtfile:
    writer = csv.writer(odtfile)
    writer.writerow(['ma_thong_tin_hd', 'ma_dh', 'ma_sp', 'don_vi', 'gia'])
    for _ in range(3500):
        ma_thong_tin_hd = uuid.uuid4()
        don_vi = random.randint(1, 5)
        gia = random.uniform(5_000.0, 1_000_000.0)
        writer.writerow([ma_thong_tin_hd, '', '', don_vi, gia])

with open('data/products.csv', mode='w', newline='') as prodfile:
    writer = csv.writer(prodfile)
    writer.writerow(['ma_sp', 'ten_sp', 'phan_loai', 'gia', 'ngay_nhap_hang', 'ngay_xuat_hang', 'mo_ta'])
    for _ in range(500):
        ma_sp = fake.ean(length=13)
        ten_sp = fake.ecommerce_name()
        phan_loai = fake.ecommerce_category()
        gia = random.uniform(5_000.0, 1_000_000.0)
        mo_ta = fake.sentences()
        ngay_nhap_hang = fake.date_between(start_date='-2y', end_date='today')
        ngay_xuat_hang = ngay_nhap_hang - datetime.timedelta(days=16)
        writer.writerow([ma_sp, ten_sp, phan_loai, gia, ngay_nhap_hang, ngay_xuat_hang, mo_ta])
