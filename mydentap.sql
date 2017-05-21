-- MySQL dump 10.16  Distrib 10.1.13-MariaDB, for Win32 (AMD64)
--
-- Host: localhost    Database: mydentap
-- ------------------------------------------------------
-- Server version	10.1.13-MariaDB

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
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointments` (
  `AppointID` int(11) NOT NULL AUTO_INCREMENT,
  `FromTime` time DEFAULT NULL,
  `ToTime` time DEFAULT NULL,
  `DateApp` date DEFAULT NULL,
  `PatientName` varchar(45) DEFAULT NULL,
  `Service` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`AppointID`)
) ENGINE=MyISAM AUTO_INCREMENT=10001 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientlist`
--

DROP TABLE IF EXISTS `patientlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patientlist` (
  `PatientID` int(11) NOT NULL AUTO_INCREMENT,
  `FName` varchar(45) DEFAULT NULL,
  `MName` varchar(45) DEFAULT NULL,
  `LName` varchar(45) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Contact` double DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `DateAdded` date DEFAULT NULL,
  PRIMARY KEY (`PatientID`)
) ENGINE=MyISAM AUTO_INCREMENT=10000001 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientlist`
--

LOCK TABLES `patientlist` WRITE;
/*!40000 ALTER TABLE `patientlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientsname`
--

DROP TABLE IF EXISTS `patientsname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patientsname` (
  `PatID` int(11) NOT NULL AUTO_INCREMENT,
  `WholeName` varchar(100) NOT NULL,
  `Address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PatID`)
) ENGINE=MyISAM AUTO_INCREMENT=10000008 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientsname`
--

LOCK TABLES `patientsname` WRITE;
/*!40000 ALTER TABLE `patientsname` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientsname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timeconcat`
--

DROP TABLE IF EXISTS `timeconcat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timeconcat` (
  `App_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Schedule` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`App_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timeconcat`
--

LOCK TABLES `timeconcat` WRITE;
/*!40000 ALTER TABLE `timeconcat` DISABLE KEYS */;
/*!40000 ALTER TABLE `timeconcat` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-21 23:42:13
