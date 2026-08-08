# 🛍️ Mall Customer Segmentation Using K-Means Clustering

## 📌 Project Overview

Mall Customer Segmentation is an **unsupervised machine learning** project that aims to identify distinct groups of customers based on their demographic characteristics and purchasing behavior.

In this project, customer information such as **age, gender, annual income, and spending score** is analyzed to discover meaningful customer segments. The **K-Means clustering algorithm** is used to group customers who have similar characteristics and spending behaviors.

The resulting customer segments can help businesses understand their customers better and develop more targeted marketing strategies, personalized promotions, and customer engagement programs.

---

## 🎯 Project Objective

The main objective of this project is to:

* Analyze customer demographic and spending information.
* Identify groups of customers with similar characteristics.
* Apply **K-Means clustering** to segment mall customers.
* Determine an appropriate number of customer clusters.
* Profile and interpret the characteristics of each cluster.
* Generate actionable business insights from the customer segments.
* Support data-driven marketing and customer relationship decisions.

---

# ❗ Problem Statement

## Business Problem

A shopping mall serves customers with different ages, income levels, and spending behaviors. However, treating all customers in the same way may not be effective because different customer groups have different needs, preferences, and purchasing patterns.

For example, some customers may have **high income and high spending**, while others may have **high income but low spending**. Similarly, younger customers may demonstrate different spending behavior compared with older customers.

Without proper customer segmentation, the mall may have difficulty:

* Identifying its most valuable customer groups.
* Understanding differences in customer spending behavior.
* Designing targeted marketing campaigns.
* Developing personalized promotions.
* Allocating marketing resources effectively.
* Identifying potential customers for increased engagement.

### Problem Statement

> **The problem is to identify meaningful customer segments from mall customer data based on demographic and purchasing characteristics, and to determine how these segments can be used to support targeted marketing and better business decision-making.**

Since there are no predefined customer segment labels in the dataset, this is an **unsupervised machine learning problem**.

---

# 📊 Dataset Description

The project uses the **Mall Customers dataset**, which contains information about 200 mall customers.

### Dataset Dimensions

* **Number of customers:** 200
* **Number of features:** 5
* **Missing values:** None
* **Target variable:** None
* **Machine Learning Type:** Unsupervised Learning
* **Clustering Algorithm:** K-Means

### Features

| Feature                  | Description                                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `CustomerID`             | Unique identification number assigned to each customer                                                             |
| `Gender`                 | Gender of the customer                                                                                             |
| `Age`                    | Age of the customer                                                                                                |
| `Annual Income (k$)`     | Customer's annual income measured in thousands of dollars                                                          |
| `Spending Score (1-100)` | Score assigned to the customer based on spending behavior, where a higher score indicates higher spending activity |

---

# 🔍 Understanding the Key Variables

### CustomerID

A unique identifier for each customer.

It is useful for identifying individual customers but generally **should not be used as a clustering feature**, because the ID itself has no meaningful relationship with customer behavior.

### Gender

Represents the customer's gender.

It can be used for demographic analysis and understanding the composition of customer segments.

### Age

Represents the customer's age.

Age may help identify differences in purchasing behavior among younger, middle-aged, and older customers.

### Annual Income (k$)

Represents the customer's annual income in thousands of dollars.

For example:

`60` means approximately **$60,000 annual income**.

Income is an important factor for understanding the customer's purchasing capacity.

### Spending Score (1-100)

Represents the customer's spending behavior.

* **Low score** → relatively low spending activity
* **Medium score** → moderate spending activity
* **High score** → relatively high spending activity

This is one of the most important variables for identifying customer segments.

---

# 🧠 Why Is This an Unsupervised Learning Problem?

This project does not contain a predefined column that tells us which customer belongs to which segment.

For example, the dataset does not contain a column such as:

```text
Customer Segment
----------------
Premium
Budget
Regular
Potential
```

Instead, the algorithm must discover the natural groups within the data.

Therefore, this project uses **unsupervised learning**, specifically **K-Means clustering**.

---

# ⚙️ Methodology

The project follows a complete data science workflow:

```text
Dataset
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Data Preprocessing
   ↓
Determine Optimal Number of Clusters
   ↓
K-Means Clustering
   ↓
Cluster Visualization
   ↓
Cluster Profiling
   ↓
Business Insights
   ↓
Conclusion
```

---

# 🔬 Exploratory Data Analysis

Exploratory Data Analysis (EDA) is performed to understand the structure and characteristics of the customer data.

The analysis includes:

* Checking dataset dimensions.
* Checking data types.
* Checking missing values.
* Checking duplicate records.
* Analyzing numerical distributions.
* Analyzing gender distribution.
* Examining relationships between age, income, and spending score.
* Identifying possible patterns and customer groups.

---

# 🤖 K-Means Clustering

K-Means is an unsupervised machine learning algorithm that divides observations into a predefined number of clusters.

The algorithm works by:

1. Selecting the number of clusters, **K**.
2. Initializing cluster centroids.
3. Assigning each customer to the nearest centroid.
4. Recalculating the centroid of each cluster.
5. Repeating the assignment and centroid update process.
6. Continuing until the clusters stabilize.

The goal is to create clusters where customers within the same cluster are **similar to each other**, while customers in different clusters are **as different as possible**.

---

# 📐 Choosing the Optimal Number of Clusters

The appropriate value of **K** can be investigated using techniques such as:

### Elbow Method

The Elbow Method examines the relationship between the number of clusters and the clustering objective function, commonly represented by **Within-Cluster Sum of Squares (WCSS)**.

The point where adding additional clusters provides significantly smaller improvements can be considered an appropriate value of K.

### Silhouette Score

The Silhouette Score evaluates how well each customer fits within its assigned cluster compared with other clusters.

A higher silhouette score generally indicates better-separated and more cohesive clusters.

---

# 👥 Customer Segmentation

After selecting the appropriate number of clusters, K-Means assigns every customer to a cluster.

Each cluster can then be analyzed using:

* Average age
* Average annual income
* Average spending score
* Number of customers
* Gender distribution
* Other relevant characteristics

This process is called **Cluster Profiling**.

---

# 💡 Expected Business Insights
💼 Expected Business Insights
🟢 Cluster 0 — Moderate Customers

81 customers (40.5%) | Income: $55.3k | Spending Score: 49.5

This is the largest customer segment, representing 40.5% of all customers. These customers have moderate income and moderate spending behavior.

Business insight:
This group represents the mall's core customer base. Since they already show moderate spending, there is an opportunity to increase their purchasing activity through targeted promotions.

Recommended strategy:

Cross-selling complementary products
Up-selling higher-value products
Loyalty and reward programs
Personalized promotions
Seasonal discounts

Business opportunity: ⭐⭐⭐⭐
Because this is the largest segment, even a small increase in their average spending could have a significant impact on overall revenue.

🔵 Cluster 1 — High-Value Customers

39 customers (19.5%) | Income: $86.5k | Spending Score: 82.1

These customers have high income and very high spending scores. They are among the most valuable customers for the mall.

Business insight:
They have both strong purchasing power and a strong tendency to spend. Losing these customers could have a significant impact on revenue.

Recommended strategy:

VIP loyalty programs
Exclusive offers
Premium products
Early access to new products
Personalized customer service
Special events and rewards

Business opportunity: ⭐⭐⭐⭐⭐
Priority: Customer retention

The main objective should be to retain and strengthen relationships with these customers, rather than simply trying to increase their spending.

🟡 Cluster 2 — Aspirational Shoppers

22 customers (11.0%) | Income: $25.7k | Spending Score: 79.4

This is a particularly interesting segment because customers have relatively low income but very high spending scores.

Business insight:
These customers spend significantly despite having lower income. They may be highly interested in fashion, lifestyle products, promotions, or socially attractive products.

Recommended strategy:

Discounts
Installment/payment options
Affordable premium products
Bundle offers
Loyalty rewards
Limited-time promotions

Business opportunity: ⭐⭐⭐⭐⭐
This segment has strong engagement and spending behavior. The mall should encourage them to remain loyal while offering products that match their purchasing capacity.

🟠 Cluster 3 — Targetable Wealthy Customers

35 customers (17.5%) | Income: $88.2k | Spending Score: 17.1

These customers have the highest average income among the five groups but one of the lowest spending scores.

Business insight:
This is one of the most important growth-opportunity segments. These customers have substantial purchasing power but currently spend relatively little at the mall.

The challenge is not their ability to spend, but understanding why they are not spending more.

Recommended strategy:

Personalized marketing
Premium product recommendations
Exclusive promotions
VIP invitations
High-end product demonstrations
Personalized customer experiences

Business opportunity: ⭐⭐⭐⭐⭐
Priority: Increase customer engagement

If the mall can successfully convert their purchasing potential into actual spending, this segment could generate significant additional revenue.

🔴 Cluster 4 — Frugal Customers

23 customers (11.5%) | Income: $26.3k | Spending Score: 20.9

These customers have relatively low income and low spending behavior.

Business insight:
Their purchasing capacity is limited, so expensive premium marketing strategies may not be effective for this segment.

Recommended strategy:

Affordable products
Budget-friendly promotions
Discounts
Essential products
Value-for-money bundles
Price-sensitive campaigns

Business opportunity: ⭐⭐⭐
The focus should be on retention and affordability, rather than trying to significantly increase spending.


> **Note:** The actual number and characteristics of clusters should be determined from the final K-Means results rather than assumed in advance.

---

# 📈 Dataset Summary

Based on the uploaded dataset:

| Statistic              |   Value |
| ---------------------- | ------: |
| Total Customers        |     200 |
| Total Columns          |       5 |
| Female Customers       |     112 |
| Male Customers         |      88 |
| Average Age            |   38.85 |
| Average Annual Income  | $60.56k |
| Average Spending Score |   50.20 |
| Minimum Annual Income  |    $15k |
| Maximum Annual Income  |   $137k |
| Minimum Spending Score |       1 |
| Maximum Spending Score |      99 |
| Missing Values         |       0 |

---

# 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical computation
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Scikit-learn** – Machine learning and K-Means clustering
* **Jupyter Notebook** – Development and analysis

---

# 📁 Project Structure

```text
Mall-Customer-Segmentation/
│
├── dataset/
│   └── Mall_Customers.csv
│
├── Mall_Customer_Segmentation.ipynb
│    
│
├── figures/
│   
│   
│
├── README.md
│
└── app.py
```
# 📌 Key Questions the Project Answers

This project aims to answer the following questions:

1. What are the main characteristics of mall customers?
2. How are customers distributed by age, income, and spending score?
3. Are there naturally occurring groups of customers?
4. What is the appropriate number of customer segments?
5. What are the characteristics of each customer segment?
6. Which customer groups have high spending behavior?
7. Which groups represent potential opportunities for targeted marketing?
8. How can customer segmentation support business decision-making?

---

# 🎯 Expected Outcome

At the end of the project, the K-Means model should provide meaningful customer segments that can be interpreted from a business perspective.

The final result should not simply be a collection of mathematical clusters. Instead, each cluster should be given a meaningful business interpretation based on its characteristics.

For example:

```text
Cluster 0 → MODERATE CUSTOMERS
Cluster 1 → HIGH VALUE CUSTOMERS
Cluster 2 → ASPIRATIONAL SHOPPERS
Cluster 3 → TARGETABLE WEALTHY CUSTOMERS
Cluster 4 → FRUGAL CUSTOMERS
```

The exact cluster labels and number of segments will depend on the results of the analysis.

---

# 💼 Business Value

Customer segmentation can help mall management move from **general marketing** toward **targeted marketing**.

Instead of offering the same promotion to every customer, the mall can design different strategies for different customer groups.

This can potentially help improve:

* Customer engagement
* Marketing effectiveness
* Customer retention
* Promotional targeting
* Customer experience
* Revenue opportunities
* Business decision-making

---

# 🏁 Conclusion

The Mall Customer Segmentation project demonstrates how **unsupervised machine learning** can be applied to a real-world business problem.

By combining customer demographics with income and spending behavior, the project uses K-Means clustering to discover meaningful customer groups. The resulting clusters can provide valuable insights into customer behavior and help businesses develop more effective and targeted marketing strategies.

Ultimately, the project demonstrates the practical value of **data-driven customer segmentation for business intelligence and decision-making**.

# Localapplink

http://localhost:8502


