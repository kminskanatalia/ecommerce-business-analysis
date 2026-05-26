SELECT
c.customer_city,
SUM(pay.payment_value) AS revenue
FROM orders o

LEFT JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN payments pay ON o.order_id = pay.order_id

GROUP BY c.customer_city
ORDER BY revenue DESC;

SELECT * FROM revenue_by_city
WHERE customer_city IS NOT NULL
ORDER BY city_revenue DESC
LIMIT 10;