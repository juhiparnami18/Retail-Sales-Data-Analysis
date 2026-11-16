"""
Retail Sales Analysis
Run from the project root:
    pip install -r requirements.txt
    python src/analyze_sales.py
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "retail_sales_raw.csv"
OUT = ROOT / "visuals"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
print("Raw shape:", df.shape)
print("Missing values before cleaning:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())

# Cleaning: parse dates, remove exact duplicates, and handle missing values.
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df = df.drop_duplicates(subset=["order_id"])
df["unit_price"] = df["unit_price"].fillna(df.groupby("category")["unit_price"].transform("median"))
df["region"] = df["region"].fillna("Unknown")
df["sales_channel"] = df["sales_channel"].fillna("Unknown")
df = df.dropna(subset=["order_date", "category", "quantity", "revenue", "cost"])
df["profit"] = df["revenue"] - df["cost"]
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# Descriptive summaries
kpis = {
    "Total Revenue": round(df["revenue"].sum(), 2),
    "Total Profit": round(df["profit"].sum(), 2),
    "Total Units": int(df["quantity"].sum()),
    "Average Order Value": round(df["revenue"].mean(), 2),
    "Profit Margin (%)": round(df["profit"].sum() / df["revenue"].sum() * 100, 2)
}
print("\nKEY PERFORMANCE INDICATORS")
for name, value in kpis.items():
    print(f"{name}: {value}")

category_summary = df.groupby("category").agg(
    orders=("order_id", "nunique"),
    units=("quantity", "sum"),
    revenue=("revenue", "sum"),
    profit=("profit", "sum")
).sort_values("revenue", ascending=False)
print("\nCATEGORY SUMMARY\n", category_summary.round(2))
category_summary.to_csv(ROOT / "data" / "category_summary.csv")

monthly = df.groupby("month").agg(revenue=("revenue","sum"), profit=("profit","sum")).reset_index()
monthly.to_csv(ROOT / "data" / "monthly_summary.csv", index=False)

# Visual 1: revenue by category
ax = category_summary["revenue"].plot(kind="bar", figsize=(8,5), title="Revenue by Product Category")
ax.set_ylabel("Revenue")
ax.set_xlabel("Category")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_category.png", dpi=160)
plt.close()

# Visual 2: monthly revenue trend
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(monthly["month"], monthly["revenue"], marker="o")
ax.set_title("Monthly Revenue Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.savefig(OUT / "monthly_revenue_trend.png", dpi=160)
plt.close()

# Visual 3: profit by region
region_profit = df.groupby("region")["profit"].sum().sort_values(ascending=False)
ax = region_profit.plot(kind="bar", figsize=(8,5), title="Profit by Region")
ax.set_ylabel("Profit")
ax.set_xlabel("Region")
plt.tight_layout()
plt.savefig(OUT / "profit_by_region.png", dpi=160)
plt.close()

# Simple statistical comparison: mean revenue per order by channel.
channel_stats = df.groupby("sales_channel")["revenue"].agg(["count","mean","median","std"])
print("\nREVENUE BY CHANNEL (descriptive statistics)\n", channel_stats.round(2))
channel_stats.to_csv(ROOT / "data" / "channel_statistics.csv")

# Flag unusually high order revenues using the IQR rule; this is exploratory, not proof of error.
q1, q3 = df["revenue"].quantile([0.25, 0.75])
iqr = q3 - q1
upper_fence = q3 + 1.5 * iqr
print("\nPotential high-revenue outliers:", int((df["revenue"] > upper_fence).sum()))
print("\nAnalysis complete. Charts saved in /visuals and summaries in /data.")
