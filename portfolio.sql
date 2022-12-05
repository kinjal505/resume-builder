-- phpMyAdmin SQL Dump
-- version 5.3.0-dev+20221125.2e001c186a
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 03, 2022 at 07:38 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `portfolio`
--

-- --------------------------------------------------------

--
-- Table structure for table `resume`
--

CREATE TABLE `resume` (
  `name` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `objective` text DEFAULT NULL,
  `Board10` varchar(20) DEFAULT NULL,
  `school10` varchar(20) DEFAULT NULL,
  `marks10` float DEFAULT NULL,
  `passingyear10` int(11) DEFAULT NULL,
  `board12` varchar(20) DEFAULT NULL,
  `school12` varchar(20) DEFAULT NULL,
  `marks12` float DEFAULT NULL,
  `stream12` varchar(20) DEFAULT NULL,
  `passingyear12` int(11) DEFAULT NULL,
  `graduations` varchar(20) DEFAULT NULL,
  `cgpa` float DEFAULT NULL,
  `graduationcoll` varchar(20) DEFAULT NULL,
  `graduationpy` int(11) DEFAULT NULL,
  `masters` varchar(20) DEFAULT NULL,
  `mscgpa` float DEFAULT NULL,
  `mastercoll` varchar(20) DEFAULT NULL,
  `masterpy` int(11) DEFAULT NULL,
  `project` text DEFAULT NULL,
  `skills` text DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `language` text DEFAULT NULL,
  `link` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resume`
--

INSERT INTO `resume` (`name`, `email`, `contact`, `objective`, `Board10`, `school10`, `marks10`, `passingyear10`, `board12`, `school12`, `marks12`, `stream12`, `passingyear12`, `graduations`, `cgpa`, `graduationcoll`, `graduationpy`, `masters`, `mscgpa`, `mastercoll`, `masterpy`, `project`, `skills`, `dob`, `address`, `language`, `link`) VALUES
('jkkj', 'kinjals505@gmail.com', 2147483647, 'hkjhjk', 'fgfty', 'jggu', 90, 90, 'jjh', 'jkljl', 90, 'hkhkj', 90, 'ljlkjlk', 90, 'lkkjlkjlk', 90, 'jlkjk', 90, 'jkljkljlk', 90, 'jljklj', 'jlkjljkl', '2022-08-05', 'ljljl', 'jkkk', 'https://youtu.be/zMh'),
('xyz', 'kinjal29@somaiya.edu', 90987, 'cffhuifhioreruior', 'hiroi', 'jggu', 90, 90, 'jjh', 'jkljl', 90, 'hkhkj', 90, 'ljlkjlk', 90, 'lkkjlkjlk', 89, 'jlkjk', 90, 'jkljkljlk', 80, 'jljklj', 'jlkjljkl', '2022-08-11', 'ljljl', 'jljlk', 'https://www.youtube.'),
('xyz', 'kinjal29@somaiya.edu', 90987, 'cffhuifhioreruior', 'hiroi', 'jggu', 90, 90, 'jjh', 'jkljl', 90, 'hkhkj', 90, 'ljlkjlk', 90, 'lkkjlkjlk', 89, 'jlkjk', 90, 'jkljkljlk', 80, 'jljklj', 'jlkjljkl', '2022-08-11', 'ljljl', 'jljlk', 'https://www.youtube.'),
('xyz', 'kinjal29@somaiya.edu', 90987, 'cffhuifhioreruior', 'hiroi', 'jggu', 90, 90, 'jjh', 'jkljl', 90, 'hkhkj', 90, 'ljlkjlk', 90, 'lkkjlkjlk', 89, 'jlkjk', 90, 'jkljkljlk', 80, 'jljklj', 'jlkjljkl', '2022-08-11', 'ljljl', 'jljlk', 'https://www.youtube.');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
