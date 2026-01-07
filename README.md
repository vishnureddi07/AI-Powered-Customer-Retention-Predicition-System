# AI-Powered-Customer-Retention-Predicition-System

📝 Project Overview

This project focuses on analyzing customer churn using Python through data cleaning, feature analysis, and extensive data visualization.
The primary goal is to understand customer behavior patterns and identify the key factors influencing churn using clear, interpretable visual insights.
This analysis lays a strong foundation for building machine learning–based retention models in future stages.

🎯 Project Objectives

Understand customer demographics and service usage patterns

Analyze churn behavior across different customer segments

Visualize important features using appropriate charts

Prepare clean, structured data for future machine learning models

🗺️ Project Roadmap
Stage	Task	Status
Stage 1	Data Understanding & Documentation	✅ Completed
Stage 2	Data Cleaning & Exploratory Data Analysis (EDA)	⏳ Pending
Stage 3	Model Development	⏳ Pending
Stage 4	Explainability & Deployment	⏳ Pending
📂 Dataset Information

Dataset Name: Telco Customer Churn

Number of Rows: 7,043

Number of Columns: 21 (before encoding)

🔑 Key Features
👥 Demographic Features

Gender

SeniorCitizen

Partner

Dependents

🌐 Service Features

PhoneService

MultipleLines

InternetService (DSL / Fiber Optic / No)

OnlineSecurity

OnlineBackup

DeviceProtection

TechSupport

StreamingTV

StreamingMovies

💳 Account Information

Tenure

Contract

PaymentMethod

MonthlyCharges

TotalCharges

🎯 Target Variable

Churn (Yes / No)

🧹 Data Preprocessing

The following preprocessing steps were performed before visualization:

Converted TotalCharges from text to numeric format

Removed rows with missing TotalCharges values

Dropped customerID as it does not contribute to analysis

Grouped tenure into meaningful year-based categories

bins = [0, 12, 24, 48, 72]
labels = ['0-1 Year', '1-2 Years', '2-4 Years', '4-6 Years']

📊 Data Visualization

All visualizations were created using Matplotlib to clearly represent customer distributions and churn behavior.

📈 Numerical Feature Analysis

Histograms were used to analyze:

MonthlyCharges

TotalCharges

These plots help understand the distribution, range, and skewness of billing amounts among customers.

📊 Categorical Feature Analysis

Bar Charts and Pie Charts were used to analyze:

Gender distribution

Senior Citizen status

PhoneService and MultipleLines

InternetService type

OnlineSecurity, OnlineBackup, DeviceProtection

Contract type

Payment Method

Tenure groups

Bar charts enable category comparison, while pie charts show proportional representation.

🔍 Churn-Based Visual Analysis

The following churn-focused visualizations were created:

Male vs Churn (Bar & Pie)

Female vs Churn (Bar & Pie)

Senior Citizen vs Churn

Payment Method vs Churn

These visualizations help identify high-risk customer segments and churn patterns.

🔢 Encoding for Future Modeling

Categorical features were converted into numeric format using One-Hot Encoding:

df_final = pd.get_dummies(df, drop_first=True, dtype=int)


Dataset expanded from 20 to 31 columns

All features are now numeric and ML-ready

🛠️ Tools & Technologies

Python

Pandas

Matplotlib

PyCharm

✅ Project Outcome

This project successfully demonstrates how data preprocessing and visualization can be used to gain meaningful insights into customer churn behavior.
The clean dataset and detailed visual analysis provide a strong foundation for building predictive machine learning models in the next phase of the project.
