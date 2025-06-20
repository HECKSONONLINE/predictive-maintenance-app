import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv('mining_equipment_data.csv')

X = data.drop('failure', axis=1)
y = data['failure']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
print("Model trained and saved as model.pkl")