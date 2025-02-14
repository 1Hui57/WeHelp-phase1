-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'Unique ID',
  `name` varchar(255) NOT NULL COMMENT 'Name',
  `username` varchar(255) NOT NULL COMMENT 'Username',
  `password` varchar(255) NOT NULL COMMENT 'Passsword',
  `follower_count` int unsigned NOT NULL DEFAULT '0' COMMENT 'Follower Count',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',55,'2025-02-11 11:12:30'),(2,'haha','zxc','asd',64,'2025-02-11 11:13:00'),(3,'today','is','Tuesday',502,'2025-02-11 11:13:45'),(4,'Melody','melody888','happy',100,'2025-02-11 11:14:20'),(5,'Sean','sean87','hdjfk',22,'2025-02-11 11:15:00');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'Unique ID',
  `member_id` bigint NOT NULL COMMENT 'Member ID for Message Sender',
  `content` varchar(255) NOT NULL COMMENT 'Content',
  `like_count` int unsigned NOT NULL DEFAULT '0' COMMENT 'Like Count',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,2,'真的好冷',356,'2025-02-11 16:25:57'),(2,3,'虧今天天氣回暖了說',221,'2025-02-11 16:27:25'),(3,1,'測試測試1',555,'2025-02-11 16:14:33'),(4,3,'Yeah, today is my birthday.',22,'2025-02-11 16:14:45'),(5,2,'已購買，孩子很愛吃',999,'2025-02-11 16:15:39'),(6,4,'大家好我是意惠',666,'2025-02-11 16:16:17'),(7,5,'為什麼新買的褲子會越穿越冷？',71,'2025-02-11 16:17:44'),(8,4,'庫子裡面說有松鼠',594522,'2025-02-11 16:18:27'),(9,3,'想要跨步你可以這麼跳~~',8944,'2025-02-11 16:19:16'),(10,5,'因為他買的是冷凍褲',5,'2025-02-11 16:19:54'),(11,1,'我不記得我也有買冷凍褲...',451,'2025-02-11 16:20:29');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-11 18:34:13
