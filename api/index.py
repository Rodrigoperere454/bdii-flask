from flask import Flask
import psycopg2

app = Flask(__name__)

def db_connection():
    try:
        conn = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="bdii"
        )
        return conn
    except Exception as e:
        print(e)
        return None
@app.route('/')
def home():
    return 'Hello, World!- BD2-10/03/2025'

@app.route('/about')
def about():
    return 'About'

@app.rout('/emp')
def emp():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM emp;")

    print(cur.fetchall())

