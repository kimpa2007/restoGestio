-- MySQL dump 10.14  Distrib 5.5.37-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: tpvP
-- ------------------------------------------------------
-- Server version	5.5.37-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `SEQUENCE`
--

DROP TABLE IF EXISTS `SEQUENCE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEQUENCE` (
  `SEQ_NAME` varchar(50) NOT NULL,
  `SEQ_COUNT` decimal(38,0) DEFAULT NULL,
  PRIMARY KEY (`SEQ_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEQUENCE`
--

LOCK TABLES `SEQUENCE` WRITE;
/*!40000 ALTER TABLE `SEQUENCE` DISABLE KEYS */;
INSERT INTO `SEQUENCE` VALUES ('SEQ_GEN',9450);
/*!40000 ALTER TABLE `SEQUENCE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add opcio',7,'add_opcio'),(20,'Can change opcio',7,'change_opcio'),(21,'Can delete opcio',7,'delete_opcio'),(22,'Can add categoria',8,'add_categoria'),(23,'Can change categoria',8,'change_categoria'),(24,'Can delete categoria',8,'delete_categoria'),(25,'Can add producte',9,'add_producte'),(26,'Can change producte',9,'change_producte'),(27,'Can delete producte',9,'delete_producte'),(28,'Can add usuari',10,'add_usuari'),(29,'Can change usuari',10,'change_usuari'),(30,'Can delete usuari',10,'delete_usuari'),(31,'Can add moment apat',11,'add_momentapat'),(32,'Can change moment apat',11,'change_momentapat'),(33,'Can delete moment apat',11,'delete_momentapat'),(34,'Can add taula',12,'add_taula'),(35,'Can change taula',12,'change_taula'),(36,'Can delete taula',12,'delete_taula'),(37,'Can add comanda',13,'add_comanda'),(38,'Can change comanda',13,'change_comanda'),(39,'Can delete comanda',13,'delete_comanda'),(40,'Can add linia comanda',14,'add_liniacomanda'),(41,'Can change linia comanda',14,'change_liniacomanda'),(42,'Can delete linia comanda',14,'delete_liniacomanda');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(150) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9366 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$7fYPdEaXq2KL$KsTyIHO91sP0iqy4h5+m2uBBA+J8i5jx3vfqnjSmhOw=','2014-06-04 19:45:24',1,'kimpa2007','','','',1,1,'2014-06-03 14:12:58');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comanda_comanda`
--

DROP TABLE IF EXISTS `comanda_comanda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comanda_comanda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuari_id` int(11) NOT NULL,
  `taula_id` int(11) NOT NULL,
  `dataHora` datetime NOT NULL,
  `metodePagament` varchar(255) DEFAULT NULL,
  `estat` varchar(255) NOT NULL,
  `total` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `comanda_comanda_cb138487` (`usuari_id`),
  KEY `comanda_comanda_7ead8759` (`taula_id`),
  CONSTRAINT `taula_id_refs_id_f937c998` FOREIGN KEY (`taula_id`) REFERENCES `comanda_taula` (`id`),
  CONSTRAINT `usuari_id_refs_id_3cc449d3` FOREIGN KEY (`usuari_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9436 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comanda_comanda`
--

LOCK TABLES `comanda_comanda` WRITE;
/*!40000 ALTER TABLE `comanda_comanda` DISABLE KEYS */;
/*!40000 ALTER TABLE `comanda_comanda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comanda_liniacomanda`
--

DROP TABLE IF EXISTS `comanda_liniacomanda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comanda_liniacomanda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comanda_id` int(11) NOT NULL,
  `producte_id` int(11) NOT NULL,
  `total` double DEFAULT NULL,
  `commentari` longtext,
  `opcio` varchar(200) DEFAULT NULL,
  `momentApat_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comanda_liniacomanda_55620e10` (`comanda_id`),
  KEY `comanda_liniacomanda_47e0e7b3` (`producte_id`),
  KEY `comanda_liniacomanda_96193b62` (`momentApat_id`),
  CONSTRAINT `comanda_id_refs_id_3e4d607d` FOREIGN KEY (`comanda_id`) REFERENCES `comanda_comanda` (`id`),
  CONSTRAINT `momentApat_id_refs_id_670cd490` FOREIGN KEY (`momentApat_id`) REFERENCES `comanda_momentapat` (`id`),
  CONSTRAINT `producte_id_refs_id_d7105a0b` FOREIGN KEY (`producte_id`) REFERENCES `productes_producte` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9444 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comanda_liniacomanda`
--

LOCK TABLES `comanda_liniacomanda` WRITE;
/*!40000 ALTER TABLE `comanda_liniacomanda` DISABLE KEYS */;
/*!40000 ALTER TABLE `comanda_liniacomanda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comanda_momentapat`
--

DROP TABLE IF EXISTS `comanda_momentapat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comanda_momentapat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcio` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comanda_momentapat`
--

LOCK TABLES `comanda_momentapat` WRITE;
/*!40000 ALTER TABLE `comanda_momentapat` DISABLE KEYS */;
INSERT INTO `comanda_momentapat` VALUES (1,'Primer'),(2,'Segon'),(3,'Postre'),(4,'Café'),(5,'QuanSigui');
/*!40000 ALTER TABLE `comanda_momentapat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comanda_taula`
--

DROP TABLE IF EXISTS `comanda_taula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comanda_taula` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `capacitat` int(11) NOT NULL,
  `estat` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comanda_taula`
--

LOCK TABLES `comanda_taula` WRITE;
/*!40000 ALTER TABLE `comanda_taula` DISABLE KEYS */;
INSERT INTO `comanda_taula` VALUES (1,6,'ocupada'),(2,4,'ocupada'),(3,6,'ocupada'),(4,4,'ocupada'),(5,4,'ocupada'),(6,4,'ocupada'),(7,4,'ocupada'),(8,4,'ocupada'),(9,4,'disponible'),(10,4,'disponible'),(11,4,'disponible'),(12,4,'disponible'),(13,8,'disponible'),(14,6,'disponible');
/*!40000 ALTER TABLE `comanda_taula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-06-03 14:18:59',1,8,'1','Aperitiu',1,''),(2,'2014-06-03 14:19:15',1,8,'2','Entrants',1,''),(3,'2014-06-03 14:19:31',1,7,'1','amanida',1,''),(4,'2014-06-03 14:19:36',1,7,'2','patates',1,''),(5,'2014-06-03 14:19:39',1,7,'3','mongetes',1,''),(6,'2014-06-03 14:19:41',1,8,'3','Carns',1,''),(7,'2014-06-03 14:19:52',1,8,'4','Postres',1,''),(8,'2014-06-03 14:19:59',1,7,'4','sucre',1,''),(9,'2014-06-03 14:20:05',1,7,'5','sacarina',1,''),(10,'2014-06-03 14:20:08',1,7,'6','res',1,''),(11,'2014-06-03 14:20:13',1,8,'5','Cafés',1,''),(12,'2014-06-03 14:20:28',1,8,'6','Alcohols',1,''),(13,'2014-06-03 14:20:43',1,8,'6','Cerveses',2,'Modificat categoria i imatge.'),(14,'2014-06-03 14:21:00',1,8,'7','Aigües',1,''),(15,'2014-06-03 14:21:10',1,8,'8','Vins',1,''),(16,'2014-06-03 14:21:25',1,8,'9','Varis',1,''),(17,'2014-06-03 14:21:41',1,9,'1','Olives',1,''),(18,'2014-06-03 14:22:05',1,9,'2','Berberetxos',1,''),(19,'2014-06-03 14:22:18',1,9,'3','Chips',1,''),(20,'2014-06-03 14:22:35',1,9,'4','Amanida Verda',1,''),(21,'2014-06-03 14:22:42',1,9,'5','Cargols ',1,''),(22,'2014-06-03 14:22:50',1,9,'6','Espàrrecs maionesa',1,''),(23,'2014-06-03 14:23:09',1,9,'7','Torrades Anxoves',1,''),(24,'2014-06-03 14:23:23',1,9,'8','Esc',1,''),(25,'2014-06-03 14:23:31',1,9,'8','Escalivada',2,'Modificat producte i preu.'),(26,'2014-06-03 14:23:39',1,9,'9','Embotits',1,''),(27,'2014-06-03 14:23:50',1,9,'10','Paté al pebre',1,''),(28,'2014-06-03 14:23:55',1,9,'11','Xai',1,''),(29,'2014-06-03 14:24:00',1,9,'12','Entrecot',1,''),(30,'2014-06-03 14:24:07',1,9,'13','Cansalada',1,''),(31,'2014-06-03 14:24:22',1,9,'14','Botifarra',1,''),(32,'2014-06-03 14:24:34',1,9,'15','Pollastre',1,''),(33,'2014-06-03 14:24:43',1,9,'16','Bistec',1,''),(34,'2014-06-03 14:25:01',1,9,'16','Bistec',2,'Modificat preu.'),(35,'2014-06-03 14:25:15',1,9,'17','Graellada de carn',1,''),(36,'2014-06-03 14:25:25',1,9,'18','Tiramisu',1,''),(37,'2014-06-03 14:25:33',1,9,'19','Flam',1,''),(38,'2014-06-03 14:25:40',1,9,'20','Crema Catalana',1,''),(39,'2014-06-03 14:25:47',1,9,'21','Pastis de formatge',1,''),(40,'2014-06-03 14:25:59',1,9,'22','Gelat d\'aigua',1,''),(41,'2014-06-03 14:26:14',1,9,'23','Mousse de xocolata',1,''),(42,'2014-06-03 14:26:22',1,9,'24','Coulant de xocolata',1,''),(43,'2014-06-03 14:26:43',1,9,'25','Io',1,''),(44,'2014-06-03 14:26:52',1,9,'25','Iogurt',2,'Modificat producte i preu.'),(45,'2014-06-03 14:27:03',1,9,'26','Café ',1,''),(46,'2014-06-03 14:27:10',1,9,'27','Tallat',1,''),(47,'2014-06-03 14:27:20',1,9,'28','Café amb llet',1,''),(48,'2014-06-03 14:27:32',1,9,'29','Café irlandés',1,''),(49,'2014-06-03 14:27:45',1,9,'30','Cigaló',1,''),(50,'2014-06-03 14:27:53',1,9,'27','Tallat',2,'Modificat categoria.'),(51,'2014-06-03 14:28:06',1,9,'31','Mit',1,''),(52,'2014-06-03 14:28:15',1,9,'31','Mitjana Voll Damm',2,'Modificat producte i preu.'),(53,'2014-06-03 14:28:29',1,9,'32','Mitjana San Miquel',1,''),(54,'2014-06-03 14:28:40',1,9,'33','Mitjana Estrella',1,''),(55,'2014-06-03 14:28:49',1,9,'34','Vichy 1L',1,''),(56,'2014-06-03 14:29:03',1,9,'35','Aigua 1L',1,''),(57,'2014-06-03 14:29:10',1,9,'36','Gasosa 1L',1,''),(58,'2014-06-03 14:29:23',1,9,'37','3 Fincas ',1,''),(59,'2014-06-03 14:29:36',1,9,'38','3/8 3Fincas',1,''),(60,'2014-06-03 14:29:49',1,9,'39','1L Casa',1,''),(61,'2014-06-03 14:29:56',1,9,'40','1/2 Casa',1,''),(62,'2014-06-03 14:30:08',1,9,'41','1/4 Casa',1,''),(63,'2014-06-03 14:30:18',1,9,'42','Cava Peralada Brut',1,''),(64,'2014-06-03 14:30:34',1,9,'43','Alioli',1,''),(65,'2014-06-03 14:30:44',1,12,'1','Taula object',1,''),(66,'2014-06-03 14:30:46',1,12,'2','Taula object',1,''),(67,'2014-06-03 14:30:47',1,12,'3','Taula object',1,''),(68,'2014-06-03 14:30:49',1,12,'4','Taula object',1,''),(69,'2014-06-03 14:30:50',1,12,'5','Taula object',1,''),(70,'2014-06-03 14:30:51',1,12,'6','Taula object',1,''),(71,'2014-06-03 14:30:53',1,12,'7','Taula object',1,''),(72,'2014-06-03 14:30:54',1,12,'8','Taula object',1,''),(73,'2014-06-03 14:30:55',1,12,'9','Taula object',1,''),(74,'2014-06-03 14:30:56',1,12,'10','Taula object',1,''),(75,'2014-06-03 14:30:58',1,12,'11','Taula object',1,''),(76,'2014-06-03 14:30:59',1,12,'12','Taula object',1,''),(77,'2014-06-03 14:31:00',1,12,'13','Taula object',1,''),(78,'2014-06-03 14:31:02',1,12,'14','Taula object',1,''),(79,'2014-06-03 14:31:26',1,11,'1','MomentApat object',1,''),(80,'2014-06-03 14:31:29',1,11,'2','MomentApat object',1,''),(81,'2014-06-03 14:31:32',1,11,'3','MomentApat object',1,''),(82,'2014-06-03 14:31:40',1,11,'4','MomentApat object',1,''),(83,'2014-06-04 17:03:27',1,13,'8167','LuisGarcía',2,'Modificat estat i total.'),(84,'2014-06-04 17:45:00',1,13,'9392','ÒscarLópez',2,'Modificat estat i total.'),(85,'2014-06-04 17:45:44',1,13,'9329','Òscar',2,'Modificat estat i total.'),(86,'2014-06-04 19:58:33',1,13,'9380','ÒscarLópez',2,'Modificat estat.'),(87,'2014-06-04 19:58:39',1,13,'9135','Oleguer',2,'Modificat estat.'),(88,'2014-06-04 19:58:45',1,13,'8916','MiguelÁngel',2,'Modificat estat i total.'),(89,'2014-06-04 19:58:51',1,13,'8266','Manel',2,'Modificat estat.'),(90,'2014-06-04 23:23:51',1,13,'9034','Hurtado',2,'Modificat estat.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'opcio','productes','opcio'),(8,'categoria','productes','categoria'),(9,'producte','productes','producte'),(10,'usuari','usuaris','usuari'),(11,'moment apat','comanda','momentapat'),(12,'taula','comanda','taula'),(13,'comanda','comanda','comanda'),(14,'linia comanda','comanda','liniacomanda');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('trtovxyqy8pws7713otdr59x8git6xix','ODM5Y2Q2MWNkODMwNWI3ZTU5OGRhMTlmZmQ2NTJjZDA2MWIyNGZhYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-06-18 19:45:24');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productes_categoria`
--

DROP TABLE IF EXISTS `productes_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productes_categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria` varchar(255) NOT NULL,
  `imatge` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productes_categoria`
--

LOCK TABLES `productes_categoria` WRITE;
/*!40000 ALTER TABLE `productes_categoria` DISABLE KEYS */;
INSERT INTO `productes_categoria` VALUES (1,'Aperitiu','categories/aperitiu_1.png'),(2,'Entrants','categories/entrants_1.png'),(3,'Carns','categories/carns_1.png'),(4,'Postres','categories/postres_1.png'),(5,'Cafés','categories/coffee_1.png'),(6,'Cerveses','categories/beer_1.png'),(7,'Aigües','categories/aigua_1.png'),(8,'Vins','categories/wine_1.png'),(9,'Varis','categories/varis_1.png');
/*!40000 ALTER TABLE `productes_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productes_categoria_opcio`
--

DROP TABLE IF EXISTS `productes_categoria_opcio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productes_categoria_opcio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria_id` int(11) NOT NULL,
  `opcio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `categoria_id` (`categoria_id`,`opcio_id`),
  KEY `productes_categoria_opcio_5f2644f7` (`categoria_id`),
  KEY `productes_categoria_opcio_48cb017f` (`opcio_id`),
  CONSTRAINT `categoria_id_refs_id_06c91212` FOREIGN KEY (`categoria_id`) REFERENCES `productes_categoria` (`id`),
  CONSTRAINT `opcio_id_refs_id_067ea9e3` FOREIGN KEY (`opcio_id`) REFERENCES `productes_opcio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productes_categoria_opcio`
--

LOCK TABLES `productes_categoria_opcio` WRITE;
/*!40000 ALTER TABLE `productes_categoria_opcio` DISABLE KEYS */;
INSERT INTO `productes_categoria_opcio` VALUES (1,3,1),(2,3,2),(3,3,3),(4,5,4),(5,5,5),(6,5,6);
/*!40000 ALTER TABLE `productes_categoria_opcio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productes_opcio`
--

DROP TABLE IF EXISTS `productes_opcio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productes_opcio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcio` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productes_opcio`
--

LOCK TABLES `productes_opcio` WRITE;
/*!40000 ALTER TABLE `productes_opcio` DISABLE KEYS */;
INSERT INTO `productes_opcio` VALUES (1,'amanida'),(2,'patates'),(3,'mongetes'),(4,'sucre'),(5,'sacarina'),(6,'res');
/*!40000 ALTER TABLE `productes_opcio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productes_producte`
--

DROP TABLE IF EXISTS `productes_producte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productes_producte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria_id` int(11) NOT NULL,
  `producte` varchar(255) NOT NULL,
  `preu` decimal(4,2) NOT NULL,
  `imatge` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `productes_producte_5f2644f7` (`categoria_id`),
  CONSTRAINT `categoria_id_refs_id_68ecc0c3` FOREIGN KEY (`categoria_id`) REFERENCES `productes_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productes_producte`
--

LOCK TABLES `productes_producte` WRITE;
/*!40000 ALTER TABLE `productes_producte` DISABLE KEYS */;
INSERT INTO `productes_producte` VALUES (1,1,'Olives',3.00,''),(2,1,'Berberetxos',9.00,''),(3,1,'Chips',4.00,''),(4,2,'Amanida Verda',7.00,''),(5,2,'Cargols ',11.00,''),(6,2,'Espàrrecs maionesa',8.00,''),(7,2,'Torrades Anxoves',11.00,''),(8,2,'Escalivada',8.00,''),(9,2,'Embotits',11.00,''),(10,2,'Paté al pebre',7.00,''),(11,3,'Xai',12.00,''),(12,3,'Entrecot',14.00,''),(13,3,'Cansalada',8.00,''),(14,3,'Botifarra',7.00,''),(15,3,'Pollastre',8.00,''),(16,3,'Bistec',11.00,''),(17,3,'Graellada de carn',23.00,''),(18,4,'Tiramisu',3.00,''),(19,4,'Flam',3.50,''),(20,4,'Crema Catalana',4.50,''),(21,4,'Pastis de formatge',4.00,''),(22,4,'Gelat d\'aigua',2.00,''),(23,4,'Mousse de xocolata',4.00,''),(24,4,'Coulant de xocolata',4.75,''),(25,4,'Iogurt',2.00,''),(26,5,'Café ',1.10,''),(27,5,'Tallat',1.25,''),(28,5,'Café amb llet',1.50,''),(29,5,'Café irlandés',5.50,''),(30,5,'Cigaló',1.90,''),(31,6,'Mitjana Voll Damm',1.90,''),(32,6,'Mitjana San Miquel',1.50,''),(33,6,'Mitjana Estrella',1.70,''),(34,7,'Vichy 1L',2.20,''),(35,7,'Aigua 1L',1.80,''),(36,7,'Gasosa 1L',0.00,''),(37,8,'3 Fincas ',8.00,''),(38,8,'3/8 3Fincas',4.00,''),(39,8,'1L Casa',4.00,''),(40,8,'1/2 Casa',2.20,''),(41,8,'1/4 Casa',1.75,''),(42,8,'Cava Peralada Brut',12.00,''),(43,9,'Alioli',1.70,'');
/*!40000 ALTER TABLE `productes_producte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuaris_usuari`
--

DROP TABLE IF EXISTS `usuaris_usuari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuaris_usuari` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `esAdminSistema` varchar(100) DEFAULT NULL,
  `usuari_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuari_id` (`usuari_id`),
  CONSTRAINT `usuari_id_refs_id_bd1023a5` FOREIGN KEY (`usuari_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9367 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuaris_usuari`
--

LOCK TABLES `usuaris_usuari` WRITE;
/*!40000 ALTER TABLE `usuaris_usuari` DISABLE KEYS */;
INSERT INTO `usuaris_usuari` VALUES (1,'',1);
/*!40000 ALTER TABLE `usuaris_usuari` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-06-05  1:38:12
