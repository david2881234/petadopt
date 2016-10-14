-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- 主機: localhost
-- 產生時間： 2016 年 10 月 08 日 18:50
-- 伺服器版本: 10.1.13-MariaDB
-- PHP 版本： 5.6.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `Trisoap`
--

-- --------------------------------------------------------

--
-- 資料表結構 `CUSMAS`
--

CREATE TABLE `CUSMAS` (
  `EMAIL` varchar(50) COLLATE utf8_bin NOT NULL,
  `CUSPW` varchar(15) COLLATE utf8_bin NOT NULL,
  `CUSNM` varchar(30) COLLATE utf8_bin NOT NULL,
  `CUSIDT` varchar(1) COLLATE utf8_bin NOT NULL DEFAULT 'B',
  `CUSADD` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `CUSBIRTHY` smallint(4) NOT NULL,
  `CUSBIRTHM` tinyint(2) NOT NULL,
  `CUSBIRTHD` tinyint(2) NOT NULL,
  `COUNTRY` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `ZCODE` varchar(5) COLLATE utf8_bin DEFAULT NULL,
  `TEL` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `CUSTYPE` varchar(1) COLLATE utf8_bin NOT NULL,
  `KNOWTYPE` varchar(1) COLLATE utf8_bin NOT NULL,
  `CREDITSTAT` varchar(1) COLLATE utf8_bin NOT NULL DEFAULT 'A',
  `TAXID` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `DISCOUNT` int(8) NOT NULL DEFAULT '0',
  `SALEAMTMTD` int(8) NOT NULL DEFAULT '0',
  `SALEAMTSTD` int(8) NOT NULL DEFAULT '0',
  `SALEAMTYTD` int(8) NOT NULL DEFAULT '0',
  `SALEAMT` int(8) NOT NULL DEFAULT '0',
  `CURAR` int(8) NOT NULL DEFAULT '0',
  `SPEINS` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `CREATEDATE` datetime DEFAULT NULL,
  `UPDATEDATE` datetime DEFAULT NULL,
  `ACTCODE` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `CUSMAS`
--

INSERT INTO `CUSMAS` (`EMAIL`, `CUSPW`, `CUSNM`, `CUSIDT`, `CUSADD`, `CUSBIRTHY`, `CUSBIRTHM`, `CUSBIRTHD`, `COUNTRY`, `ZCODE`, `TEL`, `CUSTYPE`, `KNOWTYPE`, `CREDITSTAT`, `TAXID`, `DISCOUNT`, `SALEAMTMTD`, `SALEAMTSTD`, `SALEAMTYTD`, `SALEAMT`, `CURAR`, `SPEINS`, `CREATEDATE`, `UPDATEDATE`, `ACTCODE`) VALUES
('b02705002@ntu.edu.tw', 'dfb4aa16c789', 'yeeeee', 'B', '', 1995, 7, 22, NULL, NULL, '', 'D', 'B', 'A', '', 0, 0, 0, 0, 0, 0, '我要嫁給頓頓', '2016-09-20 00:04:02', '2016-09-20 00:04:02', 1),
('test1@domain.com', '7db4cd6e7093', '管理員1', 'A', 'home', 1991, 1, 1, NULL, NULL, '0911111111', 'A', 'B', 'A', '12345678', 0, 0, 0, 0, 5920, 0, '', '2016-07-23 14:25:41', '2016-07-23 14:25:41', 1),
('test2@domain.com', '7db4cd6e7093', '管理員2', 'A', 'home', 1992, 2, 2, NULL, NULL, '0922222222', 'C', 'D', 'A', '55555555', 25, 0, 0, 0, 580, 0, '', '2016-07-25 09:11:53', '2016-07-25 09:11:53', 1),
('test3@domain.com', '7db4cd6e7093', '測試員1', 'B', 'home', 1993, 3, 3, NULL, NULL, '0933333333', 'B', 'A', 'A', '', 50, 0, 0, 0, 920, 0, '嗨嗨', '2016-08-15 11:07:11', '2016-08-15 11:07:11', 1),
('test4@domain.com', '7db4cd6e7093', '測試員2', 'B', 'somewhere', 1994, 4, 4, NULL, NULL, '0987654321', 'A', 'C', 'A', '', 25, 0, 0, 0, 3605, 0, '', '2016-08-20 20:01:12', '2016-08-20 20:01:12', 1),
('test5@domain.com', '7db4cd6e7093', '測試員3', 'B', 'home', 1995, 5, 5, NULL, NULL, '0912345678', 'A', 'A', 'A', '87654321', 50, 0, 0, 0, 0, 0, '', '2016-08-28 12:00:18', '2016-09-05 06:23:59', 1);

-- --------------------------------------------------------

--
-- 資料表結構 `ITEMMAS`
--

CREATE TABLE `ITEMMAS` (
  `ITEMNO` int(15) NOT NULL,
  `ITEMNM` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `ITEMAMT` int(8) NOT NULL DEFAULT '0',
  `PRICE` int(8) DEFAULT NULL,
  `DESCRIPTION` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `CREATEDATE` datetime NOT NULL,
  `UPDATEDATE` datetime NOT NULL,
  `ACTCODE` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `ITEMMAS`
--

INSERT INTO `ITEMMAS` (`ITEMNO`, `ITEMNM`, `ITEMAMT`, `PRICE`, `DESCRIPTION`, `CREATEDATE`, `UPDATEDATE`, `ACTCODE`) VALUES
(1, '田靜山巒禾風皂', 2, 300, '我的編號是1', '2016-05-20 00:00:00', '2016-09-13 22:31:52', 1),
(2, '金絲森林渲染皂', 1, 300, '', '2016-05-20 00:00:00', '2016-09-13 22:31:52', 1),
(3, '釋迦手感果力皂', 0, 300, '', '2016-05-20 00:00:00', '2016-05-20 00:00:00', 1),
(4, '三三臺東意象禮盒組', 5, 900, '我是編號4', '2016-05-20 00:00:00', '2016-09-13 22:31:52', 1);

-- --------------------------------------------------------

--
-- 資料表結構 `MSGMAS`
--

CREATE TABLE `MSGMAS` (
  `MSGNO` int(15) NOT NULL,
  `EMAIL` varchar(50) COLLATE utf8_bin NOT NULL,
  `MSGTXT` text COLLATE utf8_bin NOT NULL,
  `MSGPHOTO` tinyint(1) NOT NULL,
  `MSGVIDEO` tinyint(1) NOT NULL,
  `MSGSTAT` varchar(1) COLLATE utf8_bin NOT NULL DEFAULT 'A',
  `REWARDSTAT` tinyint(1) NOT NULL DEFAULT '0',
  `CREATEDATE` datetime NOT NULL,
  `PUBLICDATE` datetime DEFAULT NULL,
  `ACTCODE` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `MSGMAS`
--

INSERT INTO `MSGMAS` (`MSGNO`, `EMAIL`, `MSGTXT`, `MSGPHOTO`, `MSGVIDEO`, `MSGSTAT`, `REWARDSTAT`, `CREATEDATE`, `PUBLICDATE`, `ACTCODE`) VALUES
(100001, 'test3@domain.com', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 1, 1, 'D', 1, '2016-09-14 21:58:15', '2016-09-14 23:47:21', 1),
(100002, 'test5@domain.com', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 1, 0, 'A', 0, '2016-09-14 21:59:27', '0000-00-00 00:00:00', 1),
(100003, 'test2@domain.com', 'I just left some message.', 0, 0, 'C', 0, '2016-09-14 22:00:12', '0000-00-00 00:00:00', 1),
(100004, 'test2@domain.com', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 1, 1, 'E', 1, '2016-09-14 22:01:29', '0000-00-00 00:00:00', 1),
(100005, 'test4@domain.com', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 0, 0, 'B', 1, '2016-09-14 22:55:51', '0000-00-00 00:00:00', 1);

-- --------------------------------------------------------

--
-- 資料表結構 `ORDITEMMAS`
--

CREATE TABLE `ORDITEMMAS` (
  `ORDNO` varchar(15) COLLATE utf8_bin NOT NULL,
  `ITEMNO` varchar(15) COLLATE utf8_bin NOT NULL,
  `ORDAMT` int(8) DEFAULT NULL,
  `EMAIL` varchar(50) COLLATE utf8_bin NOT NULL,
  `CREATEDATE` datetime NOT NULL,
  `UPDATEDATE` datetime NOT NULL,
  `ACTCODE` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `ORDITEMMAS`
--

INSERT INTO `ORDITEMMAS` (`ORDNO`, `ITEMNO`, `ORDAMT`, `EMAIL`, `CREATEDATE`, `UPDATEDATE`, `ACTCODE`) VALUES
('100000001', '1', 1, 'test1@domain.com', '2016-09-13 16:06:11', '2016-09-13 16:06:11', 1),
('100000001', '2', 2, 'test1@domain.com', '2016-09-13 16:10:15', '2016-09-13 16:10:15', 1),
('100000002', '3', 3, 'test3@domain.com', '2016-09-14 12:52:43', '2016-09-14 12:52:43', 1),
('100000003', '1', 2, 'test4@domain.com', '2016-09-14 12:54:18', '2016-09-14 12:54:18', 1),
('100000003', '2', 2, 'test4@domain.com', '2016-09-14 12:54:24', '2016-09-14 12:54:24', 1),
('100000003', '3', 2, 'test4@domain.com', '2016-09-14 12:54:42', '2016-09-14 12:54:42', 1),
('100000003', '4', 2, 'test4@domain.com', '2016-09-14 12:54:51', '2016-09-14 12:54:51', 1),
('100000005', '2', 2, 'test2@domain.com', '2016-09-14 13:05:54', '2016-09-14 13:05:54', 1),
('999000001', '1', 2, 'test1@domain.com', '2016-09-13 22:31:52', '2016-09-13 22:31:52', 1),
('999000001', '2', 1, 'test1@domain.com', '2016-09-13 22:31:52', '2016-09-13 22:31:52', 1),
('999000001', '4', 5, 'test1@domain.com', '2016-09-13 22:31:52', '2016-09-13 22:31:52', 1);

-- --------------------------------------------------------

--
-- 資料表結構 `ORDMAS`
--

CREATE TABLE `ORDMAS` (
  `ORDNO` int(15) NOT NULL,
  `ORDTYPE` varchar(1) COLLATE utf8_bin NOT NULL,
  `EMAIL` varchar(50) COLLATE utf8_bin NOT NULL,
  `INVOICENO` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `BACKSTAT` tinyint(1) DEFAULT '0',
  `ORDSTAT` varchar(1) COLLATE utf8_bin DEFAULT 'E',
  `PAYSTAT` tinyint(1) DEFAULT '0',
  `PAYTYPE` varchar(1) COLLATE utf8_bin DEFAULT NULL,
  `ORDINST` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `DCTID` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `TOTALPRICE` int(8) DEFAULT '0',
  `REALPRICE` int(8) NOT NULL,
  `SHIPFEE` int(8) DEFAULT '0',
  `TOTALAMT` int(8) DEFAULT '0',
  `DATEREQ` date DEFAULT NULL,
  `CREATEDATE` datetime NOT NULL,
  `UPDATEDATE` datetime NOT NULL,
  `ACTCODE` tinyint(1) NOT NULL DEFAULT '1',
  `MerchantTradeNo` varchar(50) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `ORDMAS`
--

INSERT INTO `ORDMAS` (`ORDNO`, `ORDTYPE`, `EMAIL`, `INVOICENO`, `BACKSTAT`, `ORDSTAT`, `PAYSTAT`, `PAYTYPE`, `ORDINST`, `DCTID`, `TOTALPRICE`, `REALPRICE`, `SHIPFEE`, `TOTALAMT`, `DATEREQ`, `CREATEDATE`, `UPDATEDATE`, `ACTCODE`, `MerchantTradeNo`) VALUES
(100000001, 'G', 'test1@domain.com', NULL, 0, 'R', 1, NULL, '', NULL, 900, 920, 20, 920, NULL, '2016-09-13 16:11:13', '2016-09-13 16:11:13', 1, 'Test1473754274'),
(100000002, 'G', 'test3@domain.com', NULL, 1, 'R', 1, NULL, '', NULL, 900, 920, 20, 920, NULL, '2016-09-14 12:52:51', '2016-09-14 12:52:51', 1, 'Test1473828772'),
(100000003, 'G', 'test4@domain.com', 'TS33333333', 0, 'C', 1, NULL, '', 'mWaquTVgXFhb', 3600, 3605, 20, 3620, NULL, '2016-09-14 12:56:00', '2016-09-14 12:56:00', 1, 'Test1473828961'),
(100000004, 'G', 'test2@domain.com', NULL, 0, 'F', 1, NULL, '', NULL, 0, 20, 20, 20, NULL, '2016-09-14 12:57:24', '2016-09-14 12:57:24', 1, NULL),
(100000005, 'G', 'test2@domain.com', NULL, 0, 'E', 1, NULL, '', NULL, 600, 560, 20, 620, NULL, '2016-09-14 13:05:54', '2016-09-19 15:01:08', 1, NULL),
(999000001, 'S', 'test1@domain.com', 'AB12341234', 0, 'C', 1, NULL, NULL, NULL, 5400, 5000, 0, 5400, NULL, '2016-09-13 22:31:52', '2016-09-13 22:31:52', 1, NULL);

-- --------------------------------------------------------

--
-- 資料表結構 `OWNMAS`
--

CREATE TABLE `OWNMAS` (
  `COMNM` varchar(15) COLLATE utf8_bin NOT NULL,
  `COMADD` varchar(100) COLLATE utf8_bin NOT NULL,
  `COMTEL` varchar(15) COLLATE utf8_bin NOT NULL,
  `COMEMAIL` varchar(50) COLLATE utf8_bin NOT NULL,
  `COMWEB` varchar(50) COLLATE utf8_bin NOT NULL,
  `COMTAXID` varchar(15) COLLATE utf8_bin NOT NULL,
  `NORDNOG` int(15) NOT NULL,
  `NORDNOS` int(15) NOT NULL,
  `NMSGNO` int(15) NOT NULL,
  `SALEAMTDATE` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `OWNMAS`
--

INSERT INTO `OWNMAS` (`COMNM`, `COMADD`, `COMTEL`, `COMEMAIL`, `COMWEB`, `COMTAXID`, `NORDNOG`, `NORDNOS`, `NMSGNO`, `SALEAMTDATE`) VALUES
('Trisoap', '台灣台北市大安區和平東路二段265巷3號', '0952527077', 'trisoap2015@gmail.com', 'needs replenishment', '43864595', 100000006, 999000001, 100006, '0000-00-00');

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `CUSMAS`
--
ALTER TABLE `CUSMAS`
  ADD PRIMARY KEY (`EMAIL`);

--
-- 資料表索引 `ITEMMAS`
--
ALTER TABLE `ITEMMAS`
  ADD PRIMARY KEY (`ITEMNO`);

--
-- 資料表索引 `MSGMAS`
--
ALTER TABLE `MSGMAS`
  ADD PRIMARY KEY (`MSGNO`);

--
-- 資料表索引 `ORDITEMMAS`
--
ALTER TABLE `ORDITEMMAS`
  ADD PRIMARY KEY (`ORDNO`,`ITEMNO`,`EMAIL`);

--
-- 資料表索引 `ORDMAS`
--
ALTER TABLE `ORDMAS`
  ADD PRIMARY KEY (`ORDNO`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
