from flask import Flask, jsonify
import psycopg2
import os
app = Flask(__name__)

def db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("db_name"),
            user=os.environ.get("db_username"),
            password=os.environ.get("db_password"),
            host=os.environ.get("db_host"),
            port=os.environ.get("db_port")

        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

@app.route('/var')
def var():
    return jsonify({
        "db_name": os.environ.get("db_name"),
        "db_user": os.environ.get("db_user"),
        "db_password": os.environ.get("db_password"),
        "db_host": os.environ.get("db_host"),
        "db_port": os.environ.get("db_port")
    })

@app.route('/')
def home():
    return 'Hello, World! - BD2 - 10/03/2025'

@app.route('/about')
def about():
    return 'About'

@app.route('/emp')
def emp():
    conn = db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]

        employees = [dict(zip(col_names, row)) for row in rows]

        cur.close()
        conn.close()
        return jsonify(employees)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
