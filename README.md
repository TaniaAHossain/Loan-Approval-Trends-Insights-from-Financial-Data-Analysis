# Loan-Approval-Trends-Insights-from-Financial-Data

![Image](https://github.com/user-attachments/assets/b1df4564-d1c8-4d3a-aaa0-16d81b69561c)

This repository comprehensively analyzes loan application data, leveraging Azure Synapse Analytics, SQL, and Power BI to extract meaningful insights. It contains:

* Jupyter Notebooks using PySpark for large-scale data processing.
* SQL Scripts for structured analysis on Azure Synapse Analytics.
* Power BI Dashboards for interactive visualization of loan approval trends.
  
The project aims to improve financial decision-making by analyzing credit history, income, employment type, and demographic factors affecting loan approvals.

# Objective

The primary objective of this project is to leverage Azure Synapse Analytics, SQL, and Power BI for a comprehensive analysis of loan approval data, enabling financial institutions to make data-driven lending decisions. By integrating PySpark for large-scale data processing, the project aims to identify key factors influencing loan approvals, including credit history, applicant income, employment type, education level, and property area. The analysis optimizes loan eligibility criteria through SQL-based aggregations and filtering while uncovering approval trends across demographics and income groups. Additionally, interactive Power BI dashboards and visual analytics using Seaborn, Matplotlib, and Plotly enhance financial insights, helping lenders refine risk assessment models and develop personalized lending strategies. The project also focuses on improving financial inclusion and addressing disparities in loan approvals among self-employed vs. salaried applicants across urban and rural regions. Ultimately, this initiative supports scalable and automated loan processing, utilizing Azure Synapse Spark Pools to streamline loan approval predictions based on historical data, ensuring efficient and transparent decision-making in financial institutions.

# Key Features

## Data Processing & Analysis
* PySpark-based Data Ingestion & Cleaning
    * Loads train/test datasets from Azure Data Lake Storage (ADLS).
    * Uses Spark transformations for feature selection and cleaning.
* SQL-Based Loan Data Insights
    * Analyzes total loan applications, income-based eligibility, and credit history impact.
    * Aggregates loan amounts based on employment type, education, and marital status.

## Visualization & Business Insights
* Power BI Dashboard
   * Interactive loan approval trends visualization.
   * Demographic breakdown of applicants by education, gender, and property location.
   * Approval vs. rejection trends and income-loan correlations.

* Matplotlib, Seaborn & Plotly Graphs
   * Loan distribution by property area, employment status, and credit score.
   * Violin & histogram plots to explore income-based loan approval trends

## Data Source
[Data Source](https://www.kaggle.com/datasets/krishnaraj30/finance-loan-approval-prediction-data/data)

## Built-in
- [Azure](https://azure.microsoft.com/en-us/)
- [Power BI](https://powerbi.microsoft.com/en-us/)
  
## Built With 
-  [Azure Synapse-Analytics](https://azure.microsoft.com/en-us/products/synapse-analytics)
-  [Python](https://www.python.org/)
-  [Power BI](https://powerbi.microsoft.com/en-us/)
-  [Synapse Analytics SQL](https://azure.microsoft.com/en-us/products/synapse-analytics)
-  [Excel](https://www.microsoft.com/en-us/)

## Exploratory Analysis and Visualization

### SQL Analysis

The SQL queries analyze loan applications using Azure Synapse Analytics, merging train and test datasets to extract key insights.

* **Loan Application Trends:** Counts total applications and unique applicants by property area.
* **Loan Amount Insights:** Identifies highest loan amounts, average income by credit history, and loan distributions.
* **Credit History & Approval Rates:** Examines credit history impact and compares trends across datasets.
* **Income & Employment Trends:** Filters high-income applicants and analyzes self-employed loan trends.

### Examples of Some Queries

* **Loan Distribution by Property Area:**
```
SELECT 'Train' AS Dataset, 
       Property_Area, 
       COUNT(*) AS Total_Loans
FROM train
GROUP BY Property_Area

UNION ALL

SELECT 'Test' AS Dataset, 
       Property_Area, 
       COUNT(*) AS Total_Loans
FROM test
GROUP BY Property_Area
ORDER BY Dataset, Total_Loans DESC;
```
![Image](https://github.com/user-attachments/assets/206a5317-6711-4ea1-b8a8-ca8d01f4b4ee)

*  **Credit History Impact:**
```
SELECT 'Train' AS Dataset, 
       Credit_History, 
       COUNT(*) AS Total_Applicants
FROM train
GROUP BY Credit_History

UNION ALL

SELECT 'Test' AS Dataset, 
       Credit_History, 
       COUNT(*) AS Total_Applicants
FROM test
GROUP BY Credit_History
ORDER BY Dataset, Total_Applicants DESC;
```
![Image](https://github.com/user-attachments/assets/88a72b42-e59c-423b-b384-383f52a2af08)

* **Get the Average Applicant Income Based on Credit History:**
```
SELECT Credit_History, AVG(ApplicantIncome) AS Avg_Applicant_Income
FROM (
    SELECT Credit_History, ApplicantIncome FROM train
    UNION ALL
    SELECT Credit_History, ApplicantIncome FROM test
) AS CombinedData
GROUP BY Credit_History;
```
![Image](https://github.com/user-attachments/assets/4786eb15-4d62-4470-8178-75646e377f71)

* **Loan Applications Where Income is Higher Than a Certain Threshold:**
```
SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount
FROM (
    SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount FROM train
    UNION ALL
    SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount FROM test
) AS CombinedData
WHERE ApplicantIncome > 5000;
```
![Image](https://github.com/user-attachments/assets/ebce5f07-137e-4133-88bc-9c9e8017cba9)

* **Total Loan Applications by Property Area:**
```
SELECT Property_Area, COUNT(*) AS Total_Applications
FROM (
    SELECT Loan_ID, Property_Area FROM train
    UNION ALL
    SELECT Loan_ID, Property_Area FROM test
) AS CombinedData
GROUP BY Property_Area;
```

![Image](https://github.com/user-attachments/assets/17fc651c-c4a7-49a0-8c37-d9c947db7bc2)


### Excel Project

![Power BI dashboard link](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-from-Financial-Data-Analysis/blob/7fa6e0148f7066fcf6ff3aab03a57d0b3be135c0/Excel-Project-of-Finance-Loan-Approval-Data/finance-loan-approval-prediction-dashboard.pbix)

![Power BI dashboard Analysis](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-from-Financial-Data-Analysis/blob/8ce5a9e4b68a53e8424af20029a5f25788b19ccd/Excel-Project-of-Finance-Loan-Approval-Data/Power%20BI%20dashboard%20analysis%20README%20(1).md)

![Power Bi dashboard images](https://github.com/user-attachments/assets/7b716a5b-a455-49c4-9d35-c2431bc15b3c)

The Loan Application Insights Dashboard comprehensively analyzes loan application trends and approval rates based on multiple factors such as gender, education level, property area, and income. Here’s a summary analysis:

* Total Loan Amount: 109K
* Approval Rate: 44.6% (332 approved, 148 rejected, 289 pending)
* Education: 79% Graduates, 21% Non-Graduates
* Gender: 81% Male, 19% Female
* Property Area:
   * Semiurban: 149 approved, 42 rejected
   * Urban: 98 approved, 54 rejected
   * Rural: 85 approved, 89 rejected (higher rejection rate)
* Financial Trends:
   * Higher-income applicants request larger loans, but approvals vary.
   * Urban & Semiurban areas receive more loans than rural areas.
* Pending Decisions: A large number of applications remain in the "Unknown" category.

The loan application analysis reveals that graduates and male applicants dominate the application pool, with higher approval rates observed in semiurban and urban areas compared to rural regions. While higher-income applicants tend to request larger loans, approval is not solely based on income, suggesting other influencing factors such as credit history and collateral. A significant number of applications remain in the "Unknown" category, indicating delays in processing or missing information. To enhance approval rates and streamline the process, financial institutions should improve transparency, address rejection reasons, and ensure equitable access to loans across different property areas.




























