import os
import uuid
import platform
from flask import Flask, jsonify

app = Flask(__name__)

# Получение имени хоста
@app.route('/hostname', methods=['GET'])
def get_hostname():
    return jsonify({'hostname': platform.node()})
    
# Получение имени автора из переменной окружения
@app.route('/author', methods=['GET'])
def get_author():
    author = os.environ.get('AUTHOR', 'Unknown')
    return jsonify({'author': author})

# Генерация идентификатора UUID
@app.route('/id', methods=['GET'])
def get_id():
    unique_id = str(uuid.uuid4())
    return jsonify({'uuid': unique_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
