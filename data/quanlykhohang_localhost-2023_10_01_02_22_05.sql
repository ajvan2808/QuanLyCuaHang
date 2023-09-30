-- MySQL dump 10.13  Distrib 8.1.0, for macos13.3 (x86_64)
--
-- Host: 127.0.0.1    Database: quanlykhohang
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ChiTietDonHang`
--

DROP TABLE IF EXISTS `ChiTietDonHang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ChiTietDonHang` (
  `ma_chi_tiet_dh` char(32) NOT NULL,
  `so_luong` int NOT NULL,
  `ma_dh` varchar(200) NOT NULL,
  `ma_sp` varchar(200) NOT NULL,
  PRIMARY KEY (`ma_chi_tiet_dh`),
  KEY `ma_dh` (`ma_dh`),
  KEY `ma_sp` (`ma_sp`),
  CONSTRAINT `chitietdonhang_ibfk_1` FOREIGN KEY (`ma_dh`) REFERENCES `DonHang` (`ma_don_hang`),
  CONSTRAINT `chitietdonhang_ibfk_2` FOREIGN KEY (`ma_sp`) REFERENCES `SanPham` (`ma_san_pham`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ChiTietDonHang`
--

LOCK TABLES `ChiTietDonHang` WRITE;
/*!40000 ALTER TABLE `ChiTietDonHang` DISABLE KEYS */;
INSERT INTO `ChiTietDonHang` VALUES ('00256e62',7,'HD82','SP11'),('013c4b97',6,'HD105','SP23'),('01c63a18',8,'HD16','SP18'),('021406d1',7,'HD22','SP20'),('029bf77b',9,'HD41','SP11'),('02b5ef80',9,'HD48','SP16'),('0313005d',7,'HD26','SP11'),('033355a2',6,'HD24','SP19'),('058950b0',7,'HD107','SP18'),('05a46c65',5,'HD20','SP14'),('0663c777',6,'HD94','SP24'),('070b7a6c',5,'HD75','SP21'),('08b1f24d',5,'HD63','SP15'),('08cf44bd',9,'HD25','SP16'),('0a4bf651',10,'HD14','SP13'),('0a602481',5,'HD61','SP11'),('0a695921',5,'HD100','SP12'),('0ade6b15',10,'HD50','SP11'),('0b7f9193',9,'HD80','SP14'),('0d0651c3',7,'HD85','SP20'),('0f20960b',6,'HD20','SP13'),('0ff1cbe3',9,'HD102','SP15'),('115f05ac',10,'HD12','SP17'),('117678be',5,'HD106','SP14'),('11c6affb',6,'HD71','SP16'),('12b21ae8',10,'HD38','SP19'),('150c051d',10,'HD110','SP20'),('17d123ef',8,'HD16','SP15'),('18c2ea1e',6,'HD100','SP11'),('198bccff',5,'HD77','SP20'),('1a20856a',8,'HD29','SP23'),('1ab41e90',9,'HD55','SP25'),('1ac298c1',7,'HD70','SP20'),('1b1535c9',9,'HD58','SP18'),('1b253317',8,'HD99','SP13'),('1cbf79e6',8,'HD95','SP25'),('1cfb1936',6,'HD93','SP20'),('1d9798e3',10,'HD50','SP14'),('1df5f455',6,'HD36','SP24'),('1e2ed8ca',10,'HD15','SP11'),('1f2230a3',7,'HD53','SP20'),('1f34a615',10,'HD32','SP17'),('20139993',8,'HD84','SP18'),('21e5418d',5,'HD95','SP24'),('22397492',7,'HD32','SP16'),('22e59e91',7,'HD98','SP18'),('23758f61',8,'HD80','SP13'),('238418c9',9,'HD48','SP17'),('24aa3a9d',5,'HD97','SP19'),('24c81eeb',5,'HD99','SP15'),('262ed076',10,'HD45','SP19'),('282d82b9',8,'HD59','SP15'),('286520d6',8,'HD22','SP19'),('291998aa',6,'HD54','SP25'),('2ade1b95',8,'HD105','SP25'),('2b2a3a3b',10,'HD20','SP12'),('2b5ecc33',6,'HD102','SP14'),('2c32ba17',10,'HD26','SP13'),('2d0464a1',7,'HD62','SP12'),('2eebc087',9,'HD102','SP13'),('2f61b749',5,'HD86','SP21'),('2fe8c56e',7,'HD18','SP22'),('30188080',9,'HD105','SP24'),('308bbfea',8,'HD47','SP20'),('322b65e7',8,'HD30','SP23'),('32ad935e',10,'HD97','SP20'),('33759819',5,'HD11','SP22'),('33da4c24',10,'HD18','SP21'),('33e28e19',10,'HD52','SP15'),('348b0ed2',8,'HD87','SP19'),('35c6ba4e',9,'HD44','SP16'),('35eac8fc',5,'HD30','SP25'),('3715ad6c',6,'HD108','SP22'),('376e4120',9,'HD51','SP11'),('37955b08',9,'HD100','SP13'),('379802c5',10,'HD107','SP20'),('3923104b',5,'HD94','SP21'),('398c63c2',10,'HD24','SP18'),('3a94d1a5',10,'HD53','SP18'),('3b2ab73e',10,'HD56','SP23'),('3cfe9c9e',5,'HD37','SP23'),('407d3d04',10,'HD40','SP15'),('41a122b3',7,'HD26','SP12'),('41dd0fdd',9,'HD86','SP22'),('41f2fdaa',10,'HD45','SP18'),('423c8d27',8,'HD14','SP11'),('43287958',10,'HD72','SP13'),('4394d6c6',8,'HD65','SP21'),('4395a470',7,'HD98','SP16'),('442e325e',10,'HD100','SP14'),('44cf0609',7,'HD47','SP23'),('4655295a',8,'HD12','SP19'),('46749bb3',6,'HD33','SP11'),('47d96dde',5,'HD101','SP11'),('4813b5dd',6,'HD29','SP21'),('48571f2c',5,'HD109','SP23'),('48ce37af',7,'HD33','SP12'),('48cf08c3',9,'HD94','SP22'),('4920abe8',6,'HD67','SP24'),('498692be',10,'HD16','SP16'),('49afe016',5,'HD99','SP12'),('4a637dda',9,'HD27','SP17'),('4a8c6bed',9,'HD86','SP24'),('4d3e21e8',8,'HD54','SP23'),('4dc906b4',5,'HD107','SP16'),('4f61cf76',8,'HD106','SP15'),('4f8287c3',8,'HD35','SP23'),('5012cb61',6,'HD16','SP14'),('51087d71',7,'HD78','SP19'),('51f4f112',10,'HD68','SP24'),('5201a001',5,'HD13','SP15'),('52bbefb8',5,'HD52','SP17'),('563f8f15',5,'HD37','SP22'),('56d2687a',10,'HD106','SP11'),('5713e340',10,'HD110','SP21'),('5756cf57',8,'HD35','SP25'),('5768849b',9,'HD25','SP17'),('5850a731',6,'HD57','SP20'),('5aeccca4',8,'HD36','SP25'),('5b0beda0',5,'HD22','SP22'),('5b37b8c8',9,'HD76','SP25'),('5c301be9',7,'HD17','SP19'),('5cefb798',8,'HD102','SP12'),('5ef86d14',7,'HD58','SP19'),('5f48d8a1',9,'HD108','SP23'),('5fba22b5',10,'HD84','SP16'),('61be574b',8,'HD66','SP23'),('642a1c9a',9,'HD108','SP21'),('64700cd7',9,'HD59','SP16'),('64eb18cf',5,'HD53','SP19'),('6517770a',9,'HD49','SP15'),('652cb6f9',8,'HD27','SP15'),('66bb2f6d',6,'HD40','SP14'),('6803667b',5,'HD71','SP18'),('692e4ad7',9,'HD62','SP11'),('69a90308',7,'HD98','SP14'),('6a59e9d9',5,'HD45','SP17'),('6aea7d97',10,'HD35','SP22'),('6dc9da18',5,'HD84','SP17'),('6f24f8cf',7,'HD16','SP17'),('6fe7f02e',5,'HD103','SP25'),('712ee0c6',6,'HD62','SP13'),('716836af',5,'HD72','SP12'),('720ea8ff',6,'HD53','SP22'),('72230283',10,'HD86','SP23'),('72b77135',10,'HD39','SP17'),('72fa997d',10,'HD60','SP13'),('73351fdd',10,'HD75','SP22'),('73ba3cd6',5,'HD71','SP17'),('760e027b',10,'HD72','SP11'),('7634e112',7,'HD47','SP24'),('76f3cb51',10,'HD39','SP16'),('776861ae',7,'HD109','SP24'),('77d40431',9,'HD22','SP21'),('7ba4999a',6,'HD19','SP23'),('7bd5a968',9,'HD65','SP20'),('7cbed59d',6,'HD19','SP24'),('7d66005d',9,'HD47','SP25'),('7e7cf973',9,'HD41','SP12'),('7e961752',8,'HD32','SP18'),('7f16eec2',7,'HD63','SP17'),('80f91ef3',8,'HD42','SP11'),('8149ec9b',8,'HD21','SP16'),('8379a791',9,'HD73','SP15'),('848e7698',6,'HD83','SP13'),('85b58ee7',7,'HD54','SP24'),('85bd6a7d',8,'HD33','SP13'),('85f5c529',9,'HD87','SP20'),('8628d9a0',6,'HD31','SP20'),('86519d4a',10,'HD12','SP16'),('86e01a6d',6,'HD60','SP12'),('883b8f84',7,'HD94','SP23'),('88a8766f',7,'HD21','SP17'),('89375de2',5,'HD84','SP19'),('89530b37',5,'HD53','SP21'),('8c82765b',6,'HD35','SP21'),('8d15c261',10,'HD93','SP18'),('8d6fb3ca',6,'HD32','SP15'),('8e569898',10,'HD46','SP20'),('8fa5129b',6,'HD83','SP14'),('901155d7',6,'HD81','SP12'),('9372f914',7,'HD57','SP21'),('93b866f0',5,'HD93','SP19'),('93fbde7f',5,'HD27','SP19'),('945261ab',8,'HD91','SP15'),('95e150f8',8,'HD15','SP13'),('96dec761',8,'HD30','SP24'),('970d4551',8,'HD62','SP14'),('990a6281',7,'HD23','SP24'),('9c6913f8',9,'HD106','SP13'),('9d31f7f6',9,'HD34','SP17'),('9e5b10c6',6,'HD74','SP20'),('9e61653b',9,'HD109','SP25'),('9e88981d',8,'HD94','SP25'),('9f93f375',6,'HD90','SP14'),('a0602198',8,'HD48','SP18'),('a083e98c',8,'HD64','SP18'),('a19d7264',6,'HD91','SP12'),('a1dc4892',6,'HD25','SP15'),('a1f606d2',5,'HD51','SP12'),('a20ba807',6,'HD44','SP14'),('a22ed915',5,'HD24','SP20'),('a32befb0',6,'HD104','SP25'),('a36c5122',8,'HD68','SP25'),('a3959744',6,'HD58','SP17'),('a3a74d1a',6,'HD99','SP14'),('a3dbaed3',6,'HD89','SP16'),('a4840f6f',10,'HD14','SP12'),('a4b14c32',5,'HD39','SP18'),('a5b5401c',5,'HD66','SP22'),('a5f6e671',8,'HD23','SP21'),('a6101e7b',10,'HD27','SP16'),('a719b282',10,'HD20','SP15'),('a7afce77',9,'HD34','SP18'),('a8c547e3',7,'HD107','SP17'),('abf68f1a',7,'HD43','SP13'),('acbe2c10',5,'HD71','SP14'),('adfcce07',9,'HD107','SP19'),('b0304891',6,'HD31','SP19'),('b079b619',10,'HD63','SP16'),('b0dbe81a',8,'HD25','SP13'),('b10b8325',7,'HD92','SP17'),('b1737099',5,'HD47','SP19'),('b1e95386',6,'HD44','SP15'),('b1fe3e65',5,'HD52','SP14'),('b357c505',9,'HD13','SP14'),('b45979da',6,'HD23','SP22'),('b63f79f9',9,'HD96','SP23'),('b6aa14cb',9,'HD64','SP19'),('b6d774f7',6,'HD77','SP22'),('b8769c6b',7,'HD74','SP19'),('b93771fb',10,'HD47','SP21'),('b99e3427',5,'HD17','SP20'),('baea9019',10,'HD74','SP17'),('bc0bbbe3',5,'HD78','SP18'),('bc134ef9',8,'HD23','SP23'),('bc22ea2a',10,'HD33','SP15'),('bce944ad',10,'HD72','SP14'),('bd1c2be0',10,'HD52','SP16'),('bd6e37b0',6,'HD90','SP15'),('befc9c96',10,'HD25','SP14'),('bfa70371',8,'HD31','SP22'),('bfc06302',9,'HD21','SP18'),('c1e466ca',6,'HD47','SP22'),('c1e8d91d',8,'HD38','SP20'),('c2db5c9b',7,'HD15','SP12'),('c39876c3',6,'HD73','SP16'),('c6381f44',8,'HD78','SP17'),('c65e9456',8,'HD28','SP20'),('c72033b9',10,'HD40','SP13'),('c7e531f6',9,'HD91','SP11'),('c8a9218c',10,'HD99','SP11'),('c8e28884',8,'HD74','SP18'),('c97be154',6,'HD23','SP25'),('c9e9822a',5,'HD88','SP18'),('cbe7b87e',10,'HD60','SP14'),('ceaf124b',7,'HD42','SP12'),('cedc48ce',7,'HD76','SP24'),('cedd3932',8,'HD77','SP21'),('cf3be9b7',9,'HD92','SP16'),('d037bcd3',7,'HD105','SP22'),('d14dc3da',10,'HD27','SP18'),('d1cbaa25',9,'HD38','SP21'),('d688b3b2',5,'HD83','SP15'),('d79cc4e3',10,'HD50','SP13'),('d7cb19d5',8,'HD80','SP15'),('d8d18469',10,'HD56','SP22'),('db0b81f3',9,'HD56','SP24'),('db75aa31',5,'HD26','SP14'),('de076963',6,'HD96','SP22'),('de8ab357',9,'HD102','SP11'),('e14ee17a',6,'HD98','SP15'),('e2c0e928',10,'HD35','SP19'),('e2ce7a89',9,'HD98','SP17'),('e46362d4',10,'HD79','SP16'),('e5177177',5,'HD20','SP11'),('e7f00a4c',8,'HD68','SP22'),('e96e3b86',7,'HD88','SP17'),('e970809e',5,'HD85','SP22'),('edb55e62',6,'HD91','SP13'),('ee3de871',9,'HD70','SP19'),('ef7bb934',8,'HD82','SP12'),('f0353265',6,'HD86','SP25'),('f35a599a',6,'HD35','SP24'),('f6410655',7,'HD29','SP22'),('f6d5c757',8,'HD50','SP12'),('f73e60af',7,'HD85','SP21'),('f8bbe0de',5,'HD33','SP14'),('f9eb04a6',8,'HD71','SP15'),('fa82a81d',6,'HD12','SP18'),('fa9188e2',9,'HD77','SP23'),('fb54bf96',6,'HD34','SP16'),('fdd69c42',5,'HD91','SP14'),('fddac903',5,'HD35','SP20'),('fe3f1896',5,'HD106','SP12'),('fe4d3c8e',9,'HD69','SP21'),('ff67ebe1',7,'HD51','SP13'),('ff6fd6bf',7,'HD31','SP21'),('ff7f740a',5,'HD68','SP23'),('ff864c4e',9,'HD96','SP21');
/*!40000 ALTER TABLE `ChiTietDonHang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DonHang`
--

DROP TABLE IF EXISTS `DonHang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DonHang` (
  `ma_don_hang` varchar(200) NOT NULL,
  `ngay_tao_dh` varchar(200) NOT NULL,
  `tong_so_luong` int NOT NULL,
  `tong_tien` int NOT NULL,
  `ma_kh` varchar(200) NOT NULL,
  `ma_nv` varchar(50) NOT NULL,
  PRIMARY KEY (`ma_don_hang`),
  KEY `ma_kh` (`ma_kh`),
  KEY `ma_nv` (`ma_nv`),
  CONSTRAINT `donhang_ibfk_1` FOREIGN KEY (`ma_kh`) REFERENCES `KhachHang` (`ma_khach_hang`),
  CONSTRAINT `donhang_ibfk_2` FOREIGN KEY (`ma_nv`) REFERENCES `NhanVien` (`ma_nhan_vien`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DonHang`
--

LOCK TABLES `DonHang` WRITE;
/*!40000 ALTER TABLE `DonHang` DISABLE KEYS */;
INSERT INTO `DonHang` VALUES ('HD100','21/10/2019',6,83000000,'KH14','NV18'),('HD101','22/2/2018',10,5000000,'KH30','NV16'),('HD102','14/1/2005',50,139000000,'KH15','NV16'),('HD103','3/9/2005',15,16000000,'KH20','NV13'),('HD104','16/1/2020',6,19200000,'KH36','NV16'),('HD105','11/9/2018',30,83200000,'KH18','NV17'),('HD106','8/4/2019',37,123000000,'KH32','NV17'),('HD107','28/6/2020',38,34200000,'KH30','NV19'),('HD108','12/12/2006',24,54000000,'KH29','NV18'),('HD109','2/10/2016',21,61400000,'KH15','NV17'),('HD11','27/12/2021',5,12000000,'KH24','NV14'),('HD110','28/2/2022',20,32000000,'KH32','NV12'),('HD12','24/8/2016',34,20400000,'KH31','NV11'),('HD13','7/4/2017',14,71000000,'KH35','NV18'),('HD14','26/2/2014',28,58000000,'KH15','NV13'),('HD15','12/7/2020',25,48000000,'KH32','NV16'),('HD16','27/2/2000',39,91200000,'KH38','NV12'),('HD17','17/2/2020',12,15400000,'KH26','NV16'),('HD18','4/10/2001',17,34800000,'KH35','NV20'),('HD19','3/12/2022',12,32400000,'KH34','NV15'),('HD20','18/10/2016',36,133000000,'KH14','NV11'),('HD21','6/7/2003',24,11600000,'KH28','NV12'),('HD22','21/3/2001',29,47600000,'KH36','NV20'),('HD23','3/7/2013',35,88400000,'KH19','NV12'),('HD24','5/10/2015',21,22200000,'KH23','NV20'),('HD25','28/4/2007',42,111400000,'KH21','NV17'),('HD26','18/4/2009',29,71000000,'KH14','NV19'),('HD27','6/2/2008',42,75600000,'KH25','NV16'),('HD28','1/1/2007',8,11200000,'KH31','NV20'),('HD29','17/4/2015',21,48400000,'KH17','NV20'),('HD30','15/7/2015',21,59200000,'KH33','NV18'),('HD31','15/3/2018',27,47400000,'KH12','NV12'),('HD32','16/4/2014',31,53800000,'KH19','NV16'),('HD33','9/8/2007',36,134000000,'KH35','NV17'),('HD34','16/1/2009',24,12000000,'KH11','NV12'),('HD35','5/11/2015',53,117000000,'KH30','NV20'),('HD36','11/3/2022',14,42400000,'KH25','NV18'),('HD37','1/10/2014',10,25000000,'KH25','NV12'),('HD38','25/7/2004',27,39400000,'KH39','NV12'),('HD39','28/1/2021',25,10000000,'KH12','NV15'),('HD40','30/9/2010',26,124000000,'KH16','NV12'),('HD41','8/12/2002',18,27000000,'KH16','NV17'),('HD42','18/8/2022',15,22000000,'KH26','NV17'),('HD43','11/10/2003',7,21000000,'KH35','NV15'),('HD44','24/10/2006',21,67800000,'KH35','NV11'),('HD45','12/5/2010',25,22000000,'KH26','NV18'),('HD46','12/4/2013',10,14000000,'KH34','NV12'),('HD47','28/1/2021',52,116200000,'KH13','NV18'),('HD48','4/3/2010',26,11800000,'KH20','NV16'),('HD49','9/1/2009',9,63000000,'KH24','NV16'),('HD50','17/1/2006',38,96000000,'KH30','NV13'),('HD51','21/11/2005',21,40000000,'KH13','NV15'),('HD52','23/10/2021',30,94000000,'KH11','NV15'),('HD53','16/4/2005',33,47200000,'KH28','NV18'),('HD54','20/9/2015',21,59600000,'KH40','NV17'),('HD55','13/1/2022',9,28800000,'KH34','NV18'),('HD56','16/12/2007',29,75200000,'KH40','NV16'),('HD57','11/8/2020',13,21000000,'KH27','NV19'),('HD58','22/8/2004',22,18000000,'KH16','NV13'),('HD59','25/7/2020',17,57800000,'KH16','NV14'),('HD60','21/2/2002',26,82000000,'KH37','NV17'),('HD61','30/6/2003',5,5000000,'KH19','NV14'),('HD62','22/1/2022',30,73000000,'KH13','NV15'),('HD63','20/10/2004',22,39800000,'KH21','NV14'),('HD64','14/5/2003',17,17200000,'KH24','NV20'),('HD65','10/12/2012',17,27000000,'KH19','NV18'),('HD66','10/11/2015',13,32800000,'KH26','NV20'),('HD67','25/6/2006',6,16800000,'KH31','NV17'),('HD68','6/10/2013',31,85800000,'KH37','NV19'),('HD69','7/2/2011',9,16200000,'KH21','NV16'),('HD70','5/4/2006',16,20600000,'KH36','NV19'),('HD71','8/7/2015',29,83200000,'KH31','NV11'),('HD72','15/4/2010',35,90000000,'KH13','NV18'),('HD73','18/5/2011',15,64200000,'KH22','NV17'),('HD74','3/10/2002',31,27200000,'KH23','NV15'),('HD75','9/5/2010',15,33000000,'KH35','NV15'),('HD76','9/10/2015',16,48400000,'KH24','NV19'),('HD77','4/4/2007',28,59200000,'KH24','NV15'),('HD78','3/8/2009',20,15600000,'KH11','NV16'),('HD79','21/8/2008',10,2000000,'KH21','NV18'),('HD80','17/9/2015',25,116000000,'KH28','NV11'),('HD81','6/12/2005',6,12000000,'KH19','NV11'),('HD82','16/12/2017',15,23000000,'KH24','NV14'),('HD83','30/9/2010',17,77000000,'KH15','NV20'),('HD84','20/2/2006',28,16400000,'KH30','NV14'),('HD85','1/9/2014',19,34400000,'KH38','NV12'),('HD86','20/3/2019',39,101000000,'KH33','NV20'),('HD87','22/12/2008',17,22200000,'KH17','NV16'),('HD88','12/4/2004',12,6800000,'KH33','NV11'),('HD89','14/8/2013',6,1200000,'KH31','NV13'),('HD90','25/10/2001',12,66000000,'KH20','NV17'),('HD91','12/1/2014',34,115000000,'KH13','NV18'),('HD92','20/12/2001',16,4600000,'KH11','NV15'),('HD93','23/2/2001',21,22400000,'KH23','NV18'),('HD94','23/6/2017',35,91200000,'KH18','NV12'),('HD95','3/10/2001',13,39600000,'KH29','NV17'),('HD96','12/8/2021',24,54000000,'KH20','NV11'),('HD97','8/8/2011',15,20000000,'KH28','NV17'),('HD98','18/11/2018',36,80600000,'KH17','NV20'),('HD99','25/7/2010',34,103000000,'KH18','NV13');
/*!40000 ALTER TABLE `DonHang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `KhachHang`
--

DROP TABLE IF EXISTS `KhachHang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `KhachHang` (
  `ma_khach_hang` varchar(200) NOT NULL,
  `ten_khach_hang` varchar(200) NOT NULL,
  `dien_thoai` varchar(20) NOT NULL,
  `dia_chi` varchar(200) DEFAULT NULL,
  `ngay_sinh` varchar(200) DEFAULT NULL,
  `doanh_thu` int DEFAULT NULL,
  PRIMARY KEY (`ma_khach_hang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `KhachHang`
--

LOCK TABLES `KhachHang` WRITE;
/*!40000 ALTER TABLE `KhachHang` DISABLE KEYS */;
INSERT INTO `KhachHang` VALUES ('KH11','Hà Minh Anh','093379655','Số 111, Phường 3, Quận Ô Môn, TP.Cần Thơ','7/10/1984',126200000),('KH12','Tô Minh  Anh','096875676','Số 136, Phường 3, Quận Bình Thủy, TP.Cần Thơ','24/2/1979',57400000),('KH13','Trần Ngọc Quỳnh Anh','083478889','Số 213, Phường 10, Quận Bình Thủy, TP.Cần Thơ','21/5/1986',434200000),('KH14','Trần Nguyễn Hoài Anh','098570680','Số 213, Phường 6, Quận Ô Môn, TP.Cần Thơ','22/7/1981',287000000),('KH15','Lê Thị Ngọc Ánh','098830282','Số 105, Phường 9, Quận Bình Thủy, TP.Cần Thơ','9/2/1979',335400000),('KH16','Hồ Phúc  Bảo','090672020','Số 30, Phường 10, Quận Ô Môn, TP.Cần Thơ','10/7/1973',226800000),('KH17','Phan Thành Danh','090312583','Số 221, Phường 8, Quận Ninh Kiều, TP.Cần Thơ','12/3/1980',151200000),('KH18','Lê Hoàng Bảo  Duyên','098404353','Số 79, Phường 4, Quận Ô Môn, TP.Cần Thơ','11/12/1970',277400000),('KH19','Nguyễn Công Thành Đạt','097417125','Số 104, Phường 8, Quận Cái Răng, TP.Cần Thơ','21/7/1985',186200000),('KH20','Nguyễn Quang Trí Đức','090298473','Số 342, Phường 5, Quận Ninh Kiều, TP.Cần Thơ','17/8/1968',147800000),('KH21','Giang Nguyễn Gia Hân','093387880','Số 179, Phường 3, Quận Bình Thủy, TP.Cần Thơ','20/10/1984',169400000),('KH22','Phan Nhã Hân','093970649','Số 80, Phường 2, Quận Ô Môn, TP.Cần Thơ','14/6/1981',64200000),('KH23','Đặng Lâm Huy Hoàng','091511653','Số 171, Phường 8, Quận Ô Môn, TP.Cần Thơ','12/4/1981',71800000),('KH24','Đặng Nguyễn Bảo Khang','093829844','Số 217, Phường 7, Quận Ô Môn, TP.Cần Thơ','3/2/1974',222800000),('KH25','Huỳnh Trần Vĩnh  Khang','093924324','Số 137, Phường 4, Quận Ô Môn, TP.Cần Thơ','13/9/1981',143000000),('KH26','Nguyễn Quy Khang','096360462','Số 176, Phường 10, Quận Bình Thủy, TP.Cần Thơ','20/4/1978',92200000),('KH27','Hoàng Gia  Khiêm','097283130','Số 50, Phường 4, Quận Ô Môn, TP.Cần Thơ','21/5/1980',21000000),('KH28','Lê Minh Khôi','079856786','Số 267, Phường 2, Quận Cái Răng, TP.Cần Thơ','20/12/1985',194800000),('KH29','Mai Phương  Linh','038369038','Số 109, Phường 6, Quận Bình Thủy, TP.Cần Thơ','25/8/1979',93600000),('KH30','Nguyễn Ngọc Khánh Linh','077414639','Số 108, Phường 3, Quận Bình Thủy, TP.Cần Thơ','25/9/1969',268600000),('KH31','Hà Văn Mạnh','090278380','Số 43, Phường 3, Quận Ô Môn, TP.Cần Thơ','4/7/1982',132800000),('KH32','Đàm Ngọc Mi Na','090849261','Số 117, Phường 1, Quận Bình Thủy, TP.Cần Thơ','1/11/1982',203000000),('KH33','Trần Hoàng Thư Nghi','098309843','Số 259, Phường 3, Quận Bình Thủy, TP.Cần Thơ','23/8/1971',167000000),('KH34','Trần Ngọc Phương Nghi','093353847','Số 180, Phường 7, Quận Cái Răng, TP.Cần Thơ','12/12/1971',75200000),('KH35','Trần Phương Nghi','093517514','Số 125, Phường 10, Quận Cái Răng, TP.Cần Thơ','16/10/1967',361600000),('KH36','Lê Kim Bảo Ngọc','097918768','Số 250, Phường 5, Quận Ô Môn, TP.Cần Thơ','2/5/1972',87400000),('KH37','Trương Lê Thảo Nguyên','093107865','Số 283, Phường 2, Quận Ô Môn, TP.Cần Thơ','7/11/1974',167800000),('KH38','Nguyễn Trọng Nhân','098760076','Số 182, Phường 6, Quận Cái Răng, TP.Cần Thơ','19/2/1981',125600000),('KH39','Nguyễn Thảo Nhi','093429968','Số 25, Phường 5, Quận Cái Răng, TP.Cần Thơ','20/9/1972',39400000),('KH40','Nguyễn Phạm Quỳnh Như','090978028','Số 91, Phường 5, Quận Cái Răng, TP.Cần Thơ','30/12/1981',134800000);
/*!40000 ALTER TABLE `KhachHang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `KhoHang`
--

DROP TABLE IF EXISTS `KhoHang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `KhoHang` (
  `stt` int NOT NULL AUTO_INCREMENT,
  `ten_san_pham` varchar(200) NOT NULL,
  `don_vi_tinh` varchar(50) DEFAULT NULL,
  `nuoc_san_xuat` varchar(50) DEFAULT NULL,
  `han_su_dung` int DEFAULT NULL,
  `gia` int DEFAULT NULL,
  `so_luong` int NOT NULL,
  `trang_thai` varchar(50) DEFAULT NULL,
  `ma_sp` varchar(200) NOT NULL,
  PRIMARY KEY (`stt`),
  KEY `ma_sp` (`ma_sp`),
  CONSTRAINT `khohang_ibfk_1` FOREIGN KEY (`ma_sp`) REFERENCES `SanPham` (`ma_san_pham`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `KhoHang`
--

LOCK TABLES `KhoHang` WRITE;
/*!40000 ALTER TABLE `KhoHang` DISABLE KEYS */;
INSERT INTO `KhoHang` VALUES (1,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,1000000,1000,'Nhập kho','SP11'),(2,'Phân bón NPK 16-16-8 + TE','Bao','Trung Quốc',3,2000000,1000,'Nhập kho','SP12'),(3,'Phân bón NPK 20-20-15 + TE','Bao','Hàn Quốc',3,3000000,1000,'Nhập kho','SP13'),(4,'Phân bón NPK 12-12-8 + TE','Bao','Nga',3,4000000,1000,'Nhập kho','SP14'),(5,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,7000000,1000,'Nhập kho','SP15'),(6,'Phân bón lá Mát cây-Giải độc','Chai','Việt Nam',3,200000,1000,'Nhập kho','SP16'),(7,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,400000,1000,'Nhập kho','SP17'),(8,'Phân bón lá Siêu phì trái','Chai','Nga',3,800000,1000,'Nhập kho','SP18'),(9,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,1200000,1000,'Nhập kho','SP19'),(10,'Phân bón lá Supper Silika','Chai','Nga',3,1400000,1000,'Nhập kho','SP20'),(11,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,1800000,1000,'Nhập kho','SP21'),(12,'Phân bón lá Thioure 99','Chai','Trung Quốc',3,2400000,1000,'Nhập kho','SP22'),(13,'Phân bón lá Dowin','Chai','Trung Quốc',3,2600000,1000,'Nhập kho','SP23'),(14,'Phân bón lá Đẹp trái','Chai','Việt Nam',3,2800000,1000,'Nhập kho','SP24'),(15,'Phân bón lá Siêu ra rễ','Chai','Trung Quốc',3,3200000,1000,'Nhập kho','SP25'),(16,'Phân bón NPK 20-20-15 + TE','Bao','Hàn Quốc',3,0,5,'Hết Date','SP13'),(17,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,4,'Hết Date','SP17'),(18,'Phân bón lá Đẹp trái','Chai','Việt Nam',3,0,1,'Hư Hỏng','SP24'),(19,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,5,'Hết Date','SP17'),(20,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,0,2,'Hết Date','SP19'),(21,'Phân bón lá Dowin','Chai','Trung Quốc',3,0,3,'Hết Date','SP23'),(22,'Phân bón lá Mát cây-Giải độc','Chai','Việt Nam',3,0,4,'Hư Hỏng','SP16'),(23,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,0,5,'Hết Date','SP19'),(24,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,0,4,'Hết Date','SP21'),(25,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,0,5,'Hư Hỏng','SP15'),(26,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,0,2,'Hư Hỏng','SP19'),(27,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,0,3,'Hư Hỏng','SP15'),(28,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,1,'Hư Hỏng','SP17'),(29,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,1,'Hư Hỏng','SP17'),(30,'Phân bón lá Siêu phì trái','Chai','Nga',3,0,4,'Hết Date','SP18'),(31,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,0,5,'Hết Date','SP19'),(32,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,0,4,'Hết Date','SP15'),(33,'Phân bón lá Supper Silika','Chai','Nga',3,0,3,'Hết Date','SP20'),(34,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,0,4,'Hết Date','SP19'),(35,'Phân bón lá Mát cây-Giải độc','Chai','Việt Nam',3,0,4,'Hết Date','SP16'),(36,'Phân bón NPK 16-16-8 + TE','Bao','Trung Quốc',3,0,3,'Hết Date','SP12'),(37,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,3,'Hư Hỏng','SP17'),(38,'Phân bón NPK 20-20-15 + TE','Bao','Hàn Quốc',3,0,3,'Hư Hỏng','SP13'),(39,'Phân bón lá Thioure 99','Chai','Trung Quốc',3,0,5,'Hết Date','SP22'),(40,'Phân bón lá Mát cây-Giải độc','Chai','Việt Nam',3,0,3,'Hết Date','SP16'),(41,'Phân bón lá Supper Silika','Chai','Nga',3,0,1,'Hết Date','SP20'),(42,'Phân bón lá Siêu phì trái','Chai','Nga',3,0,5,'Hết Date','SP18'),(43,'Phân bón lá Thioure 99','Chai','Trung Quốc',3,0,3,'Hư Hỏng','SP22'),(44,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,2,'Hư Hỏng','SP17'),(45,'Phân bón lá Mát cây-Giải độc','Chai','Việt Nam',3,0,4,'Hư Hỏng','SP16'),(46,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,4,'Hư Hỏng','SP17'),(47,'Phân bón lá Supper Silika','Chai','Nga',3,0,5,'Hư Hỏng','SP20'),(48,'Phân bón lá Dowin','Chai','Trung Quốc',3,0,3,'Hư Hỏng','SP23'),(49,'Phân bón lá Đẹp trái','Chai','Việt Nam',3,0,4,'Hư Hỏng','SP24'),(50,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,0,1,'Hết Date','SP15'),(51,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,0,1,'Hết Date','SP11'),(52,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,0,2,'Hư Hỏng','SP11'),(53,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,0,1,'Hết Date','SP21'),(54,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,0,4,'Hết Date','SP21'),(55,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,4,'Hết Date','SP17'),(56,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,0,2,'Hết Date','SP15'),(57,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,0,4,'Hết Date','SP21'),(58,'Phân bón NPK 12-12-8 + TE','Bao','Nga',3,0,5,'Hư Hỏng','SP14'),(59,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,0,4,'Hư Hỏng','SP15'),(60,'Phân bón lá Thioure 99','Chai','Trung Quốc',3,0,5,'Hư Hỏng','SP22'),(61,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,0,5,'Hư Hỏng','SP11'),(62,'Phân bón NPK 16-16-8 + TE','Bao','Trung Quốc',3,0,5,'Hư Hỏng','SP12'),(63,'Phân bón lá Supper Silika','Chai','Nga',3,0,4,'Hư Hỏng','SP20'),(64,'Phân bón lá Siêu ra rễ','Chai','Trung Quốc',3,0,1,'Hư Hỏng','SP25'),(65,'Phân bón lá Siêu phì trái','Chai','Nga',3,0,1,'Hết Date','SP18'),(66,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,0,2,'Hết Date','SP11'),(67,'Phân bón NPK 12-12-8 + TE','Bao','Nga',3,0,3,'Hết Date','SP14'),(68,'Phân bón lá Thioure 99','Chai','Trung Quốc',3,0,2,'Hư Hỏng','SP22'),(69,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,1,'Hư Hỏng','SP17'),(70,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,5,'Hư Hỏng','SP17'),(71,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,0,4,'Hư Hỏng','SP21'),(72,'Phân bón lá Supper Silika','Chai','Nga',3,0,3,'Hết Date','SP20'),(73,'Phân bón NPK 20-20-15 + TE','Bao','Hàn Quốc',3,0,3,'Hết Date','SP13'),(74,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,0,2,'Hư Hỏng','SP11'),(75,'Phân bón NPK 16-16-8 + TE','Bao','Trung Quốc',3,0,4,'Hư Hỏng','SP12'),(76,'Phân bón lá Siêu ra rễ','Chai','Trung Quốc',3,0,3,'Hết Date','SP25'),(77,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,2,'Hết Date','SP17'),(78,'Phân bón lá Dowin','Chai','Trung Quốc',3,0,4,'Hư Hỏng','SP23'),(79,'Phân bón lá Đẹp trái','Chai','Việt Nam',3,0,2,'Hư Hỏng','SP24'),(80,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,0,3,'Hư Hỏng','SP21'),(81,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,0,4,'Hư Hỏng','SP11'),(82,'Phân bón lá Đẹp trái','Chai','Việt Nam',3,0,3,'Hư Hỏng','SP24'),(83,'Phân bón lá Thioure 99','Chai','Trung Quốc',3,0,3,'Hết Date','SP22'),(84,'Phân bón lá Siêu ra rễ','Chai','Trung Quốc',3,0,1,'Hết Date','SP25'),(85,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,0,1,'Hư Hỏng','SP15'),(86,'Phân bón lá Supper Silika','Chai','Nga',3,0,2,'Hết Date','SP20'),(87,'Phân bón lá Dowin','Chai','Trung Quốc',3,0,4,'Hết Date','SP23'),(88,'Phân bón lá Supper Silika','Chai','Nga',3,0,5,'Hư Hỏng','SP20'),(89,'Phân bón lá Supper Silika','Chai','Nga',3,0,4,'Hư Hỏng','SP20'),(90,'Phân bón lá Siêu phì trái','Chai','Nga',3,0,4,'Hư Hỏng','SP18'),(91,'Phân bón lá Mát cây-Giải độc','Chai','Việt Nam',3,0,2,'Hết Date','SP16'),(92,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,0,3,'Hết Date','SP19'),(93,'Phân bón NPK 16-16-8 + TE','Bao','Trung Quốc',3,0,1,'Hư Hỏng','SP12'),(94,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,0,3,'Hết Date','SP21'),(95,'Phân bón NPK 20-20-15 + TE','Bao','Hàn Quốc',3,0,1,'Hết Date','SP13'),(96,'Phân bón lá Siêu phì trái','Chai','Nga',3,0,3,'Hư Hỏng','SP18'),(97,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,0,3,'Hết Date','SP11'),(98,'Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,0,3,'Hết Date','SP11'),(99,'Phân bón NPK 12-12-8 + TE','Bao','Nga',3,0,5,'Hư Hỏng','SP14'),(100,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,0,3,'Hư Hỏng','SP19'),(101,'Phân bón lá Mát cây-Giải độc','Chai','Việt Nam',3,0,2,'Hết Date','SP16'),(102,'Phân bón lá Đẹp trái','Chai','Việt Nam',3,0,3,'Hư Hỏng','SP24'),(103,'Phân bón NPK 20-20-15 + TE','Bao','Hàn Quốc',3,0,3,'Hết Date','SP13'),(104,'Phân bón lá Siêu phì trái','Chai','Nga',3,0,3,'Hết Date','SP18'),(105,'Phân bón lá Nano Đồng','Chai','Trung Quốc',3,0,3,'Hết Date','SP21'),(106,'Phân bón NPK 16-16-8 + TE','Bao','Trung Quốc',3,0,4,'Hư Hỏng','SP12'),(107,'Phân bón lá Siêu ra rễ','Chai','Trung Quốc',3,0,5,'Hết Date','SP25'),(108,'Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,0,3,'Hết Date','SP15'),(109,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,2,'Hư Hỏng','SP17'),(110,'Phân bón lá Thioure 99','Chai','Trung Quốc',3,0,4,'Hư Hỏng','SP22'),(111,'Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,0,5,'Hư Hỏng','SP17'),(112,'Phân bón lá Thioure 99','Chai','Trung Quốc',3,0,1,'Hư Hỏng','SP22'),(113,'Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,0,1,'Hư Hỏng','SP19'),(114,'Phân bón lá Siêu phì trái','Chai','Nga',3,0,2,'Hư Hỏng','SP18'),(115,'Phân bón NPK 16-16-8 + TE','Bao','Trung Quốc',3,0,2,'Hết Date','SP12');
/*!40000 ALTER TABLE `KhoHang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NhanVien`
--

DROP TABLE IF EXISTS `NhanVien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NhanVien` (
  `ma_nhan_vien` varchar(50) NOT NULL,
  `ho_ten` varchar(200) NOT NULL,
  `dien_thoai` varchar(50) NOT NULL,
  `dia_chi` varchar(200) DEFAULT NULL,
  `ngay_vao_lam` varchar(200) NOT NULL,
  `chuc_vu` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ma_nhan_vien`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NhanVien`
--

LOCK TABLES `NhanVien` WRITE;
/*!40000 ALTER TABLE `NhanVien` DISABLE KEYS */;
INSERT INTO `NhanVien` VALUES ('NV11','Bùi Nguyễn Minh Anh','090832719','Số 37, Phường 5, Quận 11, TP.HCM','1/7/2009','Nhân viên'),('NV12','Nguyễn Gia  Bảo','033304147','Số 22, Phường 4, Quận 4, TP.HCM','29/6/2016','Nhân viên'),('NV13','Nguyễn Quốc Bảo','097893768','Số 276, Phường 1, Quận 6, TP.HCM','15/5/2022','Nhân viên'),('NV14','Phan Phạm Thế Bảo','093635217','Số 165, Phường 8, Quận 8, TP.HCM','6/7/2006','Quản lý'),('NV15','Đinh Đặng Nguyệt Cát','081817047','Số 135, Phường 5, Quận 9, TP.HCM','1/1/2022','Nhân viên'),('NV16','Trần Chí  Dĩnh','090893690','Số 35, Phường 9, Quận 1, TP.HCM','29/7/2000','Nhân viên'),('NV17','Phạm Quốc Đạt','090485878','Số 36, Phường 7, Quận 5, TP.HCM','17/8/2000','Nhân viên'),('NV18','Châu Đại Đồng','079333655','Số 239, Phường 2, Quận 12, TP.HCM','29/12/2016','Quản lý'),('NV19','Tạ Trương Phú Hải','093113967','Số 196, Phường 9, Quận 7, TP.HCM','4/7/2010','Nhân viên'),('NV20','Nguyễn Ngọc Hân','097797724','Số 190, Phường 8, Quận 3, TP.HCM','12/4/2003','Nhân viên');
/*!40000 ALTER TABLE `NhanVien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SanPham`
--

DROP TABLE IF EXISTS `SanPham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SanPham` (
  `ma_san_pham` varchar(200) NOT NULL,
  `ten_san_pham` varchar(200) NOT NULL,
  `don_vi_tinh` varchar(50) DEFAULT NULL,
  `nuoc_san_xuat` varchar(50) DEFAULT NULL,
  `han_su_dung` int DEFAULT NULL,
  `gia` int NOT NULL,
  PRIMARY KEY (`ma_san_pham`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SanPham`
--

LOCK TABLES `SanPham` WRITE;
/*!40000 ALTER TABLE `SanPham` DISABLE KEYS */;
INSERT INTO `SanPham` VALUES ('SP11','Phân bón NPK 30-10-10 + TE','Bao','Hàn Quốc',3,1000000),('SP12','Phân bón NPK 16-16-8 + TE','Bao','Trung Quốc',3,2000000),('SP13','Phân bón NPK 20-20-15 + TE','Bao','Hàn Quốc',3,3000000),('SP14','Phân bón NPK 12-12-8 + TE','Bao','Nga',3,4000000),('SP15','Phân bón DAP 18-46-0 + TE','Bao','Trung Quốc',3,7000000),('SP16','Phân bón lá Mát cây-Giải độc','Chai','Việt Nam',3,200000),('SP17','Phân bón lá MKP 0-52-34','Chai','Việt Nam',3,400000),('SP18','Phân bón lá Siêu phì trái','Chai','Nga',3,800000),('SP19','Phân bón lá Siêu rửa bông','Chai','Hàn Quốc',3,1200000),('SP20','Phân bón lá Supper Silika','Chai','Nga',3,1400000),('SP21','Phân bón lá Nano Đồng','Chai','Trung Quốc',3,1800000),('SP22','Phân bón lá Thioure 99','Chai','Trung Quốc',3,2400000),('SP23','Phân bón lá Dowin','Chai','Trung Quốc',3,2600000),('SP24','Phân bón lá Đẹp trái','Chai','Việt Nam',3,2800000),('SP25','Phân bón lá Siêu ra rễ','Chai','Trung Quốc',3,3200000);
/*!40000 ALTER TABLE `SanPham` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-01  2:22:06
