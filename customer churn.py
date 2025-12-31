# import pandas as pd
# import numpy as np
# import matplotlib
# matplotlib.use('Agg')

# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
# df = df.dropna()

# binary_cols = ['Partner','Dependents','PhoneService',
#                'PaperlessBilling','Churn']

# for col in binary_cols:
#     df[col] = df[col].map({'Yes':1,'No':0})

# df['TenureGroup'] = pd.cut(
#     df['tenure'],
#     bins=[0,12,36,72],
#     labels=['0-1 Year','1-3 Years','3-6 Years']
# )

# sns.countplot(x='Churn', data=df)
# plt.title("Churn Distribution")
# plt.savefig("churn_distribution.png", dpi=300, bbox_inches='tight')
# plt.close()

# df.to_csv("telecom_churn_cleaned.csv", index=False)


# # print(df.shape)
# # print(df.info())
# # print(df.isnull().sum())

# # df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# # print(df)


# # df = df.dropna()
# # print(df)

# import sqlite3

# conn = sqlite3.connect("telecom_churn.db")
# query = """
# SELECT COUNT(*) AS total_customers
# FROM customers;
# """

# query = """
# SELECT COUNT(*) AS churned_customers
# FROM customers
# WHERE Churn = 1;
# """


# query = """
# SELECT
# ROUND(
#     SUM(CASE WHEN Churn = 1 THEN 1 ELSE 0 END) * 100.0
#     / COUNT(*),
# 2
# ) AS churn_rate
# FROM customers;
# """


# query = """
# SELECT
# Contract,
# COUNT(*) AS total_customers,
# SUM(Churn) AS churned_customers
# FROM customers
# GROUP BY Contract;
# """


# query = """
# SELECT
# Churn,
# ROUND(AVG(MonthlyCharges),2) AS avg_monthly_charges
# FROM customers
# GROUP BY Churn;
# """

# query = """
# SELECT
# SUM(TotalCharges) AS churn_revenue_loss
# FROM customers
# WHERE Churn = 1;
# """
# query = """
# SELECT
# PaymentMethod,
# COUNT(*) AS total_customers,
# SUM(Churn) AS churned_customers
# FROM customers
# GROUP BY PaymentMethod
# ORDER BY churned_customers DESC;
# """

# query = """
# SELECT
# TenureGroup,
# COUNT(*) AS total_customers,
# SUM(Churn) AS churned_customers
# FROM customers
# GROUP BY TenureGroup;
# """
# result = pd.read_sql(query, conn)
# print(result)
# conn.close()

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# ==============================
# 1. LOAD DATA
# ==============================

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# ==============================
# 2. DATA CLEANING
# ==============================

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

binary_cols = ['Partner','Dependents','PhoneService',
               'PaperlessBilling','Churn']

for col in binary_cols:
    df[col] = df[col].map({'Yes':1,'No':0})

df['TenureGroup'] = pd.cut(
    df['tenure'],
    bins=[0,12,36,72],
    labels=['0-1 Year','1-3 Years','3-6 Years']
)

df.to_csv("telecom_churn_cleaned.csv", index=False)

# ==============================
# 3. CREATE SQLITE DATABASE
# ==============================

conn = sqlite3.connect("telecom_churn.db")
df.to_sql("customers", conn, if_exists="replace", index=False)

# ==============================
# 4. RUN SQL QUERIES
# ==============================

queries = {
    "Tenure Group Analysis": """
        SELECT TenureGroup,
               COUNT(*) AS total_customers,
               SUM(Churn) AS churned_customers
        FROM customers
        GROUP BY TenureGroup;
    """,

    "Total Customers": """
        SELECT COUNT(*) AS total_customers
        FROM customers;
    """,

    "Churned Customers": """
        SELECT COUNT(*) AS churned_customers
        FROM customers
        WHERE Churn = 1;
    """,

    "Churn Rate": """
        SELECT ROUND(
            SUM(CASE WHEN Churn = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2) AS churn_rate
        FROM customers;
    """,

    "Contract Analysis": """
        SELECT Contract,
               COUNT(*) AS total_customers,
               SUM(Churn) AS churned_customers
        FROM customers
        GROUP BY Contract;
    """,

    "Payment Method Risk": """
        SELECT PaymentMethod,
               COUNT(*) AS total_customers,
               SUM(Churn) AS churned_customers
        FROM customers
        GROUP BY PaymentMethod
        ORDER BY churned_customers DESC;
    """,

    "Revenue Lost to Churn": """
        SELECT SUM(TotalCharges) AS churn_revenue_loss
        FROM customers
        WHERE Churn = 1;
    """
}

for title, query in queries.items():
    print(f"\n--- {title} ---")
    print(pd.read_sql(query, conn))

# ==============================
# 5. CLOSE DATABASE (LAST STEP)
# ==============================

conn.close()
