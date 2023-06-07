-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: iot
-- ------------------------------------------------------
-- Server version	5.7.42-0ubuntu0.18.04.1

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
-- Table structure for table `actuator`
--

DROP TABLE IF EXISTS `actuator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `actuator` (
  `ip_address` varchar(25) NOT NULL,
  `state` varchar(25) DEFAULT NULL,
  `type` varchar(25) DEFAULT NULL,
  `wagon` int(11) DEFAULT NULL,
  PRIMARY KEY (`ip_address`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actuator`
--

LOCK TABLES `actuator` WRITE;
/*!40000 ALTER TABLE `actuator` DISABLE KEYS */;
INSERT INTO `actuator` VALUES ('fd00::203:3:3:3','standard','energy',1),('fd00::f6ce:36db:3e8b:b5bc','idle','brakes',1);
/*!40000 ALTER TABLE `actuator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor_data`
--

DROP TABLE IF EXISTS `sensor_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensor_data` (
  `sensor_id` int(11) NOT NULL,
  `timestamp` bigint(20) NOT NULL,
  `type` varchar(25) DEFAULT NULL,
  `value` float DEFAULT NULL,
  `wagon` int(11) DEFAULT NULL,
  PRIMARY KEY (`sensor_id`,`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor_data`
--

LOCK TABLES `sensor_data` WRITE;
/*!40000 ALTER TABLE `sensor_data` DISABLE KEYS */;
INSERT INTO `sensor_data` VALUES (2,1685827343,'consumption',162,1),(2,1685827373,'consumption',133,1),(2,1685827404,'consumption',208,1),(2,1685827410,'consumption',140,1),(2,1685827416,'consumption',139,1),(2,1685827422,'consumption',205,1),(2,1685827428,'consumption',159,1),(2,1685827434,'consumption',120,1),(2,1685827440,'consumption',163,1),(2,1685827446,'consumption',163,1),(2,1685827452,'consumption',205,1),(2,1685827458,'consumption',204,1),(2,1685827464,'consumption',171,1),(2,1685827470,'consumption',178,1),(2,1685827476,'consumption',178,1),(2,1685827483,'consumption',188,1),(2,1685827489,'consumption',221,1),(2,1685827495,'consumption',223,1),(2,1685827501,'consumption',202,1),(2,1685827507,'consumption',150,1),(2,1685827513,'consumption',149,1),(2,1685827519,'consumption',177,1),(2,1685827525,'consumption',126,1),(2,1685827531,'consumption',171,1),(2,1685827537,'consumption',160,1),(2,1685827543,'consumption',223,1),(2,1685827549,'consumption',150,1),(2,1685827555,'consumption',155,1),(2,1685827561,'consumption',127,1),(2,1685827567,'consumption',203,1),(2,1685827573,'consumption',160,1),(2,1685827579,'consumption',166,1),(2,1685827585,'consumption',144,1),(2,1685827591,'consumption',154,1),(2,1685827597,'consumption',121,1),(2,1685827603,'consumption',162,1),(2,1685827609,'consumption',126,1),(2,1685827615,'consumption',185,1),(2,1685827621,'consumption',136,1),(2,1685827627,'consumption',208,1),(2,1685827633,'consumption',144,1),(2,1685827639,'consumption',196,1),(2,1685827645,'consumption',141,1),(2,1685827651,'consumption',170,1),(2,1685827657,'consumption',175,1),(2,1685827663,'consumption',182,1),(2,1685827669,'consumption',219,1),(2,1685827675,'consumption',129,1),(2,1685827681,'consumption',227,1),(2,1685827687,'consumption',170,1),(2,1685827693,'consumption',187,1),(2,1685827699,'consumption',162,1),(2,1685827705,'consumption',144,1),(2,1685827711,'consumption',178,1),(2,1685827717,'consumption',228,1),(2,1685827723,'consumption',127,1),(2,1685827729,'consumption',161,1),(2,1685827735,'consumption',215,1),(2,1685827741,'consumption',211,1),(2,1685827747,'consumption',208,1),(2,1685827753,'consumption',221,1),(2,1685827759,'consumption',217,1),(2,1685827765,'consumption',132,1),(2,1685827771,'consumption',160,1),(2,1685827777,'consumption',223,1),(2,1685827783,'consumption',226,1),(2,1685827789,'consumption',184,1),(2,1685827795,'consumption',164,1),(2,1685827801,'consumption',122,1),(2,1685827807,'consumption',215,1),(2,1685827813,'consumption',188,1),(2,1685827819,'consumption',223,1),(2,1685827825,'consumption',173,1),(2,1685827831,'consumption',184,1),(2,1685827838,'consumption',210,1),(2,1685827844,'consumption',174,1),(2,1685827850,'consumption',180,1),(2,1685827856,'consumption',141,1),(2,1685827862,'consumption',180,1),(2,1685827868,'consumption',175,1),(2,1685827874,'consumption',195,1),(2,1685827880,'consumption',188,1),(2,1685827886,'consumption',129,1),(2,1685827892,'consumption',225,1),(2,1685827898,'consumption',134,1),(2,1685827904,'consumption',160,1),(2,1685827910,'consumption',194,1),(2,1685827916,'consumption',222,1),(2,1685869002,'consumption',139,1),(2,1685869033,'consumption',189,1),(2,1685869048,'consumption',201,1),(2,1685869063,'consumption',165,1),(2,1685869079,'consumption',151,1),(2,1685869095,'consumption',185,1),(2,1685869110,'consumption',207,1),(2,1685869126,'consumption',192,1),(2,1685869141,'consumption',131,1),(2,1685869156,'consumption',154,1),(2,1685869172,'consumption',212,1),(2,1685869188,'consumption',140,1),(2,1685869203,'consumption',167,1),(2,1685869219,'consumption',178,1),(2,1685869234,'consumption',172,1),(2,1685869250,'consumption',206,1),(2,1685869724,'consumption',157,1),(2,1685869739,'consumption',151,1),(2,1685869755,'consumption',152,1),(2,1685869770,'consumption',193,1),(2,1685869786,'consumption',120,1),(2,1685869802,'consumption',140,1),(2,1685869817,'consumption',130,1),(2,1685869833,'consumption',184,1),(2,1685869849,'consumption',195,1),(2,1685869865,'consumption',161,1),(2,1685869880,'consumption',127,1),(2,1685869895,'consumption',124,1),(2,1685869911,'consumption',229,1),(2,1685869926,'consumption',164,1),(2,1685869942,'consumption',207,1),(2,1685869958,'consumption',210,1),(2,1685869973,'consumption',174,1),(2,1685869989,'consumption',180,1),(2,1685870004,'consumption',158,1),(2,1685870019,'consumption',221,1),(2,1685870035,'consumption',187,1),(2,1685870050,'consumption',224,1),(2,1685870065,'consumption',206,1),(2,1685870081,'consumption',188,1),(2,1685870096,'consumption',155,1),(2,1685870111,'consumption',225,1),(2,1685870126,'consumption',198,1),(2,1685870141,'consumption',208,1),(2,1685870156,'consumption',128,1),(2,1685870172,'consumption',193,1),(2,1685870187,'consumption',131,1),(2,1685870202,'consumption',146,1),(2,1685870217,'consumption',182,1),(2,1685870232,'consumption',202,1),(2,1685870247,'consumption',174,1),(2,1685870262,'consumption',200,1),(2,1685870277,'consumption',148,1),(2,1685870292,'consumption',226,1),(2,1685870308,'consumption',205,1),(2,1685870323,'consumption',187,1),(2,1685870338,'consumption',158,1),(2,1685870353,'consumption',215,1),(2,1685870368,'consumption',151,1),(2,1685870383,'consumption',151,1),(2,1685870398,'consumption',192,1),(2,1685870413,'consumption',205,1),(2,1685870429,'consumption',146,1),(2,1685870444,'consumption',143,1),(2,1685870459,'consumption',211,1),(2,1685870474,'consumption',153,1),(2,1685870489,'consumption',139,1),(2,1685870504,'consumption',130,1),(2,1685870519,'consumption',211,1),(2,1685870535,'consumption',227,1),(2,1685870550,'consumption',135,1),(2,1685870565,'consumption',219,1),(2,1685870580,'consumption',190,1),(2,1685870596,'consumption',125,1),(2,1685870611,'consumption',146,1),(2,1685870626,'consumption',225,1),(2,1685870641,'consumption',169,1),(2,1685870656,'consumption',182,1),(2,1685870672,'consumption',172,1),(2,1685870687,'consumption',126,1),(2,1685870702,'consumption',154,1),(2,1685870717,'consumption',210,1),(2,1685870732,'consumption',213,1),(2,1685870747,'consumption',184,1),(2,1685870762,'consumption',171,1),(2,1685870778,'consumption',156,1),(2,1685870793,'consumption',163,1),(2,1685870808,'consumption',223,1),(2,1685870823,'consumption',123,1),(2,1685870838,'consumption',127,1),(2,1685870853,'consumption',226,1),(2,1685870868,'consumption',182,1),(2,1685870883,'consumption',188,1),(2,1685870898,'consumption',194,1),(2,1685870913,'consumption',190,1),(2,1685870929,'consumption',202,1),(2,1685870944,'consumption',122,1),(2,1685870959,'consumption',213,1),(2,1685870974,'consumption',193,1),(2,1685870989,'consumption',175,1),(2,1685871004,'consumption',228,1),(2,1685871019,'consumption',123,1),(2,1685871034,'consumption',134,1),(2,1685871049,'consumption',217,1),(2,1685871064,'consumption',121,1),(2,1685871079,'consumption',182,1),(2,1685871094,'consumption',165,1),(2,1685871109,'consumption',179,1),(2,1685871124,'consumption',206,1),(2,1685871139,'consumption',138,1),(2,1685871154,'consumption',224,1),(2,1685871169,'consumption',197,1),(2,1685871184,'consumption',170,1),(2,1685871199,'consumption',122,1),(2,1685871214,'consumption',144,1),(2,1685871229,'consumption',190,1),(2,1685871244,'consumption',163,1),(2,1685871259,'consumption',138,1),(2,1685871274,'consumption',152,1),(2,1685871289,'consumption',214,1),(2,1685871304,'consumption',145,1),(2,1685871319,'consumption',184,1),(2,1685871334,'consumption',141,1),(2,1685871349,'consumption',145,1),(2,1685871364,'consumption',132,1),(2,1685871379,'consumption',141,1),(2,1685871394,'consumption',129,1),(2,1685871409,'consumption',150,1),(2,1685871425,'consumption',162,1),(2,1685871440,'consumption',122,1),(2,1685871455,'consumption',184,1),(2,1685871470,'consumption',204,1),(2,1685871485,'consumption',131,1),(2,1685871500,'consumption',171,1),(2,1685871516,'consumption',158,1),(2,1685871531,'consumption',168,1),(2,1685871546,'consumption',122,1),(2,1685871561,'consumption',188,1),(2,1685871576,'consumption',186,1),(2,1685871591,'consumption',174,1),(2,1685871606,'consumption',151,1),(2,1685871621,'consumption',222,1),(2,1685871636,'consumption',168,1),(2,1685871651,'consumption',196,1),(2,1685871666,'consumption',168,1),(2,1685871681,'consumption',221,1),(2,1685871696,'consumption',130,1),(2,1685871711,'consumption',172,1),(2,1685871726,'consumption',152,1),(2,1685871741,'consumption',211,1),(2,1685871756,'consumption',159,1),(2,1685871771,'consumption',153,1),(2,1685871786,'consumption',216,1),(2,1685872220,'consumption',133,1),(2,1685872250,'consumption',211,1),(2,1685872402,'consumption',120,1),(2,1685872462,'consumption',217,1),(2,1685872492,'consumption',139,1),(2,1685872522,'consumption',153,1),(2,1685872643,'consumption',135,1),(2,1685872704,'consumption',192,1),(2,1685872824,'consumption',140,1),(2,1685872884,'consumption',225,1),(2,1685872944,'consumption',130,1),(2,1685872975,'consumption',183,1),(3,1685828224,'brake_temperature',64,1),(3,1685828254,'brake_temperature',46,1),(3,1685828284,'brake_temperature',56,1),(3,1685828314,'brake_temperature',66,1),(3,1685828345,'brake_temperature',34,1),(3,1685828375,'brake_temperature',32,1),(3,1685828405,'brake_temperature',63,1),(3,1685828435,'brake_temperature',78,1),(3,1685828465,'brake_temperature',60,1),(3,1685828495,'brake_temperature',34,1),(3,1685828525,'brake_temperature',62,1),(3,1685828555,'brake_temperature',54,1),(3,1685828585,'brake_temperature',30,1),(3,1685828615,'brake_temperature',58,1),(3,1685828645,'brake_temperature',60,1),(3,1685828675,'brake_temperature',33,1),(3,1685828705,'brake_temperature',41,1),(3,1685828736,'brake_temperature',73,1),(3,1685828766,'brake_temperature',31,1),(3,1685828796,'brake_temperature',67,1),(3,1685828826,'brake_temperature',42,1),(3,1685828856,'brake_temperature',35,1),(3,1685828886,'brake_temperature',50,1),(3,1685828918,'brake_temperature',63,1),(3,1685828948,'brake_temperature',50,1),(3,1685828978,'brake_temperature',38,1),(3,1685829008,'brake_temperature',73,1),(3,1685829038,'brake_temperature',43,1),(3,1685829068,'brake_temperature',33,1),(3,1685829098,'brake_temperature',44,1),(3,1685829129,'brake_temperature',79,1),(3,1685829159,'brake_temperature',40,1),(3,1685829189,'brake_temperature',53,1),(3,1685829219,'brake_temperature',48,1),(3,1685829249,'brake_temperature',56,1),(3,1685829279,'brake_temperature',77,1),(3,1685829309,'brake_temperature',72,1),(3,1685829339,'brake_temperature',30,1),(3,1685829369,'brake_temperature',54,1),(3,1685829399,'brake_temperature',71,1),(3,1685829429,'brake_temperature',46,1),(3,1685829459,'brake_temperature',32,1),(3,1685829489,'brake_temperature',76,1),(3,1685829519,'brake_temperature',30,1),(3,1685829549,'brake_temperature',76,1),(3,1685829579,'brake_temperature',78,1),(3,1685829609,'brake_temperature',32,1),(3,1685829639,'brake_temperature',54,1),(3,1685829669,'brake_temperature',46,1),(3,1685829699,'brake_temperature',38,1),(3,1685829729,'brake_temperature',34,1),(3,1685829759,'brake_temperature',77,1),(3,1685829789,'brake_temperature',74,1),(3,1685829819,'brake_temperature',76,1),(3,1685898527,'brake_temperature',56,1),(3,1685898587,'brake_temperature',90,1),(4,1685900573,'consumption',145,1),(4,1685900603,'consumption',181,1),(4,1685900665,'consumption',161,1),(5,1685900605,'brake_temperature',47,1),(10624,0,'brake_temperature',79,1);
/*!40000 ALTER TABLE `sensor_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wagon`
--

DROP TABLE IF EXISTS `wagon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wagon` (
  `wagon_id` int(11) NOT NULL,
  `max_br_temp` int(11) DEFAULT NULL,
  `max_consumption` int(11) DEFAULT NULL,
  PRIMARY KEY (`wagon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wagon`
--

LOCK TABLES `wagon` WRITE;
/*!40000 ALTER TABLE `wagon` DISABLE KEYS */;
INSERT INTO `wagon` VALUES (1,70,170);
/*!40000 ALTER TABLE `wagon` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-07 15:02:40
