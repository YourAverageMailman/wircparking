from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS
socketio = SocketIO(app, cors_allowed_origins="*")  # Enable CORS for socket.io

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                    id INTEGER PRIMARY KEY, 
                    value BOOLEAN
                )''')
    for i in range(1, 7):
        c.execute('INSERT OR IGNORE INTO sensor_data (id, value) VALUES (?, 0)', (i,))
    conn.commit()
    conn.close()

# Route to handle data insertion from ESP32
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    if not data or 'values' not in data:
        return jsonify({'error': 'Invalid data format'}), 400

    values = data['values']
    if len(values) != 6:
        return jsonify({'error': 'Expected 6 sensor values'}), 400

    updates = [(i + 1, values[i]) for i in range(6)]

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.executemany('REPLACE INTO sensor_data (id, value) VALUES (?, ?)', updates)
    conn.commit()
    conn.close()

    # Notify all clients about the update
    socketio.emit('data_updated', {'values': values})

    return jsonify({'message': 'Data updated successfully'}), 200

# Route to return data as JSON
@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sensor_data ORDER BY id')
    data = c.fetchall()
    conn.close()

    return jsonify({row[0]: row[1] for row in data}), 200

if __name__ == '__main__':
    init_db()
    socketio.run(app, host='0.0.0.0', port=5000)
