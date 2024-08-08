from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database connection
def get_db_connection():
    conn = sqlite3.connect('user_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the database table if it doesn't exist
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            user_input TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/store_data', methods=['POST'])
def store_data():
    data = request.json
    user_name = data['user_name']
    user_input = data['user_input']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO user_data (user_name, user_input) VALUES (?, ?)', (user_name, user_input))
    conn.commit()
    conn.close()
    
    return jsonify({"message": f"Data stored for {user_name}: {user_input}"}), 201

@app.route('/retrieve_data', methods=['GET'])
def retrieve_data():
    user_name = request.args.get('user_name')
    
    conn = get_db_connection()
    rows = conn.execute('SELECT user_input FROM user_data WHERE user_name = ?', (user_name,)).fetchall()
    conn.close()
    
    if rows:
        user_data = [row['user_input'] for row in rows]
        return jsonify({"data": user_data}), 200
    else:
        return jsonify({"message": f"No data found for {user_name}"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
