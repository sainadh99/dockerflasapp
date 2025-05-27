from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )

@app.route('/')
def index():
    return 'Flask + PostgreSQL is running!'

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    users = [{'id': row[0], 'name': row[1], 'email': row[2], 'age': row[3]} for row in rows]
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    # Instead of getting JSON input, insert the fixed data you gave:
    name = 'sainadh'
    email = 'sainadh@gmail.com'
    age = 24

    conn = get_db_connection()
    cur = conn.cursor()

    insert_query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s) RETURNING id;"
    cur.execute(insert_query, (name, email, age))

    new_id = cur.fetchone()[0]  # Get the id of inserted row

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'User added', 'id': new_id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)