from flask import Flask, render_template, request, redirect, session, send_file
from db_config import get_connection
from datetime import datetime
import csv
import io

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers WHERE username=%s AND password=%s", (username, password))
        teacher = cursor.fetchone()
        conn.close()
        if teacher:
            session['username'] = username
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect('/')
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    filter_date = request.form.get('date') if request.method == 'POST' else None
    if filter_date:
        cursor.execute("SELECT * FROM attendance WHERE date=%s", (filter_date,))
    else:
        cursor.execute("SELECT * FROM attendance ORDER BY date DESC, time DESC")

    records = cursor.fetchall()
    conn.close()

    return render_template('index.html', records=records)

@app.route('/mark', methods=['POST'])
def mark_attendance():
    if 'username' not in session:
        return redirect('/')

    name = request.form['name']
    status = request.form['status']
    now = datetime.now()
    date = now.date()
    time = now.time()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (name, status, date, time) VALUES (%s, %s, %s, %s)",
                   (name, status, date, time))
    conn.commit()
    conn.close()
    return redirect('/dashboard')

@app.route('/export')
def export_csv():
    if 'username' not in session:
        return redirect('/')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, status, date, time FROM attendance")
    data = cursor.fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Name', 'Status', 'Date', 'Time'])
    writer.writerows(data)
    output.seek(0)

    return send_file(io.BytesIO(output.read().encode()), mimetype='text/csv', as_attachment=True, download_name="attendance.csv")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
