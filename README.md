# Sales-and-Marketing-Analytics-Project

🧾 Overview
This project provides a comprehensive sales and marketing analysis for a retail business using a real-world transactional dataset. The goal is to help business stakeholders identify sales trends, product performance, regional performance, and key drivers of revenue to make data-driven decisions.

Built entirely using Python, Pandas, Matplotlib, and Seaborn, this analysis mimics the work of a real-world Data Analyst in a retail environment.

🎯 Business Objectives
📈 Understand sales trends over time.

🛒 Identify top-performing products.

🌍 Determine high-revenue countries/regions.

🔍 Analyze the correlation between quantity, price, and sales.

💡 Generate actionable business insights for marketing and inventory strategy.

🗃️ Dataset
File: sales_data_sample.csv

Rows: ~2800 transactions

Columns: 25

Source: Sample transactional data from a global retail business.

Key Features:
Column	Description
ORDERDATE	Order date
QUANTITYORDERED	Number of units sold
PRICEEACH	Price per unit
SALES	Revenue from the transaction
PRODUCTLINE	Product category
COUNTRY	Country of customer
STATUS	Order status (Shipped, Cancelled, etc.)
DEALSIZE	Size of the transaction (Small, Medium, Large)

⚙️ Technologies Used
Tool	Purpose
Python	Programming language
Pandas	Data cleaning and manipulation
Matplotlib	Data visualization
Seaborn	Advanced visual analytics
VS Code	Development environment

📊 Visual Analytics Performed
1. Monthly Sales Trend
Shows how sales vary across different months.

Helps identify peak and off-peak seasons.

2. Top 10 Products by Sales
Determines best-selling products by revenue.

Supports product planning and inventory strategy.

3. Top 10 Countries by Sales
Identifies top-performing regions globally.

Helps in regional marketing and resource allocation.

4. Correlation Heatmap
Shows relationships between key variables like Quantity, Price, and Total Sales.

Informs how different features affect revenue.

📁 Project Structure
bash
Copy
Edit
Retail-Analytics-Project/
│
├── charts/                    # Output visualizations
│   ├── monthly_sales_trend.png
│   ├── top_10_products.png
│   ├── top_10_countries.png
│   └── correlation_heatmap.png
│
├── sales_data_sample.csv      # Dataset
├── sales.py                   # Python analysis script
└── README.md                  # Project description (this file)
✅ Key Insights
📅 Q4 months consistently show high sales volumes, indicating strong seasonal demand.

🛵 Motorcycles and Classic Cars dominate sales across product lines.

🇺🇸 USA, France, and Spain are the top-performing countries.

📉 Sales positively correlate with quantity and price, but vary by product line.

🧠 What You’ll Learn
How to approach a real-world business dataset.

How to structure a complete data analysis workflow in Python.

How to generate and save charts for reporting or dashboards.

How to extract insights and write a business-focused narrative.



📌 Future Work (Optional Enhancements)
Build an interactive Streamlit dashboard.

Connect to a live SQL database for continuous updates.

Export insights to Power BI or Tableau.

SANJAI R
Data Analyst | Python & BI Tools | Data Storyteller
