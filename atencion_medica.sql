-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: atencion_medica
-- ------------------------------------------------------
-- Server version	8.0.45

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atencion_medica`
--

LOCK TABLES `atencion_medica` WRITE;
/*!40000 ALTER TABLE `atencion_medica` DISABLE KEYS */;
INSERT INTO `atencion_medica` VALUES (1,'Gripe','Paciente con fiebre leve','2026-03-10','',''),(2,'Dolor estomacal','Molestia abdominal','2026-03-11','',''),(3,'Presion alta','Presion elevada','2026-03-12','',''),(4,'TYTTUYU','GGJHGHGH','2026-07-12','1115729778','Glucosa'),(5,'dolor de cabeza','dolor muy suerte','2026-07-14','106687451','Orina'),(6,'gripe comun','reposo e hidratacion','2026-07-14','123456789','Glucosa'),(7,'Gripe común','Reposo e hidratación','2026-07-14','106687451','Hemograma'),(8,'gripe','reposo','2026-07-14','777888999','Hemograma');
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
  `PENDIENTE` varchar(100) NOT NULL,
  PRIMARY KEY (`ID_CITA`),
  UNIQUE KEY `ID_PACIENTE` (`ID_PACIENTE`),
  UNIQUE KEY `ID_MEDICO` (`ID_MEDICO`),
  CONSTRAINT `cita_ibfk_1` FOREIGN KEY (`ID_PACIENTE`) REFERENCES `paciente` (`ID_PACIENTE`),
  CONSTRAINT `cita_ibfk_2` FOREIGN KEY (`ID_MEDICO`) REFERENCES `medico` (`ID_MEDICO`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cita`
--

LOCK TABLES `cita` WRITE;
/*!40000 ALTER TABLE `cita` DISABLE KEYS */;
INSERT INTO `cita` VALUES (1,1,1,'2026-03-10 09:00:00',1,'No'),(2,2,2,'2026-03-11 10:30:00',0,'No'),(3,3,3,'2026-03-12 14:00:00',1,'Si');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examen`
--

LOCK TABLES `examen` WRITE;
/*!40000 ALTER TABLE `examen` DISABLE KEYS */;
INSERT INTO `examen` VALUES (1,1,'Examen de sangre','2026-03-10',1,'Dr. Andres Gomez',1,'Juan Perez'),(2,2,'Radiografia','2026-03-11',2,'Dra. Laura Torres',2,'Maria Lopez'),(3,3,'Electrocardiograma','2026-03-12',3,'Dr. Miguel Castro',3,'Carlos Ramirez');
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
  PRIMARY KEY (`ID_LAB`),
  UNIQUE KEY `NOMBRE_LAB` (`NOMBRE_LAB`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laboratorio`
--

LOCK TABLES `laboratorio` WRITE;
/*!40000 ALTER TABLE `laboratorio` DISABLE KEYS */;
INSERT INTO `laboratorio` VALUES (1,'Laboratorio Central','Ana Martinez','labcentral@gmail.com','3201234567'),(2,'Lab Clinico Salud','Pedro Garcia','labsalud@gmail.com','3214567890'),(3,'Diagnostico Medico','Luisa Fernandez','diagnostico@gmail.com','3229876543');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medico`
--

LOCK TABLES `medico` WRITE;
/*!40000 ALTER TABLE `medico` DISABLE KEYS */;
INSERT INTO `medico` VALUES (1,'Dr. Andres Gomez','Cardiologia','3104567890','andresgomez@gmail.com'),(2,'Dra. Laura Torres','Pediatria','3117894561','lauratorres@gmail.com'),(3,'Dr. Miguel Castro','Medicina General','3126549870','miguelcastro@gmail.com'),(5,'string','naturista','string','string');
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
  `APELLIDOS_PACIENTES` varchar(255) DEFAULT NULL,
  `FECHA_NACIMIENTO` date DEFAULT NULL,
  `NUMERO_DOCUMENTO` int NOT NULL,
  `CORREO` varchar(120) NOT NULL,
  `FECHA_REGISTRO` date DEFAULT NULL,
  `TELEFONO` varchar(20) NOT NULL,
  PRIMARY KEY (`ID_PACIENTE`),
  UNIQUE KEY `NUMERO_DOCUMENTO` (`NUMERO_DOCUMENTO`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES (1,'Juan Perez','Perez','2000-01-01',106687451,'juanperez@gmail.com','2026-07-12','300123456'),(2,'Maria Lopez','Lopez','2001-02-02',1024512021,'marialopez@gmail.com','2026-07-12','301456789'),(3,'Carlos Ramirez','Ramirez','1999-03-03',106608541,'carlosramirez@gmail.com','2026-07-12','302789456'),(4,'pedro','gomez','2001-05-10',123456789,'pedro@gmail.com','2026-07-13','3115556677'),(5,'Ana','Torres ','2002-04-10',777888999,'ana@gmail.com','2026-07-14','3001112233');
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
  UNIQUE KEY `ID_LAB` (`ID_LAB`),
  KEY `ID_EXAMEN` (`ID_EXAMEN`),
  CONSTRAINT `resultado_ibfk_1` FOREIGN KEY (`ID_EXAMEN`) REFERENCES `examen` (`ID_EXAMEN`),
  CONSTRAINT `resultado_ibfk_2` FOREIGN KEY (`ID_LAB`) REFERENCES `laboratorio` (`ID_LAB`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resultado`
--

LOCK TABLES `resultado` WRITE;
/*!40000 ALTER TABLE `resultado` DISABLE KEYS */;
INSERT INTO `resultado` VALUES (1,1,'2026-03-11','resultado1.pdf',1),(2,2,'2026-03-12','resultado2.pdf',2),(3,3,'2026-03-13','resultado3.pdf',3);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'wilsonfv777@gmail.com','W290208f','MEDICO'),(2,'recepcion@gmail.com','12345','RECEPCIONISTA');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-14 19:18:48
