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
                    id INTEGER PRIMARY KEY CHECK (id = 1), 
                    value REAL
                )''')
    c.execute('INSERT OR IGNORE INTO sensor_data (id, value) VALUES (1, 0.0)')
    conn.commit()
    conn.close()

# Route to handle data insertion and updating
@app.route('/add', methods=['POST'])
def add_data():
    value = request.json.get('value')
    if value is None:
        return jsonify({'error': 'No value provided'}), 400

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('REPLACE INTO sensor_data (id, value) VALUES (1, ?)', (value,))
    conn.commit()
    conn.close()

    # Notify all clients about the update
    socketio.emit('data_updated', {'id': 1, 'value': value})

    return jsonify({'message': 'Data updated successfully'}), 200

# Route to return data as JSON
@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sensor_data WHERE id = 1')
    data = c.fetchone()
    conn.close()

    if data:
        return jsonify({'id': data[0], 'value': data[1]}), 200
    else:
        return jsonify({'error': 'No data found'}), 404

if __name__ == '__main__':
    init_db()
    socketio.run(app, host='0.0.0.0', port=5000)
