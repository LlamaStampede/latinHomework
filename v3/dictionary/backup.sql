-- MySQL dump 10.13  Distrib 8.0.11, for macos10.13 (x86_64)
--
-- Host: localhost    Database: TLD_DCT
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
-- Current Database: `TLD_DCT`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `TLD_DCT` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

USE `TLD_DCT`;

--
-- Table structure for table `adjs`
--

DROP TABLE IF EXISTS `adjs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `adjs` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `term1` varchar(20) DEFAULT NULL,
  `term2` varchar(20) DEFAULT NULL,
  `term3` varchar(20) DEFAULT NULL,
  `trn` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adjs`
--

LOCK TABLES `adjs` WRITE;
/*!40000 ALTER TABLE `adjs` DISABLE KEYS */;
INSERT INTO `adjs` VALUES (1,'furiosus','-a','-um','raging'),(2,'improbus','-a','-um','wicked'),(3,'publicus','-a','-um','public'),(4,'antiquus','-a','-um','ancient'),(5,'magnus','-a','-um','great'),(6,'meus','-a','-um','my'),(7,'multus','-a','-um','many'),(8,'tuus','-a','-um','your'),(9,'avarus','-a','-um','greedy'),(10,'paucus','-a','-um','few(pl)'),(11,'Romanus','-a','-um','Roman'),(12,'bellus','-a','-um','handsome'),(13,'bonus','-a','-um','good'),(14,'humanus','-a','-um','human'),(15,'malus','-a','-um','bad'),(16,'parvus','-a','-um','small'),(17,'stultus','-a','-um','foolish'),(18,'verus','-a','-um','true'),(19,'liber','libera','liberum','free'),(20,'noster','nostra','nostrum','our'),(21,'pulcher','pulchra','pulchrum','beautiful'),(22,'sanus','-a','-um','sane'),(23,'Graecus','-a','-um','Greek'),(24,'perpetuus','-a','-um','continuous'),(25,'plenus','-a','-um','abundant'),(26,'salvus','-a','-um','safe'),(27,'secundus','-a','-um','second'),(28,'vester','vestra','vestrum','your'),(29,'novus','-a','-um','new'),(30,'beatus','-a','-um','happy'),(31,'amicus','-a','-um','friendly'),(32,'carus','-a','-um','dear'),(33,'acerbus','-a','-um','bitter'),(34,'doctus','-a','-um','learned'),(35,'fortunatus','-a','-um','fortunate'),(36,'suus','-a','-um','refl. adj.'),(37,'miser','misera','miserum','wretched'),(38,'unus','-a','-um','one'),(39,'acer','acris','acre','sharp'),(40,NULL,'brevis','breve','short'),(41,'celer','celeris','celere','swift'),(42,NULL,'difficilis','difficile','difficult'),(43,NULL,'dulcis','dulce','sweet'),(44,NULL,'facilis','facile','easy'),(45,NULL,'fortis','forte','strong'),(46,NULL,'incredibilis','incredibile','incredible'),(47,NULL,'ingens','ingentis','huge'),(48,'iucundus','-a','-um','pleasant'),(49,'longus','-a','-um','long'),(50,NULL,'omnis','omne','all'),(51,NULL,'potens','potentis','able'),(52,'caecus','-a','-um','blind'),(53,NULL,'levis','leve','light'),(54,'clarus','-a','-um','clear'),(55,NULL,'mortalis','mortale','mortal'),(56,'certus','-a','-um','certain'),(57,NULL,'gravis','grave','heavy! serious'),(58,NULL,'immortalis','immortale','immortal'),(59,NULL,'communis','commune','common'),(60,'dexter','dextra','dextrum','right-hand'),(61,'sinister','sinistra','sinistrum','left-hand'),(62,'asper','aspera','asperum','rough'),(63,'aequus','-a','-um','level'),(64,NULL,'felix','felicis','lucky'),(65,'incertus','-a','-um','uncertain'),(66,'Latinus','-a','-um','Latin'),(67,'medius','-a','-um','middle'),(68,'magnanimus','-a','-um','magnanimous'),(69,NULL,'ferox','ferocis','fierce! savage'),(70,NULL,'fidelis','fidele','loyal'),(71,'geminus','-a','-um','twin'),(72,NULL,'sapiens','sapientis','wise'),(73,'ultimus','-a','-um','last'),(74,'pudicus','-a','-um','modest'),(75,'superbus','-a','-um','arrogant'),(76,NULL,'tristis','triste','sad'),(77,NULL,'turpis','turpe','ugly'),(78,'urbanus','-a','-um','urban'),(79,NULL,'diligens','diligentis','diligent'),(80,NULL,'dissimilis','dissimile','different'),(81,NULL,'gracilis','gracile','slender'),(82,NULL,'humilis','humile','humble'),(83,'primus','-a','-um','first'),(84,NULL,'similis','simile','similar'),(85,'superus','-a','-um','superior'),(86,NULL,'utilis','utile','useful'),(87,'mortuus','-a','-um','dead'),(88,NULL,'princeps','principis','chief'),(89,'dignus','-a','-um','worthy'),(90,'durus','-a','-um','hard'),(91,'tantus','-a','-um','so great'),(92,'ceterus','-a','-um','the rest!others(pl)'),(93,'quantus','-a','-um','how great'),(94,'ridiculus','-a','-um','ridiculous'),(95,'vivus','-a','-um','alive'),(96,NULL,'mediocris','medicre','mediocre'),(97,NULL,'dives','divitis','rich'),(98,NULL,'par','paris','equal'),(99,NULL,'pauper','pauperis','poor'),(100,'candidus','-a','-um','bright'),(101,'merus','-a','-um','pure'),(102,NULL,'suavis','suave','sweet'),(103,'adversus','-a','-um','opposite'),(104,NULL,'talis','tale','such'),(105,'iratus','-a','-um','angry'),(106,NULL,'absens','absentis','absent'),(107,'gratus','-a','-um','pleasing'),(108,'idoneus','-a','-um','suitable'),(109,'immotus','-a','-um','unmoved'),(110,'firmus','-a','-um','firm'),(111,'infirmus','-a','-um','weak'),(112,NULL,'mirabilis','mirabilie','remarkable'),(113,'pristinus','-a','-um','former'),(114,NULL,'sublimis','sublime','lofty'),(115,'cupidus','-a','-um','eager'),(116,NULL,'liberalis','liberale','decent!liberal'),(117,NULL,'vetus','veteris','old'),(118,'iustus','-a','-um','just'),(119,NULL,'alacrior','alacrius','happier'),(120,'sanctus','-a','-um','sacred'),(121,'propinquus','-a','-um','near'),(122,'splendidus','-a','-um','splendid'),(123,'lacteus','-a','-um','milky'),(124,'praeclarus','-a','-um','bright'),(125,'sonus','-a','-um','sounding'),(126,'cingula','-a','-um','two'),(127,NULL,'caelestis','caeleste','heavenly'),(128,'rarus','-a','-um','rare/few'),(129,'angustus','-a','-um','confined'),(130,'obliquus','-a','-um','oblique'),(131,'transverus','-a','-um','lying across'),(132,'subnixus','-a','-um','relying on (w/Ab)'),(133,NULL,'habitabilis','habitabile','habitable'),(134,NULL,'australis','australe','southern'),(135,'latus','-a','-um','wide'),(136,'reliquus','-a','-um','rest of'),(137,'futurus','-a','-um','future'),(138,'posterus','-a','-um','coming after'),(139,'aeternus','-a','-um','eternal'),(140,'diuturnus','-a','-um','lasting');
/*!40000 ALTER TABLE `adjs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `advs`
--

DROP TABLE IF EXISTS `advs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `advs` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `trn` varchar(20) NOT NULL,
  `term` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `advs`
--

LOCK TABLES `advs` WRITE;
/*!40000 ALTER TABLE `advs` DISABLE KEYS */;
INSERT INTO `advs` VALUES (1,'yesterday','heri'),(2,'today','hodie'),(3,'tomorrow','cras'),(4,'now','nunc'),(5,'then','tunc'),(6,'later','postea'),(7,'already','iam'),(8,'recently','nuper'),(9,'lately','tarde'),(10,'soon','cito'),(11,'immediately','statim'),(12,'still','etiam'),(13,'yet','etiamnunc'),(14,'ago','abhinc'),(15,'here','hic'),(16,'there','illic'),(17,'over there','illac'),(18,'everywhere','undique'),(19,'anywhere','usquam'),(20,'nowhere','nusquam'),(21,'home','domus'),(22,'away','longe'),(23,'out','foris'),(24,'very','valde'),(25,'quite','satis'),(26,'pretty','satis'),(27,'really','vere'),(28,'fast','velox'),(29,'well','recte'),(30,'hard','difficilis'),(31,'quickly','velociter'),(32,'slowly','sensim'),(33,'carefully','diligenter'),(34,'hardly','aegre'),(35,'barely','vix'),(36,'mostly','plerumque'),(37,'almost','fere'),(38,'absolutely','absolute'),(39,'together','una'),(40,'alone','unus'),(41,'always','semper'),(42,'frequently','saepe'),(43,'usually','solite'),(44,'sometimes','interdum'),(45,'occasionally','aliquando'),(46,'seldom','rare'),(47,'rarely','rare'),(48,'never','numquam'),(49,'not','non'),(50,'finally','tandem'),(51,'previously','pridem'),(52,'indeed','quidem'),(53,'only','non_modo'),(54,'near','prope'),(55,'then','tum'),(56,'now','etiam_num'),(57,'whether','num'),(58,'formerly','quondam'),(59,'todo','denique'),(60,'rather','quam'),(61,'surely','nonne'),(62,'partly','partim'),(63,'by day','diu'),(64,'successively','deinceps');
/*!40000 ALTER TABLE `advs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nouns`
--

DROP TABLE IF EXISTS `nouns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `nouns` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nom` varchar(20) NOT NULL,
  `gen` varchar(20) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `trn` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=388 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nouns`
--

LOCK TABLES `nouns` WRITE;
/*!40000 ALTER TABLE `nouns` DISABLE KEYS */;
INSERT INTO `nouns` VALUES (1,'terra','-ae','2','land'),(2,'vita','-ae','2','life'),(3,'causa','-ae','2','cause'),(4,'fortuna','-ae','2','fortune'),(5,'natura','-ae','2','nature'),(6,'cura','-ae','2','care'),(7,'ira','irae','2','anger'),(8,'via','-ae','2','street'),(9,'unda','-ae','2','wave'),(10,'poena','-ae','2','punishment'),(11,'puella','-ae','2','girl'),(12,'silva','-ae','2','forest'),(13,'umbra','-ae','2','shadow'),(14,'aqua','-ae','2','water'),(15,'fama','-ae','2','rumor'),(16,'flamma','-ae','2','flame'),(17,'turba','-ae','2','crowd'),(18,'copia','-ae','2','abundance (pl)troops'),(19,'patria','-ae','2','fatherland'),(20,'lacrima','-ae','2','tear'),(21,'gloria','-ae','2','glory'),(22,'fuga','-ae','2','flight'),(23,'ara','-ae','2','altar'),(24,'gratia','-ae','2','gratitude'),(25,'iniuria','-ae','2','injustice'),(26,'mora','-ae','2','delay'),(27,'coma','-ae','2','hair'),(28,'aura','-ae','2','breeze'),(29,'forma','-ae','2','shape'),(30,'anima','-ae','2','spirit'),(31,'femina','-ae','2','woman'),(32,'pecunia','-ae','2','money'),(33,'sententia','-ae','2','judgement'),(34,'provincia','-ae','2','province'),(35,'praeda','-ae','2','prey'),(36,'memoria','-ae','2','memory'),(37,'pugna','-ae','2','battle'),(38,'ripa','-ae','2','riverbank'),(39,'hora','-ae','2','hour'),(40,'amicitia','-ae','2','friendship'),(41,'invidia','-ae','2','envy'),(42,'littera','-ae','2','letter (pl)literature'),(43,'divitiae','-arum','2','wealth'),(44,'lingua','-ae','2','language'),(45,'mensa','-ae','2','table'),(46,'victoria','-ae','2','victory'),(47,'porta','-ae','2','gate'),(48,'culpa','-ae','2','fault'),(49,'tenebrae','-brarum','2','darkness'),(50,'sapientia','-ae','2','wisdom'),(51,'opera','-ae','2','work'),(52,'materia','-ae','2','material'),(53,'luna','-ae','2','moon'),(54,'insula','-ae','2','island'),(55,'filia','-ae','2','daughter'),(56,'filius','-i','1','son'),(57,'poeta','-ae','1','poet'),(58,'stella','-ae','2','star'),(59,'familia','-ae','2','family'),(60,'epistula','-ae','2','letter'),(61,'fabula','-ae','2','story'),(62,'scientia','-ae','2','knowledge'),(63,'disciplina','-ae','2','discipline'),(64,'amentia','-ae','2','madness?insanity'),(65,'Africanus','-i','1','Africa'),(66,'amicus','-i','1','friend'),(67,'animus','-i','1','mind'),(68,'deus','-i','1','god'),(69,'dea','-ae','2','goddess'),(70,'locus','-i','1','place'),(71,'vir','viri','1','man'),(72,'bellum','-i','0','war'),(73,'arma','-orum','0','weapons'),(74,'caelum','-i','0','heavens'),(75,'regnum','-i','0','kingdom'),(76,'populus','-i','1','people'),(77,'fatum','-i','0','fate'),(78,'annus','-i','1','year'),(79,'beneficium','-i','0','kindness'),(80,'verbum','-i','0','word'),(81,'puer','pueri','1','boy'),(82,'modus','-i','1','measure'),(83,'imperium','-i','0','command'),(84,'oculus','-i','1','eye'),(85,'natus','-i','1','son'),(86,'derelictus','-i','1','derelict'),(87,'consilium','-i','0','plan council'),(88,'castrum','-i','0','fortress (pl)camp'),(89,'ferrum','-i','0','iron'),(90,'dominus','-i','1','lord'),(91,'domina','-ae','2','mistress'),(92,'equus','-i','1','horse'),(93,'telum','-i','0','spear'),(94,'signum','-i','0','sign'),(95,'periculum','-i','0','danger'),(96,'ventus','-i','1','wind'),(97,'aurum','-i','0','gold'),(98,'saxum','-i','0','rock'),(99,'ager','agri','1','field'),(100,'vitium','-i','0','vice'),(101,'votum','-i','0','vow'),(102,'iugum','-i','0','yoke ridge'),(103,'numerus','-i','1','number'),(104,'proelium','-i','0','battle'),(105,'mundus','-i','1','world'),(106,'tectum','-i','0','roof'),(107,'ingenium','-i','0','ability'),(108,'campus','-i','1','field'),(109,'spatium','-i','0','space'),(110,'somnus','-i','1','sleep'),(111,'studium','-i','0','eagerness'),(112,'legatus','-i','1','lieutenant'),(113,'tergum','-i','0','rear'),(114,'donum','-i','0','gift'),(115,'membrum','-i','0','limb'),(116,'templum','-i','0','region'),(117,'servus','-i','1','slave'),(118,'murus','-i','1','wall'),(119,'exemplum','-i','0','example'),(120,'odium','-i','0','hatred'),(121,'auxilium','-i','0','support'),(122,'praesidium','-i','0','garrison'),(123,'vinculum','-i','0','bond'),(124,'officium','-i','0','duty'),(125,'factum','-i','0','deed'),(126,'pretium','-i','0','price'),(127,'pontus','-i','1','sea'),(128,'oppidum','-i','0','town'),(129,'arvum','-i','0','field'),(130,'vinum','-i','0','wine'),(131,'maritus','-i','1','husband'),(132,'morbus','-i','1','disease'),(133,'vulgus','-i','3','commoner'),(134,'praemium','-i','0','bounty'),(135,'supplicium','-i','0','penalty'),(136,'astrum','-i','0','star'),(137,'dolus','-i','1','device'),(138,'superi','-orum','1','gods'),(139,'otium','-i','0','leisure, peace'),(140,'vestigium','-i','0','footstep'),(141,'gaudium','-i','0','delight'),(142,'humus','-i','2','ground'),(143,'iudicium','-i','0','judgment'),(144,'barbarus','-i','1','foreigner'),(145,'saeculum','-i','0','age'),(146,'exsilium','-i','0','exile'),(147,'tribunus','-i','1','tribune'),(148,'forum','-i','0','market-place?forum'),(149,'praeceptum','-i','0','command'),(150,'negotium','-i','0','business'),(151,'argentum','-i','0','silver'),(152,'gladius','-i','1','sword'),(153,'cibus','-i','1','food'),(154,'initium','-i','0','beginning'),(155,'aevum','-i','0','eternity'),(156,'reus','-i','1','defendant'),(157,'liber','libri','1','book'),(158,'nuntius','-i','1','messenger'),(159,'convivium','-i','0','feast'),(160,'latrocinium','-i','0','robbery'),(161,'damnum','-i','0','damage'),(162,'magister','magistri','1','master'),(163,'frumentum','-i','0','grain'),(164,'principium','-i','0','beginning'),(165,'sepulcrum','-i','0','tomb?grave'),(166,'cupiditas','cupiditatis','2','desire'),(167,'rex','regis','1','king'),(168,'pars','partis','2','part'),(169,'pater','patris','1','father'),(170,'corpus','corporis','0','body'),(171,'urbs','urbis','2','city'),(172,'homo','hominis','1','human'),(173,'tempus','-oris','0','time'),(174,'hostis','-is','3','enemy'),(175,'mors','mortis','2','death'),(176,'virtus','-utis','2','virtue'),(177,'vis','vis','2','force (pl)strength'),(178,'amor','-oris','1','love'),(179,'nox','noctis','2','night'),(180,'caput','capitis','0','head'),(181,'mare','-is','0','sea'),(182,'mater','matris','2','mother'),(183,'nomen','-inis','0','name'),(184,'os','oris','0','mouth'),(185,'ignis','-is','1','fire'),(186,'scelus','-eris','0','crime'),(187,'miles','-itis','1','soldier'),(188,'vox','vocis','2','voice'),(189,'genus','generis','0','origin'),(190,'mens','mentis','2','mind'),(191,'mos','moris','1','custom'),(192,'pectus','-oris','0','chest'),(193,'parens','-ntis','3','parent'),(194,'dolor','-oris','1','pain'),(195,'gens','gentis','2','clan'),(196,'pes','pedis','1','foot'),(197,'labor','-oris','1','toil'),(198,'sanguis','-inis','1','blood'),(199,'coniunx','coniugis','3','spouse'),(200,'frater','fratris','1','brother'),(201,'iter','itineris','0','journey'),(202,'finis','-is','1','boundary'),(203,'dux','ducis','3','leader'),(204,'mons','montis','1','mountain'),(205,'litus','-oris','0','shore'),(206,'carmen','-inis','0','song'),(207,'ratio','-onis','2','reason'),(208,'ars','artis','2','skill'),(209,'lex','legis','2','law'),(210,'munus','muneris','0','offering'),(211,'iuvenis','-is','1','youth'),(212,'flumen','-inis','0','river'),(213,'honor','-oris','1','honor'),(214,'eques','equitis','1','horseman'),(215,'lux','lucis','2','light'),(216,'aetas','-tatis','2','age'),(217,'ius','iuris','0','right'),(218,'ops','opis','2','resources'),(219,'sol','solis','1','sun'),(220,'consul','-ulis','1','consul'),(221,'orbis','-is','1','circle'),(222,'vulnus','-eris','0','wound'),(223,'opus','operis','0','work'),(224,'tellus','telluris','2','earth'),(225,'victor','-oris','1','conqueror'),(226,'civitas','-atis','2','state'),(227,'navis','-is','2','ship'),(228,'agmen','-minis','0','line of march'),(229,'sidus','-eris','0','star'),(230,'auris','-is','2','ear'),(231,'legio','-onis','2','legion'),(232,'lumen','luminis','0','light'),(233,'voluptas','-atis','2','pleasure'),(234,'latus','-eris','0','side?flank'),(235,'pax','pacis','2','peace'),(236,'sedes','-is','2','seat'),(237,'vestis','-is','2','garment'),(238,'caedes','-is','2','slaughter'),(239,'ordo','-inis','1','rank'),(240,'virgo','-inis','2','maiden'),(241,'aequor','aequoris','0','level surface'),(242,'laus','laudis','2','praise'),(243,'comes','comitis','3','comrade'),(244,'numen','-inis','0','divine will'),(245,'nemus','nemoris','0','grove'),(246,'furor','-oris','1','fury'),(247,'amnis','-is','1','torrent'),(248,'arbor','arboris','2','tree'),(249,'civis','-is','3','citizen'),(250,'crimen','-inis','0','verdict?accusation'),(251,'libertas','-atis','2','freedom'),(252,'soror','-oris','2','sister'),(253,'classis','-is','2','class'),(254,'fax','facis','2','torch'),(255,'limen','liminis','0','threshold'),(256,'prex','precis','2','prayers'),(257,'funus','funeris','0','funeral?corpse'),(258,'timor','-oris','1','fear'),(259,'tutor','-oris','1','defender'),(260,'auctor','-oris','1','founder'),(261,'animal','-alis','0','soul'),(262,'decus','decoris','0','grace'),(263,'salus','-utis','2','health'),(264,'uxor','uxoris','2','wife'),(265,'senex','-is','1','elder'),(266,'frons','frontis','2','forehead'),(267,'pecus','-oris','0','cattle'),(268,'sermo','-onis','1','conversation'),(269,'regio','-onis','2','region'),(270,'moenia','-ium','0','city walls'),(271,'clamor','-oris','1','outcry'),(272,'pudor','pudoris','1','modesty'),(273,'custos','custodis','1','guardian'),(274,'pondus','ponderis','0','weight'),(275,'arx','arcis','2','summit'),(276,'sors','sortis','2','destiny'),(277,'facinus','facinoris','0','passionate act?'),(278,'plebs','plebis','2','commoner'),(279,'cohors','cohortis','2','cohort'),(280,'magnitudo','-inis','2','magnitude'),(281,'vates','-is','1','poet'),(282,'canis','-is','3','dog'),(283,'os','ossis','0','bone'),(284,'fons','fontis','1','fountain'),(285,'imperator','-oris','1','commander'),(286,'color','-oris','1','color'),(287,'multitudo','-inis','2','multitude'),(288,'oratio','-onis','2','speech'),(289,'potestas','-atis','2','power'),(290,'testis','-is','1','witness'),(291,'aes','aeris','0','copper?bronze'),(292,'tempestas','-tatis','2','storm'),(293,'imago','-inis','2','image'),(294,'libido','-inis','2','lust'),(295,'maiores','maiorum','1','ancestors'),(296,'pietas','-tatis','2','devotion'),(297,'cinis','cineris','3','ashes'),(298,'cor','cordis','0','heart'),(299,'hiems','hiemis','2','winter'),(300,'bos','bovis','1','ox'),(301,'flos','floris','1','flower'),(302,'fames','-is','2','famine'),(303,'error','-oris','1','error'),(304,'iudex','iudicis','1','judge'),(305,'lapis','lapidis','1','stone'),(306,'onus','oneris','0','burden'),(307,'aer','aeris','1','air'),(308,'aether','aetheris','0','sky'),(309,'avis','-is','2','bird'),(310,'voluntas','-atis','2','desire'),(311,'hospes','hospitis','1','guest?host'),(312,'praetor','-oris','1','praetor'),(313,'rus','ruris','0','country'),(314,'auctoritas','-atis','2','authority'),(315,'cupido','-inis','2','desire'),(316,'necessitas','-tatis','2','necessity'),(317,'condicio','-onis','2','condition'),(318,'sacerdos','-dotis','3','priest'),(319,'consuetudo','-inis','2','custom'),(320,'dignitas','-atis','2','reputation'),(321,'mulier','-eris','2','woman'),(322,'aedes','-is','2','building'),(323,'volucris','-is','3','bird'),(324,'fors','fortis','2','chance'),(325,'fletus','-us','1','tears'),(326,'manus','-us','2','hand, band'),(327,'domus','-us','2','home'),(328,'vultus','-us','1','expression'),(329,'metus','-us','1','fear'),(330,'exercitus','-us','1','army'),(331,'senatus','-us','1','senate'),(332,'casus','-us','1','chance'),(333,'cursus','-us','1','course'),(334,'impetus','-us','1','attack'),(335,'usus','-us','1','use'),(336,'sinus','-us','1','crease, bay'),(337,'currus','-us','1','chariot'),(338,'fluctus','-us','1','flood'),(339,'gradus','-us','1','step?rank'),(340,'cornu','-us','0','horn'),(341,'spiritus','-us','1','spirit'),(342,'sensus','-us','1','sense'),(343,'ictus','-us','1','stroke'),(344,'fructus','-us','1','fruit'),(345,'res','rei','2','thing'),(346,'dies','diei','3','day'),(347,'fides','-ei','2','trust?faith'),(348,'spes','spei','2','hope'),(349,'acies','-ei','2','line'),(350,'facies','-ei','2','form'),(351,'species','-ei','2','aspect'),(352,'detrimentum','-i','0','damage'),(353,'seditio','seditionis','2','sedition'),(354,'suspicio','suspicionis','2','suspicion'),(355,'magnitudo','magnitudinis','2','magnitude'),(356,'Scipio','Scipionis','1','Scipio'),(357,'avus','avi','1','grandfather'),(358,'iustitia','iustitiae','2','justice'),(359,'pietas','pietatis','2','piety'),(360,'coetus','coetus','1','union'),(361,'candor','candoris','1','radiance'),(362,'circus','-i','1','circle'),(363,'globus','-i','1','globe'),(364,'intervallum','-i','0','interval'),(365,'ratio','rationis','2','reason'),(366,'cingula','-ae','2','belt'),(367,'inpulsus','-us','1','impetus'),(368,'motus','-us','1','motion'),(369,'celebritas','celebritatis','2','multitude/renown'),(370,'sermo','sermonis','1','discussion'),(371,'macula','-ae','2','stain'),(372,'solitudo','solitudinis','2','solitude'),(373,'vertex','verticis','1','vortex'),(374,'pruina','-ae','2','rime'),(375,'ardor','ardoris','1','flame'),(376,'aquilo','aquilonis','1','north wind'),(377,'Atlanticus','-i','1','Atlantic'),(378,'Oceanus','-i','1','Ocean'),(379,'oriens','orientis','1','rise'),(380,'austrum','austri','0','purple'),(381,'angustia','-ae','2','narrow pass'),(382,'proles','prolis','2','offspring'),(383,'eluvio','eluvionis','2','inundation'),(384,'exustio','exustionis','2','conflagration'),(385,'Troia','Troiae','2','Troy'),(386,'Italia','Italiae','2','Italy'),(387,'Iuno','Iunonis','2','Juno');
/*!40000 ALTER TABLE `nouns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preps`
--

DROP TABLE IF EXISTS `preps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `preps` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `term` varchar(10) NOT NULL,
  `takesCase` int(1) NOT NULL,
  `trn` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `term` (`term`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preps`
--

LOCK TABLES `preps` WRITE;
/*!40000 ALTER TABLE `preps` DISABLE KEYS */;
INSERT INTO `preps` VALUES (30,'CAUSA',0,'because, for the sake (of)'),(31,'ANTE',1,'before'),(32,'PER',1,'through, because of'),(33,'AD',1,'to, toward'),(34,'PROPTER',1,'on account of'),(35,'CIRCUM',1,'around'),(36,'CONTRA',1,'against'),(37,'VERSUS',1,'against'),(38,'INTER',1,'between'),(39,'EXTRA',1,'outside of'),(40,'INTRA',1,'within'),(41,'TRANS',1,'across'),(42,'POST',1,'after, behind'),(43,'OB',1,'on account of'),(44,'PRAETER',1,'except for'),(45,'PROPE',1,'near, about'),(46,'A',2,'from, by'),(47,'AB',2,'from, by'),(48,'SINE',2,'without'),(49,'DE',2,'down from, about'),(50,'PRO',2,'for'),(51,'CUM',2,'with'),(52,'PRAE',2,'before, in front of'),(53,'E',2,'out from'),(54,'EX',2,'out from'),(55,'IN',3,'in, on/into, onto'),(56,'SUPER',3,'above'),(57,'SUB',3,'under');
/*!40000 ALTER TABLE `preps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verbs`
--

DROP TABLE IF EXISTS `verbs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `verbs` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `pp1` varchar(20) NOT NULL,
  `pp2` varchar(20) NOT NULL,
  `pp3` varchar(20) NOT NULL,
  `pp4` varchar(20) NOT NULL,
  `trn` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=232 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verbs`
--

LOCK TABLES `verbs` WRITE;
/*!40000 ALTER TABLE `verbs` DISABLE KEYS */;
INSERT INTO `verbs` VALUES (1,'fero','ferre','tuli','latus','bear, speak'),(2,'adfero','adferre','attuli','allatus','bring forth'),(3,'paro','parare','paravi','paratum','prepare'),(4,'moneo','monere','monui','monitum','warn'),(5,'rego','regere','rexi','rectum','rule'),(6,'capio','capere','cepi','captum','seize'),(7,'audio','audire','audivi','auditum','hear'),(8,'conor','conari','conatum sum','-','attempt'),(9,'fateor','fateri','fassum sum','-','confess'),(10,'sequor','sequi','secutum sum','-','follow'),(11,'patior','pati','passum sum','-','endure'),(12,'molior','moliri','molitum sum','-','work at'),(13,'hortor','hortari','hortatum sum','-','urge'),(14,'loquor','loqui','locutum sum','-','speak'),(15,'labor','labi','lapsum sum','-','glide'),(16,'caedo','caedere','cecidi','caesum','cut'),(17,'reprimo','reprimere','repressi','repressum','restrain'),(18,'servio','servire','servivi','servitum','serve'),(19,'tuto','tutare','tutari','tutatum','be defended'),(20,'effreno','effrenare','effrenavi','effrenatum','unbridle'),(21,'rapio','rapere','rapui','raptum','snatch, hasten'),(22,'pario','parere','peperi','partum','produce'),(23,'exerceo','exercere','exercui','exercitum','drive, work'),(24,'utor','uti','usus sum','-','use'),(25,'perdo','perdere','perdidi','perditum','destroy?waste?lose'),(26,'amo','amare','amavi','amatum','love'),(27,'cogito','cogitare','cogitavi','cogitatum','consider'),(28,'debeo','debere','debui','debitum','ought, hesitate'),(29,'do','dare','dedi','datum','give'),(30,'eo','ire','ivi','itus','go'),(31,'abeo','abire','abivi','abitus','leave'),(32,'erro','errare','erravi','erratum','wander'),(33,'laudo','laudare','laudavi','laudatum','praise'),(34,'salveo','salvere','-','-','be healthy'),(35,'servo','servare','servavi','servatum','save, preserve'),(36,'conservo','conservare','conservavi','conservatum','conserve'),(37,'terreo','terrere','terrui','territum','frighten'),(38,'valeo','valere','valui','valiturum','be strong'),(39,'video','videre','vidi','visum','see'),(40,'voco','vocare','vocavi','vocatum','call'),(41,'habeo','habere','habui','habitum','have, hold'),(42,'satio','satiare','satiavi','satiatum','satisfy'),(43,'iuvo','iuvare','iuvi','iutum','help'),(44,'ceno','cenare','cenavi','cenatum','dine'),(45,'culpo','culpare','culpavi','culpatum','blame'),(46,'maneo','manere','mansi','mansum','remain'),(47,'supero','superare','superavi','superatum','surpass'),(48,'possum','posse','potui','-','be able'),(49,'sum','esse','fui','-','be'),(50,'absum','abesse','abfui','-','be away'),(51,'tolero','tolerare','toleravi','toleratum','tolerate'),(52,'audeo','audere','ausum sum','-','dare'),(53,'neco','necare','necavi','necatum','kill'),(54,'ago','agere','egi','actum','do'),(55,'demonstro','demonstrare','demonstravi','demonstratum','demonstrate'),(56,'disco','discere','didici','-','learn'),(57,'doceo','docere','docui','doctum','teach'),(58,'duco','ducere','duxi','ductum','lead'),(59,'gero','gerere','gessi','gestum','accomplish'),(60,'scribo','scribere','scripsi','scriptum','write'),(61,'traho','trahere','traxi','tractum','drag'),(62,'vinco','vincere','vici','victum','conquer'),(63,'dico','dicere','dixi','dictum','speak'),(64,'facio','facere','feci','factum','make'),(65,'fugio','fugere','fugi','fugiturum','flee'),(66,'venio','venire','veni','ventum','come'),(67,'invenio','invenire','inveni','inventum','find'),(68,'vivo','vivere','vixi','victum','live'),(69,'intellego','intellegere','intellexi','intellectum','understand'),(70,'mitto','mittere','misi','missum','send'),(71,'sentio','sentire','sensi','sensum','sense'),(72,'amitto','amittere','amisi','amissum','lose'),(73,'cado','cadere','cecidi','casum','fall'),(74,'creo','creare','creavi','creatum','create'),(75,'alo','alere','alui','altum','nourish'),(76,'diligo','diligere','dilexi','dilectum','esteem'),(77,'iungo','iungere','iunxi','iunctum','join'),(78,'sto','stare','steti','statum','stand'),(79,'appello','appellare','appellavi','appellatum','call (name)'),(80,'curro','currere','cucurri','cursum','run'),(81,'muto','mutare','mutavi','mutatum','change'),(82,'teneo','tenere','tenui','tentum','hold'),(83,'vito','vitare','vitavi','vitatum','avoid'),(84,'committo','committere','commisi','commissum','entrust'),(85,'exspecto','exspectare','exspectavi','exspectatum','wait for'),(86,'iacio','iacere','ieci','iactum','throw, hurl'),(87,'eicio','eicere','eieci','eiectum','throw out'),(88,'timeo','timere','timui','-','be afraid'),(89,'admitto','admittere','admisi','admissum','receive'),(90,'-','coepisse','coepi','coeptum','begin'),(91,'cupio','cupere','cupivi','cupitum','desire'),(92,'deleo','delere','delevi','deletum','erase'),(93,'desidero','desiderare','desideravi','desideratum','desire'),(94,'incipio','incipere','incepi','inceptum','begin'),(95,'navigo','navigare','navigavi','navigatum','navigate'),(96,'neglego','neglegere','neglexi','neglectum','neglect'),(97,'recito','recitare','recitavi','recitatum','recite'),(98,'fluo','fluere','fluxi','fluxum','flow'),(99,'lego','legere','legi','lectum','choose, read'),(100,'misceo','miscere','miscui','mixtum','mix'),(101,'moveo','movere','movi','motum','move'),(102,'delecto','delectare','delectavi','delectatum','please'),(103,'libero','liberare','liberavi','liberatum','free'),(104,'careo','carere','carui','cariturum','be free (from)'),(105,'defendo','defendere','defendi','defensum','defend'),(106,'discedo','discedere','discessi','discessum','depart'),(107,'-','odisse','odi','-','hate'),(108,'prohibeo','prohibere','prohibui','prohibitum','prohibit'),(109,'pronuntio','pronuntiare','pronuntiavi','pronuntiatum','proclaim'),(110,'contineo','continere','continui','contentum','contain'),(111,'iubeo','iubere','iussi','iussum','order'),(112,'laboro','laborare','laboravi','laboratum','work'),(113,'relinquo','relinquere','reliqui','relictum','leave'),(114,'scio','scire','scivi','scitum','know'),(115,'tango','tangere','tetigi','tactum','touch'),(116,'cerno','cernere','crevi','cretum','discern'),(117,'eripio','eripere','eripui','ereptum','snatch away'),(118,'inquit','inquiunt','-','-','he said'),(119,'tollo','tollere','sustuli','sublatum','lift, destroy'),(120,'educo','educare','educavi','educatum','educate'),(121,'gaudeo','gaudere','gavisum sum','-','rejoice'),(122,'ostendo','ostendere','ostendi','ostentum','display'),(123,'peto','petere','petivi','petitum','aim at, attack'),(124,'premo','premere','pressi','pressum','press'),(125,'opprimo','opprimere','oppressi','oppressum','suppress'),(126,'verto','vertere','verti','versum','turn, change'),(127,'accipio','accipere','accepi','acceptum','accept'),(128,'excipio','excipere','excepi','exceptum','capture'),(129,'recipio','recipere','recepi','receptum','take back'),(130,'pello','pellere','pepuli','pulsum','strike'),(131,'expello','expellere','expuli','expulsum','drive out'),(132,'narro','narrare','narravi','narratum','report'),(133,'quaero','quaerere','quaesivi','quaesitum','look for'),(134,'rideo','ridere','risi','risum','laugh'),(135,'ait','aiunt','-','-','he says'),(136,'credo','credere','credidi','creditum','believe'),(137,'iaceo','iacere','iacui','iacitum','lie'),(138,'nego','negare','negavi','negatum','deny'),(139,'nescio','nescire','nescivi','nescitum','be ignorant'),(140,'nuntio','nuntiare','nuntiavi','nuntiatum','report'),(141,'patefacio','patefacere','patefeci','patefactum','reveal'),(142,'puto','putare','putavi','putatum','think'),(143,'spero','sperare','speravi','speratum','hope'),(144,'suscipio','suscipere','suscepi','susceptum','undertake'),(145,'invito','invitare','invitavi','invitatum','invite'),(146,'pono','ponere','posui','positum','place'),(147,'probo','probare','probavi','probatum','approve'),(148,'cedo','cedere','cessi','cessum','go, yield'),(149,'dedico','dedicare','dedicavi','dedicatum','dedicate'),(150,'egeo','egere','egui','-','lack'),(151,'expleo','explere','explevi','expletum','fill'),(152,'praesto','praestare','praestiti','praestitum','excel'),(153,'taceo','tacere','tacui','tacitum','be silent'),(154,'condo','condere','condidi','conditum','establish'),(155,'contendo','contendere','contendi','contenditum','strive, hasten'),(156,'mollio','mollire','mollivi','mollitum','soften'),(157,'pugno','pugnare','pugnavi','pugnatum','fight'),(158,'respondeo','respondere','respondi','responsum','answer'),(159,'surgo','surgere','surrexi','surrectum','arise'),(160,'bibo','bibere','bibi','bibitum','drink'),(161,'cognosco','cognoscere','cognovi','cognitum','recognize'),(162,'comprehendo','comprehendere','comprehendi','comprehensum','understand'),(163,'consumo','consumere','consumpsi','consumptum','consume'),(164,'dubito','dubitare','dubitavi','dubitatum','doubt, hesitate'),(165,'expono','exponere','exposui','expositum','set forth'),(166,'minuo','minuere','minui','minutum','diminish'),(167,'rogo','rogare','rogavi','rogatum','ask'),(168,'nosco','noscere','novi','notum','know'),(169,'-','meminisse','memini','-','remember'),(170,'fido','fidere','fisum sum','-','trust'),(171,'pateo','patere','patui','-','lie open'),(172,'placet','-','-','-','be pleasing'),(173,'opportet','-','-','-','be proper'),(174,'licet','-','-','-','be permitted'),(175,'decerno','decernere','decrevi','decretum','decree'),(176,'occido','occidere','occidi','occasum','fall'),(177,'occido','occidere','occidi','occisum','kill'),(178,'detero','deterere','detrivi','detritum','weaken'),(179,'intercedo','intercedere','intercessi','intercessum','intercede/interrupt'),(180,'interficio','interficere','interfeci','interfectum','kill'),(181,'suspicio','suspicere','suspexi','suspectum','suspect'),(182,'libo','libare','libavi','libatum','spill/dedicate'),(183,'gigno','gignere','genui','genitum','give birth to'),(184,'laxo','laxare','laxavi','laxatum','loosen'),(185,'luceo','lucere','luxi','-','shine'),(186,'eluceo','elucere','eluxi','-','shine forth'),(187,'nuncupo','nuncupare','nuncupavi','nuncupatum','call?name'),(188,'contemplo','contemplare','contemplavi','contemplatum','regard'),(189,'suspicor','suspicari','suspicatum sum','-','suspect'),(190,'intueor','intueri','intuitus sum','-','gaze'),(191,'stupeo','stupere','stupui','-','be stunned'),(192,'conpleo','conplere','conplevi','conpletus','fill'),(193,'disiungo','disiungere','disiunxi','disiunctus','seperate'),(194,'reor','reri','ratus sum','-','measure'),(195,'reor','reri','ratus sum','-','measure'),(196,'distinguo','distingere','distinxi','distinctus','divide'),(197,'efficio','efficere','effeci','effectus','produce'),(198,'specto','spectare','spectare','spectatus','spectate'),(199,'contemno','contemnere','contempsi','contemptus','scorn'),(200,'expeto','expetere','expetivi','expetitus','desire'),(201,'consequor','consequi','consecutus sum','-','pursue'),(202,'habito','habitare','habitavi','habitatus','inhabit'),(203,'vasto','vastare','vastavi','vastatus','devastate'),(204,'intericio','intericere','interieci','interiectus','insert'),(205,'incolo','incolere','incolui','-','dwell'),(206,'interrumpo','interrumpere','interrupi','interruptus','interrupt'),(207,'mano','manare','manavi','manatus','pour'),(208,'expecto','expectare','expectavi','expectatus','expect'),(209,'redimio','redimire','redimivi','redimitus','surround'),(210,'circumdo','circumdare','circumdedi','circumdatus','envelop'),(211,'diverto','divertere','diverti','diversus','divert'),(212,'obrigesco','obrigescere','obrigui','-','stiffen'),(213,'torreo','torrere','torrui','tostus','scorch'),(214,'insisto','insistere','institi','-','insist'),(215,'urgeo','urgere','ursi','-','urge'),(216,'subicio','subicere','subieci','subiectus','throw under'),(217,'contingo','contingere','contigi','contactus','touch'),(218,'colo','colere','colui','coltus','cultivate'),(219,'angusto','angustare','angustavi','angustatus','constrict'),(220,'circumfundo','circumfundere','circumfudi','circumfusus','pour around'),(221,'transcendo','transcendere','transcendi','transcensus','go across'),(222,'obeo','obire','obivi','obitus','go to meet'),(223,'amputo','amputare','amputavi','amputatus','amputate'),(224,'proficio','proficere','profeci','profectus','accomplish'),(225,'dilato','dilatare','dilatavi','dilatatus','dilate'),(226,'prodo','prodere','prodidi','proditus','project'),(227,'accido','accidere','accidi','accisus','cut up'),(228,'adsequor','adsequi','adsecutus sum','-','go after'),(229,'nascor','nasci','natus sum','-','be born'),(230,'iacto','iactare','iactavi','iactatus','cast'),(231,'cano','canere','ceceni','cantus','sing');
/*!40000 ALTER TABLE `verbs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Current Database: `TLD_SHT`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `TLD_SHT` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

USE `TLD_SHT`;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-12 19:20:01
