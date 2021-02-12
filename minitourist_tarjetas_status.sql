-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: minitourist
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `tarjetas_status`
--

DROP TABLE IF EXISTS `tarjetas_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarjetas_status` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `ciudad` varchar(100) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjetas_status`
--

LOCK TABLES `tarjetas_status` WRITE;
/*!40000 ALTER TABLE `tarjetas_status` DISABLE KEYS */;
INSERT INTO `tarjetas_status` VALUES (1,'11.jpg','Zihuatanejo','Descarga','2020-11-10'),(2,'Coctelito.jpg','Acapulco','Visita','2020-11-10'),(3,'Barra%20Vieja.jpg','Acapulco','Visita','2020-11-10'),(4,'Barra%20Vieja.jpg','Acapulco','Descarga','2020-11-10'),(5,'Beto%C2%B4s.jpg','Acapulco','Visita','2020-11-10'),(6,'3t.jpg','Zihuatanejo','Visita','2020-11-10'),(7,'5.jpg','Zihuatanejo','Visita','2020-11-10'),(8,'Believe.jpg','Acapulco','Visita','2020-11-10'),(9,'Believe.jpg','Acapulco','Descarga','2020-11-10'),(10,'Believe.jpg','Acapulco','Visita','2020-11-13'),(11,'Believe.jpg','Acapulco','Visita','2020-11-17'),(12,'Believe.jpg','Acapulco','Descarga','2020-11-17'),(13,'Believe.jpg','Acapulco','Descarga','2020-11-17'),(14,'Believe.jpg','Acapulco','Descarga','2020-11-17'),(15,'Believe.jpg','Acapulco','Descarga','2020-11-17'),(16,'Believe.jpg','Acapulco','Descarga','2020-11-17'),(17,'Believe.jpg','Acapulco','Descarga','2020-11-17'),(18,'Believe.jpg','Acapulco','Descarga','2020-11-17');
/*!40000 ALTER TABLE `tarjetas_status` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-21 17:29:02
