-- Retail Sales Analysis SQL
-- Load retail_sales_raw.csv into a table named retail_sales.
-- SQL syntax is compatible with common SQL systems with minor date-function adjustments.

-- 1. Overall business KPIs
SELECT
    SUM(revenue) AS total_revenue,
    SUM(revenue - cost) AS total_profit,
    SUM(quantity) AS total_units,
    AVG(revenue) AS average_order_value,
    100.0 * SUM(revenue - cost) / NULLIF(SUM(revenue), 0) AS profit_margin_percent
FROM retail_sales;

-- 2. Revenue and profit by category
SELECT
    category,
    SUM(revenue) AS revenue,
    SUM(revenue - cost) AS profit,
    SUM(quantity) AS units_sold
FROM retail_sales
GROUP BY category
ORDER BY revenue DESC;

-- 3. Regional performance
SELECT
    region,
    SUM(revenue) AS revenue,
    SUM(revenue - cost) AS profit
FROM retail_sales
GROUP BY region
ORDER BY profit DESC;

-- 4. Sales channel comparison
SELECT
    sales_channel,
    COUNT(DISTINCT order_id) AS orders,
    AVG(revenue) AS average_order_value,
    SUM(revenue) AS total_revenue
FROM retail_sales
GROUP BY sales_channel
ORDER BY total_revenue DESC;

-- 5. Monthly trend (PostgreSQL-style date formatting)
SELECT
    TO_CHAR(order_date, 'YYYY-MM') AS sales_month,
    SUM(revenue) AS monthly_revenue,
    SUM(revenue - cost) AS monthly_profit
FROM retail_sales
GROUP BY TO_CHAR(order_date, 'YYYY-MM')
ORDER BY sales_month;

-- 6. Discount analysis
SELECT
    discount_rate,
    COUNT(*) AS order_lines,
    AVG(revenue) AS average_revenue,
    AVG(revenue - cost) AS average_profit
FROM retail_sales
GROUP BY discount_rate
ORDER BY discount_rate;
