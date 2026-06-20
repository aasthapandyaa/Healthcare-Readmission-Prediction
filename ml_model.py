
# Healthcare Patient Readmission Prediction Model
# This model predicts which patients will be readmitted

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# STEP 1: Load the data
print("Loading data...")
df = pd.read_csv('hospital_readmission_dataset.csv')
print(f"Data loaded! Shape: {df.shape}")
print(df.head())


# STEP 2: Prepare features for ML model
print("\nPreparing features...")

# Select columns to use for prediction
# These are the factors that predict readmission
feature_columns = [
    'age', 
    'comorbidities_count', 
    'length_of_stay', 
    'medications_count',
    'followup_visits_last_year', 
    'prev_readmissions'
]

# Create X (features) and y (target)
X = df[feature_columns]
y = df['label']  # 1 = readmitted, 0 = not readmitted

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")
print(f"Readmission rate: {y.mean() * 100:.2f}%")

# STEP 3: Split data into training (70%) and testing (30%)
print("\nSplitting data into train/test...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Training set: {X_train.shape[0]} patients")
print(f"Testing set: {X_test.shape[0]} patients")

# STEP 4: Train the Random Forest model
print("\nTraining Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model trained successfully!")

# STEP 5: Test accuracy on test set
print("\nEvaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# STEP 6: Detailed results
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred))

# STEP 7: Feature importance - what matters most?
print("\nFeature Importance (what predicts readmission):")
feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance.to_string(index=False))

# STEP 8: Make predictions on new data
print("\nMaking predictions on all patients...")
all_predictions = model.predict(X)
all_probabilities = model.predict_proba(X)[:, 1]  # Probability of readmission

# Add to dataframe
df['predicted_readmission'] = all_predictions
df['readmission_probability'] = all_probabilities

print("\nSample predictions:")
print(df[['patient_id', 'age', 'comorbidities_count', 'followup_visits_last_year', 
          'predicted_readmission', 'readmission_probability']].head(10))

print("\n✅ ML MODEL COMPLETE!")