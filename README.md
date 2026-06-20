# Healthcare-Readmission-Prediction
A data-driven predictive analytics project that identifies high-risk hospital patients using SQL analysis, machine learning, and interactive dashboards.

## Problem & Impact

- **77.3% of hospital patients are readmitted** - a critical healthcare issue
- **Built ML model that predicts readmission with 77% accuracy**
- Identified **Age as the #1 risk factor (44% importance)** and insurance disparities
- Enables hospitals to target interventions for high-risk patients (51.8% of population)

## What I Built

| Component | Output |
|-----------|--------|
| **SQL Analysis** | 9 queries analyzing 8,000 patient records → identified readmission patterns |
| **ML Model** | Random Forest classifier → 77% accuracy, 84% precision, 87% recall |
| **Power BI Dashboard** | 4 interactive visualizations with age/diagnosis filters → actionable insights |
| **AI Integration** | Claude API → auto-generates clinical recommendations for each patient |

## Key Findings

✅ **Age**: Elderly patients 96.7% readmission vs young 40.5%

✅ **Insurance**: Medicare 95% vs Private 66% (29% equity gap)

✅ **Follow-up**: No visits = 85% readmission | Weekly visits = 20% readmission

✅ **Comorbidities**: 6+ conditions = 96% readmission risk

## Technologies

SQL • Python • Random Forest • Power BI • Claude API • Data Visualization

## Project Files

- `hospital_readmission_dataset.csv` - 8,000 patient records
- `SQLQuery.sql` - 9 exploratory queries
- `ml_model.py` - Model training (77% accuracy)
- `Power BI Project 1` - Interactive dashboard
- `claude_integration.py` - AI insights generator

## How to Use

```bash
# View dashboard
Open 'Power BI Project 1' in Power BI Desktop
# Run ML model
python ml_model.py
# Generate AI recommendations
python claude_integration.py
```

## Author

**Aastha Pandya** | MIS Graduate (GPA: 3.8) | Data Analyst
- GitHub: github.com/aasthapandyaa
- LinkedIn: www.linkedin.com/in/aastha-pandya12


