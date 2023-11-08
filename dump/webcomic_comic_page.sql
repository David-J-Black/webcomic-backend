-- MySQL dump 10.13  Distrib 8.0.34, for macos13 (arm64)
--
-- Host: localhost    Database: webcomic
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `comic_page`
--

DROP TABLE IF EXISTS `comic_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comic_page` (
  `page_id` int NOT NULL AUTO_INCREMENT,
  `chapter_id` int NOT NULL,
  `page_number` int DEFAULT NULL,
  `release_date` date NOT NULL,
  `description` text,
  `page_position` varchar(1) DEFAULT NULL,
  `image_name` varchar(30) DEFAULT NULL COMMENT 'name of the image in the pages folder',
  `status` varchar(1) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`page_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comic_page`
--

LOCK TABLES `comic_page` WRITE;
/*!40000 ALTER TABLE `comic_page` DISABLE KEYS */;
INSERT INTO `comic_page` VALUES (1,1,1,'2023-08-05','Welcome to the first page of the comic!\nI hope you enjoy reading it a fraction of as much as I enjoyed writing it.','R','Looking For Darwin_001.png','A','2023-08-06 05:00:49','2023-09-05 05:08:50'),(3,1,2,'2023-08-05',NULL,'L','Looking For Darwin_002.png','A','2023-08-06 06:12:39','2023-08-24 05:41:48'),(5,1,3,'2023-08-05',NULL,'R','Looking For Darwin_003.png','A','2023-08-06 06:14:43','2023-08-24 05:41:48'),(7,1,4,'2023-08-05',NULL,'L','Looking For Darwin_004.png','A','2023-08-06 06:16:06','2023-08-24 05:41:48'),(8,1,5,'2023-08-05',NULL,'R','Looking For Darwin_005.png','A','2023-08-06 06:17:45','2023-08-24 05:41:48'),(9,1,6,'2023-08-06',NULL,'L','Looking For Darwin_006.png','A','2023-08-06 07:37:56','2023-08-24 05:41:48'),(10,1,7,'2023-08-06',NULL,'R','Looking For Darwin_007.png','A','2023-08-06 07:37:56','2023-08-24 05:41:48'),(11,1,8,'2023-08-06',NULL,'L','Looking For Darwin_008.png','A','2023-08-06 07:37:56','2023-08-24 05:41:48'),(12,1,9,'2023-08-06',NULL,'R','Looking For Darwin_009.png','A','2023-08-06 07:37:56','2023-08-24 05:41:48'),(13,1,10,'2023-08-06',NULL,'L','Looking For Darwin_010.png','A','2023-08-06 07:37:56','2023-08-24 05:43:40'),(14,1,11,'2023-08-23',NULL,'R','Looking For Darwin_011.png','A','2023-08-24 05:43:33','2023-08-24 05:43:38'),(15,1,12,'2023-08-23',NULL,'L','Looking For Darwin_012.png','A','2023-08-24 05:43:33','2023-08-24 06:09:29'),(16,1,13,'2023-08-23',NULL,'R','Looking For Darwin_013.png','A','2023-08-24 05:43:33','2023-08-24 06:09:29'),(17,1,14,'2023-08-23',NULL,'L','Looking For Darwin_014.png','A','2023-08-24 05:43:33','2023-08-24 06:10:02'),(18,1,15,'2023-08-23',NULL,'R','Looking For Darwin_015.png','A','2023-08-24 05:43:33','2023-08-24 06:10:20'),(19,1,16,'2023-08-23',NULL,'L','Looking For Darwin_016.png','A','2023-08-24 05:43:33','2023-08-24 06:10:26'),(20,1,17,'2023-08-23',NULL,'R','Looking For Darwin_017.png','A','2023-08-24 05:43:33','2023-08-24 06:10:26'),(21,1,18,'2023-08-23',NULL,'L','Looking For Darwin_018.png','A','2023-08-24 05:43:33','2023-08-24 06:14:01'),(22,1,19,'2023-08-23',NULL,'R','Looking For Darwin_019.png','A','2023-08-24 05:43:33','2023-08-24 06:14:01'),(23,1,20,'2023-08-23',NULL,'L','Looking For Darwin_020.png','A','2023-08-24 05:43:33','2023-08-24 06:14:01'),(24,2,1,'2023-08-23',NULL,'R','Looking For Darwin_022.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(25,2,2,'2023-08-23',NULL,'L','Looking For Darwin_023.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(26,2,3,'2023-08-23',NULL,'R','Looking For Darwin_024.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(27,2,4,'2023-08-23',NULL,'L','Looking For Darwin_025.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(28,2,5,'2023-08-23',NULL,'R','Looking For Darwin_026.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(29,2,6,'2023-08-23',NULL,'L','Looking For Darwin_027.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(30,2,7,'2023-08-23',NULL,'R','Looking For Darwin_028.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(31,2,8,'2023-08-23',NULL,'L','Looking For Darwin_029.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(32,2,9,'2023-08-23',NULL,'R','Looking For Darwin_030.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(33,2,10,'2023-08-23',NULL,'L','Looking For Darwin_031.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(34,2,11,'2023-08-23',NULL,'R','Looking For Darwin_032.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(35,2,12,'2023-08-23',NULL,'L','Looking For Darwin_033.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(36,2,13,'2023-08-23',NULL,'R','Looking For Darwin_034.png','A','2023-08-24 05:43:33','2023-08-24 06:18:45'),(37,2,14,'2023-08-23',NULL,'L','Looking For Darwin_035.png','I','2023-08-24 05:43:33','2023-08-24 06:27:35'),(38,2,15,'2023-08-23',NULL,'L','Looking For Darwin_036.png','I','2023-08-24 05:43:33','2023-08-24 06:27:35'),(39,1,21,'2023-08-23',NULL,'L','Looking For Darwin_021.png','A','2023-08-24 06:17:21','2023-08-24 06:17:22');
/*!40000 ALTER TABLE `comic_page` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-06 23:22:28
