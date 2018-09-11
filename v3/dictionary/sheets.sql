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
INSERT INTO `aeneid1_main` VALUES (1,'arma','arma(1D)','N-[N+Ac]-S','weapons',NULL),(2,'virum','vir,viri','M-Ac-S','man',NULL),(3,'+que','+que','Conj',NULL,NULL),(4,'cano','cano,-ere,ceceni,-tus','1S-P-I-A','to sing','fact'),(5,'Troiae','Troia,-ae','F-[G+D+N]-[S+P]','Troy',NULL),(6,'qui','qui,quae,quod','M-N-[S+P]','rel./inq.',NULL),(7,'primus','primus,-a,-um','M-N-S','first','w/'),(8,'ab','ab','Prep+Ab','from, by',NULL),(9,'oris','os,oris','N-G-S','mouth',NULL),(10,'Italiam','Italia,-ae','F-Ac-S','Italy',NULL),(11,'fato','fatum,-i','N-[D+Ab]-S','fate',NULL),(12,'profugus',NULL,NULL,NULL,NULL),(13,'Lavinia',NULL,NULL,NULL,NULL),(14,'+que','+que','Conj','and',NULL),(15,'venit','venio,-ire,-i,-tus',NULL,'to come',NULL),(16,'litora','litus,litoris','N-[N+Ac]-P','shore',NULL),(17,'multum','multus,-a,-um','[M+N]-[Ac+N]-S','many','w/'),(18,'ille','ille,illa,illud','[M+N]-[N+V]-S','that',NULL),(19,'et','et','Conj','and',NULL),(20,'terris','terra,-ae','F-[D+Ab]-P','land',NULL),(21,'iactatus','iacto(1)','Pf-Ppl-P/M-N-S','to cast',NULL),(22,'et','et','Conj','and',NULL),(23,'alto','alo,-ere,-ui,-tus','Pf-Ppl-P/[M+N]-[D+Ab]-S','to nourish',NULL),(24,'vi','vis,vis','F-D-S','force (pl)strength',NULL),(25,'superum','superus,-a,-um','[M+N]-[Ac+N]-S','superior','w/'),(26,'saevae',NULL,NULL,NULL,NULL),(27,'memorem',NULL,NULL,NULL,NULL),(28,'Iunonis','Iuno,Iunonis','F-G-S','Juno',NULL),(29,'ob','ob','Prep+Ac','on account of',NULL),(30,'iram',NULL,NULL,NULL,NULL),(31,'multa','multus,-a,-um','[F+N]-[N+Ab+Ac]-[S(Pos.)+P(Pos.)]','many','w/'),(32,'quo','qui,quae,quod','[M+N]-Ab-S','rel./inq.',NULL),(33,'+que','+que','Conj','and',NULL),(34,'et','et','Conj','and',NULL),(35,'bello',NULL,NULL,NULL,NULL),(36,'passus','patior,pati,passus sum','Pf-Ppl-P/M-N-S','to endure',NULL),(37,'dum','dum','Conj','while(I)/until(S)',NULL),(38,'conderet','condo,-ere,-idi,-itus','3S-Impf-S-A','to establish',NULL),(39,'urbem','urbs,urbis','F-Ac-S','city',NULL),(40,'inferret',NULL,NULL,NULL,NULL),(41,'+que','+que','Conj','and',NULL),(42,'deos','deus,-i','M-Ac-P','god',NULL),(43,'Latio',NULL,NULL,NULL,NULL),(44,'genus','genus,generis','N-[N+Ac]-S','origin',NULL),(45,'unde',NULL,NULL,NULL,NULL),(46,'Latinum','Latinus,-a,-um','[M+N]-[Ac+N]-S','Latin','w/'),(47,'Albani',NULL,NULL,NULL,NULL),(48,'+que','+que','Conj','and',NULL),(49,'patres','pater,patris','M-[N+Ac]-P','father',NULL),(50,'atque','atque','Conj','and',NULL),(51,'altae','alo,-ere,-ui,-tus','Pf-Ppl-P/F-[G+D+N]-[S+P]','to nourish',NULL),(52,'moenia','moene,moenis','N-[N+Ac]-P','city walls',NULL),(53,'Romae',NULL,NULL,NULL,NULL);
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

--
-- Table structure for table `aeneid300_1_error`
--

DROP TABLE IF EXISTS `aeneid300_1_error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `aeneid300_1_error` (
  `trm` varchar(20) NOT NULL,
  `type` varchar(8) NOT NULL,
  `conf1` varchar(50) DEFAULT NULL,
  `conf2` varchar(50) DEFAULT NULL,
  `conf3` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`trm`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeneid300_1_error`
--

LOCK TABLES `aeneid300_1_error` WRITE;
/*!40000 ALTER TABLE `aeneid300_1_error` DISABLE KEYS */;
INSERT INTO `aeneid300_1_error` VALUES ('+que','none',NULL,NULL,NULL),('ab','none',NULL,NULL,NULL),('ac','none',NULL,NULL,NULL),('accesserit','unknown',NULL,NULL,NULL),('accipit','none',NULL,NULL,NULL),('Achate','unknown',NULL,NULL,NULL),('adstitit','unknown',NULL,NULL,NULL),('Aeneas','unknown',NULL,NULL,NULL),('aera','none',NULL,NULL,NULL),('ait','none',NULL,NULL,NULL),('alarum','unknown',NULL,NULL,NULL),('alma','unknown',NULL,NULL,NULL),('alto','none',NULL,NULL,NULL),('animum','none',NULL,NULL,NULL),('arboribus','none',NULL,NULL,NULL),('arceret','unknown',NULL,NULL,NULL),('arces','none',NULL,NULL,NULL),('at','none',NULL,NULL,NULL),('atque','none',NULL,NULL,NULL),('benignam','unknown',NULL,NULL,NULL),('bina','unknown',NULL,NULL,NULL),('cauata','unknown',NULL,NULL,NULL),('circum','multi','circum Prep+Ac around','circus,circi M-Ac-S circle',NULL),('citus','unknown',NULL,NULL,NULL),('classem','none',NULL,NULL,NULL),('clausam','unknown',NULL,NULL,NULL),('comitatus','unknown',NULL,NULL,NULL),('constituit','unknown',NULL,NULL,NULL),('conuexo','unknown',NULL,NULL,NULL),('corda','none',NULL,NULL,NULL),('crispans','unknown',NULL,NULL,NULL),('cui','none',NULL,NULL,NULL),('data','none',NULL,NULL,NULL),('demittit','unknown',NULL,NULL,NULL),('deo','none',NULL,NULL,NULL),('Dido','unknown',NULL,NULL,NULL),('est','none',NULL,NULL,NULL),('et','none',NULL,NULL,NULL),('exacta','unknown',NULL,NULL,NULL),('exire','unknown',NULL,NULL,NULL),('explorare','unknown',NULL,NULL,NULL),('facit','none',NULL,NULL,NULL),('fati','none',NULL,NULL,NULL),('feraene','unknown',NULL,NULL,NULL),('ferocia','unknown',NULL,NULL,NULL),('ferro','none',NULL,NULL,NULL),('finibus','none',NULL,NULL,NULL),('genitum','none',NULL,NULL,NULL),('graditur','unknown',NULL,NULL,NULL),('haec','none',NULL,NULL,NULL),('hastilia','unknown',NULL,NULL,NULL),('hominesne','unknown',NULL,NULL,NULL),('horrentibus','unknown',NULL,NULL,NULL),('hospitio','unknown',NULL,NULL,NULL),('iam','none',NULL,NULL,NULL),('ille','none',NULL,NULL,NULL),('in','none',NULL,NULL,NULL),('inculta','unknown',NULL,NULL,NULL),('ipse','none',NULL,NULL,NULL),('iussa','none',NULL,NULL,NULL),('Karthaginis','unknown',NULL,NULL,NULL),('lato','multi','fero,ferre,tuli,latus Pf-Ppl-P/[M+N]-[D+Ab]-S to b','latus,lata,latum [M+N]-[D+Ab]-S wide',NULL),('Libyae','unknown',NULL,NULL,NULL),('locos','none',NULL,NULL,NULL),('lux','none',NULL,NULL,NULL),('magnum','none',NULL,NULL,NULL),('Maia','unknown',NULL,NULL,NULL),('manu','none',NULL,NULL,NULL),('mater','none',NULL,NULL,NULL),('media','none',NULL,NULL,NULL),('mentem','none',NULL,NULL,NULL),('nam','none',NULL,NULL,NULL),('ne','none',NULL,NULL,NULL),('nemorum','none',NULL,NULL,NULL),('nescia','unknown',NULL,NULL,NULL),('noctem','none',NULL,NULL,NULL),('nouae','unknown',NULL,NULL,NULL),('nouos','unknown',NULL,NULL,NULL),('obuia','unknown',NULL,NULL,NULL),('occulit','unknown',NULL,NULL,NULL),('oras','unknown',NULL,NULL,NULL),('oris','none',NULL,NULL,NULL),('pateant','none',NULL,NULL,NULL),('per','none',NULL,NULL,NULL),('pius','unknown',NULL,NULL,NULL),('plurima','none',NULL,NULL,NULL),('Poeni','unknown',NULL,NULL,NULL),('ponunt','none',NULL,NULL,NULL),('primis','none',NULL,NULL,NULL),('primum','none',NULL,NULL,NULL),('quaerere','none',NULL,NULL,NULL),('quas','none',NULL,NULL,NULL),('qui','none',NULL,NULL,NULL),('quietum','unknown',NULL,NULL,NULL),('referre','unknown',NULL,NULL,NULL),('regina','unknown',NULL,NULL,NULL),('remigio','unknown',NULL,NULL,NULL),('rupe','unknown',NULL,NULL,NULL),('sese','unknown',NULL,NULL,NULL),('silua','unknown',NULL,NULL,NULL),('sociis','unknown',NULL,NULL,NULL),('sub','none',NULL,NULL,NULL),('teneant','none',NULL,NULL,NULL),('terrae','none',NULL,NULL,NULL),('Teucris','unknown',NULL,NULL,NULL),('Teucros','unknown',NULL,NULL,NULL),('tulit','none',NULL,NULL,NULL),('uento','unknown',NULL,NULL,NULL),('uidet','unknown',NULL,NULL,NULL),('umbris','none',NULL,NULL,NULL),('uno','multi','unus,una,unum [M+N]-Ab-S one','unus,una,unum [M+N]-[D+Ab]-S one',NULL),('uolat','unknown',NULL,NULL,NULL),('uolente','unknown',NULL,NULL,NULL),('uoluens','unknown',NULL,NULL,NULL),('ut','none',NULL,NULL,NULL);
/*!40000 ALTER TABLE `aeneid300_1_error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aeneid300_1_main`
--

DROP TABLE IF EXISTS `aeneid300_1_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `aeneid300_1_main` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `trm` varchar(20) NOT NULL,
  `dct` varchar(30) DEFAULT NULL,
  `prs` varchar(40) DEFAULT NULL,
  `trn` varchar(20) DEFAULT NULL,
  `cmt` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_aeneid300_1_main` (`trm`),
  CONSTRAINT `FK_aeneid300_1_main` FOREIGN KEY (`trm`) REFERENCES `aeneid300_1_error` (`trm`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeneid300_1_main`
--

LOCK TABLES `aeneid300_1_main` WRITE;
/*!40000 ALTER TABLE `aeneid300_1_main` DISABLE KEYS */;
INSERT INTO `aeneid300_1_main` VALUES (1,'haec','hic,haec,hoc','N-[N+Ac]-P','this',NULL),(2,'ait','ait','2S-P-Imp-A','to he says',NULL),(3,'et','et','Conj','and',NULL),(4,'Maia',NULL,NULL,NULL,NULL),(5,'genitum','gigno,-ere,genui,genitus','Pf-Ppl-P/[M+N]-[Ac+N]-S','to give birth to',NULL),(6,'demittit',NULL,NULL,NULL,NULL),(7,'ab','ab','Prep+Ab','from, by',NULL),(8,'alto','alo,-ere,-ui,-tus','Pf-Ppl-P/[M+N]-[D+Ab]-S','to nourish',NULL),(9,'ut','ut','Conj','.',NULL),(10,'terrae','terra,-ae','F-[G+D+N]-[S+P]','land',NULL),(11,'ut','ut','Conj','.',NULL),(12,'+que','+que','Conj','and',NULL),(13,'nouae',NULL,NULL,NULL,NULL),(14,'pateant','pateo,-ere,-ui,-us','3P-P-S-A','to lie open',NULL),(15,'Karthaginis',NULL,NULL,NULL,NULL),(16,'arces','arx,arcis','F-[N+Ac]-P','summit',NULL),(17,'hospitio',NULL,NULL,NULL,NULL),(18,'Teucris',NULL,NULL,NULL,NULL),(19,'ne','ne','Conj','.',NULL),(20,'fati','fatum,-i','N-G-S','fate',NULL),(21,'nescia',NULL,NULL,NULL,NULL),(22,'Dido',NULL,NULL,NULL,NULL),(23,'finibus','finis,finis','M-[D+Ab]-P','boundary',NULL),(24,'arceret',NULL,NULL,NULL,NULL),(25,'uolat',NULL,NULL,NULL,NULL),(26,'ille','ille,illa,illud','[M+N]-[N+V]-S','that',NULL),(27,'per','per','Prep+Ac','through, because of',NULL),(28,'aera','aes,aeris','N-[N+Ac]-P','copper?bronze',NULL),(29,'magnum','magnus,-a,-um','[M+N]-[Ac+N]-S','great','w/'),(30,'remigio',NULL,NULL,NULL,NULL),(31,'alarum',NULL,NULL,NULL,NULL),(32,'ac','atque','Conj','and',NULL),(33,'Libyae',NULL,NULL,NULL,NULL),(34,'citus',NULL,NULL,NULL,NULL),(35,'adstitit',NULL,NULL,NULL,NULL),(36,'oris','os,oris','N-G-S','mouth',NULL),(37,'et','et','Conj','and',NULL),(38,'iam','iam','Adv','already','w/'),(39,'iussa','iubeo,-ere,iussi,iussus','Pf-Ppl-P/[F+N]-[N+Ab]-[S+P]','to order',NULL),(40,'facit','facio,-ere,feci,-tus','3S-P-I-A','to make','fact'),(41,'ponunt','pono,-ere,posui,positus','3P-P-I-A','to place','fact'),(42,'+que','+que','Conj','and',NULL),(43,'ferocia',NULL,NULL,NULL,NULL),(44,'Poeni',NULL,NULL,NULL,NULL),(45,'corda','cor,cordis','N-[N+Ac]-P','heart',NULL),(46,'uolente',NULL,NULL,NULL,NULL),(47,'deo','deus,-i','M-[D+Ab]-S','god',NULL),(48,'in','in','Prep+Ab/Ac','in, on/into, onto',NULL),(49,'primis','primus,-a,-um','[M+F+N]-[D+Ab]-P','first','w/'),(50,'regina',NULL,NULL,NULL,NULL),(51,'quietum',NULL,NULL,NULL,NULL),(52,'accipit','accipio,-ere,accepi,acceptus','3S-P-I-A','to accept','fact'),(53,'in','in','Prep+Ab/Ac','in, on/into, onto',NULL),(54,'Teucros',NULL,NULL,NULL,NULL),(55,'animum','animus,-i','M-Ac-S','mind',NULL),(56,'mentem','mens,-ntis','F-Ac-S','mind',NULL),(57,'+que','+que','Conj','and',NULL),(58,'benignam',NULL,NULL,NULL,NULL),(59,'at','at','Conj','but',NULL),(60,'pius',NULL,NULL,NULL,NULL),(61,'Aeneas',NULL,NULL,NULL,NULL),(62,'per','per','Prep+Ac','through, because of',NULL),(63,'noctem','nox,noctis','F-Ac-S','night',NULL),(64,'plurima','multus,-a,-um','[F+N]-[N+Ac]-[S(Sup.)+P(Sup.)]','many','w/'),(65,'uoluens',NULL,NULL,NULL,NULL),(66,'ut','ut','Conj','.',NULL),(67,'primum','primus,-a,-um','[M+N]-[Ac+N]-S','first','w/'),(68,'lux','lux,lucis','F-N-S','light',NULL),(69,'alma',NULL,NULL,NULL,NULL),(70,'data','do(1)','Pf-Ppl-P/[F+N]-[N+Ab]-[S+P]','to give',NULL),(71,'est','sum,esse,fui','3S-P-I-A','to be','fact'),(72,'exire',NULL,NULL,NULL,NULL),(73,'locos','locus,-i','M-Ac-P','place',NULL),(74,'+que','+que','Conj','and',NULL),(75,'explorare',NULL,NULL,NULL,NULL),(76,'nouos',NULL,NULL,NULL,NULL),(77,'quas','qui,quae,quod','F-Ac-P','rel./inq.',NULL),(78,'uento',NULL,NULL,NULL,NULL),(79,'accesserit',NULL,NULL,NULL,NULL),(80,'oras',NULL,NULL,NULL,NULL),(81,'qui','qui,quae,quod','M-N-[S+P]','rel./inq.',NULL),(82,'teneant','teneo,-ere,-ui,-tus','3P-P-S-A','to hold',NULL),(83,'nam','nam','Conj','for',NULL),(84,'inculta',NULL,NULL,NULL,NULL),(85,'uidet',NULL,NULL,NULL,NULL),(86,'hominesne',NULL,NULL,NULL,NULL),(87,'feraene',NULL,NULL,NULL,NULL),(88,'quaerere','quaero,-ere,quaesivi,quaesitus','{P-Inf-A};{2S-[P+F]-I-P}','to look for',NULL),(89,'constituit',NULL,NULL,NULL,NULL),(90,'sociis',NULL,NULL,NULL,NULL),(91,'+que','+que','Conj','and',NULL),(92,'exacta',NULL,NULL,NULL,NULL),(93,'referre',NULL,NULL,NULL,NULL),(94,'classem','classis,classis','F-Ac-S','class',NULL),(95,'in','in','Prep+Ab/Ac','in, on/into, onto',NULL),(96,'conuexo',NULL,NULL,NULL,NULL),(97,'nemorum','nemus,nemoris','N-G-P','grove',NULL),(98,'sub','sub','Prep+Ab/Ac','under',NULL),(99,'rupe',NULL,NULL,NULL,NULL),(100,'cauata',NULL,NULL,NULL,NULL),(101,'arboribus','arbor,-oris','F-[D+Ab]-P','tree',NULL),(102,'clausam',NULL,NULL,NULL,NULL),(103,'circum',NULL,NULL,NULL,NULL),(104,'atque','atque','Conj','and',NULL),(105,'horrentibus',NULL,NULL,NULL,NULL),(106,'umbris','umbra,-ae','F-[D+Ab]-P','shadow',NULL),(107,'occulit',NULL,NULL,NULL,NULL),(108,'ipse','ipse,ipsa,ipsum','[M+N]-[N+V]-S','refl. adj.',NULL),(109,'uno','unus,-a,-um',NULL,'one',NULL),(110,'graditur',NULL,NULL,NULL,NULL),(111,'comitatus',NULL,NULL,NULL,NULL),(112,'Achate',NULL,NULL,NULL,NULL),(113,'bina',NULL,NULL,NULL,NULL),(114,'manu','manus,-us','F-Ab-S','hand, band',NULL),(115,'lato',NULL,NULL,NULL,NULL),(116,'crispans',NULL,NULL,NULL,NULL),(117,'hastilia',NULL,NULL,NULL,NULL),(118,'ferro','ferrum,-i','N-[D+Ab]-S','iron',NULL),(119,'cui','qui,quae,quod','[M+F+N]-D-S','rel./inq.',NULL),(120,'mater','mater,matris','F-N-S','mother',NULL),(121,'media','medius,-a,-um','[F+N]-[N+Ab+Ac]-[S(Pos.)+P(Pos.)]','middle','w/'),(122,'sese',NULL,NULL,NULL,NULL),(123,'tulit','fero,-rre,tuli,latus','3S-Pf-I-A','to bear, speak','fact'),(124,'obuia',NULL,NULL,NULL,NULL),(125,'silua',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `aeneid300_1_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sep7test2_error`
--

DROP TABLE IF EXISTS `sep7test2_error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sep7test2_error` (
  `trm` varchar(20) NOT NULL,
  `type` varchar(8) NOT NULL,
  `conf1` varchar(50) DEFAULT NULL,
  `conf2` varchar(50) DEFAULT NULL,
  `conf3` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`trm`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sep7test2_error`
--

LOCK TABLES `sep7test2_error` WRITE;
/*!40000 ALTER TABLE `sep7test2_error` DISABLE KEYS */;
INSERT INTO `sep7test2_error` VALUES ('+que','none',NULL,NULL,NULL),('ab','none',NULL,NULL,NULL),('arma','none',NULL,NULL,NULL),('cano','none',NULL,NULL,NULL),('oris','none',NULL,NULL,NULL),('primus','none',NULL,NULL,NULL),('profugus','none',NULL,NULL,NULL),('qui','none',NULL,NULL,NULL),('Troiae','none',NULL,NULL,NULL),('virum','none',NULL,NULL,NULL);
/*!40000 ALTER TABLE `sep7test2_error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sep7test2_main`
--

DROP TABLE IF EXISTS `sep7test2_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sep7test2_main` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `trm` varchar(20) NOT NULL,
  `dct` varchar(30) DEFAULT NULL,
  `prs` varchar(40) DEFAULT NULL,
  `trn` varchar(20) DEFAULT NULL,
  `cmt` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_sep7test2_main` (`trm`),
  CONSTRAINT `FK_sep7test2_main` FOREIGN KEY (`trm`) REFERENCES `sep7test2_error` (`trm`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sep7test2_main`
--

LOCK TABLES `sep7test2_main` WRITE;
/*!40000 ALTER TABLE `sep7test2_main` DISABLE KEYS */;
INSERT INTO `sep7test2_main` VALUES (1,'arma','arma(1D)','N-[N+Ac]-S','weapons',''),(2,'virum','vir,viri','M-Ac-S','man',''),(3,'+que','+que','Conj','and',''),(4,'cano','cano,-ere,ceceni,-tus','1S-P-I-A','to sing','fact'),(5,'Troiae','Troia,-ae','F-[G+D+N]-[S+P]','Troy',''),(6,'qui','qui,quae,quod','M-N-[S+P]','rel./inq.',''),(7,'primus','primus,-a,-um','M-N-S','first','w/'),(8,'ab','ab','Prep+Ab','from, by',''),(9,'oris','os,oris','N-G-S','mouth',''),(10,'profugus','','','','');
/*!40000 ALTER TABLE `sep7test2_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sep7test_error`
--

DROP TABLE IF EXISTS `sep7test_error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sep7test_error` (
  `trm` varchar(20) NOT NULL,
  `type` varchar(8) NOT NULL,
  `conf1` varchar(50) DEFAULT NULL,
  `conf2` varchar(50) DEFAULT NULL,
  `conf3` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`trm`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sep7test_error`
--

LOCK TABLES `sep7test_error` WRITE;
/*!40000 ALTER TABLE `sep7test_error` DISABLE KEYS */;
INSERT INTO `sep7test_error` VALUES ('+que','none',NULL,NULL,NULL),('ab','none',NULL,NULL,NULL),('arma','none',NULL,NULL,NULL),('cano','none',NULL,NULL,NULL),('oris','none',NULL,NULL,NULL),('primus','none',NULL,NULL,NULL),('qui','none',NULL,NULL,NULL),('Troiae','none',NULL,NULL,NULL),('virum','none',NULL,NULL,NULL);
/*!40000 ALTER TABLE `sep7test_error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sep7test_main`
--

DROP TABLE IF EXISTS `sep7test_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sep7test_main` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `trm` varchar(20) NOT NULL,
  `dct` varchar(30) DEFAULT NULL,
  `prs` varchar(40) DEFAULT NULL,
  `trn` varchar(20) DEFAULT NULL,
  `cmt` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_sep7test_main` (`trm`),
  CONSTRAINT `FK_sep7test_main` FOREIGN KEY (`trm`) REFERENCES `sep7test_error` (`trm`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sep7test_main`
--

LOCK TABLES `sep7test_main` WRITE;
/*!40000 ALTER TABLE `sep7test_main` DISABLE KEYS */;
INSERT INTO `sep7test_main` VALUES (1,'arma','arma(1D)','N-[N+Ac]-S','weapons',''),(2,'virum','vir,viri','M-Ac-S','man',''),(3,'+que','+que','Conj','and',''),(4,'cano','cano,-ere,ceceni,-tus','1S-P-I-A','to sing','fact'),(5,'Troiae','Troia,-ae','F-[G+D+N]-[S+P]','Troy',''),(6,'qui','qui,quae,quod','M-N-[S+P]','rel./inq.',''),(7,'primus','primus,-a,-um','M-N-S','first','w/'),(8,'ab','ab','Prep+Ab','from, by',''),(9,'oris','os,oris','N-G-S','mouth','');
/*!40000 ALTER TABLE `sep7test_main` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-11  8:33:53
