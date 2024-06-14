from flask import Flask, request
import time

app = Flask(__name__)

data = {
    "Waktu": [],
    "NamaSender": [],
    "NilaiSensor": []
}

@app.route('/', methods=['GET'])
def home():
    return "Halo Home!"

@app.route('/data', methods=['GET'])
def get_data():
    return data, 200

@app.route('/send', methods=['POST'])
def post_data():
    data = request.json
    data['Waktu'] = time.time()
    data['Waktu'].append(data['Waktu'])
    data['NamaSender'].append(data['NamaSender'])
    data['NilaiSensor'].append(data['NilaiSensor'])
    
    return f"{data['name']} berhasil kirim data {data['NilaiSensor']}", 201

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='Alamat_IP')
