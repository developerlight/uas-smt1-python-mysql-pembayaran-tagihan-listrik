# ************************************************************
# Antares - SQL Client
# Version 0.6.0
# 
# https://antares-sql.app/
# https://github.com/antares-sql/antares
# 
# Host: 127.0.0.1 (MySQL Community Server - GPL 8.0.31)
# Database: db_pln
# Generation time: 2023-01-11T14:13:39+07:00
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table tb_jenisdaya
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tb_jenisdaya`;

CREATE TABLE `tb_jenisdaya` (
  `kd_daya` int NOT NULL AUTO_INCREMENT,
  `daya` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `harga` int NOT NULL,
  PRIMARY KEY (`kd_daya`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `tb_jenisdaya` WRITE;
/*!40000 ALTER TABLE `tb_jenisdaya` DISABLE KEYS */;

INSERT INTO `tb_jenisdaya` (`kd_daya`, `daya`, `harga`) VALUES
	(1, "R1/TR 900 VA", 1352),
	(2, "R1/TR 1300 VA", 1444),
	(3, "R1/TR 2200 VA", 1444),
	(4, "R2/TR 3500 VA", 1699),
	(5, "R3/TR 6600 VA", 1699),
	(6, "B2/TR 6600 VA", 1444),
	(7, "P1/TR 6600 VA", 1699);

/*!40000 ALTER TABLE `tb_jenisdaya` ENABLE KEYS */;
UNLOCK TABLES;



# Dump of table tb_pelanggan
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tb_pelanggan`;

CREATE TABLE `tb_pelanggan` (
  `id_pelanggan` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `kd_daya` int NOT NULL,
  PRIMARY KEY (`id_pelanggan`),
  KEY `fk_kd_daya` (`kd_daya`),
  CONSTRAINT `fk_kd_daya` FOREIGN KEY (`kd_daya`) REFERENCES `tb_jenisdaya` (`kd_daya`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `tb_pelanggan` WRITE;
/*!40000 ALTER TABLE `tb_pelanggan` DISABLE KEYS */;

INSERT INTO `tb_pelanggan` (`id_pelanggan`, `nama`, `kd_daya`) VALUES
	(26, "wer", 2),
	(27, "lucky", 3),
	(28, "reyhan", 3),
	(29, "dun", 3),
	(30, "wahyu", 2),
	(31, "wahyu", 2),
	(32, "wahyu", 2),
	(33, "pelanggan 1", 5);

/*!40000 ALTER TABLE `tb_pelanggan` ENABLE KEYS */;
UNLOCK TABLES;



# Dump of table tb_transaksi
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tb_transaksi`;

CREATE TABLE `tb_transaksi` (
  `id_transaksi` int NOT NULL AUTO_INCREMENT,
  `tanggal` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `kwh` int NOT NULL,
  `total_harga` int NOT NULL,
  `status` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'BELUM LUNAS',
  `id_pelanggan` int NOT NULL,
  PRIMARY KEY (`id_transaksi`),
  KEY `fk_id_pelanggan` (`id_pelanggan`),
  CONSTRAINT `fk_id_pelanggan` FOREIGN KEY (`id_pelanggan`) REFERENCES `tb_pelanggan` (`id_pelanggan`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `tb_transaksi` WRITE;
/*!40000 ALTER TABLE `tb_transaksi` DISABLE KEYS */;

INSERT INTO `tb_transaksi` (`id_transaksi`, `tanggal`, `kwh`, `total_harga`, `status`, `id_pelanggan`) VALUES
	(6, "2022-12-20", 12, 1444, "LUNAS", 26),
	(7, "2022-12-20", 31, 1444, "LUNAS", 27),
	(8, "2022-12-23", 54, 1444, "BELUM LUNAS", 28),
	(9, "2022-12-24", 21, 30324, "LUNAS", 29),
	(10, "2022-12-24", 1, 1444, "BELUM LUNAS", 31),
	(11, "2022-12-24", 1, 1444, "BELUM LUNAS", 32),
	(12, "2022-12-27", 65, 110435, "BELUM LUNAS", 33);

/*!40000 ALTER TABLE `tb_transaksi` ENABLE KEYS */;
UNLOCK TABLES;



# Dump of views
# ------------------------------------------------------------

# Creating temporary tables to overcome VIEW dependency errors


/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

# Dump completed on 2023-01-11T14:13:39+07:00
