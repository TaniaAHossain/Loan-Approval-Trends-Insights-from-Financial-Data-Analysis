# Loan-Approval-Prediction-using-Azure-Synapse

## 1. Overview
The Jupyter Notebook is designed to analyze loan application data using Azure Synapse Analytics and PySpark. It processes large datasets using Synapse Spark Pools, performs Exploratory Data Analysis (EDA), and visualizes loan approval trends.

## 2. Key Features

**Data Ingestion & Storage:**
  - Loads train and test datasets from Azure Data Lake Storage (ADLS).
  - Uses PySpark’s spark.read.load() for efficient large-scale data handling.
    
**Data Exploration & Cleaning:**
  - Displays sample records from both datasets.
  - Uses PySpark transformations for data cleaning and feature selection.
    
**Loan Application Analysis:**
  - Impact of Credit History on loan approvals.
  - Income distribution analysis to assess loan eligibility.
  - Self-Employed vs. Salaried applicants' comparison.
    
**Visualization & Insights:**
  - Uses Seaborn, Plotly, and Matplotlib for interactive graphs.
  - Analyzes loan distribution by property area and employment status.

**Performance Optimization:**
  - Utilizes Azure Synapse Spark Pools for distributed data processing.
  - Leverages Livy session metadata to track query performance.

# Setup Instructions
## Prerequisites
 * Azure Synapse Analytics workspace.
 * Storage account with train and test datasets.
 * Python environment with required dependencies.

## PySpark Transformations for:
 * Data cleaning & feature engineering.
 * Aggregation & filtering of loan applications.

## Visualization Scripts using:
 * Plotly for interactive graphs.
 * Seaborn & Matplotlib for static insights.

# Visualization Analysis
![Image](https://github.com/user-attachments/assets/57a5837c-a088-40fd-954d-baa82315e6a4)
## Loan Status by Property Area and Credit History (Treemap)

**Description:**
   * This treemap categorizes loan approval status by property area and credit history.
   * The size of the boxes represents the number of applicants in each category.
     
**Insights:**
  * Applicants with good credit history (1) have higher loan approvals.
  * The Urban and Semi-Urban areas see a greater number of approvals compared to Rural areas.

##  Applicant Income vs Loan Amount (Scatter Plot)
![Image](https://github.com/user-attachments/assets/3a5fccae-1e7f-4f77-acf8-993d9dd6c26c)
**Description:**
 * Compares applicant income to the requested loan amount.
 * Points are color-coded based on loan status (Approved = Red, Rejected = Blue).
   
**Insights:**
 * Most applicants with lower incomes request smaller loans.
 * Loan approvals tend to be concentrated around lower loan amounts.
 * High-income applicants have varying approval rates, suggesting other eligibility factors play a role.

## Average Loan Amount by Employment Type (Bar Chart)
![Image](https://github.com/user-attachments/assets/975a0ced-6287-42d6-9b03-dc504429b8c1)
**Description:**
 * Displays average loan amounts for Self-Employed vs Salaried applicants.
   
**Insights:**
 * Self-employed applicants tend to request higher loan amounts.
 * Salaried individuals have higher approval rates compared to self-employed.

## Impact of Credit History on Loan Approval (Stacked Area Chart)
![Image](https://github.com/user-attachments/assets/730c4787-3be9-430f-bf58-971479d570e0)

**Description:**
 * Shows the number of approved and rejected applications based on credit history.
   
**Insights:**
 * A strong credit history (1) leads to a much higher approval rate.
 * Applicants with no credit history (0) have a significantly lower chance of approval.

# Interactive Distribution of Loan Amounts (Histogram)

![Image](https://github.com/user-attachments/assets/68ebdf90-38f9-4a17-9375-eda1c0365849)
**Description:**
 - Represents the distribution of loan amounts across applicants.
   
**Insights:**
 - Most loans fall in the 100-200 range.
 - Higher loan amounts are less frequent, indicating stricter approval conditions.



































