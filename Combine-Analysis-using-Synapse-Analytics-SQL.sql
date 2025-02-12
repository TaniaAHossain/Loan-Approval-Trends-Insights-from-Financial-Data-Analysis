---- 1. Get Total Loan Applications by Property Area Across Both Datasets

SELECT Property_Area, COUNT(*) AS Total_Applications
FROM (
    SELECT Loan_ID, Property_Area FROM train
    UNION ALL
    SELECT Loan_ID, Property_Area FROM test
) AS CombinedData
GROUP BY Property_Area;

--- 2. Find the Highest Loan Amount from Both Datasets

SELECT MAX(LoanAmount) AS Max_Loan_Amount
FROM (
    SELECT LoanAmount FROM train
    UNION ALL
    SELECT LoanAmount FROM test
) AS CombinedLoans;

---3. Get the Count of Unique Applicants Across Both Datasets

SELECT COUNT(DISTINCT Loan_ID) AS Unique_Applicants
FROM (
    SELECT Loan_ID FROM train
    UNION ALL
    SELECT Loan_ID FROM test
) AS CombinedData;

--- 4. Find Loan Applications Where Income is Higher Than a Certain Threshold in Both Datasets

SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount
FROM (
    SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount FROM train
    UNION ALL
    SELECT Loan_ID, ApplicantIncome, CoapplicantIncome, LoanAmount FROM test
) AS CombinedData
WHERE ApplicantIncome > 5000;

---5. Get the Average Applicant Income Based on Credit History Across Both Datasets

SELECT Credit_History, AVG(ApplicantIncome) AS Avg_Applicant_Income
FROM (
    SELECT Credit_History, ApplicantIncome FROM train
    UNION ALL
    SELECT Credit_History, ApplicantIncome FROM test
) AS CombinedData
GROUP BY Credit_History;

---- 6. Count the Number of Self-Employed Applicants in Both Datasets

SELECT Self_Employed, COUNT(*) AS Total_Count
FROM (
    SELECT Self_Employed FROM train
    UNION ALL
    SELECT Self_Employed FROM test
) AS CombinedData
GROUP BY Self_Employed;

--- 7. Credit History Impact (Train vs. Test)

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

--- 8. Loan Distribution by Property Area (Train vs. Test)

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











