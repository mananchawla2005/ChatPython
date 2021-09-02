-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: chatapp
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

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
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `EVENT_ID` int NOT NULL,
  `TIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `EVENT` varchar(1000) DEFAULT NULL,
  `DESCRIPTION` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES (1,'2021-08-30 16:35:48','SERVER STARTED','Started listening on 0.0.0.0:6000'),(6,'2021-08-30 16:36:02','USER JOINED THE CHAT','manan joined the chat!'),(6,'2021-08-30 16:36:20','USER JOINED THE CHAT','suresh joined the chat!'),(4,'2021-08-30 16:36:37','ADMIN ACTION','suresh was kicked!'),(5,'2021-08-30 16:36:37','USER LEFT THE CHAT','suresh left the chat!'),(6,'2021-08-30 16:37:43','USER JOINED THE CHAT','suresh joined the chat!'),(4,'2021-08-30 16:37:47','ADMIN ACTION','suresh was banned!'),(5,'2021-08-30 16:37:47','USER LEFT THE CHAT','suresh left the chat!'),(6,'2021-08-30 16:38:05','USER JOINED THE CHAT','suresh joined the chat!'),(4,'2021-08-30 16:38:12','ADMIN ACTION','suresh was unbanned!'),(6,'2021-08-30 16:38:30','USER JOINED THE CHAT','suresh joined the chat!'),(5,'2021-08-30 16:40:48','USER LEFT THE CHAT','suresh left the chat!'),(5,'2021-08-30 16:40:48','USER LEFT THE CHAT','manan left the chat!'),(1,'2021-08-30 16:41:07','SERVER STARTED','Started listening on 0.0.0.0:6000'),(6,'2021-08-30 17:07:14','USER JOINED THE CHAT','manan joined the chat!'),(6,'2021-08-30 17:29:15','USER JOINED THE CHAT','suresh joined the chat!'),(4,'2021-08-30 17:29:52','ADMIN ACTION','suresh was banned!'),(5,'2021-08-30 17:29:52','USER LEFT THE CHAT','suresh left the chat!'),(6,'2021-08-30 17:30:44','USER JOINED THE CHAT','suresh joined the chat!'),(5,'2021-08-30 17:30:44','USER LEFT THE CHAT','USER IS BANNED'),(1,'2021-08-31 03:24:38','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:25:20','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:26:01','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:26:29','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:26:59','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:27:55','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:43:33','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:44:24','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:44:50','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:50:36','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:52:11','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:53:17','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:55:05','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:56:37','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:58:25','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:59:04','SERVER STARTED','Started listening on 0.0.0.0:6000'),(1,'2021-08-31 03:59:26','SERVER STARTED','Started listening on 0.0.0.0:6000');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-02 19:11:29
