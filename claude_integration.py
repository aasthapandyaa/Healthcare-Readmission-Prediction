
import pandas as pd
import pickle
from anthropic import Anthropic

# Read API key - simpler method
with open('claude-api-key.txt', 'r') as f:
    api_key = f.read().strip()
    
# Initialize Claude client
client = Anthropic(api_key=api_key)

# Load your trained ML model
model = pickle.load(open('ml_model.pkl', 'rb'))

# Sample patient data
patient_data = {
    'age': 75,
    'comorbidities_count': 4,
    'length_of_stay': 12,
    'medications_count': 6,
    'followup_visits_last_year': 0,
    'prev_readmissions': 2
}

print("=" * 70)
print("PATIENT READMISSION RISK ANALYSIS WITH CLAUDE AI")
print("=" * 70)
print(f"\nPatient Profile:")
print(f"  Age: {patient_data['age']}")
print(f"  Comorbidities: {patient_data['comorbidities_count']}")
print(f"  Length of Stay: {patient_data['length_of_stay']} days")
print(f"  Medications: {patient_data['medications_count']}")
print(f"  Follow-up Visits Last Year: {patient_data['followup_visits_last_year']}")
print(f"  Previous Readmissions: {patient_data['prev_readmissions']}\n")

# ML Model predicts
features = [
    patient_data['age'],
    patient_data['comorbidities_count'],
    patient_data['length_of_stay'],
    patient_data['medications_count'],
    patient_data['followup_visits_last_year'],
    patient_data['prev_readmissions']
]

risk_probability = model.predict_proba([features])[0][1]
risk_category = "HIGH RISK" if risk_probability > 0.85 else ("MEDIUM RISK" if risk_probability > 0.50 else "LOW RISK")

print("=" * 70)
print("ML MODEL PREDICTION")
print("=" * 70)
print(f"Risk Category: {risk_category}")
print(f"Readmission Probability: {risk_probability:.2%}")
print("\n" + "-" * 70 + "\n")

# Claude AI explains
print("CLAUDE AI ANALYSIS & RECOMMENDATIONS:\n")

prompt = f"""
A hospital patient has this profile:
- Age: {patient_data['age']} years old
- Number of chronic conditions: {patient_data['comorbidities_count']}
- Hospital stay length: {patient_data['length_of_stay']} days
- Number of medications: {patient_data['medications_count']}
- Follow-up visits in last year: {patient_data['followup_visits_last_year']}
- Previous readmissions: {patient_data['prev_readmissions']}

Our machine learning model predicts this patient has a {risk_probability:.2%} probability of readmission (Category: {risk_category}).

Please provide:
1. Brief explanation of WHY this patient is at {risk_category} for readmission
2. 3-4 specific, actionable recommendations for the hospital to prevent readmission
3. Key risk factors to monitor closely

Keep response professional and concise (for healthcare providers).
"""

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=600,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.content[0].text)

print("\n" + "=" * 70)
print("END OF ANALYSIS")
print("=" * 70)