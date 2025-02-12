#!/usr/bin/env python
# coding: utf-8

# ## Finance Loan approval Prediction Data
# 
# 
# 

# # **Unlocking Credit: Analyzing Loan Application Data**

# In[1]:


get_ipython().run_cell_magic('pyspark', '', "test_df = spark.read.load(path='abfss://finance-loan-approval-data@financeloanapprovaldata.dfs.core.windows.net/transformed-data/test/', format='csv',header=True)\r\ndisplay(test_df.limit (10))\n")


# In[2]:


get_ipython().run_cell_magic('pyspark', '', "train_df = spark.read.load(path='abfss://finance-loan-approval-data@financeloanapprovaldata.dfs.core.windows.net/transformed-data/train/', format='csv',header=True)\r\ndisplay(train_df.limit (10))\n")


# In[4]:


# For PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# For Plotly Interactive Visualizations
import plotly.express as px
import plotly.graph_objects as go

# For Data Manipulation
import pandas as pd

# For Basic Visualizations (if needed)
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt



# ### **Distribution of Loan Amounts**

# In[23]:


import plotly.express as px

# Convert to pandas for easy visualization
loan_amounts = train_df.select("LoanAmount").toPandas()

# Drop NaN values
loan_amounts_clean = loan_amounts['LoanAmount'].dropna()

# Create an interactive histogram using Plotly
fig = px.histogram(loan_amounts_clean, nbins=30, title="Distribution of Loan Amounts")

# Customize the plot for interactivity
fig.update_layout(
    xaxis_title="Loan Amount",
    yaxis_title="Frequency",
    bargap=0.1,  # Small gap between bars
    hovermode="x"  # Enable hover info along the x-axis
)

# Show the interactive plot
fig.show()


# This analysis aims to answer the question: What is the distribution of loan amounts in the dataset, excluding missing values, and how can an interactive histogram created with Plotly Express be used to visualize this distribution effectively? It achieves this by visually representing the frequencies of different loan amount ranges, allowing users to quickly understand the typical loan amounts and their distribution while providing interactivity for detailed exploration.

# ### **Loan Status by Gender**

# In[23]:


import plotly.express as px

# Group by Gender and Loan_Status to get counts
loan_status_by_gender = train_df.groupBy("Gender", "Loan_Status").count()

# Convert to Pandas for plotting
loan_status_by_gender_pd = loan_status_by_gender.toPandas()

# Create an interactive bar chart with Plotly Express
fig = px.bar(loan_status_by_gender_pd, 
             x="Gender", 
             y="count", 
             color="Loan_Status", 
             title="Loan Status by Gender",
             barmode='group')  # Display bars side-by-side

# Customize layout (optional)
fig.update_layout(
    xaxis_title="Gender",
    yaxis_title="Number of Loans"
)

# Show the interactive plot
fig.show()


# The resulting stacked bar chart provides a visual representation of loan approvals and rejections based on gender. Each bar represents a gender category, and the segments within each bar represent the proportions of approved and rejected loans for that gender. By comparing the heights of the stacked segments, users can quickly understand the relationship between gender and loan approval outcomes.

# ### **Applicant Income vs. Loan Amount (Segmented by Loan Status)**

# In[21]:


import plotly.express as px

# Select the relevant columns and convert to Pandas
income_vs_loan = train_df.select("ApplicantIncome", "LoanAmount", "Loan_Status").toPandas()

# Create an interactive scatter plot using Plotly
fig = px.scatter(income_vs_loan, 
                 x='ApplicantIncome', 
                 y='LoanAmount', 
                 color='Loan_Status',  # Different colors for different loan statuses
                 title='Applicant Income vs Loan Amount', 
                 labels={'ApplicantIncome':'Applicant Income', 'LoanAmount':'Loan Amount'},
                 hover_data=['ApplicantIncome', 'LoanAmount'])  # Show these columns on hover

# Customize the layout
fig.update_layout(
    xaxis_title="Applicant Income",
    yaxis_title="Loan Amount",
    height=600,  # Height of the figure
    width=1000   # Width of the figure
)

# Show the interactive plot
fig.show()


# This analysis aims to answer the question: How do applicant income and loan amount relate to each other, and how does loan status vary across these factors, within an interactive scatter plot visualization created using Plotly Express? It achieves this by visually representing the data points, allowing users to explore the relationships and identify potential correlations or patterns that might influence loan decisions.

# ### **Loan Amount Distribution with Plotly**

# In[13]:


import plotly.express as px

# Convert PySpark DataFrame to Pandas
loan_amounts_pd = train_df.select("LoanAmount").toPandas()

# Interactive histogram with Plotly
fig = px.histogram(loan_amounts_pd, x="LoanAmount", nbins=30, title="Interactive Distribution of Loan Amounts")
fig.update_layout(xaxis_title="Loan Amount", yaxis_title="Count")
fig.show()


# The resulting histogram provides a visual representation of the distribution of loan amounts. The x-axis shows the range of loan amounts, and the y-axis shows the frequency or count of loans within each bin or interval. Users can interact with the histogram by hovering over bars to see detailed information about the loan amounts and their frequencies.

# ### **Loan Status by Property Area (Interactive Bar Chart)**

# In[14]:


# Group by Property_Area and Loan_Status
status_by_area = train_df.groupBy("Property_Area", "Loan_Status").count()

# Convert to Pandas
status_by_area_pd = status_by_area.toPandas()

# Interactive bar chart
fig = px.bar(status_by_area_pd, x="Property_Area", y="count", color="Loan_Status", 
             title="Loan Status by Property Area", barmode="group")
fig.update_layout(xaxis_title="Property Area", yaxis_title="Number of Loans")
fig.show()


# The resulting bar chart provides a visual comparison of loan approval rates across different property areas. By observing the heights of the bars for approved and rejected loans within each property area, users can identify potential variations in loan approval patterns based on location. For example, they might observe whether certain property areas have higher or lower loan approval rates compared to others.

# ### **Interactive Loan Amount vs. Applicant Income Scatter Plot (With Zooming and Hover)**

# In[15]:


# Convert necessary columns to Pandas
income_vs_loan_pd = train_df.select("ApplicantIncome", "LoanAmount", "Loan_Status").toPandas()

# Scatter plot with Plotly
fig = px.scatter(income_vs_loan_pd, x="ApplicantIncome", y="LoanAmount", color="Loan_Status",
                 title="Applicant Income vs Loan Amount", hover_data=['ApplicantIncome', 'LoanAmount'])
fig.update_layout(xaxis_title="Applicant Income", yaxis_title="Loan Amount")
fig.show()


# This analysis aims to answer the question: How are applicant income, loan amount, and loan approval status related? It achieves this by visually representing the data in a scatter plot, allowing for an intuitive exploration of the relationship between these variables. Users can visually identify potential correlations and patterns, providing insights into the factors influencing loan decisions.

# ### **Loan Approval Rate by Credit History (Interactive Pie Chart)**

# In[16]:


# Group by Credit History and Loan Status
approval_credit_hist = train_df.groupBy("Credit_History", "Loan_Status").count()

# Convert to Pandas
approval_credit_hist_pd = approval_credit_hist.toPandas()

# Interactive pie chart
fig = px.pie(approval_credit_hist_pd, names="Credit_History", values="count", color="Loan_Status",
             title="Loan Approval Rate by Credit History")
fig.show()


# The resulting pie chart provides a visual representation of loan approval rates based on credit history. By comparing the sizes of the slices within each credit history category (represented by different colors for approved and rejected loans), users can quickly understand the impact of credit history on loan approval decisions.

# ### **Loan Status and Dependents (Interactive Sunburst Chart)**

# In[19]:


# Fill missing values in 'Dependents', 'Gender', and 'Loan_Status' with a placeholder, such as 'Unknown'
dependents_loan_status_pd = dependents_loan_status_pd.fillna('Unknown')

# Sunburst chart
fig = px.sunburst(dependents_loan_status_pd, path=['Dependents', 'Gender', 'Loan_Status'], values='count',
                  title="Loan Status and Dependents Analysis")
fig.show()


# The resulting sunburst chart provides a hierarchical view of the loan data, allowing for the exploration of relationships between loan status, dependents, and gender. The size of each segment reflects the frequency of that specific combination of factors. This visualization helps in identifying patterns and understanding how these factors might influence loan approvals.

# ### **Loan Amount vs. Coapplicant Income Interactive Bubble Chart**

# In[22]:


# Cast 'LoanAmount' and 'CoapplicantIncome' to numeric types in PySpark
train_df = train_df.withColumn("LoanAmount", col("LoanAmount").cast("float"))
train_df = train_df.withColumn("CoapplicantIncome", col("CoapplicantIncome").cast("float"))

# Convert to Pandas after fixing the data types
income_vs_loan_coapplicant = train_df.select("CoapplicantIncome", "LoanAmount", "Loan_Status").toPandas()

# Check if the types are now correct
print(income_vs_loan_coapplicant.dtypes)

# Now create the bubble chart after fixing the data types
fig = px.scatter(income_vs_loan_coapplicant, x="CoapplicantIncome", y="LoanAmount", 
                 size="LoanAmount", color="Loan_Status",
                 title="Loan Amount vs Coapplicant Income", hover_data=["CoapplicantIncome", "LoanAmount"])
fig.update_layout(xaxis_title="Coapplicant Income", yaxis_title="Loan Amount")
fig.show()



# This analysis aims to explore how coapplicant income and loan amount influence loan approval status. The bubble chart provides a visual representation of this relationship, where bubble size reflects loan amount and bubble color indicates loan approval status. This visualization allows for an intuitive understanding of the data and identification of potential trends or patterns.

# ### **Loan Amount Distribution by Property Area**

# In[25]:


fig3 = px.violin(train_df, x="Property_Area", y="LoanAmount", box=True, points="all", 
                 title="Loan Amount Distribution by Property Area",
                 labels={"Property_Area": "Property Area", "LoanAmount": "Loan Amount"})
fig3.show()


# The violin plot helps to answer the question: How are loan amounts distributed across different property areas? It achieves this by visually representing the distribution of loan amounts for each property area using a violin-shaped plot, making it easier to compare the distributions and identify potential differences.

# ### **Credit History Distribution**

# In[34]:


fig7 = px.pie(test_df, names="Credit_History", title="Credit History Distribution")
fig7.show()


#  The pie chart helps to answer the question: What is the distribution of credit history among the applicants in the test dataset? It achieves this by visually representing the proportion of each credit history category in the form of a pie chart, making it easier to understand the overall credit history profile of the applicants.

# ### **Loan Status by Property Area and Credit History**

# In[35]:


fig8 = px.treemap(train_df, path=["Property_Area", "Credit_History", "Loan_Status"], 
                  values="LoanAmount", 
                  title="Treemap: Loan Status by Property Area and Credit History",
                  labels={"Property_Area": "Property Area", "Credit_History": "Credit History", "Loan_Status": "Loan Status"})
fig8.show()


# The treemap provides a hierarchical view of the loan data, allowing for a quick comparison of loan amounts and distributions across different property areas, credit histories, and loan approval statuses. It aids in identifying patterns and insights regarding loan approvals based on these factors. In essence, the treemap helps to answer the question: How are loan amounts distributed across different property areas, credit histories, and loan statuses? It achieves this by visually representing the data in a hierarchical structure, making it easier to identify trends and patterns.

# ### **Loan Approvals over Property Area**

# In[39]:


fig10 = px.bar(train_df, x="Property_Area", y="LoanAmount", color="Loan_Status", 
               animation_frame="Credit_History", barmode="group",
               title="Animated Bar Chart: Loan Amounts by Property Area over Credit History",
               labels={"Property_Area": "Property Area", "LoanAmount": "Loan Amount"})
fig10.show()


# This animated bar chart helps to explore trends and patterns in loan amounts and approvals based on property area and credit history, providing insights into the factors influencing loan decisions.

# ### **Impact of Credit History on Loan Approval**

# In[18]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import count

# Initialize Spark session (if not already created)
spark = SparkSession.builder.appName("CreditHistoryAnalysis").getOrCreate()

# Group data by Credit History and Loan Status
credit_analysis = train_df.groupBy("Credit_History", "Loan_Status").agg(count("*").alias("Count"))

# Convert to Pandas DataFrame for visualization
credit_analysis_pd = credit_analysis.toPandas()

# Create an interactive area chart
import plotly.express as px
fig = px.area(credit_analysis_pd, x='Credit_History', y='Count', color='Loan_Status',
              title='Impact of Credit History on Loan Approval',
              labels={'Credit_History': 'Credit History', 'Count': 'Number of Applicants'},
              line_group='Loan_Status')

# Show the interactive visualization
fig.show()


# This analysis aims to answer the question: How does an applicant's credit history affect their chances of getting a loan approved? It achieves this by visually presenting the distribution of loan approvals and rejections based on credit history using an interactive chart.

# ### **Loan Amount Trend by Education Level**

# In[57]:


import pyspark.sql.functions as F
import plotly.express as px
from IPython.display import display

train_df = train_df.withColumn("Education", F.trim(F.col("Education")))
education_avg = train_df.groupBy("Education").agg(F.avg("LoanAmount").alias("Avg_LoanAmount"))

# Convert PySpark DataFrame to Pandas for Plotly visualization
education_pd = education_avg.toPandas()

# Create Line Chart using Plotly
fig3 = px.line(education_pd, x="Education", y="Avg_LoanAmount", markers=True, 
               title="Loan Amount Trend by Education Level", line_shape="linear")

fig3.update_xaxes(categoryorder="category ascending")
display(fig3)


# This analysis shows that graduates receive higher loan amounts than non-graduates. This trend is likely due to higher earning potential and job stability among graduates, making them lower-risk borrowers. Lenders may perceive graduates as more financially secure, leading to larger loan approvals. This suggests that education plays a key role in credit decisions, influencing both loan eligibility and borrowing capacity.

# ### **Loan Amount Distribution by Marital Status**

# In[58]:


# Compute average loan amount by Marital Status using PySpark
married_avg = train_df.groupBy("Married").agg(F.avg("LoanAmount").alias("Avg_LoanAmount"))

married_pd = married_avg.toPandas()

fig2 = px.pie(married_pd, names="Married", values="Avg_LoanAmount", 
              title="Loan Amount Distribution by Marital Status")

display(fig2)


# This analysis shows that married individuals receive higher loan amounts than unmarried applicants. This is likely due to dual-income stability, which reduces financial risk for lenders and increases borrowing capacity. Married applicants are perceived as more creditworthy, leading to higher loan approvals and larger loan disbursements. This trend suggests that financial institutions may favor married borrowers due to their stronger repayment potential.

# ### **Average Loan Amount by Employment Type**

# In[59]:


employment_avg = train_df.groupBy("Self_Employed").agg(F.avg("LoanAmount").alias("Avg_LoanAmount"))

employment_pd = employment_avg.toPandas()

fig4 = px.bar(employment_pd, x="Avg_LoanAmount", y="Self_Employed", orientation="h",
              title="Average Loan Amount by Employment Type", color="Self_Employed")

display(fig4)


# This analysis shows that self-employed individuals receive higher but more variable loan amounts compared to salaried applicants. This trend suggests that self-employed borrowers often require larger loans for business expansion and operational costs, but their irregular income patterns introduce higher risk for lenders. Unlike salaried employees, whose stable income makes them easier to assess for creditworthiness, self-employed applicants face stricter evaluations and inconsistent loan approvals. This highlights the need for customized loan products with flexible repayment terms to better accommodate the financial realities of self-employed borrowers.

# ### **Interactive Loan Amount Trends Across Different Variables**

# In[62]:


import pyspark.sql.functions as F
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import display

# Trim categorical columns to avoid mismatches
train_df = train_df.withColumn("Gender", F.trim(F.col("Gender")))
train_df = train_df.withColumn("Married", F.trim(F.col("Married")))
train_df = train_df.withColumn("Education", F.trim(F.col("Education")))
train_df = train_df.withColumn("Self_Employed", F.trim(F.col("Self_Employed")))
train_df = train_df.withColumn("Property_Area", F.trim(F.col("Property_Area")))

#  Compute Average Loan Amount by Different Categories
gender_avg = train_df.groupBy("Gender").agg(F.avg("LoanAmount").alias("Avg_LoanAmount")).toPandas()
married_avg = train_df.groupBy("Married").agg(F.avg("LoanAmount").alias("Avg_LoanAmount")).toPandas()
education_avg = train_df.groupBy("Education").agg(F.avg("LoanAmount").alias("Avg_LoanAmount")).toPandas()
employment_avg = train_df.groupBy("Self_Employed").agg(F.avg("LoanAmount").alias("Avg_LoanAmount")).toPandas()
property_avg = train_df.groupBy("Property_Area").agg(F.avg("LoanAmount").alias("Avg_LoanAmount")).toPandas()
credit_avg = train_df.groupBy("Credit_History").agg(F.avg("LoanAmount").alias("Avg_LoanAmount")).toPandas()

#  Define Subplots and Specify the Pie Chart Type
fig = make_subplots(
    rows=3, cols=2, 
    subplot_titles=(
        "Loan Amount by Gender", "Loan Amount by Marital Status",
        "Loan Amount by Education Level", "Loan Amount by Employment Type",
        "Loan Amount by Property Area", "Loan Amount by Credit History"
    ),
    vertical_spacing=0.15,
    specs=[[{"type": "xy"}, {"type": "domain"}],  # Row 1: Bar + Pie
           [{"type": "xy"}, {"type": "xy"}],     # Row 2: Line + Bar
           [{"type": "xy"}, {"type": "xy"}]]     # Row 3: Scatter + Bar
)

# Add Bar Chart: Loan Amount by Gender
fig.add_trace(go.Bar(x=gender_avg["Gender"], y=gender_avg["Avg_LoanAmount"], name="Gender"), row=1, col=1)

# Add Pie Chart: Loan Amount by Marital Status (Corrected!)
fig.add_trace(go.Pie(labels=married_avg["Married"], values=married_avg["Avg_LoanAmount"], name="Marital Status"), row=1, col=2)

# Add Line Chart: Loan Amount by Education Level
fig.add_trace(go.Scatter(x=education_avg["Education"], y=education_avg["Avg_LoanAmount"], mode="lines+markers", name="Education"), row=2, col=1)

# Add Horizontal Bar Chart: Loan Amount by Employment Type
fig.add_trace(go.Bar(y=employment_avg["Self_Employed"], x=employment_avg["Avg_LoanAmount"], name="Employment Type", orientation="h"), row=2, col=2)

#  Add Scatter Plot: Loan Amount by Property Area
fig.add_trace(go.Scatter(x=property_avg["Property_Area"], y=property_avg["Avg_LoanAmount"], mode="markers", name="Property Area", marker=dict(size=12)), row=3, col=1)

# Add Stacked Bar Chart: Loan Amount by Credit History
fig.add_trace(go.Bar(x=credit_avg["Credit_History"].astype(str), y=credit_avg["Avg_LoanAmount"], name="Credit History"), row=3, col=2)

# Step 4: Add Dropdown Filters for Interactivity
fig.update_layout(
    title_text="Interactive Loan Amount Trends Across Different Variables",
    updatemenus=[{
        "buttons": [
            {"label": "Show All", "method": "update", "args": [{"visible": [True] * 6}]},
            {"label": "Gender", "method": "update", "args": [{"visible": [True, False, False, False, False, False]}]},
            {"label": "Marital Status", "method": "update", "args": [{"visible": [False, True, False, False, False, False]}]},
            {"label": "Education", "method": "update", "args": [{"visible": [False, False, True, False, False, False]}]},
            {"label": "Employment Type", "method": "update", "args": [{"visible": [False, False, False, True, False, False]}]},
            {"label": "Property Area", "method": "update", "args": [{"visible": [False, False, False, False, True, False]}]},
            {"label": "Credit History", "method": "update", "args": [{"visible": [False, False, False, False, False, True]}]},
        ],
        "direction": "down",
        "showactive": True,
    }]
)

#  Display the interactive combined chart
display(fig)



# The interactive loan amount trends analysis highlights key factors influencing loan approvals and amounts across different demographic and financial categories. Gender differences show minimal impact, while married individuals receive higher loan amounts, likely due to dual-income stability. Graduates secure larger loans, reflecting their higher earning potential and financial security. Self-employed applicants tend to take larger but more variable loans, indicating their diverse financial needs and income fluctuations. Urban applicants receive higher loan amounts, aligning with higher property values, and applicants with a strong credit history are favored in loan approvals. This analysis provides insights for lenders to refine loan policies, ensuring fair and data-driven lending decisions while managing risk effectively.
