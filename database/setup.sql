-- Database Setup for Coding Bootcamp Student Enrollment System
-- Created: 2025

-- Create database
CREATE DATABASE IF NOT EXISTS coding_bootcamp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the database
USE coding_bootcamp_db;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_date DATETIME NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    email_address VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NOT NULL,
    home_address TEXT,
    gender ENUM('Laki-laki', 'Perempuan') DEFAULT NULL,
    course_track ENUM('Web Development', 'Mobile Development', 'Data Science', 'UI/UX Design', 'DevOps Engineering') DEFAULT NULL,
    education_level ENUM('SMA/SMK', 'D3', 'S1', 'S2', 'Lainnya') DEFAULT NULL,
    experience_level ENUM('Pemula', 'Dasar', 'Menengah', 'Mahir') DEFAULT NULL,
    career_goals TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create index for better performance
CREATE INDEX idx_enrollment_date ON students(enrollment_date);
CREATE INDEX idx_course_track ON students(course_track);
CREATE INDEX idx_email ON students(email_address);

-- Insert sample data for testing (optional)
INSERT INTO students (
    enrollment_date, 
    full_name, 
    birth_date, 
    email_address, 
    phone_number, 
    home_address, 
    gender, 
    course_track, 
    education_level, 
    experience_level, 
    career_goals
) VALUES 
(
    '2025-01-15 10:30:00',
    'Ahmad Rizki Pratama',
    '1999-05-12',
    'ahmad.rizki@email.com',
    '081234567890',
    'Jl. Merdeka No. 123, Jakarta Pusat',
    'Laki-laki',
    'Web Development',
    'S1',
    'Pemula',
    'Ingin menjadi Full Stack Developer di perusahaan teknologi terkemuka'
),
(
    '2025-01-16 14:15:00',
    'Siti Nurhaliza',
    '2000-08-23',
    'siti.nurhaliza@email.com',
    '082345678901',
    'Jl. Sudirman No. 456, Bandung',
    'Perempuan',
    'UI/UX Design',
    'S1',
    'Dasar',
    'Menjadi UI/UX Designer yang ahli dalam design thinking dan user research'
),
(
    '2025-01-17 09:45:00',
    'Budi Santoso',
    '1998-12-10',
    'budi.santoso@email.com',
    '083456789012',
    'Jl. Gatot Subroto No. 789, Surabaya',
    'Laki-laki',
    'Data Science',
    'S1',
    'Menengah',
    'Berkarir sebagai Data Scientist untuk membantu pengambilan keputusan bisnis'
),
(
    '2025-01-18 11:20:00',
    'Dewi Sartika',
    '2001-03-07',
    'dewi.sartika@email.com',
    '084567890123',
    'Jl. Diponegoro No. 321, Yogyakarta',
    'Perempuan',
    'Mobile Development',
    'D3',
    'Pemula',
    'Mengembangkan aplikasi mobile yang bermanfaat untuk masyarakat'
),
(
    '2025-01-19 16:30:00',
    'Eko Prasetyo',
    '1997-11-18',
    'eko.prasetyo@email.com',
    '085678901234',
    'Jl. Ahmad Yani No. 654, Semarang',
    'Laki-laki',
    'DevOps Engineering',
    'S1',
    'Menengah',
    'Menjadi DevOps Engineer untuk mengoptimalkan proses development dan deployment'
);

-- Create table for course tracks information (optional)
CREATE TABLE IF NOT EXISTS course_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(50) NOT NULL,
    description TEXT,
    duration_weeks INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert course track data
INSERT INTO course_tracks (track_name, description, duration_weeks) VALUES
('Web Development', 'Belajar membuat website dan aplikasi web modern menggunakan HTML, CSS, JavaScript, dan framework terpopuler', 16),
('Mobile Development', 'Mengembangkan aplikasi mobile untuk Android dan iOS menggunakan React Native, Flutter, atau native development', 14),
('Data Science', 'Analisis data, machine learning, dan artificial intelligence untuk mengextract insights dari big data', 18),
('UI/UX Design', 'Design thinking, user research, prototyping, dan tools design untuk menciptakan user experience yang optimal', 12),
('DevOps Engineering', 'Automation, CI/CD, cloud computing, dan infrastructure management untuk mendukung software development lifecycle', 14);

-- Show tables structure
DESCRIBE students;
DESCRIBE course_tracks;
