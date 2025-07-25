import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set(style="whitegrid")

# Paths
input_file = "sales_data_sample.csv"
output_dir = "charts"
os.makedirs(output_dir, exist_ok=True)

# Load data with encoding fix
try:
    df = pd.read_csv(input_file, encoding="latin1")
except Exception as e:
    print("❌ Error loading CSV:", e)
    exit()

# Print column info
print("\n✅ Data loaded successfully!\n")
print("Columns:\n", df.columns)
print("\nSample Data:\n", df.head())

# Add TotalSales column
df["TotalSales"] = df["QUANTITYORDERED"] * df["PRICEEACH"]

# Convert ORDERDATE to datetime
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

# -------------------------------
# 1. Monthly Sales Trend
# -------------------------------
df["YearMonth"] = df["ORDERDATE"].dt.to_period("M")
monthly_sales = df.groupby("YearMonth")["TotalSales"].sum().sort_index()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o", color="blue")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "monthly_sales_trend.png"))
plt.close()

# -------------------------------
# 2. Top 10 Products by Total Sales
# -------------------------------
product_sales = df.groupby("PRODUCTCODE")["TotalSales"].sum().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.values, y=product_sales.index, palette="viridis")
plt.title("Top 10 Products by Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Code")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_10_products.png"))
plt.close()

# -------------------------------
# 3. Top 10 Countries by Total Sales
# -------------------------------
country_sales = df.groupby("COUNTRY")["TotalSales"].sum().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=country_sales.values, y=country_sales.index, palette="coolwarm")
plt.title("Top 10 Countries by Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_10_countries.png"))
plt.close()

# -------------------------------
# 4. Correlation Heatmap
# -------------------------------
plt.figure(figsize=(8, 6))
sns.heatmap(df[["QUANTITYORDERED", "PRICEEACH", "TotalSales"]].corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
plt.close()

# -------------------------------
# Show saved files
# -------------------------------
print("\n📁 Charts saved in 'charts/' folder:")
for file in os.listdir(output_dir):
    print(" -", file)
