# Combine-Analysis-using-Synapse-Analytics-SQL-for-Financial-Loan-Approval-Data

## Overview
This repository contains SQL scripts designed for data analysis on loan application datasets using Azure Synapse Analytics SQL. The scripts merge multiple datasets (train and test) and perform various analytical operations, including aggregations, maximum values, and filtering based on income thresholds.

## Features
* Total Loan Applications by Property Area: Counts applications across datasets.
* Highest Loan Amount Analysis: Identifies the highest loan amount.
* Unique Loan Applicants: Determines unique applicants across datasets.
* Income-Based Loan Application Filtering: Retrieves applications where income surpasses a threshold.

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
