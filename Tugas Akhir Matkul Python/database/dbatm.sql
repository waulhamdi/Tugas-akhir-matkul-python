-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Des 2022 pada 14.30
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbatm`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_ambil`
--

CREATE TABLE `tb_ambil` (
  `no_voucher` varchar(10) NOT NULL,
  `tgl` datetime DEFAULT NULL,
  `pin_atm` varchar(10) DEFAULT NULL,
  `jumlah` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_nasabah`
--

CREATE TABLE `tb_nasabah` (
  `no_rekening` varchar(10) NOT NULL,
  `nama_nasabah` varchar(50) DEFAULT NULL,
  `pin_atm` varchar(10) DEFAULT NULL,
  `saldo` float DEFAULT NULL,
  `alamat` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tb_nasabah`
--

INSERT INTO `tb_nasabah` (`no_rekening`, `nama_nasabah`, `pin_atm`, `saldo`, `alamat`) VALUES
('001', 'waulhamdi', '246802', 100000, 'wisma asri 2'),
('002', 'taufik', '234567', 100000, 'bojong'),
('003', 'vito', '456788', 100000, 'alinda'),
('004', 'ricki', '987654', 100000, 'kranji');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tb_ambil`
--
ALTER TABLE `tb_ambil`
  ADD PRIMARY KEY (`no_voucher`);

--
-- Indeks untuk tabel `tb_nasabah`
--
ALTER TABLE `tb_nasabah`
  ADD PRIMARY KEY (`no_rekening`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
