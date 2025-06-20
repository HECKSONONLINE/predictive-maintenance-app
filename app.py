from flask import Flask, request, jsonify
import joblib
import numpy as np
import mysql.connector  # Corrected import
from pathlib import Path

app = Flask(_name_)

# Load model - adjust path as needed
try:
    model_path = Path('ml_model/model.pkl')  # Change to your actual model path
    model = joblib.load(model_path)
except FileNotFoundError:
    raise Exception(f"Model file not found at {model_path.absolute()}")

def log_prediction(features, prediction):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="predictive_maintenance"
        )
        cursor = conn.cursor()
        # Your database operations here
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    log_prediction(features, prediction[0])
    return jsonify({'prediction': prediction[0]})

if _name_ == '_main_':
    app.run(debug=True)