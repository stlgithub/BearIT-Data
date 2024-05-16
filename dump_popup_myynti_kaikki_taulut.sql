-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: popup_myynti
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `asiakas`
--

DROP TABLE IF EXISTS `asiakas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asiakas` (
  `asiakas_id` smallint NOT NULL,
  `puhelinnumero` varchar(10) NOT NULL,
  `sähköposti` varchar(100) NOT NULL,
  `ikä` tinyint DEFAULT NULL,
  `sukupuoli` enum('M','F','O') DEFAULT NULL,
  PRIMARY KEY (`asiakas_id`),
  UNIQUE KEY `Puhelinnumero_UNIQUE` (`puhelinnumero`),
  UNIQUE KEY `Sähköposti_UNIQUE` (`sähköposti`)
  ADD CONSTRAINT check_not_both_null CHECK (`sähköposti` IS NOT NULL OR `puhelinnumero` IS NOT NULL);
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asiakas`
--

LOCK TABLES `asiakas` WRITE;
/*!40000 ALTER TABLE `asiakas` DISABLE KEYS */;
/*!40000 ALTER TABLE `asiakas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myynti`
--

DROP TABLE IF EXISTS `myynti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myynti` (
  `rivi_id` smallint NOT NULL,
  `ostotapahtuma_id` smallint NOT NULL,
  `tuote_id` smallint NOT NULL,
  `asiakas_id` smallint NOT NULL,
  `aika` datetime NOT NULL,
  PRIMARY KEY (`rivi_id`),
  KEY `Asiakas ID_idx` (`asiakas_id`),
  CONSTRAINT `asiakas_id` FOREIGN KEY (`asiakas_id`) REFERENCES `asiakas` (`asiakas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myynti`
--

LOCK TABLES `myynti` WRITE;
/*!40000 ALTER TABLE `myynti` DISABLE KEYS */;
/*!40000 ALTER TABLE `myynti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tuotekategoriat`
--

DROP TABLE IF EXISTS `tuotekategoriat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tuotekategoriat` (
  `kategoria_id` decimal(4,2) NOT NULL,
  `pääkategoria_nimi` varchar(100) NOT NULL,
  `alakategoria_nimi` varchar(100) NOT NULL,
  `alv` decimal(5,2) NOT NULL,
  PRIMARY KEY (`kategoria_id`),
  UNIQUE KEY `alakategoria_nimi` (`alakategoria_nimi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tuotekategoriat`
--

LOCK TABLES `tuotekategoriat` WRITE;
/*!40000 ALTER TABLE `tuotekategoriat` DISABLE KEYS */;
INSERT INTO `tuotekategoriat` VALUES (1.10,'Elintarvikkeet','Kahvit',14.00),(1.20,'Elintarvikkeet','Teet',14.00),(1.30,'Elintarvikkeet','Glögit',14.00),(1.40,'Elintarvikkeet','Suklaat',14.00),(1.50,'Elintarvikkeet','Muut makeiset',14.00),(1.60,'Elintarvikkeet','Piparit',14.00),(1.70,'Elintarvikkeet','Kuivat hedelmät ja pähkinät',14.00),(1.80,'Elintarvikkeet','Lahjakorit',14.00),(2.10,'Koristeet','Joulukuusen koristeet',24.00),(2.20,'Koristeet','Jouluvalot',24.00),(2.30,'Koristeet','Kranssit',24.00),(2.40,'Koristeet','Pöytäkoristeet',24.00),(2.50,'Koristeet','Kynttilät',24.00),(3.10,'Tekstiilit','Tonttulakit',24.00),(3.20,'Tekstiilit','Hiuspannat ja sarvet',24.00),(3.30,'Tekstiilit','Muut asusteet',24.00),(3.40,'Tekstiilit','Joulupukin asut',24.00),(3.50,'Tekstiilit','Kattaustekstiilit',24.00),(4.10,'Paperitavara','Soivat postikortit',24.00),(4.20,'Paperitavara','Tavalliset postikortit',24.00),(4.30,'Paperitavara','Paketointimateriaalit',24.00),(4.40,'Paperitavara','Postimerkit',24.00),(4.50,'Paperitavara','Servetit',24.00);
/*!40000 ALTER TABLE `tuotekategoriat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tuotteet`
--

DROP TABLE IF EXISTS `tuotteet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tuotteet` (
  `kategoria_id` decimal(4,2) NOT NULL,
  `tuote_id` smallint NOT NULL,
  `tuote_nimi` varchar(100) DEFAULT NULL,
  `tukkuhinta` decimal(6,2) NOT NULL,
  `myyntihinta` decimal(6,2) NOT NULL,
  PRIMARY KEY (`tuote_id`),
  UNIQUE KEY `tuote_nimi` (`tuote_nimi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tuotteet`
--

LOCK TABLES `tuotteet` WRITE;
/*!40000 ALTER TABLE `tuotteet` DISABLE KEYS */;
INSERT INTO `tuotteet` VALUES (1.10,1,'Paahtimo K Joulukahvi 250g',2.20,5.99),(1.10,2,'Paahtimo M Jouluinen Kofeiinipommi',5.00,11.99),(1.10,3,'Paahtimo T Joulun Taikakahvi 250g',3.50,8.49),(1.10,4,'Joulukahvisekoitus 500g',4.50,10.99),(1.10,5,'Joulun Aromikahvi 250g',3.00,7.49),(1.20,6,'Joulutee Luomu 50g',1.20,2.99),(1.20,7,'Teelehti K Joulun Taika 100g',1.80,3.99),(1.20,8,'Joulun Hetki Mustikka-vaniljatee',4.50,9.99),(1.20,9,'Joulun Tunnelmatee 100g',2.00,4.99),(1.20,10,'Joulun Glögitee 100g',2.80,6.49),(1.30,11,'Glögiherkku Marrasglögi 500ml',3.00,6.99),(1.30,12,'Jouluglögi Kaneli-Appelsiini 0.75L',4.80,11.49),(1.30,13,'Glögi K Jouluinen Maku 1L',5.00,11.99),(1.30,14,'Glögipullo 1.5L',6.50,14.99),(1.30,15,'Perinteinen Glögi 0.25L',1.80,3.99),(1.40,16,'Joulusuklaalevy Manteli & Appelsiini',3.00,6.99),(1.40,17,'Suklaa T Joulun Taika 100g',1.80,4.49),(1.40,18,'Joulusuklaarasia 250g',3.50,8.99),(1.40,19,'Joulun Herkkusuklaat 150g',2.80,6.99),(1.40,20,'Joulun Valkosuklaa 100g',2.20,5.49),(1.50,21,'Piparikakku 500g',4.50,10.99),(1.50,22,'Joulun Taikapiparit 250g',2.80,6.99),(1.50,23,'Joulun Maustepiparit 250g',3.00,7.49),(1.50,24,'Piparimuffinit Jouluksi 6 kpl',2.00,4.99),(1.50,25,'Suklaiset Piparit 200g',3.00,6.99),(1.60,26,'Joulun Taikapiparkakut 250g',2.00,4.99),(1.60,27,'Piparikranssi 500g',4.50,10.99),(1.60,28,'Joulupiparit Lumihiutaleet 250g',3.00,7.49),(1.60,29,'Joulusydämet 150g',2.50,5.99),(1.60,30,'Glögipiparit 200g',2.20,5.49),(1.70,31,'Kuivatut Jouluhedelmät 250g',3.50,7.99),(1.70,32,'Joulun Pähkinäsekoitus 150g',2.50,5.99),(1.70,33,'Taatelit Jouluiset 500g',4.50,10.99),(1.70,34,'Mantelit Joulun Aikaan 250g',3.00,7.49),(1.70,35,'Joulun Taika -sekoitus 200g',2.80,6.99),(1.80,36,'Jouluinen Herkkukori',12.00,29.99),(1.80,37,'Joulun Makupaketti',10.00,24.99),(1.80,38,'Glögiherkkukori',8.00,19.99),(1.80,39,'Kahvi- ja teepaketti',15.00,34.99),(1.80,40,'Joulun Makeiskori',9.80,22.49),(2.10,41,'Jouluvalot 50 led',5.00,13.99),(2.10,42,'Valosarja Joulun Taika 100 led',8.00,19.99),(2.10,43,'Joulukynttilät 10 kpl',3.00,7.99),(2.10,44,'Led-tähdet 25 kpl',4.50,11.99),(2.10,45,'Joulutähdet Valosarja 5 kpl',2.00,5.99),(2.20,46,'Kranssivalot 100 led',4.50,11.99),(2.20,47,'Jouluvaloketju 250 led',7.00,17.99),(2.20,48,'Kynttilävalot 50 led',5.00,13.99),(2.20,49,'Joulutähtiä Valosarja 25 kpl',3.50,9.99),(2.20,50,'Jouluvalot Jääpuikot 5 kpl',2.50,6.99),(2.30,51,'Ovipöytäkranssi 25 cm',3.00,7.99),(2.30,52,'Mantelikranssi 20 cm',4.00,9.99),(2.30,53,'Kuusenkranssi Luonnonmateriaalit',8.00,19.99),(2.30,54,'Sydänkranssi Pajusta 15 cm',2.50,6.99),(2.30,55,'Joulutähti Kranssi 30 cm',4.50,11.99),(2.40,56,'Joulupöydän Koristekuusi 25 cm',3.00,7.99),(2.40,57,'Pöytäkuusi Joulupallot 15 cm',4.00,9.99),(2.40,58,'Joulukuusenkoristeet 50 kpl',4.50,11.99),(2.40,59,'Joulupöydän Kynttilät 5 kpl',2.50,6.99),(2.40,60,'Joulukoristeet Nalle 3 kpl',3.00,7.99),(2.50,61,'Joulukynttiläsetti 5 kpl',4.00,11.99),(2.50,62,'Kynttilät K Jouluinen Tunnelma 10 kpl',6.00,17.99),(2.50,63,'Joulun Tuoksukynttilät 3 kpl',5.00,13.99),(2.50,64,'Tähtikynttilät 4 kpl',3.50,9.99),(2.50,65,'Joulukynttilät Poro 2 kpl',3.00,8.99),(3.10,66,'Tonttulakki Punainen',2.50,6.99),(3.10,67,'Tonttulakki Vihreä',2.50,6.99),(3.10,68,'Tonttulakki Pikkuväki 1 kpl',4.00,11.99),(3.10,69,'Tonttulakki Vauvoille 1 kpl',2.00,5.99),(3.10,70,'Tonttulakki aikuisille 1 kpl',2.80,7.99),(3.20,71,'Hiuspanta Punainen Joulutähti',3.00,7.99),(3.20,72,'Hiuspanta Hopea',3.00,7.99),(3.20,73,'Sarvet Joulupukille',5.00,12.99),(3.20,74,'Joulusukkahousut ja Hiuspanta',2.50,6.99),(3.20,75,'Tähtipinnit ja Hiuspanta',3.50,8.99),(3.30,76,'Joulun Käsineet Punainen',4.00,10.99),(3.30,77,'Joulutuubit Musta',3.50,8.99),(3.30,78,'Joulusolmio Vihreä',5.00,12.99),(3.30,79,'Joulusukat Valkoinen',3.50,10.99),(3.30,80,'Joulumyssy Ruudullinen',2.80,7.99),(3.40,81,'Joulupukin Asu Deluxe',30.00,99.99),(3.40,82,'Joulupukin Saapas 39-42',18.00,59.99),(3.40,83,'Joulupukin Parta',9.00,29.99),(3.40,84,'Joulupukin Silmälasit',5.00,15.99),(3.40,85,'Joulupukin Käsineet',7.50,24.99),(3.50,86,'Joulupöydän Liina',6.00,19.99),(3.50,87,'Joululiina 120x120 cm',4.80,15.99),(3.50,88,'Jouluservetti 20 kpl',1.50,4.99),(3.50,89,'Joulun Pöytäliina 100x100 cm',3.00,11.99),(3.50,90,'Joulupöytäliina 150x150 cm',4.00,15.99),(4.10,91,'Soiva Joulukortti',3.50,10.99),(4.10,92,'Joulun Tervehdyskortti 5 kpl',2.50,6.99),(4.10,93,'Joulupuu Kortti',3.00,7.99),(4.10,94,'Joulutervehdys Pupu',5.00,12.99),(4.10,95,'Musiikillinen Joulukortti',5.50,13.99),(4.20,96,'Joulun Taika Kortit 5 kpl',3.50,8.99),(4.20,97,'Joulutervehdys Kulkuset 5 kpl',3.50,8.99),(4.20,98,'Joulukortti Paketti 10 kpl',4.80,15.99),(4.20,99,'Tonttupostikortti 5 kpl',2.50,6.99),(4.20,100,'Joulukortti Kultakuvio 5 kpl',3.00,7.99),(4.30,101,'Paketointipaperi Joulun Tunnelma 2m',1.50,3.99),(4.30,102,'Joulupaperi Lahjapaketti 2.5m',1.20,2.99),(4.30,103,'Joulupaperi Kultakuvio 5m',2.50,5.99),(4.30,104,'Lahjapaperi Jouluvaakuna 2m',2.00,4.99),(4.30,105,'Pakettikääre Jouluvalot 3m',2.80,6.99);
/*!40000 ALTER TABLE `tuotteet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'popup_myynti'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-08 11:52:13
