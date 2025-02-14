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

## SQL Analysis using Azure Synapse Analytics

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
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/30ef3be84a36e27abb05b50cf18f4a04703a8f9c/Images-for-readme/Loan%20Distribution%20by%20Property%20Area%201.jpeg)

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
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/fe50e0c226de3f3933e67e5335fcac4e74c7d04b/Images-for-readme/Credit%20History%20Impact.png)

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
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/fe50e0c226de3f3933e67e5335fcac4e74c7d04b/Images-for-readme/Get%20the%20Average%20Applicant%20Income%20Based%20on%20Credit%20History.png)

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

The SQL analysis highlights that credit history is the strongest predictor of loan approvals, with higher-income applicants and urban residents receiving more loans. Self-employed applicants face stricter scrutiny despite requesting higher amounts. Trends in train and test datasets remain consistent, confirming the data’s reliability for predictive modeling. This analysis helps financial institutions refine risk assessment models and optimize loan approval strategies.

## Excel Project

![Power BI dashboard link](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-from-Financial-Data-Analysis/blob/7fa6e0148f7066fcf6ff3aab03a57d0b3be135c0/Excel-Project-of-Finance-Loan-Approval-Data/finance-loan-approval-prediction-dashboard.pbix)

![Power BI dashboard Analysis](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-from-Financial-Data-Analysis/blob/8ce5a9e4b68a53e8424af20029a5f25788b19ccd/Excel-Project-of-Finance-Loan-Approval-Data/Power%20BI%20dashboard%20analysis%20README%20(1).md)

![Power Bi dashboard images](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/61ffd8d86a78b2ad80e7b7b695852b059d795bd0/Excel-Project-of-Finance-Loan-Approval-Data/Finance%20Loan%20Approval%20Data%20dashboard%20Image.jpg)

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

## Python Works using Azure Synapse Analytics

![Loan-Approval-data-using-Synapse-python.md](https://github.com/user-attachments/files/18792174/Readme-Loan-Approval-data-using-Synapse-python.md)

The Loan Approval Prediction project uses Azure Synapse Analytics and PySpark to analyze loan data, perform EDA, and visualize approval trends. Key insights reveal that credit history is the strongest predictor, with 85.4% of approved loans linked to good credit. Higher-income applicants have better approval rates, while self-employed individuals face stricter scrutiny. Semi-Urban areas see the highest approvals, and married and graduate applicants receive larger loans, emphasizing financial stability. This project helps financial institutions refine risk models, optimize lending policies, and improve decision-making.

### Some examples of the 


### **Interactive Loan Amount Trends Across Different Variables**

![Image](https://github.com/user-attachments/assets/260a2afc-3607-489c-b261-ed2e293569e7)

The interactive loan amount trends analysis reveals key factors in loan approvals. Married applicants and graduates receive higher loans due to financial stability, while self-employed individuals take larger but variable loans. Urban applicants secure higher amounts due to property values, and a strong credit history boosts approval chances. These insights help lenders refine policies for fair, data-driven lending and risk management.

* **Loan Approvals over Property Area**

![Image](https://github.com/user-attachments/assets/2018a194-69cb-4e16-adf8-fb3a5722a591)

This animated bar chart helps to explore trends and patterns in loan amounts and approvals based on property area and credit history, providing insights into the factors influencing loan decisions.

### **Loan Status by Property Area and Credit History**

![Image](https://github.com/user-attachments/assets/f1daa409-1a6c-4d46-b2c8-6418e6c93746)

The treemap visually compares loan amounts and distributions across property areas, credit history, and approval status, highlighting key patterns and trends. It helps answer: How are loans distributed based on these factors? by providing a clear, hierarchical view for quick insights.


### **Loan Amount Distribution by Property Area**

![Image](https://github.com/user-attachments/assets/c669d8cd-acd3-4c3b-ba62-161b4e7621ca)

The violin plot helps to answer the question: How are loan amounts distributed across different property areas? It achieves this by visually representing the distribution of loan amounts for each property area using a violin-shaped plot, making it easier to compare the distributions and identify potential differences.

### **Loan Amount vs. Coapplicant Income**

![Image](https://github.com/user-attachments/assets/0e7b652a-8d20-441d-828e-fe7c773541f9)

This analysis explores the impact of co-applicant income and loan amount on loan approval status. The bubble chart visually represents this relationship, with size indicating loan amount and color showing approval status, making trends easy to identify.

### **Loan Status and Dependents**

![Image](https://github.com/user-attachments/assets/6331d0d3-c533-4d32-8bbb-cedbfd679594)

The resulting sunburst chart provides a hierarchical view of the loan data, allowing for the exploration of relationships between loan status, dependents, and gender. The size of each segment reflects the frequency of that specific combination of factors. This visualization helps identify patterns and understand how these factors might influence loan approvals.

## Potential Results and Reasoning

- **1. Credit History is the Most Significant Factor in Loan Approvals**

      * Result: 85.4% of approved applicants have a strong credit history.
      * Reasoning: Lenders prioritize applicants with good credit records as they indicate lower default risk. Those with no credit history face a significantly lower approval rate.

      
- **2. Income Levels Influence Loan Approvals and Loan Amounts**

      * Result: Higher-income applicants tend to receive larger loan amounts.
      * Reasoning: Higher-income applicants are perceived as lower financial risk, making them eligible for larger loans and higher approval rates.

- **3. Self-Employed Individuals Face More Scrutiny Despite Requesting Higher Loans**

      * Result: Self-employed applicants apply for larger loan amounts but have lower approval rates.
      * Reasoning: Variable income patterns and financial uncertainty among self-employed individuals result in stricter approval conditions.
        
- **4. Married and Graduate Applicants Have a Higher Loan Approval Rate**

      * Result: Married and graduate applicants receive more loan approvals and larger loan amounts.
      * Reasoning: Dual-income stability in married couples and higher earning potential among graduates make them more creditworthy.

- **5. Semi-Urban Areas Have the Highest Loan Approvals, Rural Areas the Lowest**
     
      * Result: Loan approvals are highest in semi-urban areas and lowest in rural regions.
      * Reasoning: Semi-urban areas offer better financial stability and infrastructure, whereas rural areas may have higher financial risks and lower applicant income levels.

- **6. Gender Disparity Exists in Loan Applications and Approvals**

      * Result: 81.14% of loan applicants are male, while only 18.86% are female.
      * Reasoning: Societal and economic factors contribute to fewer women applying for loans, and approval rates may differ due to considerations of income and employment stability.

- **7. Loan Approval Rate is 44.6%, Indicating a High Rejection Rate.**

       * Result: 332 loans were approved, 148 were rejected, and 289 were pending.
       * Reasoning: Lenders use strict eligibility criteria such as credit history, income levels, and employment status to minimize financial risk.

- **8. Loan Amounts Vary by Property Area and Credit History**

       * Result: Semi-Urban and Urban applicants receive higher loan amounts compared to Rural applicants.
       * Reasoning: Higher property values in urban and semi-urban areas lead to larger loan requests, while rural applicants typically request smaller loans due to lower property costs.

## Closing Remarks

The loan approval analysis using Azure Synapse Analytics, SQL, and Power BI highlights key trends in creditworthiness, income influence, property area impact, and demographic variations. The insights can help financial institutions refine lending policies, target customer segments, and enhance risk assessment models. By leveraging data-driven decision-making, lenders can ensure fair, efficient, and profitable loan distribution while also addressing financial inclusion challenges.



















