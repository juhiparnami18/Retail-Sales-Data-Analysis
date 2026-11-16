# Retail Sales Data Analysis & Business Intelligence

## Project overview
This portfolio project analyzes a **synthetic retail sales dataset** covering 2025. It demonstrates a practical data workflow: data inspection, cleaning, descriptive analysis, SQL business queries, and visual reporting.

## Tools
- Python
- Pandas and NumPy
- Matplotlib
- SQL
- Excel (optional exploration of the CSV)
- Power BI (dashboard extension using the cleaned CSV)

## Dataset
`data/retail_sales_raw.csv` contains order-level records with order date, category, product, quantity, unit price, discount, revenue, cost, profit, region, and sales channel. The file intentionally includes a small number of missing values and duplicate rows so that data-quality checks can be demonstrated. It is synthetic and must not be interpreted as actual company performance.

## Repository structure
```text
retail-sales-data-science/
├── data/
│   ├── retail_sales_raw.csv
│   ├── category_summary.csv
│   ├── monthly_summary.csv
│   └── channel_statistics.csv
├── notebooks/
├── src/
│   └── analyze_sales.py
├── sql/
│   └── retail_analysis.sql
├── visuals/
│   ├── revenue_by_category.png
│   ├── monthly_revenue_trend.png
│   └── profit_by_region.png
├── requirements.txt
└── README.md
```

## Run the analysis
1. Install Python 3.10 or later.
2. Open a terminal in the repository folder.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python src/analyze_sales.py`

The script prints data-quality checks and KPIs, creates category/month/channel summaries, and saves charts in `visuals/`.

## SQL practice
Import `data/retail_sales_raw.csv` into a SQL table called `retail_sales`, then run the queries in `sql/retail_analysis.sql`. Date formatting syntax may need small changes for MySQL or SQLite.

## Power BI dashboard extension
Import the CSV into Power BI. Add cards for Total Revenue, Total Profit, Total Units, Average Order Value, and Profit Margin. Add a monthly revenue line chart, category revenue bar chart, regional profit chart, and slicers for region, category, and sales channel.

## Key questions
- Which product category contributes the most revenue?
- How does revenue change month by month?
- Which region contributes the most profit?
- How do average order values differ by sales channel?
- How should discounts be reviewed alongside profit?

## Statistical choices and limitations
This project uses descriptive statistics (mean, median, standard deviation) to summarize revenue by channel. The median is included because it is less sensitive to extreme values than the mean. The interquartile-range rule is used only to flag potential high-revenue observations for review; it does not prove that an observation is an error. Because the data is synthetic and generated from chosen assumptions, it may not reflect real customer behavior, seasonality, pricing, regional demand, or operational costs. Random sampling and simplified cost assumptions can introduce artificial patterns and bias. Results are demonstrations of analytical methods, not business recommendations for a real retailer.
