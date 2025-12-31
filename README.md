# 📊 Customer Churn Analysis – Telecom Industry

## 📌 Project Overview

This project focuses on analyzing **customer churn behavior in the telecom industry** using an end-to-end data analytics workflow. The goal is to identify key factors driving customer churn and provide actionable business insights that can help improve customer retention strategies.

The project demonstrates practical skills across **Python (EDA & data cleaning)**, **SQLite (SQL business analysis)**, and **Power BI (interactive dashboard visualization)**.

---

## 🎯 Business Objective

* Identify churn patterns across customer demographics and service usage
* Understand the impact of contract type, tenure, payment method, and charges on churn
* Quantify revenue loss due to customer churn
* Enable data-driven decision-making for retention strategies

---

## 🗂 Dataset Information

* **Dataset Name:** Telco Customer Churn Dataset
* **Source:** IBM Sample Dataset
* **Total Records:** 7,032 customers
* **Total Columns:** 21

### Key Columns:

* `customerID`
* `gender`, `SeniorCitizen`, `Partner`, `Dependents`
* `tenure`, `TenureGroup`
* `Contract`, `PaymentMethod`, `PaperlessBilling`
* `MonthlyCharges`, `TotalCharges`
* `Churn`

---

## 🛠 Tools & Technologies

| Tool                   | Purpose                               |
| ---------------------- | ------------------------------------- |
| Python (Pandas, NumPy) | Data cleaning & preprocessing         |
| Matplotlib, Seaborn    | Exploratory Data Analysis             |
| SQLite                 | SQL-based business analysis           |
| Power BI               | Interactive dashboard & visualization |
| VS Code                | Development environment               |

---

## 🔄 Project Workflow

### 1️⃣ Data Loading & Cleaning (Python)

* Loaded raw CSV dataset using Pandas
* Converted `TotalCharges` to numeric values
* Handled missing values by removing invalid rows
* Encoded binary variables (Yes/No → 1/0)
* Created tenure segmentation (`TenureGroup`)
* Exported cleaned dataset to CSV

**Output:** `telecom_churn_cleaned.csv`

---

### 2️⃣ Database Creation & SQL Analysis (SQLite)

* Created SQLite database: `telecom_churn.db`
* Loaded cleaned data into `customers` table
* Performed business-driven SQL analysis

#### Sample SQL Queries:

```sql
-- Total Customers
SELECT COUNT(*) FROM customers;

-- Churn Rate
SELECT ROUND(SUM(Churn)*100.0/COUNT(*),2) AS churn_rate FROM customers;

-- Churn by Contract Type
SELECT Contract, COUNT(*) AS total_customers, SUM(Churn) AS churned_customers
FROM customers
GROUP BY Contract;
```

---

### 3️⃣ Power BI Dashboard

* Connected SQLite database using ODBC
* Designed interactive dashboard with KPIs and slicers

#### Key KPIs:

* Total Customers
* Churned Customers
* Churn Rate (%)
* Average Monthly Charges

#### Visual Insights:

* Churn by Contract Type
* Churn by Tenure Group
* Churn by Payment Method
* Monthly Charges vs Churn

---


## 🔍 Key Insights

* **Month-to-month contracts** have the highest churn rate
* **Early tenure customers (0–1 year)** are more likely to churn
* **Electronic check payment method** shows higher churn risk
* Long-term contracts and auto-pay methods improve retention
* Churned customers contribute significant revenue loss

---



## 🏁 Conclusion

This project showcases the ability to transform raw customer data into meaningful business insights using a full analytics pipeline. It reflects real-world data analyst responsibilities, including data preparation, SQL querying, and executive-level dashboard reporting.

---



