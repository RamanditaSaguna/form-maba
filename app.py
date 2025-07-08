from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from config.database_sqlite import get_db_connection, close_connection, initialize_database
import sqlite3

app = Flask(__name__)
app.secret_key = 'coding_bootcamp_enrollment_key'

# Initialize database on startup
initialize_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enroll', methods=['POST'])
def process_enrollment():
    if request.method == 'POST':
        try:
            # Mengambil data dari form pendaftaran bootcamp
            full_name = request.form['full_name']
            birth_date = request.form['birth_date']
            email_address = request.form['email_address']
            phone_number = request.form['phone_number']
            home_address = request.form['home_address']
            gender = request.form['gender']
            course_track = request.form['course_track']
            education_level = request.form['education_level']
            experience_level = request.form['experience_level']
            goals = request.form['goals']
            
            # Validasi input wajib
            if not full_name or not email_address or not phone_number:
                flash('Semua bidang yang wajib harus diisi!')
                return redirect(url_for('home'))
            
            # Menyimpan data ke MySQL database
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                
                # Query SQL untuk insert data (SQLite syntax)
                insert_query = """INSERT INTO students 
                        (enrollment_date, full_name, birth_date, email_address, phone_number, home_address, 
                        gender, course_track, education_level, experience_level, career_goals)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                
                # Data yang akan dimasukkan
                student_data = (
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    full_name, birth_date, email_address, phone_number, home_address,
                    gender, course_track, education_level, experience_level, goals
                )
                
                # Eksekusi query
                cursor.execute(insert_query, student_data)
                conn.commit()
                
                # Tutup koneksi database
                close_connection(conn, cursor)
                
                # Redirect ke halaman konfirmasi
                return render_template('confirmation.html', student_name=full_name)
            else:
                flash('Gagal terhubung ke database!')
                return redirect(url_for('home'))
        
        except sqlite3.Error as db_error:
            flash(f'Error database: {str(db_error)}')
            return redirect(url_for('home'))
        except Exception as general_error:
            flash(f'Terjadi kesalahan: {str(general_error)}')
            return redirect(url_for('home'))

# Endpoint untuk dashboard admin
@app.route('/dashboard/students')
def view_students():
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            
            # Query untuk mengambil semua data siswa
            select_query = "SELECT * FROM students ORDER BY enrollment_date DESC"
            cursor.execute(select_query)
            
            # Ambil semua data siswa dan convert ke list of dicts
            rows = cursor.fetchall()
            students_data = []
            for row in rows:
                student_dict = {}
                for key in row.keys():
                    student_dict[key] = row[key]
                # Convert enrollment_date string to datetime object for template
                if student_dict.get('enrollment_date'):
                    try:
                        student_dict['enrollment_date'] = datetime.strptime(
                            student_dict['enrollment_date'], '%Y-%m-%d %H:%M:%S'
                        )
                    except:
                        pass
                students_data.append(student_dict)
            
            # Tutup koneksi
            close_connection(conn, cursor)
            
            # Render template dashboard
            return render_template('dashboard/students.html', students_data=students_data)
        else:
            flash('Gagal terhubung ke database!')
            return redirect(url_for('home'))
    
    except sqlite3.Error as db_error:
        flash(f'Error database: {str(db_error)}')
        return redirect(url_for('home'))
    except Exception as general_error:
        flash(f'Terjadi kesalahan: {str(general_error)}')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
