-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: popup_myynti
-- ------------------------------------------------------
-- Server version	8.0.37

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
  `puhelinnumero` varchar(20) NOT NULL,
  `sähköposti` varchar(100) NOT NULL,
  `ikä` tinyint DEFAULT NULL,
  `sukupuoli` enum('M','F','O') DEFAULT NULL,
  PRIMARY KEY (`asiakas_id`),
  UNIQUE KEY `Puhelinnumero_UNIQUE` (`puhelinnumero`),
  UNIQUE KEY `Sähköposti_UNIQUE` (`sähköposti`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asiakas`
--

LOCK TABLES `asiakas` WRITE;
/*!40000 ALTER TABLE `asiakas` DISABLE KEYS */;
INSERT INTO `asiakas` VALUES (1,'040-1234567','anna.korhonen@example.com',66,'F'),(2,'040-2345678','laura.lehtinen@example.com',45,'F'),(3,'040-3456789','pekka.virtanen@example.com',39,'M'),(4,'040-4567890','matti.makinen@example.com',51,'M'),(5,'040-7890123','sari.hakala@example.com',82,'F'),(6,'040-6789012','mikko.nieminen@example.com',70,'M'),(7,'','katri.heikkila@example.com',27,'F'),(8,'040-8901234','jari.karvonen@example.com',35,'O'),(9,'040-9012345','maria.salminen@example.com',20,'F'),(11,'041-1234567','elina.aho@example.com',78,'F'),(12,'041-2345678','juha.hautala@example.com',43,'M'),(13,'041-3456789','minna.koivisto@example.com',88,'F'),(14,'041-4567890','jukka.savolainen@example.com',24,'M'),(16,'041-5678901','antti.laaksonen@example.com',62,'M'),(17,'041-7890123','heidi.rantanen@example.com',65,'F'),(18,'041-8901234','janne.saarinen@example.com',48,'M'),(19,'041-9012345','tiina.hirvonen@example.com',68,'F'),(20,'041-0123456','',85,'F'),(22,'050-2345678','teemu.oksanen@example.com',58,'M'),(23,'050-3456789','kaisa.kemppainen@example.com',22,'F'),(26,'050-6789012','tommi.tikkanen@example.com',77,'M'),(27,'050-7890123','helena.toivonen@example.com',83,'F'),(29,'050-9012345','marja.liimatainen@example.com',32,'F'),(31,'044-1234567','anja.kaasalainen@example.com',52,'M'),(32,'044-2345678','tuomas.valtonen@example.com',18,'O'),(35,'044-5678901','kirsi.hanninen@example.com',84,'F'),(38,'044-8901234','kai.manninen@example.com',28,'M'),(39,'044-9012345','aino.heinonen@example.com',38,'O'),(40,'044-0123456','marko.vuorinen@example.com',67,'M'),(41,'045-1234567','anu.ahola@example.com',21,'F'),(43,'045-3456789','lauri.rasanen@example.com',34,'M'),(45,'045-5678901','seppo.miettinen@example.com',61,'M'),(46,'045-6789012','anneli.hakala@example.com',60,'F'),(48,'045-8901234','merja.hakala@example.com',79,'F'),(49,'045-9012345','harri.virtanen@example.com',50,'M'),(50,'045-0123456','emilia.savolainen@example.com',89,'F'),(52,'046-2345678','hanna.koskinen@example.com',69,'F'),(53,'046-3456789','pasi.lahti@example.com',53,'M'),(54,'046-4567890','sini.heikkinen@example.com',25,'O'),(56,'046-6789012','auli.virtanen@example.com',30,'F'),(58,'046-8901234','minna.turunen@example.com',86,'F'),(59,'046-9012345','arto.sorjonen@example.com',40,'M'),(60,'046-0123456','kaisa.ojala@example.com',37,'F'),(61,'049-1234567','timo.kuusisto@example.com',75,'M'),(62,'049-2345678','katja.nurmi@example.com',41,'F'),(64,'049-4567890','juha.tamminen@example.com',42,'M'),(65,'049-5678901','marja.pulkkanen@example.com',44,'F'),(67,'049-7890123','paivi.saarinen@example.com',64,'F'),(69,'049-9012345','jaana.heiskanen@example.com',59,'F'),(70,'049-8901234','jukka.lehmusvuori@example.com',74,'M'),(71,'041-1234560','anna.makela@example.com',81,'F'),(76,'041-6789010','tommi.laaksonen@example.com',32,'M'),(77,'041-7890120','susanna.salo@example.com',61,'F'),(78,'041-8901230','teppo.lahti@example.com',24,'M'),(79,'041-9012340','tuula.harkonen@example.com',89,'F'),(80,'041-0123450','olli.timonen@example.com',43,'M'),(81,'050-3456780','sini.kaarna@example.com',65,'F'),(82,'050-2345670','markus.kuusela@example.com',83,'M'),(84,'050-4567890','hannu.tervonen@example.com',59,'M'),(85,'050-5678900','anneli.vaaranen@example.com',55,'F'),(86,'050-6789010','mika.tapanainen@example.com',78,'M'),(87,'050-7890120','maarit.lampinen@example.com',27,'F'),(89,'050-9012340','timo.korpi@example.com',68,'M'),(90,'050-0123450','paula.valimaki@example.com',87,'F'),(91,'044-1234560','jari.koponen@example.com',52,'M'),(92,'044-2345670','sanna.saari@example.com',60,'F'),(93,'044-3456780','heikki.makinen@example.com',88,'M'),(95,'044-5678900','pekka.lahti@example.com',44,'M'),(97,'044-6789010','hannu.ylitalo@example.com',79,'M'),(98,'044-8901230','kaisa.hietala@example.com',57,'F'),(99,'044-9012340','jari.pitkanen@example.com',63,'O'),(100,'040-4481216','sari.leppanen@example.com',77,'F'),(101,'046-5678901','matti.manninen@example.com',45,'M'),(105,'045-7890123','elina.laakso@example.com',25,'O'),(107,'041-2345670','minna.heikkinen@example.com',71,'F'),(109,'044-0123450','maija.rantala@example.com',62,'F'),(110,'050-1234560','markku.kemppainen@example.com',35,'M'),(112,'044-7890123','teppo.saarinen@example.com',74,'M'),(115,'050-5678901','auli.nieminen@example.com',53,'F'),(117,'044-4567890','hanna.tiainen@example.com',31,'F'),(119,'046-7890123','paivi.rahkonen@example.com',33,'F'),(120,'044-1337420','lauri.koski@example.com',85,'M'),(122,'040-5678901','pekka.heinonen@example.com',37,'M'),(123,'040-0123456','anna.hietala@example.com',73,'F'),(125,'049-3456789','marja.savolainen@example.com',56,'F'),(127,'044-120437','kati.lehtonen@example.com',70,'O'),(128,'041-6789012','juho.koskinen@example.com',76,'M'),(129,'049-0123456','tiina.makinen@example.com',51,'F'),(132,'045-254754','markku.saarinen@example.com',66,'M'),(133,'041-5678900','minna.salmela@example.com',34,'O'),(136,'046-1234567','pasi.ahola@example.com',30,'M'),(137,'045-1998542','elina.saarinen@example.com',84,'F'),(138,'044-7890120','janne.virtanen@example.com',72,'M'),(139,'049-6789012','katri.hakala@example.com',23,'F'),(140,'050-0123456','maria.koivisto@example.com',29,'F');
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
  KEY `tuotteet_idx` (`tuote_id`),
  CONSTRAINT `asiakas_id` FOREIGN KEY (`asiakas_id`) REFERENCES `asiakas` (`asiakas_id`),
  CONSTRAINT `tuote_id` FOREIGN KEY (`tuote_id`) REFERENCES `tuotteet` (`tuote_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tuotteet`
--

LOCK TABLES `tuotteet` WRITE;
/*!40000 ALTER TABLE `tuotteet` DISABLE KEYS */;
INSERT INTO `tuotteet` VALUES (1.10,1,'Paahtimo K Joulukahvi 250g',2.20,5.99),(1.10,2,'Paahtimo M Jouluinen Kofeiinipommi',5.00,11.99),(1.10,3,'Paahtimo T Joulun Taikakahvi 250g',3.50,8.49),(1.10,4,'Joulukahvisekoitus 500g',4.50,10.99),(1.10,5,'Joulun Aromikahvi 250g',3.00,7.49),(1.20,6,'Joulutee Luomu 50g',1.20,2.99),(1.20,7,'Teelehti K Joulun Taika 100g',1.80,3.99),(1.20,8,'Joulun Hetki Mustikka-vaniljatee',4.50,9.99),(1.20,9,'Joulun Tunnelmatee 100g',2.00,4.99),(1.20,10,'Joulun Glögitee 100g',2.80,6.49),(1.30,11,'Glögiherkku Marrasglögi 500ml',3.00,6.99),(1.30,12,'Jouluglögi Kaneli-Appelsiini 0.75L',4.80,11.49),(1.30,13,'Glögi K Jouluinen Maku 1L',5.00,11.99),(1.30,14,'Glögipullo 1.5L',6.50,14.99),(1.30,15,'Perinteinen Glögi 0.25L',1.80,3.99),(1.40,16,'Joulusuklaalevy Manteli & Appelsiini',3.00,6.99),(1.40,17,'Suklaa T Joulun Taika 100g',1.80,4.49),(1.40,18,'Joulusuklaarasia 250g',3.50,8.99),(1.40,19,'Joulun Herkkusuklaat 150g',2.80,6.99),(1.40,20,'Joulun Valkosuklaa 100g',2.20,5.49),(1.50,21,'Piparikakku 500g',4.50,10.99),(1.50,22,'Joulun Taikapiparit 250g',2.80,6.99),(1.50,23,'Joulun Maustepiparit 250g',3.00,7.49),(1.50,24,'Piparimuffinit Jouluksi 6 kpl',2.00,4.99),(1.50,25,'Suklaiset Piparit 200g',3.00,6.99),(1.60,26,'Joulun Taikapiparkakut 250g',2.00,4.99),(1.60,27,'Piparikranssi 500g',4.50,10.99),(1.60,28,'Joulupiparit Lumihiutaleet 250g',3.00,7.49),(1.60,29,'Joulusydämet 150g',2.50,5.99),(1.60,30,'Glögipiparit 200g',2.20,5.49),(1.70,31,'Kuivatut Jouluhedelmät 250g',3.50,7.99),(1.70,32,'Joulun Pähkinäsekoitus 150g',2.50,5.99),(1.70,33,'Taatelit Jouluiset 500g',4.50,10.99),(1.70,34,'Mantelit Joulun Aikaan 250g',3.00,7.49),(1.70,35,'Joulun Taika -sekoitus 200g',2.80,6.99),(1.80,36,'Jouluinen Herkkukori',12.00,29.99),(1.80,37,'Joulun Makupaketti',10.00,24.99),(1.80,38,'Glögiherkkukori',8.00,19.99),(1.80,39,'Kahvi- ja teepaketti',15.00,34.99),(1.80,40,'Joulun Makeiskori',9.80,22.49),(2.10,41,'Jouluvalot 50 led',5.00,13.99),(2.10,42,'Valosarja Joulun Taika 100 led',8.00,19.99),(2.10,43,'Joulukynttilät 10 kpl',3.00,7.99),(2.10,44,'Led-tähdet 25 kpl',4.50,11.99),(2.10,45,'Joulutähdet Valosarja 5 kpl',2.00,5.99),(2.20,46,'Kranssivalot 100 led',4.50,11.99),(2.20,47,'Jouluvaloketju 250 led',7.00,17.99),(2.20,48,'Kynttilävalot 50 led',5.00,13.99),(2.20,49,'Joulutähtiä Valosarja 25 kpl',3.50,9.99),(2.20,50,'Jouluvalot Jääpuikot 5 kpl',2.50,6.99),(2.30,51,'Ovipöytäkranssi 25 cm',3.00,7.99),(2.30,52,'Mantelikranssi 20 cm',4.00,9.99),(2.30,53,'Kuusenkranssi Luonnonmateriaalit',8.00,19.99),(2.30,54,'Sydänkranssi Pajusta 15 cm',2.50,6.99),(2.30,55,'Joulutähti Kranssi 30 cm',4.50,11.99),(2.40,56,'Joulupöydän Koristekuusi 25 cm',3.00,7.99),(2.40,57,'Pöytäkuusi Joulupallot 15 cm',4.00,9.99),(2.40,58,'Joulukuusenkoristeet 50 kpl',4.50,11.99),(2.40,59,'Joulupöydän Kynttilät 5 kpl',2.50,6.99),(2.40,60,'Joulukoristeet Nalle 3 kpl',3.00,7.99),(2.50,61,'Joulukynttiläsetti 5 kpl',4.00,11.99),(2.50,62,'Kynttilät K Jouluinen Tunnelma 10 kpl',6.00,17.99),(2.50,63,'Joulun Tuoksukynttilät 3 kpl',5.00,13.99),(2.50,64,'Tähtikynttilät 4 kpl',3.50,9.99),(2.50,65,'Joulukynttilät Poro 2 kpl',3.00,8.99),(3.10,66,'Tonttulakki Punainen',2.50,6.99),(3.10,67,'Tonttulakki Vihreä',2.50,6.99),(3.10,68,'Tonttulakki Pikkuväki 1 kpl',4.00,11.99),(3.10,69,'Tonttulakki Vauvoille 1 kpl',2.00,5.99),(3.10,70,'Tonttulakki aikuisille 1 kpl',2.80,7.99),(3.20,71,'Hiuspanta Punainen Joulutähti',3.00,7.99),(3.20,72,'Hiuspanta Hopea',3.00,7.99),(3.20,73,'Sarvet Joulupukille',5.00,12.99),(3.20,74,'Joulusukkahousut ja Hiuspanta',2.50,6.99),(3.20,75,'Tähtipinnit ja Hiuspanta',3.50,8.99),(3.30,76,'Joulun Käsineet Punainen',4.00,10.99),(3.30,77,'Joulutuubit Musta',3.50,8.99),(3.30,78,'Joulusolmio Vihreä',5.00,12.99),(3.30,79,'Joulusukat Valkoinen',3.50,10.99),(3.30,80,'Joulumyssy Ruudullinen',2.80,7.99),(3.40,81,'Joulupukin Asu Deluxe',30.00,99.99),(3.40,82,'Joulupukin Saapas 39-42',18.00,59.99),(3.40,83,'Joulupukin Parta',9.00,29.99),(3.40,84,'Joulupukin Silmälasit',5.00,15.99),(3.40,85,'Joulupukin Käsineet',7.50,24.99),(3.50,86,'Joulupöydän Liina',6.00,19.99),(3.50,87,'Joululiina 120x120 cm',4.80,15.99),(3.50,88,'Jouluservetti 20 kpl',1.50,4.99),(3.50,89,'Joulun Pöytäliina 100x100 cm',3.00,11.99),(3.50,90,'Joulupöytäliina 150x150 cm',4.00,15.99),(4.10,91,'Soiva Joulukortti',3.50,10.99),(4.10,92,'Joulun Tervehdyskortti 5 kpl',2.50,6.99),(4.10,93,'Joulupuu Kortti',3.00,7.99),(4.10,94,'Joulutervehdys Pupu',5.00,12.99),(4.10,95,'Musiikillinen Joulukortti',5.50,13.99),(4.20,96,'Joulun Taika Kortit 5 kpl',3.50,8.99),(4.20,97,'Joulutervehdys Kulkuset 5 kpl',3.50,8.99),(4.20,98,'Joulukortti Paketti 10 kpl',4.80,15.99),(4.20,99,'Tonttupostikortti 5 kpl',2.50,6.99),(4.20,100,'Joulukortti Kultakuvio 5 kpl',3.00,7.99),(4.30,101,'Paketointipaperi Joulun Tunnelma 2m',1.50,3.99),(4.30,102,'Joulupaperi Lahjapaketti 2.5m',1.20,2.99),(4.30,103,'Joulupaperi Kultakuvio 5m',2.50,5.99),(4.30,104,'Lahjapaperi Jouluvaakuna 2m',2.00,4.99),(4.30,105,'Pakettikääre Jouluvalot 3m',2.80,6.99);
/*!40000 ALTER TABLE `tuotteet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-17  9:28:33
