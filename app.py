from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import mysql.connector

app = Flask(__name__)
CORS(app)

model = joblib.load('ml_model/model.pkl')

def log_prediction(features, prediction):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="predictive_maintenance"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS logs (features TEXT, prediction INT)")
    cursor.execute("INSERT INTO logs (features, prediction) VALUES (%s, %s)", (str(features), prediction))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    log_prediction(data['features'], int(prediction[0]))
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)