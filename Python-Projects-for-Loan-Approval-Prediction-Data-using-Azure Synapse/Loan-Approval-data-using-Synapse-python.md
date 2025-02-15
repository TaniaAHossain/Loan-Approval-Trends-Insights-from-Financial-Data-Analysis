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

## Loan Status by Property Area and Credit History 
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/2612beb7d6462cc9faca5824c28480de33340377/Images-for-Finance-Loan-Approval-Data/(Treemap)Loan%20Status%20by%20Property%20Area%20and%20Credit%20History.png)

**Description:**
   * This treemap categorizes loan approval status by property area and credit history.
   * The size of the boxes represents the number of applicants in each category.
       
**Insights:**
  * Applicants with a good credit history (1) have higher loan approvals.
  * The Urban and Semi-Urban areas see a greater number of approvals compared to Rural areas.

# Loan Amounts by Property Area over Credit History 
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/45097085c9372e7be55d4014b9183b4f3d096a44/Images-for-Finance-Loan-Approval-Data/Loan%20Amounts%20by%20Property%20Area%20over%20Credit%20History%20(Animated%20Bar%20Chart).png)

**Description:**
- Displays loan amounts for different property areas, separated by credit history.
  
**Insights:**
- Credit history strongly influences loan amounts.
- Semi-Urban areas receive the highest loan amounts.

 # Loan Amount vs Coapplicant Income 
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/45097085c9372e7be55d4014b9183b4f3d096a44/Images-for-Finance-Loan-Approval-Data/Loan%20Amount%20vs%20Coapplicant%20Income.png)

**Description:**
- Analyzes the impact of co-applicant income on loan amounts.
- Bubble size represents loan amount, and color represents loan status.
  
**Insights:**
- Higher co-applicant incomes correlate with higher loan amounts.
- Many loans with low co-applicant income are rejected.

# Loan Status and Dependents Analysis 
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/8710d32e7f6b4c47744311ccd90c668192d890bc/Images-for-Finance-Loan-Approval-Data/Loan%20Status%20and%20Dependents%20Analysis.png)

**Description:**
- Examines loan approval rates based on gender and number of dependents.
  
**Insights:**
- Males have more loan applications than females.
- Dependents impact approval rates, with higher dependents reducing approval probability.

##  Applicant Income vs Loan Amount 
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/3feff5f4841748dc0bbaabb9bf559615316da8f8/Images-for-Finance-Loan-Approval-Data/Applicant%20Income%20vs%20Loan%20Amount.png)

**Description:**
 * Compares applicant income to the requested loan amount.
 * Points are color-coded based on loan status (Approved = Red, Rejected = Blue).
   
**Insights:**
 * Most applicants with lower incomes request smaller loans.
 * Loan approvals tend to be concentrated around lower loan amounts.
 * High-income applicants have varying approval rates, suggesting other eligibility factors play a role.

## Average Loan Amount by Employment Type 
![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/02b08954d7f700b6ac6d74f82f52e94646b2bddd/Images-for-Finance-Loan-Approval-Data/Average%20Loan%20Amount%20by%20Employment%20Type.png)

**Description:**
 * Displays average loan amounts for Self-Employed vs Salaried applicants.
   
**Insights:**
 * Self-employed applicants tend to request higher loan amounts.
 * Salaried individuals have higher approval rates compared to self-employed.

## Impact of Credit History on Loan Approval 

![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/dfa295d08ee58aa21b2271f6a41631ece58c370b/Images-for-Finance-Loan-Approval-Data/Impact%20of%20Credit%20History%20on%20Loan%20Approval.png)

**Description:**
 * Shows the number of approved and rejected applications based on credit history.
   
**Insights:**
 * A strong credit history (1) leads to a much higher approval rate.
 * Applicants with no credit history (0) have a significantly lower chance of approval.

# Interactive Distribution of Loan Amounts

![Image](https://github.com/TaniaAHossain/Loan-Approval-Trends-Insights-in-Azure-Synapse-Analytics/blob/312739c5efca0cb021bc48808e77317c2a2ba786/Images-for-Finance-Loan-Approval-Data/Interactive%20Distribution%20of%20Loan%20Amounts.png)

**Description:**
 - Represents the distribution of loan amounts across applicants.
   
**Insights:**
 - Most loans fall in the 100-200 range.
 - Higher loan amounts are less frequent, indicating stricter approval conditions.

# Loan Amount Distribution by Property Area 

![Image](https://github.com/user-attachments/assets/03917542-f0a8-4bc7-b865-0b58417ed7e3)

**Description:**
 - Shows loan amount variations across Urban, Semi-Urban, and Rural areas.
   
**Insights:**
- Urban areas have a wider range of loan amounts.
- Rural areas generally see lower loan amounts, likely due to different economic conditions.

# Loan Approval Rate by Credit History

![Image](https://github.com/user-attachments/assets/70edf651-6ba5-488a-828f-9e583cc4dd1b)

**Description:**
- Highlights the proportion of approved loans for different credit histories.
  
**Insights:**
- 85.4% of approved applicants have a strong credit history.
- Only 14.6% of approvals go to applicants with no credit history.

# Credit History Distribution 

![Image](https://github.com/user-attachments/assets/49b64cc8-2701-4231-bc9f-2066a81dcb02)

**Description:**
- Displays the proportion of applicants with good (1) vs. no credit history (0).
  
**Insights:**
- 84.1% of applicants have a credit history, while 15.9% do not.
- This indicates that most applicants have an existing financial history, which could improve their approval chances.

# Distribution of Loan Amounts
![Image](https://github.com/user-attachments/assets/96e5de11-b8ca-4bfc-a25b-6a3aa1d44053)

**Description:**
- Represents the frequency of different loan amounts across applicants.
  
**Insights:**
- Most loans fall within the 100-200 range.
- Higher loan amounts (>400) are less frequent, suggesting stricter approval conditions.

# Loan Amount Distribution by Marital Status 
![Image](https://github.com/user-attachments/assets/72cea29b-97b1-4393-b4b1-8d034f2b4c02)

**Description:** 
- Compares the proportion of loans by marital status (Married vs. Single).
  
**Insights:**
- 55.5% of loans go to married individuals, while 44.5% go to single applicants.
- This could indicate that married applicants have higher approval rates, possibly due to dual income sources.

# Loan Amount Trend by Education Level 
![Image](https://github.com/user-attachments/assets/821257d3-5fbd-43a8-9d6c-47b61292d062)

**Description:**
- Shows the average loan amount trends between graduates and non-graduates.
  
**Insights:**
- Graduates tend to receive higher loan amounts than non-graduates.
- This suggests that education level may influence the perceived financial stability of applicants.

 # Loan Status by Gender 
![Image](https://github.com/user-attachments/assets/17db33af-c582-44a9-ae8e-751a91b33236)

**Description:**
- Examines loan approval trends across male and female applicants.
  
**Insights:**
- Male applicants receive more loan approvals than female applicants.
- Female applicants tend to have lower approval rates, which may indicate income differences or risk assessment biases.

# Loan Status by Property Area 
![Image](https://github.com/user-attachments/assets/f9d44f5e-7512-4d30-bcfa-ed5a08bb981c)

**Description:**
- Compares loan approvals across Rural, Urban, and Semi-Urban areas.
  
**Insights:**
- Semi-Urban areas have the highest loan approvals.
- Urban areas follow closely, while rural areas have the least approvals, likely due to lower income levels or financial risks.

# Key Takeaways

**- Credit History is the Biggest Factor** – 85.4% of approved loans belong to applicants with a good credit history.

**- Loan Amounts Cluster Between 100-200** – Most approved loans fall in this range; higher amounts face stricter approvals.

**- Married and Graduate Applicants Receive More Loans** – Marital status and education level positively impact loan amounts.

**- Higher Income Leads to More Approvals** – Both applicant and co-applicant income influence loan acceptance rates.

**- Self-Employed Applicants Request Higher Loans but Face More Scrutiny** – Salaried applicants are approved more quickly.

**- Semi-Urban Areas Have the Highest Loan Approvals** – Rural applicants face lower approval rates due to financial risk factors.

**- Men Receive More Loans Than Women** – Gender disparity is evident in approval trends.

**- Property Area and Credit History Together Influence Approvals** – Rural applicants with poor credit history have the lowest chances.

# Conclusion 
Loan approvals are primarily driven by credit history, income, and demographic factors. Higher-income, married, and graduate applicants see better approval rates, especially in semi-urban areas, while self-employed and rural applicants struggle with stricter conditions. These insights can help financial institutions refine lending policies and risk models.













