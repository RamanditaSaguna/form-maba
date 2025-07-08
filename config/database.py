import mysql.connector
from mysql.connector import Error

# Konfigurasi koneksi database MySQL
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'coding_bootcamp_db',
    'user': 'root',
    'password': '',
    'port': 3306,
    'charset': 'utf8mb4',
    'autocommit': True
}

def get_db_connection():
    """
    Membuat koneksi ke database MySQL
    Returns: connection object atau None jika gagal
    """
    try:
        connection = mysql.connector.connect(**DATABASE_CONFIG)
        if connection.is_connected():
            print("Berhasil terhubung ke database MySQL")
            return connection
    except Error as e:
        print(f"Error saat menghubungkan ke database: {e}")
        return None

def close_connection(connection, cursor=None):
    """
    Menutup koneksi database dan cursor
    """
    try:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("Koneksi database telah ditutup")
    except Error as e:
        print(f"Error saat menutup koneksi: {e}")

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
