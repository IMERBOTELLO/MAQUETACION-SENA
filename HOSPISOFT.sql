-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: atencion_medica
-- ------------------------------------------------------
-- Server version	9.6.0

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'bd294991-1195-11f1-96a4-9c6b00aced05:1-320';

--
-- Table structure for table `atencion_medica`
--

DROP TABLE IF EXISTS `atencion_medica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atencion_medica` (
  `ID_ATENCION` int NOT NULL AUTO_INCREMENT,
  `DIAGNOSTICO` varchar(100) NOT NULL,
  `OBSERVACIONES` varchar(100) NOT NULL,
  `FECHA_ATENCION` date NOT NULL,
  `NUMERO_DOCUMENTO` varchar(20) NOT NULL,
  `EXAMENES` varchar(255) NOT NULL,
  PRIMARY KEY (`ID_ATENCION`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atencion_medica`
--

LOCK TABLES `atencion_medica` WRITE;
/*!40000 ALTER TABLE `atencion_medica` DISABLE KEYS */;
/*!40000 ALTER TABLE `atencion_medica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cita`
--

DROP TABLE IF EXISTS `cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cita` (
  `ID_CITA` int NOT NULL AUTO_INCREMENT,
  `ID_PACIENTE` int NOT NULL,
  `ID_MEDICO` int NOT NULL,
  `FECHA_HORA` datetime NOT NULL,
  `ESTADO` tinyint(1) NOT NULL,
  `PENDIENTE` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID_CITA`),
  KEY `ID_PACIENTE` (`ID_PACIENTE`),
  KEY `ID_MEDICO` (`ID_MEDICO`),
  CONSTRAINT `cita_ibfk_1` FOREIGN KEY (`ID_PACIENTE`) REFERENCES `paciente` (`ID_PACIENTE`),
  CONSTRAINT `cita_ibfk_2` FOREIGN KEY (`ID_MEDICO`) REFERENCES `medico` (`ID_MEDICO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cita`
--

LOCK TABLES `cita` WRITE;
/*!40000 ALTER TABLE `cita` DISABLE KEYS */;
/*!40000 ALTER TABLE `cita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examen`
--

DROP TABLE IF EXISTS `examen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `examen` (
  `ID_EXAMEN` int NOT NULL AUTO_INCREMENT,
  `ID_ATENCION` int NOT NULL,
  `TIPO_EXAMEN` varchar(100) NOT NULL,
  `FECHA` date NOT NULL,
  `ID_MEDICO` int NOT NULL,
  `NOMBRE_MEDICO` varchar(100) NOT NULL,
  `ID_PACIENTE` int NOT NULL,
  `NOMBRE_PACIENTE` varchar(100) NOT NULL,
  PRIMARY KEY (`ID_EXAMEN`),
  UNIQUE KEY `ID_ATENCION` (`ID_ATENCION`),
  CONSTRAINT `examen_ibfk_1` FOREIGN KEY (`ID_ATENCION`) REFERENCES `atencion_medica` (`ID_ATENCION`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examen`
--

LOCK TABLES `examen` WRITE;
/*!40000 ALTER TABLE `examen` DISABLE KEYS */;
/*!40000 ALTER TABLE `examen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laboratorio`
--

DROP TABLE IF EXISTS `laboratorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laboratorio` (
  `ID_LAB` int NOT NULL AUTO_INCREMENT,
  `NOMBRE_LAB` varchar(100) NOT NULL,
  `RESPONSABLE` varchar(100) DEFAULT NULL,
  `CORREO_LAB` varchar(120) DEFAULT NULL,
  `TELEFONO_CONTACTO` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_LAB`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laboratorio`
--

LOCK TABLES `laboratorio` WRITE;
/*!40000 ALTER TABLE `laboratorio` DISABLE KEYS */;
/*!40000 ALTER TABLE `laboratorio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medico`
--

DROP TABLE IF EXISTS `medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medico` (
  `ID_MEDICO` int NOT NULL AUTO_INCREMENT,
  `NOMBRE_MEDICO` varchar(100) NOT NULL,
  `ESPECIALIDAD` varchar(80) NOT NULL,
  `TELEFONO` varchar(20) NOT NULL,
  `CORREO` varchar(120) NOT NULL,
  PRIMARY KEY (`ID_MEDICO`),
  UNIQUE KEY `TELEFONO` (`TELEFONO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medico`
--

LOCK TABLES `medico` WRITE;
/*!40000 ALTER TABLE `medico` DISABLE KEYS */;
/*!40000 ALTER TABLE `medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente` (
  `ID_PACIENTE` int NOT NULL AUTO_INCREMENT,
  `NOMBRES_PACIENTE` varchar(255) NOT NULL,
  `APELLIDOS_PACIENTES` varchar(255) NOT NULL,
  `FECHA_NACIMIENTO` date NOT NULL,
  `NUMERO_DOCUMENTO` varchar(25) NOT NULL,
  `CORREO` varchar(120) NOT NULL,
  `FECHA_REGISTRO` date NOT NULL,
  `TELEFONO` varchar(20) NOT NULL,
  PRIMARY KEY (`ID_PACIENTE`),
  UNIQUE KEY `NUMERO_DOCUMENTO` (`NUMERO_DOCUMENTO`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES (5,'liliana','paez','2005-01-22','451161616','liliana@gmail.com','2026-07-09','461616346'),(6,'Imer','paez','2007-06-22','4974878416','imerantoniobotellopaez@gmail.com','2026-01-22','3004188526'),(7,'imer','botello','2008-01-22','48887846','imerbotello@gmail.com','2026-07-13','3011645152'),(9,'camilo','andrez','2007-02-06','15484651213','andrez@gmial.com','2026-07-13','30048674851');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resultado`
--

DROP TABLE IF EXISTS `resultado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resultado` (
  `ID_RESULTADO` int NOT NULL AUTO_INCREMENT,
  `ID_LAB` int NOT NULL,
  `FECHA_RESULTADO` date NOT NULL,
  `ARCHIVO` varchar(255) NOT NULL,
  `ID_EXAMEN` int NOT NULL,
  PRIMARY KEY (`ID_RESULTADO`),
  KEY `ID_EXAMEN` (`ID_EXAMEN`),
  KEY `ID_LAB` (`ID_LAB`),
  CONSTRAINT `resultado_ibfk_1` FOREIGN KEY (`ID_EXAMEN`) REFERENCES `examen` (`ID_EXAMEN`),
  CONSTRAINT `resultado_ibfk_2` FOREIGN KEY (`ID_LAB`) REFERENCES `laboratorio` (`ID_LAB`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resultado`
--

LOCK TABLES `resultado` WRITE;
/*!40000 ALTER TABLE `resultado` DISABLE KEYS */;
/*!40000 ALTER TABLE `resultado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `ID_USUARIO` int NOT NULL AUTO_INCREMENT,
  `CORREO` varchar(150) NOT NULL,
  `CONTRASEÑA` varchar(150) NOT NULL,
  `ROL` enum('RECEPCIONISTA','MEDICO','LABORATORIO','PACIENTE','ADMINISTRADOR') NOT NULL,
  PRIMARY KEY (`ID_USUARIO`),
  UNIQUE KEY `CORREO` (`CORREO`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (4,'imerbotello@gmail.com','1365645','ADMINISTRADOR'),(5,'camilobotello@gmail.com','134','PACIENTE'),(6,'liliana@gmail.com','134','RECEPCIONISTA'),(9,'imerantonio@gmail.com','12345','LABORATORIO'),(10,'imerpaez@gmail.com','12345','MEDICO');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-15 10:25:47
