-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  ven. 06 sep. 2019 à 20:28
-- Version du serveur :  10.3.16-MariaDB
-- Version de PHP :  7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `gdemandes`
--
CREATE DATABASE IF NOT EXISTS `gdemandes` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `gdemandes`;

-- --------------------------------------------------------

--
-- Structure de la table `demandes`
--

CREATE TABLE `demandes` (
  `demande_id` int(11) NOT NULL,
  `demandeur_id` varchar(30) NOT NULL,
  `demande_statut` enum('attente de validation','validée','refuser','chez le magasinier','cloturée') DEFAULT NULL,
  `validateur_id` varchar(30) NOT NULL,
  `demande_date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `demandes`
--

INSERT INTO `demandes` (`demande_id`, `demandeur_id`, `demande_statut`, `validateur_id`, `demande_date`) VALUES
(1, 'user1', 'cloturée', 'validateur1', '2019-09-06 14:59:20'),
(2, 'user1', 'cloturée', 'validateur1', '2019-09-06 14:59:39'),
(3, 'magasinier1', 'attente de validation', 'magasinier1', '2019-09-06 15:02:50'),
(4, 'user1', 'attente de validation', 'validateur1', '2019-09-06 17:06:32'),
(6, 'user1', 'attente de validation', 'validateur1', '2019-09-06 17:16:33');

-- --------------------------------------------------------

--
-- Structure de la table `fournisseur`
--

CREATE TABLE `fournisseur` (
  `fournisseur_id` int(11) NOT NULL,
  `fournisseur_nom` varchar(30) DEFAULT NULL,
  `fournisseur_phone` varchar(45) DEFAULT NULL,
  `fournisseur_email` varchar(30) DEFAULT NULL,
  `fournisseur_website` varchar(200) DEFAULT NULL,
  `fournisseur_address` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `fournisseur`
--

INSERT INTO `fournisseur` (`fournisseur_id`, `fournisseur_nom`, `fournisseur_phone`, `fournisseur_email`, `fournisseur_website`, `fournisseur_address`) VALUES
(1, 'fournisseur1', '2121', 'email@1.com', 'www/1', 'N1'),
(2, 'fournisseur2', '2122', 'email@2.com', 'www/2', 'N2'),
(3, 'fournisseur3', '2123', 'email@3.com', 'www/3', 'N3'),
(4, 'fournisseur4', '2124', 'email@4.com', 'www/4', 'N4');

-- --------------------------------------------------------

--
-- Structure de la table `produits`
--

CREATE TABLE `produits` (
  `produit_id` int(11) NOT NULL,
  `produit_categorie` varchar(30) DEFAULT NULL,
  `produit_serial` varchar(200) DEFAULT NULL,
  `produit_picture` varchar(200) DEFAULT NULL,
  `produit_designation` varchar(255) DEFAULT NULL,
  `produit_stock_qte` int(11) DEFAULT NULL,
  `fournisseur_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `produits`
--

INSERT INTO `produits` (`produit_id`, `produit_categorie`, `produit_serial`, `produit_picture`, `produit_designation`, `produit_stock_qte`, `fournisseur_id`) VALUES
(2, 'FOURNITURE ET ACCESSOIRES.', 'FBA0002', '/static/styles/images/products/FBA0002.jpg', 'BOITE AGRAFES 24/6 EXPRESS.', 28, 1),
(3, 'FOURNITURE ET ACCESSOIRES.', 'FBA0003', '/static/styles/images/products/FBA0003.jpg', 'AGRAFEUSE A PINCE 24/6 ESSENTIEL REF. 440210.', 4, 1),
(4, 'FOURNITURE ET ACCESSOIRES.', 'FBA0004', '/static/styles/images/products/FBA0004.jpg', 'ARRACHE AGRAFFES DELI 232.', 10, 1),
(5, 'FOURNITURE ET ACCESSOIRES.', 'FBA0005', '/static/styles/images/products/FBA0005.jpg', 'PILE 1.5 V (AA) DURACEL . ', 23, 1),
(6, 'FOURNITURE ET ACCESSOIRES.', 'FBA0006', '/static/styles/images/products/FBA0006.jpg', 'PILE 1.5V (AAA) DURACEL.', 14, 1),
(7, 'FOURNITURE ET ACCESSOIRES.', 'FBA0007', '/static/styles/images/products/FBA0007.jpg', 'CISEAUX ESSENTIALS GREEN 17 CM SYMETRIQUES REF 468010 MAPED.', 11, 1),
(8, 'FOURNITURE ET ACCESSOIRES.', 'FBA0008', '/static/styles/images/products/FBA0008.jpg', 'BOITE ARCHIVE EN PLASTIQUE 8 CM.', 3, 1),
(9, 'FOURNITURE ET ACCESSOIRES.', 'FBA0009', '/static/styles/images/products/FBA0009.jpg', 'CLASSEUR A LEVIER COULEUR 32X28.', 13, 1),
(10, 'FOURNITURE ET ACCESSOIRES.', 'FBA0010', '/static/styles/images/products/FBA0010.jpg', 'CUTTEUR GM DELI 2043.', 13, 1),
(11, 'FOURNITURE ET ACCESSOIRES.', 'FBA0011', '/static/styles/images/products/FBA0011.jpg', 'MINI DATEUR COLOP S120.', 30, 1),
(12, 'FOURNITURE ET ACCESSOIRES.', 'FBA0012', '/static/styles/images/products/FBA0012.jpg', 'DEVIDOIR DE SCOTCH 19X33.', 18, 1),
(13, 'FOURNITURE ET ACCESSOIRES.', 'FBA0013', '/static/styles/images/products/FBA0013.jpg', 'CALCULATRICE CASIO AX 120.', 28, 1),
(14, 'FOURNITURE ET ACCESSOIRES.', 'FBA0014', '/static/styles/images/products/FBA0014.jpg', 'BROSSE POUR TABLEAU NOIR ET BLANC MANCHE EN BOIS 1ER CHOIX.', 14, 1),
(15, 'FOURNITURE ET ACCESSOIRES.', 'FBA0015', '/static/styles/images/products/FBA0015.jpg', 'RECHARGE TRODAT 4912 BLEU.', 12, 1),
(16, 'FOURNITURE ET ACCESSOIRES.', 'FBA0016', '/static/styles/images/products/FBA0016.jpg', 'RECHARGE TRODAT 4913 ROUGE.', 13, 1),
(17, 'FOURNITURE ET ACCESSOIRES.', 'FBA0017', '/static/styles/images/products/FBA0017.jpg', 'REGLE PLATE 40CM.', 23, 1),
(18, 'FOURNITURE ET ACCESSOIRES.', 'FBA0018', '/static/styles/images/products/FBA0018.jpg', 'SCOTCH D\'EMBALLAGE 100M MARRON FANTASTIK.', 22, 1),
(19, 'FOURNITURE ET ACCESSOIRES.', 'FBA0019', '/static/styles/images/products/FBA0019.jpg', 'RUBAN ADHESIF 19X33 CAMAT.', 14, 1),
(20, 'FOURNITURE ET ACCESSOIRES.', 'FBA0020', '/static/styles/images/products/FBA0020.jpg', 'CASIER A COURRIER EN PLASTIQUE SUPER POSABLE.', 7, 1),
(21, 'FOURNITURE ET ACCESSOIRES.', 'FBA0021', '/static/styles/images/products/FBA0021.jpg', 'BATON COLLE STICK UHU 8.2G.', 10, 1),
(22, 'FOURNITURE ET ACCESSOIRES.', 'FBA0022', '/static/styles/images/products/FBA0022.jpg', 'CD-ROM 700MB 80min-CD.', 23, 1),
(23, 'FOURNITURE ET ACCESSOIRES.', 'FBA0023', '/static/styles/images/products/FBA0023.jpg', 'DVD+REC 4.7 GB RECODABLE VERBATIM.', 8, 1),
(24, 'ARTICLES ECRITURE.', 'FBE0001', '/static/styles/images/products/FBE0001.jpg', 'POCHETTE DE 4 CRAYON HB N° 2 FC.', 29, 2),
(25, 'ARTICLES ECRITURE.', 'FBE0002', '/static/styles/images/products/FBE0002.jpg', 'STYLO CORRECTEUR BLANCO UHU 8 ML.', 21, 2),
(26, 'ARTICLES ECRITURE.', 'FBE0003', '/static/styles/images/products/FBE0003.jpg', 'FLUORESCENT JUMBO MON AMI BLEU.', 22, 2),
(27, 'ARTICLES ECRITURE.', 'FBE0004', '/static/styles/images/products/FBE0004.jpg', 'FLUORESCENT JUMBO MON AMI JAUNE.', 4, 2),
(28, 'ARTICLES ECRITURE.', 'FBE0005', '/static/styles/images/products/FBE0005.jpg', 'FLUORESCENT JUMBO MON AMI ROSE.', 6, 2),
(29, 'ARTICLES ECRITURE.', 'FBE0006', '/static/styles/images/products/FBE0006.jpg', 'FLUORESCENT JUMBO MON AMI ORANGE.', 6, 2),
(30, 'ARTICLES ECRITURE.', 'FBE0007', '/static/styles/images/products/FBE0007.jpg', 'FLUORESCENT JUMBO MON AMI VERT.', 2, 2),
(31, 'ARTICLES ECRITURE.', 'FBE0008', '/static/styles/images/products/FBE0008.jpg', 'GOMME BLANCHE PELIKAN AL20.', 28, 2),
(32, 'ARTICLES ECRITURE.', 'FBE0009', '/static/styles/images/products/FBE0009.jpg', 'MARQUEUR TABLEAU MON AMI / DRY ERASE ROUGE.', 30, 2),
(33, 'ARTICLES ECRITURE.', 'FBE0010', '/static/styles/images/products/FBE0010.jpg', 'MARQUEUR TABLEAU MON AMI / DRY ERASE VERT.', 27, 2),
(34, 'ARTICLES ECRITURE.', 'FBE0011', '/static/styles/images/products/FBE0011.jpg', 'MARQUEUR TABLEAU MON AMI / DRY ERASE NOIR.', 21, 2),
(35, 'ARTICLES ECRITURE.', 'FBE0012', '/static/styles/images/products/FBE0012.jpg', 'MARQUEUR TABLEAU MON AMI / DRY ERASE BLEU.', 5, 2),
(36, 'ARTICLES ECRITURE.', 'FBE0013', '/static/styles/images/products/FBE0013.jpg', 'MARQUEUR PERM. MON AMI.', 16, 2),
(37, 'ARTICLES ECRITURE.', 'FBE0014', '/static/styles/images/products/FBE0014.jpg', 'BOITE DE 50 STYLO A BILLE BIC NOIR.', 6, 2),
(38, 'ARTICLES ECRITURE.', 'FBE0015', '/static/styles/images/products/FBE0015.jpg', 'BOITE DE 50 STYLO A BILLE BIC ROUGE.', 28, 2),
(39, 'ARTICLES ECRITURE.', 'FBE0016', '/static/styles/images/products/FBE0016.jpg', 'BOITE DE 50 STYLO A BILLE BIC BLEU.', 14, 2),
(40, 'ARTICLES ECRITURE.', 'FBE0017', '/static/styles/images/products/FBE0017.jpg', 'BOITE DE 50 STYLO A BILLE BIC VERT.', 20, 2),
(41, 'ARTICLES ECRITURE.', 'FBE0018', '/static/styles/images/products/FBE0018.jpg', 'TAILLE CRAYON 2T MAPED.', 23, 2),
(42, 'PAPETERIE.', 'FBP0001', '/static/styles/images/products/FBP0001.jpg', 'BLOC NOTE SPIRAL A5.', 19, 3),
(43, 'PAPETERIE.', 'FBP0002', '/static/styles/images/products/FBP0002.jpg', 'RAME DE PAPIER 500 FEUILLES LASER A4 21X29.7cm STRONG.', 5, 3),
(44, 'PAPETERIE.', 'FBP0003', '/static/styles/images/products/FBP0003.jpg', 'RAME PAPIER LASER TARGET PROFESSIONNAL 80G / A3.', 21, 3),
(45, 'PAPETERIE.', 'FBP0004', '/static/styles/images/products/FBP0004.jpg', 'BOITE DE 100 SPIRALE 10 MM.', 11, 3),
(46, 'PAPETERIE.', 'FBP0005', '/static/styles/images/products/FBP0005.jpg', 'BOITE DE 100 SERRE FEUILLES 6MM NOIR.', 10, 3),
(47, 'PAPETERIE.', 'FBP0006', '/static/styles/images/products/FBP0006.jpg', 'BOITE DE 100 SERRE FEUILLES 6MM BLANC.', 12, 3),
(48, 'PAPETERIE.', 'FBP0007', '/static/styles/images/products/FBP0007.jpg', 'BOITE ARCHIVE EN CARTON P.M. ', 21, 3),
(49, 'PAPETERIE.', 'FBP0008', '/static/styles/images/products/FBP0008.jpg', 'INTERCALAIRES PP3/10.21X31 . ', 26, 3),
(50, 'PAPETERIE.', 'FBP0009', '/static/styles/images/products/FBP0009.jpg', 'MIFIN DOUBLE COULEUR 21X31cm.', 23, 3),
(51, 'PAPETERIE.', 'FBP0010', '/static/styles/images/products/FBP0010.jpg', 'CHEMISES CART. 1ER CHOIX 240 GRS.', 12, 3),
(52, 'PAPETERIE.', 'FBP0011', '/static/styles/images/products/FBP0011.jpg', 'PAQUET DE 50 CHEMISES PLASTIFIEES COULEUR.', 13, 3),
(53, 'PAPETERIE.', 'FBP0012', '/static/styles/images/products/FBP0012.jpg', 'CHEMISE A RABAT EN C.L.', 13, 3),
(54, 'PAPETERIE.', 'FBP0013', '/static/styles/images/products/FBP0013.jpg', 'FEUILLES RHODOID 21X29.7 TRANSPARENT.', 7, 3),
(55, 'PAPETERIE.', 'FBP0014', '/static/styles/images/products/FBP0014.jpg', 'FEUILLES EUROCHROME A4 .', 7, 3),
(56, 'PAPETERIE.', 'FBP0015', '/static/styles/images/products/FBP0015.jpg', 'ETIQUETTES BLANCHES MULTI USAGE.', 3, 3),
(57, 'PAPETERIE.', 'FBP0016', '/static/styles/images/products/FBP0016.jpg', 'PARAPHEUR 18 VOLETS FT : 24.5 X 34.5.', 11, 3),
(58, 'PAPETERIE.', 'FBP0017', '/static/styles/images/products/FBP0017.jpg', 'POST-IT FLUO 75X75 / 100F.', 3, 3),
(59, 'PAPETERIE.', 'FBP0018', '/static/styles/images/products/FBP0018.jpg', 'POST-IT 127X76 / 100F JAUNE APLI.', 26, 3);

-- --------------------------------------------------------

--
-- Structure de la table `produits_demandes`
--

CREATE TABLE `produits_demandes` (
  `id` int(11) NOT NULL,
  `demande_id` int(11) DEFAULT NULL,
  `produit_id` int(11) DEFAULT NULL,
  `qte_demander` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `produits_demandes`
--

INSERT INTO `produits_demandes` (`id`, `demande_id`, `produit_id`, `qte_demander`) VALUES
(1, 1, 4, 4),
(2, 2, 4, 4),
(3, 3, 31, 2),
(4, 4, 13, 1),
(5, 6, 3, 2);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `user_id` varchar(20) NOT NULL,
  `user_nom` varchar(30) DEFAULT NULL,
  `user_prenom` varchar(30) DEFAULT NULL,
  `user_email` varchar(50) DEFAULT NULL,
  `user_fonction` varchar(20) DEFAULT NULL,
  `user_superieur_id` varchar(20) DEFAULT NULL,
  `user_password` varchar(100) DEFAULT NULL,
  `user_type` enum('utilisateur','validateur','magasinier','administrateur') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`user_id`, `user_nom`, `user_prenom`, `user_email`, `user_fonction`, `user_superieur_id`, `user_password`, `user_type`) VALUES
('admin', 'admin', 'admin', 'admin@uemf.ma', 'admin', 'admin', 'sha256$uAyoSbMH$b7fed250f9c06072a613d49cb6253e07bd4e83a3decc86869cd709c9b978224d', 'administrateur'),
('magasinier1', 'magasinier_nom1', 'magasinier_prenom1', 'magasinier1@uemf.ma', 'service', 'magasinier1', 'sha256$wPqRyWv1$59cdf02d3d30510102938333348e5ab2612c273eb420991f739027d890d5b637', 'magasinier'),
('magasinier2', 'magasinier_nom2', 'magasinier_prenom2', 'magasinier2@uemf.ma', 'etablissement', 'magasinier2', 'sha256$dOH11v1K$5f5bacb278e03f8091925074253b84e347ba830c2660482d9b15517264b380e3', 'magasinier'),
('user1', 'user_nom1', 'user_prenom1', 'user1@uemf.ma', 'etablissement', 'validateur1', 'sha256$BKRlgSmG$d423cf34cc0dd908d2017240e99b3391fdaa35895cd01700d1f24236af7ee604', 'utilisateur'),
('user10', 'user_nom10', 'user_prenom10', 'user10@uemf.ma', 'service', 'validateur2', 'sha256$eCdJbr5Z$639602cc96460a6a35d0582e2b10f0bb921fd3338ce5c47d093ba189ae794c30', 'utilisateur'),
('user11', 'user_nom11', 'user_prenom11', 'user11@uemf.ma', 'etablissement', 'validateur3', 'sha256$b8YzmSxv$dc81b6380bb1f32b89dd4ee4c3677b2d02bcec71377eb08a091112441ddde933', 'utilisateur'),
('user12', 'user_nom12', 'user_prenom12', 'user12@uemf.ma', 'etablissement', 'validateur3', 'sha256$cdV1lGNs$ac357212287606e5f2202f0602ed575563426116193ef282582dac95ddaccf0d', 'utilisateur'),
('user13', 'user_nom13', 'user_prenom13', 'user13@uemf.ma', 'etablissement', 'validateur3', 'sha256$0GINGmUt$ac04df858aa3ea68c364c465f6edd1191b1eab1efbe35eed109436be076e303e', 'utilisateur'),
('user14', 'user_nom14', 'user_prenom14', 'user14@uemf.ma', 'etablissement', 'validateur3', 'sha256$ec0PG6RA$e7fd76ed2949bc52bd1106f1b36179b6f149c1e436681a7e50aa2b725cb948f9', 'utilisateur'),
('user2', 'user_nom2', 'user_prenom2', 'user2@uemf.ma', 'service', 'validateur1', 'sha256$Xt3wZ9l7$eba881dbd37df8bf0d531e6c9deab691c5a298c311fcfcd740d8a5ccee78cb83', 'utilisateur'),
('user3', 'user_nom3', 'user_prenom3', 'user3@uemf.ma', 'service', 'validateur1', 'sha256$OfNiEwMa$1a99bf9b0cc25b7a1b92a7fc32caba2d53fed77b3b24a95b65a388e552b9f479', 'utilisateur'),
('user4', 'user_nom4', 'user_prenom4', 'user4@uemf.ma', 'service', 'validateur1', 'sha256$UJzGHeMf$2a6360d5f4acf8b1faeec559ce387b89edc6104f16d657245a7a62a8b5ae35fe', 'utilisateur'),
('user5', 'user_nom5', 'user_prenom5', 'user5@uemf.ma', 'service', 'validateur1', 'sha256$ZYECOqaz$d04e304fa2baf27be9288cbda19524e616d9fce023fce6cdff5633419a0a2a81', 'utilisateur'),
('user6', 'user_nom6', 'user_prenom6', 'user6@uemf.ma', 'service', 'validateur2', 'sha256$Z8TQWZxl$0bd4756b65492bb0b9b640ff5034e2cbc2a202736ee4e6c8ea589f86769793d2', 'utilisateur'),
('user7', 'user_nom7', 'user_prenom7', 'user7@uemf.ma', 'etablissement', 'validateur2', 'sha256$mp2fMNUr$3c58f3327cf62bfc8537a241743d69b0093ee27f49202a2b0df4804219af632b', 'utilisateur'),
('user8', 'user_nom8', 'user_prenom8', 'user8@uemf.ma', 'etablissement', 'validateur2', 'sha256$ZpqVuAnY$b605e114b5b95f06bbd7a206fbed1cec73b1aa2b1fcbe1f5333fc856e3d5d394', 'utilisateur'),
('user9', 'user_nom9', 'user_prenom9', 'user9@uemf.ma', 'etablissement', 'validateur2', 'sha256$qvTLeKNH$105a3058e5f29f77b6fab3f0b99d6fd10a59c84ab6c6537ad1568459d3d002e2', 'utilisateur'),
('validateur1', 'validateur_nom1', 'validateur_prenom1', 'validateur1@uemf.ma', 'service', 'validateur1', 'sha256$77QRYipv$0a79659f248e3b95e11f3461b5be67686d45da5ad055fd8420447dffe2914d9c', 'validateur'),
('validateur2', 'validateur_nom2', 'validateur_prenom2', 'validateur2@uemf.ma', 'etablissement', 'validateur2', 'sha256$9l99NpST$dec7c91e9c3f2c86d05abd743de83260417e42cccf833dd750a54199909041a8', 'validateur');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `demandes`
--
ALTER TABLE `demandes`
  ADD PRIMARY KEY (`demande_id`);

--
-- Index pour la table `fournisseur`
--
ALTER TABLE `fournisseur`
  ADD PRIMARY KEY (`fournisseur_id`);

--
-- Index pour la table `produits`
--
ALTER TABLE `produits`
  ADD PRIMARY KEY (`produit_id`);

--
-- Index pour la table `produits_demandes`
--
ALTER TABLE `produits_demandes`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `demandes`
--
ALTER TABLE `demandes`
  MODIFY `demande_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `fournisseur`
--
ALTER TABLE `fournisseur`
  MODIFY `fournisseur_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `produits`
--
ALTER TABLE `produits`
  MODIFY `produit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT pour la table `produits_demandes`
--
ALTER TABLE `produits_demandes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
