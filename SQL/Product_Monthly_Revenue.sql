SELECT * FROM revenue_by_month
WHERE month IS NOT NULL
ORDER BY monthly_revenue DESC
LIMIT 12;