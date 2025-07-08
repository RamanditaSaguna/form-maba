from app import app

if __name__ == '__main__':
    print("Starting Coding Bootcamp Enrollment System...")
    print("Server will be available at: http://localhost:5001/")
    print("Dashboard available at: http://localhost:5001/dashboard/students")
    app.run(debug=True, host='0.0.0.0', port=5001)
