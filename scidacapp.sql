-- MySQL dump 10.13  Distrib 8.0.42, for Linux (x86_64)
--
-- Host: localhost    Database: scidacapp
-- ------------------------------------------------------
-- Server version	8.0.42-0ubuntu0.24.10.1

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
-- Current Database: `scidacapp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `scidacapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `scidacapp`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add todo',1,'add_todo'),(2,'Can change todo',1,'change_todo'),(3,'Can delete todo',1,'delete_todo'),(4,'Can view todo',1,'view_todo'),(5,'Can add foto profile',2,'add_fotoprofile'),(6,'Can change foto profile',2,'change_fotoprofile'),(7,'Can delete foto profile',2,'delete_fotoprofile'),(8,'Can view foto profile',2,'view_fotoprofile'),(9,'Can add log entry',3,'add_logentry'),(10,'Can change log entry',3,'change_logentry'),(11,'Can delete log entry',3,'delete_logentry'),(12,'Can view log entry',3,'view_logentry'),(13,'Can add permission',4,'add_permission'),(14,'Can change permission',4,'change_permission'),(15,'Can delete permission',4,'delete_permission'),(16,'Can view permission',4,'view_permission'),(17,'Can add group',5,'add_group'),(18,'Can change group',5,'change_group'),(19,'Can delete group',5,'delete_group'),(20,'Can view group',5,'view_group'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add content type',7,'add_contenttype'),(26,'Can change content type',7,'change_contenttype'),(27,'Can delete content type',7,'delete_contenttype'),(28,'Can view content type',7,'view_contenttype'),(29,'Can add session',8,'add_session'),(30,'Can change session',8,'change_session'),(31,'Can delete session',8,'delete_session'),(32,'Can view session',8,'view_session'),(33,'Can add blacklisted token',9,'add_blacklistedtoken'),(34,'Can change blacklisted token',9,'change_blacklistedtoken'),(35,'Can delete blacklisted token',9,'delete_blacklistedtoken'),(36,'Can view blacklisted token',9,'view_blacklistedtoken'),(37,'Can add outstanding token',10,'add_outstandingtoken'),(38,'Can change outstanding token',10,'change_outstandingtoken'),(39,'Can delete outstanding token',10,'delete_outstandingtoken'),(40,'Can view outstanding token',10,'view_outstandingtoken'),(41,'Can add Token',11,'add_token'),(42,'Can change Token',11,'change_token'),(43,'Can delete Token',11,'delete_token'),(44,'Can view Token',11,'view_token'),(45,'Can add Token',12,'add_tokenproxy'),(46,'Can change Token',12,'change_tokenproxy'),(47,'Can delete Token',12,'delete_tokenproxy'),(48,'Can view Token',12,'view_tokenproxy'),(49,'Can add profile',13,'add_profile'),(50,'Can change profile',13,'change_profile'),(51,'Can delete profile',13,'delete_profile'),(52,'Can view profile',13,'view_profile'),(53,'Can add study session',14,'add_studysession'),(54,'Can change study session',14,'change_studysession'),(55,'Can delete study session',14,'delete_studysession'),(56,'Can view study session',14,'view_studysession'),(57,'Can add study capsule',15,'add_studycapsule'),(58,'Can change study capsule',15,'change_studycapsule'),(59,'Can delete study capsule',15,'delete_studycapsule'),(60,'Can view study capsule',15,'view_studycapsule'),(61,'Can add capsule',16,'add_capsule'),(62,'Can change capsule',16,'change_capsule'),(63,'Can delete capsule',16,'delete_capsule'),(64,'Can view capsule',16,'view_capsule'),(65,'Can add study capsule',17,'add_studycapsule'),(66,'Can change study capsule',17,'change_studycapsule'),(67,'Can delete study capsule',17,'delete_studycapsule'),(68,'Can view study capsule',17,'view_studycapsule'),(69,'Can add study session',18,'add_studysession'),(70,'Can change study session',18,'change_studysession'),(71,'Can delete study session',18,'delete_studysession'),(72,'Can view study session',18,'view_studysession');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1000000$vSlpKn0k27f4PYIwnrCECK$EtIu6lMoJACJ8ognIYfbJu0f5x/gYal4HGkNQFkAUTk=','2025-06-10 03:14:16.806943',1,'yahya','','','yahya@gmail.com',1,1,'2025-03-06 04:29:39.334639'),(2,'pbkdf2_sha256$870000$tfgnYPhVdG6IpEADPyQccL$vD5lWsiGhE8+NmYX/TmiszEBkeTuLYgWTOCeJvNPsJA=','2025-03-07 08:04:27.670184',0,'user1','','','user1@g.com',0,1,'2025-03-06 04:36:03.819459'),(3,'pbkdf2_sha256$870000$kY7DE0aSdv6ivqAeeJ5mNY$XaugX0FYCMFiedwR51eFLKlXcV6OL8G6mA+lsSQftJw=','2025-03-15 15:42:14.418621',0,'mobile','','','mobile1@gmail.com',0,1,'2025-03-13 09:58:25.822609'),(4,'pbkdf2_sha256$870000$jFGgMRqGZQqqAS2PTTh6s2$Y76xUQCIkOPHWkqTTjORLEgH71yF2Ed6lBMBAJoeA5U=','2025-03-17 16:05:10.304284',0,'mobile2','','','M@g.com',0,1,'2025-03-17 16:04:29.985641'),(5,'pbkdf2_sha256$870000$PDTUrhyqRvsOnTO8SBLgIU$bltaga27oqZZvdX+q2Wg7vNbgKkpdUb0m8af8/DLjlM=',NULL,0,'mobile3','','','M@g.com',0,1,'2025-03-17 16:08:39.699324'),(6,'pbkdf2_sha256$870000$yDqKMgX7zkfLFxf1axGlKo$uYPAJYg1/ecjHz/3hm2CgFTZmJYsn4bjMZ1KFKle9/Y=','2025-04-09 05:48:07.292695',0,'dimas12','','','d@gmail.com',0,1,'2025-04-09 05:47:32.961328'),(7,'pbkdf2_sha256$870000$ZC9YF4pzajyz3RAuWvc7Z9$fn5MI1U3xCyA+JXNYgwQQKdeRdDCLXck0fkp2VnX5kg=',NULL,0,'user4','','','user4@gmail.com',0,1,'2025-04-09 11:39:59.716873'),(8,'pbkdf2_sha256$870000$QXP8Nb814Um2jXAnuaek7z$MXrgvAEhzrInaxPkIJvLYDjt+mS5LRX+NLfEkYdgxlQ=',NULL,0,'U8','','','U8@gmail.com',0,1,'2025-04-10 03:12:26.071087'),(9,'pbkdf2_sha256$1000000$Nz2qJCNgetsAyCaa4WRNlL$YqDTH2Z9R28l83U6l3nSgAkvMZTh5rlFLg/TOVpbyus=','2025-05-28 14:18:59.626158',0,'test','','','test@gmail.com',0,1,'2025-05-28 13:21:47.997733'),(10,'pbkdf2_sha256$1000000$k9n1HaDzJXuw9p0CG0RpHv$SSutM0KGMhwiUo6ReGp6rSuwz/YhCoYUSz8nuw9LRKA=',NULL,0,'nirwana','','','nirwana@g.com',0,1,'2025-06-08 04:43:35.848359');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cache`
--

DROP TABLE IF EXISTS `cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cache` (
  `key` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `value` mediumtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expiration` int NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cache`
--

LOCK TABLES `cache` WRITE;
/*!40000 ALTER TABLE `cache` DISABLE KEYS */;
/*!40000 ALTER TABLE `cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cache_locks`
--

DROP TABLE IF EXISTS `cache_locks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cache_locks` (
  `key` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `owner` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expiration` int NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cache_locks`
--

LOCK TABLES `cache_locks` WRITE;
/*!40000 ALTER TABLE `cache_locks` DISABLE KEYS */;
/*!40000 ALTER TABLE `cache_locks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capsule_capsule`
--

DROP TABLE IF EXISTS `capsule_capsule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capsule_capsule` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `topic` varchar(255) NOT NULL,
  `question` longtext NOT NULL,
  `correct_answer` varchar(255) NOT NULL,
  `user_answer` varchar(255) DEFAULT NULL,
  `is_correct` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capsule_capsule_user_id_d9e5636c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `capsule_capsule_user_id_d9e5636c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capsule_capsule`
--

LOCK TABLES `capsule_capsule` WRITE;
/*!40000 ALTER TABLE `capsule_capsule` DISABLE KEYS */;
/*!40000 ALTER TABLE `capsule_capsule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capsule_studycapsule`
--

DROP TABLE IF EXISTS `capsule_studycapsule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capsule_studycapsule` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `topic` varchar(255) NOT NULL,
  `question` longtext NOT NULL,
  `correct_answer` longtext,
  `user_answer` varchar(255) DEFAULT NULL,
  `is_correct` tinyint(1) NOT NULL,
  `unlock_next_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `capsule_studycapsule_user_id_5bfed1d8_fk_auth_user_id` (`user_id`),
  CONSTRAINT `capsule_studycapsule_user_id_5bfed1d8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capsule_studycapsule`
--

LOCK TABLES `capsule_studycapsule` WRITE;
/*!40000 ALTER TABLE `capsule_studycapsule` DISABLE KEYS */;
INSERT INTO `capsule_studycapsule` VALUES (1,'shalat','Apa saja rukun-rukun wajib dalam shalat?','Rukun-rukun wajib dalam shalat ada 4, yaitu:',NULL,0,NULL,'2025-06-04 08:00:46.938876',1),(2,'ada 4 ','Apa yang ada 4 musim di belahan bumi utara?','Tahun. Karena dalam satu tahun, ada 4 musim, yaitu semi, panas, gugur, dan dingin.','tahun',1,'2025-06-05 08:13:38.175373','2025-06-04 08:01:24.996073',1);
/*!40000 ALTER TABLE `capsule_studycapsule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capsule_studysession`
--

DROP TABLE IF EXISTS `capsule_studysession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capsule_studysession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) NOT NULL,
  `topic` varchar(200) NOT NULL,
  `duration_minutes` int NOT NULL,
  `completed` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capsule_studysession_user_id_ab225083_fk_auth_user_id` (`user_id`),
  CONSTRAINT `capsule_studysession_user_id_ab225083_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capsule_studysession`
--

LOCK TABLES `capsule_studysession` WRITE;
/*!40000 ALTER TABLE `capsule_studysession` DISABLE KEYS */;
/*!40000 ALTER TABLE `capsule_studysession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (3,'admin','logentry'),(5,'auth','group'),(4,'auth','permission'),(6,'auth','user'),(11,'authtoken','token'),(12,'authtoken','tokenproxy'),(17,'capsule','studycapsule'),(18,'capsule','studysession'),(7,'contenttypes','contenttype'),(2,'myapp','fotoprofile'),(13,'myapp','profile'),(1,'myapp','todo'),(8,'sessions','session'),(16,'study','capsule'),(15,'study','studycapsule'),(14,'study','studysession'),(9,'token_blacklist','blacklistedtoken'),(10,'token_blacklist','outstandingtoken');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-03-06 04:24:56.640187'),(2,'auth','0001_initial','2025-03-06 04:24:57.133696'),(3,'admin','0001_initial','2025-03-06 04:24:57.266153'),(4,'admin','0002_logentry_remove_auto_add','2025-03-06 04:24:57.278611'),(5,'admin','0003_logentry_add_action_flag_choices','2025-03-06 04:24:57.292065'),(6,'contenttypes','0002_remove_content_type_name','2025-03-06 04:24:57.402056'),(7,'auth','0002_alter_permission_name_max_length','2025-03-06 04:24:57.464214'),(8,'auth','0003_alter_user_email_max_length','2025-03-06 04:24:57.496981'),(9,'auth','0004_alter_user_username_opts','2025-03-06 04:24:57.513361'),(10,'auth','0005_alter_user_last_login_null','2025-03-06 04:24:57.586227'),(11,'auth','0006_require_contenttypes_0002','2025-03-06 04:24:57.590081'),(12,'auth','0007_alter_validators_add_error_messages','2025-03-06 04:24:57.602777'),(13,'auth','0008_alter_user_username_max_length','2025-03-06 04:24:57.679414'),(14,'auth','0009_alter_user_last_name_max_length','2025-03-06 04:24:57.752998'),(15,'auth','0010_alter_group_name_max_length','2025-03-06 04:24:57.780256'),(16,'auth','0011_update_proxy_permissions','2025-03-06 04:24:57.797306'),(17,'auth','0012_alter_user_first_name_max_length','2025-03-06 04:24:57.873412'),(18,'myapp','0001_initial','2025-03-06 04:24:57.895870'),(19,'myapp','0002_fotoprofle','2025-03-06 04:24:57.986441'),(20,'myapp','0003_alter_fotoprofle_gambar_profile','2025-03-06 04:24:58.035606'),(21,'myapp','0004_fotoprofile_delete_fotoprofle','2025-03-06 04:24:58.125646'),(22,'myapp','0005_alter_fotoprofile_gambar_profile','2025-03-06 04:24:58.139085'),(23,'sessions','0001_initial','2025-03-06 04:24:58.181388'),(24,'token_blacklist','0001_initial','2025-03-16 02:06:31.371897'),(25,'token_blacklist','0002_outstandingtoken_jti_hex','2025-03-16 02:06:31.429634'),(26,'token_blacklist','0003_auto_20171017_2007','2025-03-16 02:06:31.456768'),(27,'token_blacklist','0004_auto_20171017_2013','2025-03-16 02:06:31.543938'),(28,'token_blacklist','0005_remove_outstandingtoken_jti','2025-03-16 02:06:31.604354'),(29,'token_blacklist','0006_auto_20171017_2113','2025-03-16 02:06:31.641253'),(30,'token_blacklist','0007_auto_20171017_2214','2025-03-16 02:06:31.835705'),(31,'token_blacklist','0008_migrate_to_bigautofield','2025-03-16 02:06:32.069093'),(32,'token_blacklist','0010_fix_migrate_to_bigautofield','2025-03-16 02:06:32.090226'),(33,'token_blacklist','0011_linearizes_history','2025-03-16 02:06:32.093710'),(34,'token_blacklist','0012_alter_outstandingtoken_user','2025-03-16 02:06:32.111206'),(35,'authtoken','0001_initial','2025-03-16 02:10:16.951445'),(36,'authtoken','0002_auto_20160226_1747','2025-03-16 02:10:16.999940'),(37,'authtoken','0003_tokenproxy','2025-03-16 02:10:17.006346'),(38,'authtoken','0004_alter_tokenproxy_options','2025-03-16 02:10:17.017728'),(39,'myapp','0006_profile','2025-05-18 15:13:41.277719'),(40,'myapp','0007_delete_fotoprofile','2025-05-28 04:57:47.939485'),(41,'myapp','0008_profile_nama_lengkap','2025-05-28 09:35:01.492512'),(43,'myapp','0009_profile_total_points','2025-06-01 08:41:31.018169'),(47,'myapp','0010_rename_total_points_profile_points','2025-06-03 04:58:31.029853'),(50,'capsule','0001_initial','2025-06-04 07:57:38.956319');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9bi1ksjzlev56dvto7flfx8j0hi6tsfw','.eJxVjDkOwjAUBe_iGlnE9o8dSvqcIfqbSQDZUpYKcXeIlALaNzPvZQbc1nHYFp2HSczFNOb0uxHyQ8sO5I7lVi3Xss4T2V2xB11sX0Wf18P9OxhxGb91Tg1HzBw0dSitJ8qkwTkggtgmB8itOgV0IUsQEPBMzkPEM3DuvHl_ABCBOME:1u0Elg:W9JiUekE4qkxjILlbmqBLTz5CUdWr4mZheD7zZcD5Zk','2025-04-17 07:13:40.221816'),('f9z0l69vp31ht8859jhbucwcxoctv5ar','.eJxVjDsOwjAQBe_iGlm2s_5R0nMGa9fe4ABypDipEHeHSCmgfTPzXiLhtta0dV7SVMRZaHH63Qjzg9sOyh3bbZZ5busykdwVedAur3Ph5-Vw_w4q9vqtmbwHIIc2DhGQnVIBdAwYIgzOIIfAEbJ3mbVFZ7XKQATgx5GMsVq8P8W3NyE:1uNk65:Ulc2AQ9_SPwqttMj-YTbEZPNuWbdIsEVN8IOh3-BfSo','2025-06-21 03:19:53.847612'),('s105n67s21vmkfvtezzywm2voumf33ty','.eJxVjLEOwjAMRP8lM4ocsGnKyM43RHackAJKpaadEP9OK3WA7XTv3b1N4GUuYWlpCoOai0Fz-O2E4zPVDeiD6320cazzNIjdFLvTZm-jptd1d_8OCreyroEzCRJr6gg8g8uQIXbMnhHJK8oRcqJEvZMezyoxnzw6H0loTdF8vve6OFw:1tuCxi:N3skv5ISxNLYAJSGSFvJG3q2tybT6ogLGPmNZZ14xsk','2025-03-31 16:05:10.311110'),('tgcu17er79qsvbi5m060irfy1fr0cp59','.eJxVjDkOwjAUBe_iGlnE9o8dSvqcIfqbSQDZUpYKcXeIlALaNzPvZQbc1nHYFp2HSczFNOb0uxHyQ8sO5I7lVi3Xss4T2V2xB11sX0Wf18P9OxhxGb91Tg1HzBw0dSitJ8qkwTkggtgmB8itOgV0IUsQEPBMzkPEM3DuvHl_ABCBOME:1ttdAs:okncPBDEmD8Wj9HnGaPTAJvHQexqrYPejwdXCizm5uI','2025-03-30 01:52:22.362068'),('w3xrxqa532bw48178apk20vugkvyh4ir','.eJxVjDsOwjAQBe_iGlm2s_5R0nMGa9fe4ABypDipEHeHSCmgfTPzXiLhtta0dV7SVMRZaHH63Qjzg9sOyh3bbZZ5busykdwVedAur3Ph5-Vw_w4q9vqtmbwHIIc2DhGQnVIBdAwYIgzOIIfAEbJ3mbVFZ7XKQATgx5GMsVq8P8W3NyE:1u6Oe9:BOrTWxJeMC_Dlpsw6PcAyV3CT-gP8XmJvtpWbgee2H4','2025-05-04 06:59:21.396916'),('xcwug0izq1m7ia4tuk5ryaapykpoojv8','.eJxVjDsOwjAQBe_iGlm2s_5R0nMGa9fe4ABypDipEHeHSCmgfTPzXiLhtta0dV7SVMRZaHH63Qjzg9sOyh3bbZZ5busykdwVedAur3Ph5-Vw_w4q9vqtmbwHIIc2DhGQnVIBdAwYIgzOIIfAEbJ3mbVFZ7XKQATgx5GMsVq8P8W3NyE:1uOpRI:-BKH13niIISS8E8eG8HAEHmvTKMYhuiw381MoufNGF0','2025-06-24 03:14:16.811029');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `failed_jobs`
--

DROP TABLE IF EXISTS `failed_jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `failed_jobs` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `failed_jobs`
--

LOCK TABLES `failed_jobs` WRITE;
/*!40000 ALTER TABLE `failed_jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `failed_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_batches`
--

DROP TABLE IF EXISTS `job_batches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_batches` (
  `id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `total_jobs` int NOT NULL,
  `pending_jobs` int NOT NULL,
  `failed_jobs` int NOT NULL,
  `failed_job_ids` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `options` mediumtext COLLATE utf8mb4_unicode_ci,
  `cancelled_at` int DEFAULT NULL,
  `created_at` int NOT NULL,
  `finished_at` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_batches`
--

LOCK TABLES `job_batches` WRITE;
/*!40000 ALTER TABLE `job_batches` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_batches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `queue` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `attempts` tinyint unsigned NOT NULL,
  `reserved_at` int unsigned DEFAULT NULL,
  `available_at` int unsigned NOT NULL,
  `created_at` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_queue_index` (`queue`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrations`
--

DROP TABLE IF EXISTS `migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `migrations` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrations`
--

LOCK TABLES `migrations` WRITE;
/*!40000 ALTER TABLE `migrations` DISABLE KEYS */;
INSERT INTO `migrations` VALUES (1,'0001_01_01_000000_create_users_table',1),(2,'0001_01_01_000001_create_cache_table',1),(3,'0001_01_01_000002_create_jobs_table',1),(4,'2025_04_12_032340_add_username_to_users_table',2),(5,'2025_04_12_033259_change_name_column_to_username_in_users_table',3);
/*!40000 ALTER TABLE `migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_profile`
--

DROP TABLE IF EXISTS `myapp_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `hp` varchar(15) DEFAULT NULL,
  `alamat` longtext,
  `gender` varchar(10) NOT NULL,
  `profile_picture` varchar(100) NOT NULL,
  `user_id` int NOT NULL,
  `nama_lengkap` varchar(100) DEFAULT NULL,
  `points` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `myapp_profile_user_id_9fe34268_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_profile_points_6cc3e9ec_check` CHECK ((`points` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_profile`
--

LOCK TABLES `myapp_profile` WRITE;
/*!40000 ALTER TABLE `myapp_profile` DISABLE KEYS */;
INSERT INTO `myapp_profile` VALUES (1,'081259993397','Jln Dirgahayu 5','Laki-laki','profile_pictures/aku.jpg',1,'Muhammad Yahya Abdullahissalam',70),(2,'12345678910','jln testing developer','Laki-laki','profile_pictures/terminal.jpg',9,'testing',0);
/*!40000 ALTER TABLE `myapp_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_todo`
--

DROP TABLE IF EXISTS `myapp_todo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_todo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `task` varchar(255) NOT NULL,
  `completed` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_todo`
--

LOCK TABLES `myapp_todo` WRITE;
/*!40000 ALTER TABLE `myapp_todo` DISABLE KEYS */;
INSERT INTO `myapp_todo` VALUES (2,'mobileapp',0,'2025-03-07 08:01:12.512166');
/*!40000 ALTER TABLE `myapp_todo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `password_reset_tokens`
--

DROP TABLE IF EXISTS `password_reset_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `password_reset_tokens` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `password_reset_tokens`
--

LOCK TABLES `password_reset_tokens` WRITE;
/*!40000 ALTER TABLE `password_reset_tokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `password_reset_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessions`
--

DROP TABLE IF EXISTS `sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sessions` (
  `id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` bigint unsigned DEFAULT NULL,
  `ip_address` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_agent` text COLLATE utf8mb4_unicode_ci,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_activity` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sessions_user_id_index` (`user_id`),
  KEY `sessions_last_activity_index` (`last_activity`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessions`
--

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `study_studycapsule`
--

DROP TABLE IF EXISTS `study_studycapsule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `study_studycapsule` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `correct_answer` longtext,
  `created_at` datetime(6) NOT NULL,
  `is_correct` tinyint(1) NOT NULL,
  `question` longtext NOT NULL DEFAULT (_utf8mb4'Pertanyaan akan dihasilkan oleh AI'),
  `topic` varchar(255) NOT NULL,
  `unlock_next_at` datetime(6) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `user_answer` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `study_studycapsule_user_id_2d3ad88c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `study_studycapsule_user_id_2d3ad88c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `study_studycapsule`
--

LOCK TABLES `study_studycapsule` WRITE;
/*!40000 ALTER TABLE `study_studycapsule` DISABLE KEYS */;
INSERT INTO `study_studycapsule` VALUES (1,'****','2025-06-02 11:16:48.815407',0,'****','rukun islam',NULL,1,NULL),(2,'###','2025-06-02 11:32:17.614237',0,'###','rukun iman',NULL,1,''),(3,'Persegi memiliki sifat-sifat:','2025-06-02 11:36:29.169412',0,'Apa saja sifat-sifat utama dari bangun datar persegi?','persegi',NULL,1,''),(4,'Persegi adalah bangun geometri dua dimensi (bangun datar) yang memiliki empat sisi sama panjang dan empat sudut yang semuanya berupa sudut siku-siku.','2025-06-02 11:41:59.513754',1,'Apa yang dimaksud dengan persegi?','persegi','2025-06-03 11:45:07.914528',1,'Persegi adalah bangun geometri dua dimensi (bangun datar) yang memiliki empat sisi sama panjang dan empat sudut yang semuanya berupa sudut siku-siku.'),(5,'Jawaban:\n**Template Inheritance** memungkinkan pembuatan struktur HTML dasar (seperti header, footer) yang kemudian dapat diwarisi dan diisi konten dinamis oleh halaman-halaman spesifik tanpa harus menulis ulang kode HTML dasar secara berulang. **Model-Admin** memberikan antarmuka otomatis untuk manajemen data model aplikasi secara langsung dari basis data, sangat membantu dalam pengembangan awal atau fitur admin sederhana. Namun, keunggulan **ORM (Object-Relational Mapper)** yang memungkinkan interaksi dengan basis data melalui Python objects tanpa perlu menulis query SQL secara langsung, juga menjadi tulang punggung dalam pengembangan aplikasi Django dengan mengotomatisasi manipulasi data.','2025-06-02 13:14:40.373856',0,'Pertanyaan: \nApa keunggulan utama dari menggunakan framework Django untuk pengembangan web?','django',NULL,1,'Dalam Islam, rukun iman adalah enam pokok keyakinan yang wajib diyakini oleh setiap Muslim. '),(6,'Rukun iman adalah lima pokok keyakinan atau asas kepercayaan yang harus diyakini dan diamalkan oleh seorang muslim. Kelima rukun iman itu sebagai berikut:','2025-06-03 02:05:42.823787',0,'Apa itu rukun iman dalam Islam dan sebutkan kelima rukun iman tersebut beserta penjelasannya secara singkat?','rukun iman',NULL,1,NULL),(7,'Jawaban:\nDalam Islam, rukun iman adalah enam pokok keyakinan yang wajib diyakini oleh setiap Muslim. Enam rukun iman tersebut adalah:\n\n1.  **Iman Kepada Allah (ALLAH SWT):** Yaitu berkeyakinan dan meyakini sepenuh hati akan keberadaan Allah SWT sebagai Dzat yang menciptakan, menguasai, menentukan takdir, dan Esa tanpa bersekutu. Ia Maha Suci, Maha Mendengar, Maha Melihat, Maha Mengetahui segala yang ada di alam semesta.\n\n2.  **Iman Kepada Al-Quran:** Yaitu berkeyakinan dan menerima Al-Quran sebagai wahyu Allah SWT yang sempurna, Kitab suci agung bagi kaum Muslimin, dan merupakan kata-kata Allah yang dalam bahasa Arab yang tidak dapat dimengerti atau dirubah maknanya meski dipermudah dengan tafsir. Ia diyakini dibawah otoritas Allah dan Rasul-Nya.\n\n3.  **Iman Kepada Para Malaikat:** Yaitu berkeyakinan dan menerima keberadaan para Malaikat, makhluk Allah yang diciptakan dari cahaya untuk menunaikan perintah Allah SWT. Malaikat tidak memiliki bentuk fisik, tidak berguna untuk menikmati makanan dan minuman, serta tidak mempunyai istri atau keturunan. Contohnya adalah malaikat Jibril (A.S.), Mikail (A.S.), Israfil (A.S.), Izrail (A.S.), dll.\n\n4.  **Iman Kepada Para Rasul:** Yaitu berkeyakinan dan menerima keberadaan semua Rasul (Nabi) yang diutus Allah SWT kepada umat manusia, baik itu Nabi Adam (A.S.), Nabi Nuh (Nuh A.S.), Nabi Ibrahim (A.S.), Nabi Muhammad (Muhammad SAW), dan para Nabi, Rasul, dan Prophet lainnya. Mereka adalah manusia yang dipilih Allah untuk menjadi panutan dengan menyampaikan risalah dan wahyu-Nya. Rasul Muhammad SAW adalah Rasul terakhir.\n\n5.  **Iman Kepada Al-Kitab:** Yaitu berkeyakinan dan menerima kitab-kitab suci Allah SWT yang diturunkan sebelum Al-Quran, seperti Kitab Taurat bagi Bani Israil (yang kini tidak tersisa secara lengkap), Kitab Zabur (Kitab Makkari/Himpunan Lagu-Lagu), Kitab Injil (Al-Filun), dan Kitab ini diyakini Allah menggariskan ajaran agama sebelumnya, meskipun memiliki perbedaan tertentu di akhir zaman. Kitab-kitab ini juga diyakini Allah akan mengembalikan ke bentuk aslinya di akhir zaman.\n\n6.  **Iman Kepada Hari Akhir (HARIBAKTAS):** Yaitu berkeyakinan dan meyakini akan keberadaan hari kiamat, kebangkitan bagi semua manusia dari kubur (fitrah insaniyah), dibukanya buku amal (hasil kemurahan dan kejahatan seseorang), perhitungan amal perbuatan, penilaian oleh Allah SWT, azab neraka bagi orang kafir, dan surga yang penuh berkah bagi orang mukmin.\n\nMelalui rukun iman ini, seorang Muslim membangun pondasi keyakinannya dalam menjalankan ibadah dan hidup dalam pedoman agama Islam.','2025-06-03 02:05:49.212825',0,'Pertanyaan:\nApa saja rukun iman dalam Islam dan apa makna setiap rukun tersebut?','rukun iman',NULL,1,'iman kepada allah, malaikat, kitab, rasul dan hari kiamat serta iman kepada qadha dan qadar'),(8,'Jawaban:\nYa, jagalan masih sangat berhubungan dengan dunia rukun islam. Meskipun teknologi modern seperti telepon genggam dan internet marak, jagalan sebenarnya juga termasuk dalam ragam rukun islam yang sering dilupakan umat muslim. Di jagalan, warga tetap menjalankan rukun islam seperti sholat di mesjid, puasa saat ramadhan, dan lain sebagainya. Meski berbeda teknologinya, jiwa spiritual mereka dalam menerapkan rukun islam sudah mendekati tujuh rukun islam. Tips: Bila ingin menjalankan jagalan saat sedang beribadah atau melakukan aktivitasmu sendiri, seperti menerapkan puasa hanya dengan menahan makan dan minum dalam bulan sithiyah, maka akan lebih mudah.','2025-06-03 03:00:16.419716',0,'Oke, inilah pertanyaan dan jawaban tentang rukun Islam dengan format seperti diminta:\n\nPertanyaan:\nApakah jagalan berhubungan dengan dunia rukun islam?','rukun islam',NULL,1,'iya'),(9,'Wudhu adalah ritual mencuci sebagian anggota badan dengan menggunakan air yang bertujuan untuk membersihkan diri sebelum melakukan ibadah seperti sholat. Umumnya, wudhu dilakukan dengan mencuci muka, kedua tangan sampai siku, menyeluruh kedua kaki sampai lutut, lalu mengusap kepala dan badan.','2025-06-03 03:04:37.067015',1,'Apa itu wudhu?','wudhu','2025-06-04 04:14:44.947401',1,'Wudhu adalah ritual mencuci sebagian anggota badan dengan menggunakan air yang bertujuan untuk membersihkan diri sebelum melakukan ibadah seperti sholat'),(10,'Ya, puasa Ramadan adalah salah satu dari rukun islam yang wajib dilakukan setiap muslim pada bulan Ramadan.','2025-06-03 07:35:19.683816',1,'Apakah puasa termasuk rukun islam?','rukun islam','2025-06-04 07:41:05.522607',1,'iya puasa termasuk rukun islam '),(11,'****','2025-06-03 07:41:43.604826',1,'****','asmaul husna','2025-06-04 07:43:00.162711',1,'nama-tag { properti: nilai; }. Misalnya: h1 { color: blue; }'),(12,'Format menulis rule dasar dalam CSS adalah nama-tag { properti: nilai; }. Misalnya: h1 { color: blue; }','2025-06-03 07:42:17.715496',1,'Mana yang merupakan format menulis rule dasar dalam CSS?','css','2025-06-04 08:00:17.121608',1,'nama-tag { properti: nilai; }. Misalnya: h1 { color: blue; }'),(13,'Segitiga','2025-06-03 08:02:55.031365',1,'Nama bangun datar yang memiliki tiga sisi adalah?','segitiga','2025-06-04 08:04:15.421108',1,'segitiga');
/*!40000 ALTER TABLE `study_studycapsule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `study_studysession`
--

DROP TABLE IF EXISTS `study_studysession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `study_studysession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) NOT NULL,
  `topic` varchar(200) NOT NULL,
  `duration_minutes` int NOT NULL,
  `completed` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `study_studysession_user_id_475f228d_fk_auth_user_id` (`user_id`),
  CONSTRAINT `study_studysession_user_id_475f228d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `study_studysession`
--

LOCK TABLES `study_studysession` WRITE;
/*!40000 ALTER TABLE `study_studysession` DISABLE KEYS */;
INSERT INTO `study_studysession` VALUES (3,'d','e',3,1,'2025-05-30 14:04:07.365657',1);
/*!40000 ALTER TABLE `study_studysession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--

DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

LOCK TABLES `token_blacklist_blacklistedtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_outstandingtoken`
--

DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  `jti` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outs_user_id_83bc629a_fk_auth_user` (`user_id`),
  CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

LOCK TABLES `token_blacklist_outstandingtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`),
  UNIQUE KEY `users_username_unique` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'yahya','y@gmail.com',NULL,'$2y$12$EFDHSiq/j6LXN6eBr.NPtO4h/eXOsGYBth6hNMg4j0i2blDKwf5Tq',NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-11 16:20:43
