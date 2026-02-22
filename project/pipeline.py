from extract import extract
from transform import transform
from load import load

patients = []

patients = extract("diabetes_risk_dataset.csv")
filtered_patients = transform(patients)
load(filtered_patients)