# E-Commerce Business Analysis Using SQL, Python, and Power BI

# Project Overview

This project analyzes e-commerce sales performance, customer behavior, product trends, and operational delivery performance using SQL, Python, and Power BI. My goal was to simulate a real-world business workflow by combining data cleaning, SQL analysis, Python analysis, KPI tracking, operational analysis, and interactive dashboard development.

I wanted this project to go beyond simple visualization and focus on generating business-oriented insights that could realistically support decision-making in areas such as:
- sales strategy,
- customer retention,
- product optimization,
- and logistics performance.

---

# Business Problem

The main business question that I explored throughout the project was:

> **What drives revenue and delivery performance in Brazilian e-commerce?**

To answer this question, I investigated revenue by region, top-performing product categories, customer purchasing behavior, repeat purchase patterns, monthly revenue trends and delivery performance across Brazilian states. I combined both commercial analytics and operational performance analysis.

---

# Tools & Technologies Used

## SQL

- PostgreSQL
- Views
- CASE statements
- Aggregations
- GROUP BY
- JOINS
- CTEs

## Python

- Pandas
- Matplotlib
- Seaborn
- Prophet

## Business Intelligence

- Power BI
- DAX
- KPI Cards
- Interactive Dashboard Design

---

# Dataset

Dataset used:

- **Brazilian E-Commerce Public Dataset by Olist (Kaggle)**

The original dataset consisted of multiple related tables containing:

[
- customer information,
- order data,
- payments,
- products,
- sellers,
- geolocation,
- delivery timestamps,
- and product category translations.
]

Because the dataset was relational, the project required creating joins and structured views before analysis could begin.

---

# Project Workflow

## 1. Data Cleaning & Preparation (in SQL)

The first stage focused on preparing the dataset for analysis. This included joining multiple relational tables, removing cancelled orders, excluding orders without delivery information, handling missing values, validating transaction consistency and translating product category names into English.

### Example SQL Query

```sql
CREATE VIEW revenue_by_category AS
SELECT
    t.product_category_name_english AS category,
    SUM(i.price) AS revenue

FROM orders o

LEFT JOIN items i
ON o.order_id = i.order_id

LEFT JOIN products p
ON i.product_id = p.product_id

LEFT JOIN translations t
ON p.product_category_name = t.product_category_name

WHERE o.order_status = 'delivered'

GROUP BY t.product_category_name_english;
```

The SQL preparation stage was especially important because the original dataset was distributed across multiple files and required relational modeling before meaningful analysis could be performed. Without joining those tables properly, the lack of relationships between datasets would cause errors later in the workflow.

---

## 2. SQL Business Analysis

SQL was used to answer core business questions related to product performance, city revenue generation, seasonality, repeat customer behavior and delivery performance.

Examples of explored metrics included:

- highest revenue-generating categories (example below),
- most profitable cities (example below),
- monthly revenue trends,
- repeat purchase categories,
- and average delivery delays by state.

### Revenue by Product Category

```sql
SELECT
    p.product_category_name,
    SUM(pay.payment_value) AS revenue

FROM orders o

LEFT JOIN order_items oi
ON o.order_id = oi.order_id

LEFT JOIN products p
ON oi.product_id = p.product_id

LEFT JOIN payments pay
ON o.order_id = pay.order_id

GROUP BY p.product_category_name

ORDER BY revenue DESC;
```

### Revenue by City

```sql
SELECT
    c.customer_city,
    SUM(pay.payment_value) AS revenue

FROM orders o

LEFT JOIN customers c
ON o.customer_id = c.customer_id

LEFT JOIN payments pay
ON o.order_id = pay.order_id

GROUP BY c.customer_city

ORDER BY revenue DESC;
```

---

## 3. Python Exploratory Analysis

Python was used for additional exploratory analysis and forecasting visualizations. The Python stage was primarily included to validate the analytical findings, explore trends outside dashboard software that had limited space and demonstrate flexibility with analytical tools. The project also includes forecasting experiments using Prophet to visualize potential future purchasing and revenue patterns. The screenshots of said prophets can be found in the screenshots folder of the project.

---

## 4. Power BI Dashboard Development

The final stage of the project involved building an interactive Power BI dashboard. I focused on readability and business storytelling.

The dashboard includes:

- KPI cards,
- revenue analysis,
- regional performance tracking,
- customer behavior insights,
- operational delivery metrics,
- forecasting sections,
- and interactive filtering/navigation.

---

# Business Questions

The project focused on answering several business-oriented questions:

1. Which product categories generate the highest revenue?
2. Which cities generate the highest order value?
3. Which months are the most profitable?
4. Which product categories drive repeat purchases?
5. How does delivery performance vary across regions?
6. What operational patterns may affect customer satisfaction?

---

# Dashboard Features

## KPI Tracking

The dashboard tracks:

- Total Revenue
- Total Profit
- Profit Margin
- Units Sold
- Top Performing Salesperson

---

## Revenue Analysis

Visualizations include:

- Revenue by Region
- Revenue by City
- Product Category Performance
- Monthly Revenue Trends
- Revenue Growth Tracking

---

## Customer Behavior Analysis

The project also investigates:

- repeat purchase behavior,
- high-performing categories,
- and purchasing patterns over time.

---

## Operational Analysis

An additional operational analysis section was included to investigate delivery performance across Brazilian states. This analysis explored whether estimated delivery timelines aligned with actual fulfillment performance.

---

# Key Findings

## Product Categories

The analysis identified several product categories responsible for the majority of revenue generation, including:

- health & beauty,
- watches & gifts,
- bed & bath products,
- sports & leisure,
- and computer accessories.

These categories consistently generated the highest sales volume and revenue.

---

## Revenue Distribution

The analysis showed that revenue generation was heavily concentrated in several major cities, particularly São Paulo and Rio de Janeiro. This may reflect population density, stronger purchasing activity, or regional economic concentration.

---

## Customer Purchasing Patterns

Certain product categories generated significantly more repeat purchases than others. Categories such as bed & bath and furniture & decor showed especially strong repeat purchasing behavior. This type of insight could support customer retention strategies, loyalty campaigns and inventory prioritization.

---

## Seasonal Revenue Trends

Monthly revenue analysis revealed visible fluctuations throughout the year. The strongest revenue period occurred around November, potentially reflecting seasonal purchasing behavior and promotional activity (possibly influenced by Black Friday sales).

---

## Delivery Performance Analysis

One of the more interesting findings involved delivery performance across Brazilian states. The analysis revealed that orders were generally delivered earlier than the estimated delivery date across all analyzed regions. This may suggest that the company intentionally uses conservative delivery estimates to reduce the risk of missed customer expectations. However, significant differences between states may also indicate opportunities to improve delivery forecasting accuracy and operational standardization. Some states averaged deliveries approximately 8 days earlier than expected, while others averaged almost 20 days earlier than estimated.

---

# Business Recommendations

Based on the analysis, several potential business actions were identified:

- Prioritize high-performing product categories for marketing and inventory optimization.
- Use repeat-purchase categories to support retention and loyalty strategies.
- Improve regional delivery estimate accuracy in states with excessively conservative delivery windows.
- Investigate lower-performing regions for possible operational or demand-related issues.
- Continue monitoring seasonal purchasing trends to optimize promotional timing.

---

# Dashboard Preview

<img width="1443" height="810" alt="Dashboard_1" src="https://github.com/user-attachments/assets/cc062377-6f9a-4e0d-83be-bccc0dc7314a" />
<img width="1441" height="807" alt="Dashboard_2" src="https://github.com/user-attachments/assets/ffa19985-fced-45f2-9c25-3a4259f7fa42" />
<img width="1442" height="811" alt="Dashboard_3" src="https://github.com/user-attachments/assets/6a5fca47-5a80-45e1-ae50-29e06503ac0e" />

---

# Project Structure

```text
ecommerce-business-analysis/
│
├── Datasets/
├── PowerBI/
├── Python/
├── Screenshots/
├── SQL/
└── README.md
```

---

# How to Run

## SQL Analysis

Run the SQL scripts inside the `SQL/` folder using PostgreSQL.

---

## Python Analysis

Install required libraries:

```bash
pip install pandas matplotlib seaborn prophet
```

Run the Python scripts for exploratory analysis and forecasting visualizations.

---

## Power BI Dashboard

Open:

```text
Dashboard_2017.pbix
```

inside Power BI Desktop.

---

# https://github.com/kminskanatalia

Created as part of a personal data analytics portfolio focused on:

- SQL,
- Python,
- Power BI,
- business intelligence,
- customer analytics,
- operational analytics,
- and data visualization.
