import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Create example dataset
data = {
    'temperature': [80, 90, 95, 100, 85, 120],
    'vibration': [0.3, 0.6, 0.8, 1.2, 0.5, 1.5],
    'failure': [0, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df[['temperature', 'vibration']]
y = df['failure']

# Train Random Forest model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
os.makedirs('ml_model', exist_ok=True)
joblib.dump(model, 'ml_model/model.pkl')

print("✅ Model saved to ml_model/model.pkl")
print("Model trained and saved successfully.")