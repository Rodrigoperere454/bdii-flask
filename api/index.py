from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def db_connection():
    try:
        conn = psycopg2.connect(
            dbname="db2022118930",
            user="a2022118930",
            password="a2022118930",
            host="aid.estgoh.ipc.pt",
            port="5432"

        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

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
        cur.execute("SELECT * FROM utilizadores;")
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
