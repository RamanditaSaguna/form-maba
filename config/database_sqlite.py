import sqlite3
import os
from datetime import datetime

# Database file path
DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'coding_bootcamp.db')

def get_db_connection():
    """
    Membuat koneksi ke database SQLite
    Returns: connection object atau None jika gagal
    """
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        connection.row_factory = sqlite3.Row  # Untuk mendapatkan hasil sebagai dictionary
        print("Berhasil terhubung ke database SQLite")
        return connection
    except Exception as e:
        print(f"Error saat menghubungkan ke database: {e}")
        return None

def close_connection(connection, cursor=None):
    """
    Menutup koneksi database dan cursor
    """
    try:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Koneksi database telah ditutup")
    except Exception as e:
        print(f"Error saat menutup koneksi: {e}")

def initialize_database():
    """
    Inisialisasi database dan tabel jika belum ada
    """
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        
        # Create students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                enrollment_date TEXT NOT NULL,
                full_name TEXT NOT NULL,
                birth_date TEXT,
                email_address TEXT NOT NULL UNIQUE,
                phone_number TEXT NOT NULL,
                home_address TEXT,
                gender TEXT,
                course_track TEXT,
                education_level TEXT,
                experience_level TEXT,
                career_goals TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert sample data if table is empty
        cursor.execute('SELECT COUNT(*) FROM students')
        count = cursor.fetchone()[0]
        
        if count == 0:
            sample_data = [
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
                )
            ]
            
            cursor.executemany('''
                INSERT INTO students 
                (enrollment_date, full_name, birth_date, email_address, phone_number, home_address, 
                gender, course_track, education_level, experience_level, career_goals)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', sample_data)
            
            print("Sample data inserted successfully")
        
        conn.commit()
        close_connection(conn, cursor)
        print("Database initialized successfully")
        return True
    return False

def test_connection():
    """
    Test koneksi database
    """
    conn = get_db_connection()
    if conn:
        print("Test koneksi berhasil!")
        close_connection(conn)
        return True
    else:
        print("Test koneksi gagal!")
        return False
