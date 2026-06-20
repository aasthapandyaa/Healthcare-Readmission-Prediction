
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load data
print("Loading data...")
df = pd.read_csv('hospital_readmission_dataset.csv')

# Prepare features and target
feature_columns = ['age', 'comorbidities_count', 'length_of_stay', 
                   'medications_count', 'followup_visits_last_year', 'prev_readmissions']
X = df[feature_columns]
y = df['label']

# Train model
print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
print("Saving model...")
with open('ml_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved as ml_model.pkl!")