# Loan-Approval-Trends-Insights-from-Financial-Data

![Image](https://github.com/user-attachments/assets/b1df4564-d1c8-4d3a-aaa0-16d81b69561c)

This repository comprehensively analyzes loan application data, leveraging Azure Synapse Analytics, SQL, and Power BI to extract meaningful insights. It contains:

* Jupyter Notebooks using PySpark for large-scale data processing.
* SQL Scripts for structured analysis on Azure Synapse Analytics.
* Power BI Dashboards for interactive visualization of loan approval trends.
The project aims to improve financial decision-making by analyzing credit history, income, employment type, and demographic factors affecting loan approvals.

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

## Analysis

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






























