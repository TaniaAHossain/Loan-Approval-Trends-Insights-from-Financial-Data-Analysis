# Combine-Analysis-using-Synapse-Analytics-SQL-for-Financial-Loan-Approval-Data

## Overview
This repository contains SQL scripts designed for data analysis on loan application datasets using Azure Synapse Analytics SQL. The scripts merge multiple datasets (train and test) and perform various analytical operations, including aggregations, maximum values, and filtering based on income thresholds.

## Features
- **Total Loan Applications by Property Area:** Counts applications across datasets.
- **Highest Loan Amount Analysis:** Identifies the highest loan amount.
- **Unique Loan Applicants:** Determines unique applicants across datasets.
- **Income-Based Loan Application Filtering:** Retrieves applications where income surpasses a threshold.
- **Average Applicant Income Based on Credit History:** Computes the average income grouped by credit history.
- **Self-Employed Applicant Count:** Counts the number of self-employed applicants in both datasets.
- **Credit History Impact (Train vs. Test):** Compares the distribution of credit history records across datasets.
- **Loan Distribution by Property Area (Train vs. Test):** Analyzes the distribution of loans across different property areas in both datasets.

## Prerequisites
* Azure Synapse Analytics workspace.
* Access to train and test datasets.
* Basic SQL knowledge for query modifications.
  
## SQL Queries Breakdown

**1. Total Loan Applications by Property Area**

```
SELECT Property_Area, COUNT(*) AS Total_Applications
FROM (
    SELECT Loan_ID, Property_Area FROM train
    UNION ALL
    SELECT Loan_ID, Property_Area FROM test
) AS CombinedData
GROUP BY Property_Area;
```
**2. Highest Loan Amount from Both Datasets**

```
SELECT MAX(LoanAmount) AS Max_Loan_Amount
FROM (
    SELECT LoanAmount FROM train
    UNION ALL
    SELECT LoanAmount FROM test
) AS CombinedLoans;
```
**3. Count of Unique Applicants**
```
SELECT COUNT(DISTINCT Loan_ID) AS Unique_Applicants
FROM (
    SELECT Loan_ID FROM train
    UNION ALL
    SELECT Loan_ID FROM test
) AS CombinedData;
```
**4. Loan Applications Based on Income Threshold**

```
SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount
FROM (
    SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount FROM train
    UNION ALL
    SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount FROM test
) AS CombinedData
WHERE ApplicantIncome > 5000;
```
**5. Average Applicant Income Based on Credit History**
```
SELECT Credit_History, AVG(ApplicantIncome) AS Avg_Applicant_Income
FROM (
    SELECT Credit_History, ApplicantIncome FROM train
    UNION ALL
    SELECT Credit_History, ApplicantIncome FROM test
) AS CombinedData
GROUP BY Credit_History;
```
**6. Count of Self-Employed Applicants**
```
SELECT Self_Employed, COUNT(*) AS Total_Count
FROM (
    SELECT Self_Employed FROM train
    UNION ALL
    SELECT Self_Employed FROM test
) AS CombinedData
GROUP BY Self_Employed;
```
**7. Credit History Impact (Train vs. Test)**

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
**8. Loan Distribution by Property Area (Train vs. Test)**

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






























