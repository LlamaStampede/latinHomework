-- MySQL dump 10.13  Distrib 8.0.11, for macos10.13 (x86_64)
--
-- Host: localhost    Database: TLD_SHT
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aeneid1_error`
--

DROP TABLE IF EXISTS `aeneid1_error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `aeneid1_error` (
  `trm` varchar(20) NOT NULL,
  `type` varchar(8) NOT NULL,
  `conf1` varchar(50) DEFAULT NULL,
  `conf2` varchar(50) DEFAULT NULL,
  `conf3` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`trm`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeneid1_error`
--

LOCK TABLES `aeneid1_error` WRITE;
/*!40000 ALTER TABLE `aeneid1_error` DISABLE KEYS */;
INSERT INTO `aeneid1_error` VALUES ('+que','none',NULL,NULL,NULL),('ab','none',NULL,NULL,NULL),('Albani','unknown',NULL,NULL,NULL),('altae','none',NULL,NULL,NULL),('alto','none',NULL,NULL,NULL),('arma','none',NULL,NULL,NULL),('atque','none',NULL,NULL,NULL),('bello','multi','bellum,belli N-[D+Ab]-S war','bellus,bella,bellum [M+N]-[D+Ab]-S handsome',NULL),('cano','none',NULL,NULL,NULL),('conderet','none',NULL,NULL,NULL),('deos','none',NULL,NULL,NULL),('dum','none',NULL,NULL,NULL),('et','none',NULL,NULL,NULL),('fato','none',NULL,NULL,NULL),('genus','none',NULL,NULL,NULL),('iactatus','none',NULL,NULL,NULL),('ille','none',NULL,NULL,NULL),('inferret','unknown',NULL,NULL,NULL),('iram','multi','eo,ire,ivi,itus 1S-Ppf-I-A to go','ira,irae F-Ac-S anger',NULL),('Italiam','none',NULL,NULL,NULL),('Iunonis','none',NULL,NULL,NULL),('Latinum','none',NULL,NULL,NULL),('Latio','unknown',NULL,NULL,NULL),('Lavinia','unknown',NULL,NULL,NULL),('litora','none',NULL,NULL,NULL),('memorem','unknown',NULL,NULL,NULL),('moenia','none',NULL,NULL,NULL),('multa','none',NULL,NULL,NULL),('multum','none',NULL,NULL,NULL),('ob','none',NULL,NULL,NULL),('oris','none',NULL,NULL,NULL),('passus','none',NULL,NULL,NULL),('patres','none',NULL,NULL,NULL),('primus','none',NULL,NULL,NULL),('profugus','unknown',NULL,NULL,NULL),('qui','none',NULL,NULL,NULL),('quo','none',NULL,NULL,NULL),('Romae','unknown',NULL,NULL,NULL),('saevae','unknown',NULL,NULL,NULL),('superum','none',NULL,NULL,NULL),('terris','none',NULL,NULL,NULL),('Troiae','none',NULL,NULL,NULL),('unde','unknown',NULL,NULL,NULL),('urbem','none',NULL,NULL,NULL),('venit','multi','venio,venire,veni,ventus 3S-P-I-A to come','venio,venire,veni,ventus 3S-Pf-I-A to come',NULL),('vi','none',NULL,NULL,NULL),('virum','none',NULL,NULL,NULL);
/*!40000 ALTER TABLE `aeneid1_error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aeneid1_main`
--

DROP TABLE IF EXISTS `aeneid1_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `aeneid1_main` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `trm` varchar(20) NOT NULL,
  `dct` varchar(30) DEFAULT NULL,
  `prs` varchar(40) DEFAULT NULL,
  `trn` varchar(20) DEFAULT NULL,
  `cmt` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_aeneid1_main` (`trm`),
  CONSTRAINT `FK_aeneid1_main` FOREIGN KEY (`trm`) REFERENCES `aeneid1_error` (`trm`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeneid1_main`
--

LOCK TABLES `aeneid1_main` WRITE;
/*!40000 ALTER TABLE `aeneid1_main` DISABLE KEYS */;
INSERT INTO `aeneid1_main` VALUES (1,'arma','arma(1D)','N-[N+Ac]-S','weapons',''),(2,'virum','vir,viri','M-Ac-S','man',''),(3,'+que','+que','Conj','and','and'),(4,'cano','cano,-ere,ceceni,-tus','1S-P-I-A','to sing','fact'),(5,'Troiae','Troia,-ae','F-[G+D+N]-[S+P]','Troy',''),(6,'qui','qui,quae,quod','M-N-[S+P]','rel./inq.',''),(7,'primus','primus,-a,-um','M-N-S','first','w/'),(8,'ab','ab','Prep+Ab','from, by',''),(9,'oris','os,oris','N-G-S','mouth',''),(10,'Italiam','Italia,-ae','F-Ac-S','Italy',''),(11,'fato','fatum,-i','N-[D+Ab]-S','fate',''),(12,'profugus','','','',''),(13,'Lavinia','','','',''),(14,'+que','+que','Conj','and',''),(15,'venit','venio,-ire,-i,-tus','','to come',''),(16,'litora','litus,litoris','N-[N+Ac]-P','shore',''),(17,'multum','multus,-a,-um','[M+N]-[Ac+N]-S','many','w/'),(18,'ille','ille,illa,illud','[M+N]-[N+V]-S','that',''),(19,'et','et','Conj','and',''),(20,'terris','terra,-ae','F-[D+Ab]-P','land',''),(21,'iactatus','iacto(1)','Pf-Ppl-P/M-N-S','to cast',''),(22,'et','et','Conj','and',''),(23,'alto','alo,-ere,-ui,-tus','Pf-Ppl-P/[M+N]-[D+Ab]-S','to nourish',''),(24,'vi','vis,vis','F-D-S','force (pl)strength',''),(25,'superum','superus,-a,-um','[M+N]-[Ac+N]-S','superior','w/'),(26,'saevae','','','',''),(27,'memorem','','','',''),(28,'Iunonis','Iuno,Iunonis','F-G-S','Juno',''),(29,'ob','ob','Prep+Ac','on account of',''),(30,'iram','','','',''),(31,'multa','multus,-a,-um','[F+N]-[N+Ab+Ac]-[S(Pos.)+P(Pos.)]','many','w/'),(32,'quo','qui,quae,quod','[M+N]-Ab-S','rel./inq.',''),(33,'+que','+que','Conj','and',''),(34,'et','et','Conj','and',''),(35,'bello','','','',''),(36,'passus','patior,pati,passus sum','Pf-Ppl-P/M-N-S','to endure',''),(37,'dum','dum','Conj','until',''),(38,'conderet','condo,-ere,-idi,-itus','3S-Impf-S-A','to establish',''),(39,'urbem','urbs,urbis','F-Ac-S','city',''),(40,'inferret','','','',''),(41,'+que','+que','Conj','and',''),(42,'deos','deus,-i','M-Ac-P','god',''),(43,'Latio','','','',''),(44,'genus','genus,generis','N-[N+Ac]-S','origin',''),(45,'unde','','','',''),(46,'Latinum','Latinus,-a,-um','[M+N]-[Ac+N]-S','Latin','w/'),(47,'Albani','','','',''),(48,'+que','+que','Conj','and',''),(49,'patres','pater,patris','M-[N+Ac]-P','father',''),(50,'atque','atque','Conj','and',''),(51,'altae','alo,-ere,-ui,-tus','Pf-Ppl-P/F-[G+D+N]-[S+P]','to nourish',''),(52,'moenia','','','',''),(53,'Romae','','','','');
/*!40000 ALTER TABLE `aeneid1_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aeneid2_error`
--

DROP TABLE IF EXISTS `aeneid2_error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `aeneid2_error` (
  `trm` varchar(20) NOT NULL,
  `type` varchar(8) NOT NULL,
  `conf1` varchar(50) DEFAULT NULL,
  `conf2` varchar(50) DEFAULT NULL,
  `conf3` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`trm`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeneid2_error`
--

LOCK TABLES `aeneid2_error` WRITE;
/*!40000 ALTER TABLE `aeneid2_error` DISABLE KEYS */;
INSERT INTO `aeneid2_error` VALUES ('+que','none',NULL,NULL,NULL),('ab','none',NULL,NULL,NULL),('Albani','unknown',NULL,NULL,NULL),('altae','none',NULL,NULL,NULL),('alto','none',NULL,NULL,NULL),('arma','none',NULL,NULL,NULL),('atque','none',NULL,NULL,NULL),('bello','multi','bellum,belli N-[D+Ab]-S war','bellus,bella,bellum [M+N]-[D+Ab]-S handsome',NULL),('cano','none',NULL,NULL,NULL),('conderet','none',NULL,NULL,NULL),('deos','none',NULL,NULL,NULL),('dum','none',NULL,NULL,NULL),('et','none',NULL,NULL,NULL),('fato','none',NULL,NULL,NULL),('genus','none',NULL,NULL,NULL),('iactatus','none',NULL,NULL,NULL),('ille','none',NULL,NULL,NULL),('inferret','unknown',NULL,NULL,NULL),('iram','multi','eo,ire,ivi,itus 1S-Ppf-I-A to go','ira,irae F-Ac-S anger',NULL),('Italiam','none',NULL,NULL,NULL),('Iunonis','none',NULL,NULL,NULL),('Latinum','none',NULL,NULL,NULL),('Latio','unknown',NULL,NULL,NULL),('Lavinia','unknown',NULL,NULL,NULL),('litora','none',NULL,NULL,NULL),('memorem','unknown',NULL,NULL,NULL),('moenia','none',NULL,NULL,NULL),('multa','none',NULL,NULL,NULL),('multum','none',NULL,NULL,NULL),('ob','none',NULL,NULL,NULL),('oris','none',NULL,NULL,NULL),('passus','none',NULL,NULL,NULL),('patres','none',NULL,NULL,NULL),('primus','none',NULL,NULL,NULL),('profugus','unknown',NULL,NULL,NULL),('qui','none',NULL,NULL,NULL),('quo','none',NULL,NULL,NULL),('Romae','unknown',NULL,NULL,NULL),('saevae','unknown',NULL,NULL,NULL),('superum','none',NULL,NULL,NULL),('terris','none',NULL,NULL,NULL),('Troiae','none',NULL,NULL,NULL),('unde','unknown',NULL,NULL,NULL),('urbem','none',NULL,NULL,NULL),('venit','multi','venio,venire,veni,ventus 3S-P-I-A to come','venio,venire,veni,ventus 3S-Pf-I-A to come',NULL),('vi','none',NULL,NULL,NULL),('virum','none',NULL,NULL,NULL);
/*!40000 ALTER TABLE `aeneid2_error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aeneid2_main`
--

DROP TABLE IF EXISTS `aeneid2_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `aeneid2_main` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `trm` varchar(20) NOT NULL,
  `dct` varchar(30) DEFAULT NULL,
  `prs` varchar(40) DEFAULT NULL,
  `trn` varchar(20) DEFAULT NULL,
  `cmt` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_aeneid2_main` (`trm`),
  CONSTRAINT `FK_aeneid2_main` FOREIGN KEY (`trm`) REFERENCES `aeneid2_error` (`trm`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeneid2_main`
--

LOCK TABLES `aeneid2_main` WRITE;
/*!40000 ALTER TABLE `aeneid2_main` DISABLE KEYS */;
INSERT INTO `aeneid2_main` VALUES (1,'arma','arma(1D)','N-[N+Ac]-S','weapons',''),(2,'virum','vir,viri','M-Ac-S','man',''),(3,'+que','+que','Conj','and',''),(4,'cano','cano,-ere,ceceni,-tus','1S-P-I-A','to sing','fact'),(5,'Troiae','Troia,-ae','F-[G+D+N]-[S+P]','Troy',''),(6,'qui','qui,quae,quod','M-N-[S+P]','rel./inq.',''),(7,'primus','primus,-a,-um','M-N-S','first','w/'),(8,'ab','ab','Prep+Ab','from, by',''),(9,'oris','os,oris','N-G-S','mouth',''),(10,'Italiam','Italia,-ae','F-Ac-S','Italy',''),(11,'fato','fatum,-i','N-[D+Ab]-S','fate',''),(12,'profugus','','','',''),(13,'Lavinia','','','',''),(14,'+que','+que','Conj','and',''),(15,'venit','venio,-ire,-i,-tus','','to come',''),(16,'litora','litus,litoris','N-[N+Ac]-P','shore',''),(17,'multum','multus,-a,-um','[M+N]-[Ac+N]-S','many','w/'),(18,'ille','ille,illa,illud','[M+N]-[N+V]-S','that',''),(19,'et','et','Conj','and',''),(20,'terris','terra,-ae','F-[D+Ab]-P','land',''),(21,'iactatus','iacto(1)','Pf-Ppl-P/M-N-S','to cast',''),(22,'et','et','Conj','and',''),(23,'alto','alo,-ere,-ui,-tus','Pf-Ppl-P/[M+N]-[D+Ab]-S','to nourish',''),(24,'vi','vis,vis','F-D-S','force (pl)strength',''),(25,'superum','superus,-a,-um','[M+N]-[Ac+N]-S','superior','w/'),(26,'saevae','','','',''),(27,'memorem','','','',''),(28,'Iunonis','Iuno,Iunonis','F-G-S','Juno',''),(29,'ob','ob','Prep+Ac','on account of',''),(30,'iram','','','',''),(31,'multa','multus,-a,-um','[F+N]-[N+Ab+Ac]-[S(Pos.)+P(Pos.)]','many','w/'),(32,'quo','qui,quae,quod','[M+N]-Ab-S','rel./inq.',''),(33,'+que','+que','Conj','and',''),(34,'et','et','Conj','and',''),(35,'bello','','','',''),(36,'passus','patior,pati,passus sum','Pf-Ppl-P/M-N-S','to endure',''),(37,'dum','dum','Conj','while(I)/until(S)',''),(38,'conderet','condo,-ere,-idi,-itus','3S-Impf-S-A','to establish',''),(39,'urbem','urbs,urbis','F-Ac-S','city',''),(40,'inferret','','','',''),(41,'+que','+que','Conj','and',''),(42,'deos','deus,-i','M-Ac-P','god',''),(43,'Latio','','','',''),(44,'genus','genus,generis','N-[N+Ac]-S','origin',''),(45,'unde','','','',''),(46,'Latinum','Latinus,-a,-um','[M+N]-[Ac+N]-S','Latin','w/'),(47,'Albani','','','',''),(48,'+que','+que','Conj','and',''),(49,'patres','pater,patris','M-[N+Ac]-P','father',''),(50,'atque','atque','Conj','and',''),(51,'altae','alo,-ere,-ui,-tus','Pf-Ppl-P/F-[G+D+N]-[S+P]','to nourish',''),(52,'moenia','moene,moenis','N-[N+Ac]-P','city walls',''),(53,'Romae','','','','');
/*!40000 ALTER TABLE `aeneid2_main` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-15 23:08:42
