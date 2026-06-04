from flask import Flask, jsonify
from flask_cors import CORS
import psycopg
import os

app = Flask(__name__)
CORS(app)

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

@app.route("/")
def home():
    return {"message": "Welcome to Flask DevOps Project"}

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/api/users")
def users():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    cur.close()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)