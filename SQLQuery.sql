SELECT *
FROM dbo.patients;

-- Count total number of patients
SELECT COUNT(*) AS total_patients
FROM dbo.patients;


--Count how many patients were readmitted
SELECT COUNT(*) AS readmitted_patients
FROM dbo.patients
WHERE label = 1;


---- Analyze readmission rates by age group to identify high-risk patients
SELECT 
    CASE 
        WHEN age >= 18 AND age <= 30 THEN '18-30 (Young)'
        WHEN age >= 31 AND age <= 50 THEN '31-50 (Middle-aged)'
        WHEN age >= 51 AND age <= 70 THEN '51-70 (Older)'
        WHEN age > 70 THEN '71+ (Elderly)'
    END AS age_group,
    COUNT(*) AS total_patients,
    SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) AS readmitted_patients,
    ROUND(100.0 * SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS readmission_percentage
FROM dbo.patients
GROUP BY 
    CASE 
        WHEN age >= 18 AND age <= 30 THEN '18-30 (Young)'
        WHEN age >= 31 AND age <= 50 THEN '31-50 (Middle-aged)'
        WHEN age >= 51 AND age <= 70 THEN '51-70 (Older)'
        WHEN age > 70 THEN '71+ (Elderly)'
    END
ORDER BY readmission_percentage DESC;




-- Purpose: Categorize patients into HIGH/MEDIUM/LOW risk group

SELECT 
    CASE 
        WHEN readmission_risk_score >= 0.85 THEN 'HIGH RISK (85%+)'
        WHEN readmission_risk_score >= 0.50 THEN 'MEDIUM RISK (50-85%)'
        ELSE 'LOW RISK (<50%)'
    END AS risk_category,
    COUNT(*) AS patient_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM dbo.patients), 2) AS percentage_of_total,
    SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) AS actually_readmitted,
    ROUND(100.0 * SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS actual_readmission_rate

FROM dbo.patients
GROUP BY 
    CASE 
        WHEN readmission_risk_score >= 0.85 THEN 'HIGH RISK (85%+)'
        WHEN readmission_risk_score >= 0.50 THEN 'MEDIUM RISK (50-85%)'
        ELSE 'LOW RISK (<50%)'
    END
ORDER BY risk_category DESC;


-- Analyze readmission rates by diagnosis and age group to identify which diagnoses affect different age groups differently

SELECT 
    primary_diagnosis,
    
    CASE 
        WHEN age >= 18 AND age <= 30 THEN '18-30 (Young)'
        WHEN age >= 31 AND age <= 50 THEN '31-50 (Middle-aged)'
        WHEN age >= 51 AND age <= 70 THEN '51-70 (Older)'
        WHEN age > 70 THEN '71+ (Elderly)'
    END AS age_group,
    COUNT(*) AS patient_count,
    SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) AS readmitted_count,
    ROUND(100.0 * SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS readmission_rate

FROM dbo.patients
GROUP BY 
    primary_diagnosis,
    CASE 
        WHEN age >= 18 AND age <= 30 THEN '18-30 (Young)'
        WHEN age >= 31 AND age <= 50 THEN '31-50 (Middle-aged)'
        WHEN age >= 51 AND age <= 70 THEN '51-70 (Older)'
        WHEN age > 70 THEN '71+ (Elderly)'
    END
ORDER BY primary_diagnosis, readmission_rate DESC;



-- Analyze readmission rates by comorbidity count to show how multiple health conditions increase readmission risk

SELECT 
    comorbidities_count AS condition_count,
    COUNT(*) AS patient_count,
    SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) AS readmitted_count,
    ROUND(100.0 * SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS readmission_rate
FROM dbo.patients
GROUP BY comorbidities_count
ORDER BY readmission_rate DESC;


-- Analyze readmission rates by insurance type to identify disparities in healthcare outcomes

SELECT 
    insurance_type,
    COUNT(*) AS patient_count,
    SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) AS readmitted_count,
    ROUND(100.0 * SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS readmission_rate

FROM dbo.patients
GROUP BY insurance_type
ORDER BY readmission_rate DESC;


-- Analyze readmission rates by follow-up visits to show if follow-up care prevents readmission

SELECT 
    followup_visits_last_year AS followup_count,
    COUNT(*) AS patient_count,
    SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) AS readmitted_count,
    ROUND(100.0 * SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS readmission_rate

FROM dbo.patients
GROUP BY followup_visits_last_year
ORDER BY followup_count;


-- Analyze readmission rates by hospital stay length to find optimal discharge timing

SELECT 
    length_of_stay,
    COUNT(*) AS patient_count,
    SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) AS readmitted_count,
    ROUND(100.0 * SUM(CASE WHEN label = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS readmission_rate

FROM dbo.patients
GROUP BY length_of_stay
ORDER BY length_of_stay;