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












































